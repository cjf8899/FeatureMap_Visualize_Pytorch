# FeatureMap_Visualize_Pytorch
This repo is a code that can be visualized and saved as an images.
## Demo
<img src="https://user-images.githubusercontent.com/53032349/131291421-aadda627-93d0-477b-8b16-d99ffd35eaf8.png" width="100%" height="100%" title="70px" alt="memoryblock"><br>

## Getting Started

model structures
```
ResNet(
  ... 
  (layer1): Sequential(
    (0): BasicBlock(
      (conv1): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
      (bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU(inplace=True)
      (conv2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
      (bn2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
    (1): BasicBlock(
      (conv1): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
      (bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU(inplace=True)
      (conv2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
      (bn2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  ...
```
When the module name is 'layer1', the number is '0' and '1'.

## Run
```Shell
python visualize.py --img_path ./dog.jpg
```

