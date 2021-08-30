from torchvision import models
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import argparse

class FM_visualize:
    def __init__(self, module_name, layer_index):
        self.hook = module_name[layer_index].register_forward_hook(self.hook_fn)
    
    def hook_fn(self, module, input, output):
        self.features = output.cpu().data.numpy()

        
parser = argparse.ArgumentParser(description='Feature Map Visualizing')
parser.add_argument('--img_path', default='./dog.jpg', type=str, help='pretrained model')
args = parser.parse_args()


model = models.resnet18(pretrained=True).cuda()
print('Check the module name and number of the model!!')
print(model)


#############################
visual = FM_visualize(model.layer1, 0)   # Enter the model module and number to visualize
out_channal = 64   # Enter the last channel of the model layer to visualize
#############################

img = Image.open(args.img_path)
trans = transforms.ToTensor()
img = trans(img).unsqueeze(0).cuda()
model(img)
activations = visual.features


rows = int(out_channal/8)
columns = 8
fig, axes = plt.subplots(rows,columns,figsize=(30, 30))

for row in range(rows):
    for column in range(columns):
        axis = axes[row][column]
        axis.get_xaxis().set_ticks([])
        axis.get_yaxis().set_ticks([])
        axis.imshow(activations[0][row*8+column])

plt.savefig('fmv_result.jpg')