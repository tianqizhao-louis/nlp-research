import torch
import torch.onnx as onnx
import torchvision.models as models

model = models.vgg16(pretrained=True)
torch.save(model.state_dict(), 'model_weights.pth')

model = models.vgg16()
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()

torch.save(model, 'model.pth')

model = torch.load('model.pth')
input_image = torch.zeros((1,3,224,224))
onnx.export(model, input_image, 'model.onnx')
