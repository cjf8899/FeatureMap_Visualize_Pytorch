# FeatureMap_Visualize_Pytorch
This repo is a code that can be visualized and saved as an images.
## Demo
<img src="https://user-images.githubusercontent.com/53032349/131292093-36aa6ccb-f3b2-41b2-8544-cd13d600ad59.png" width="100%" height="100%" title="70px" alt="memoryblock"><br>

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
When the module name is **layer1**, the number is **0** and **1**.
```
visualize.py
...
visual = FM_visualize(model.layer1, 0)
or
visual = FM_visualize(model.layer1, 1)  
...
```
## Run
```Shell
python visualize.py --img_path ./dog.jpg
```

