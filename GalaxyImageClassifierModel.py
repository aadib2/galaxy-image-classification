# importing necessary libraries/packages
import torch.nn as nn
import timm


''' 
Creating our Deep Learning Model
Utilizing a predefined, pretrained CNN 'efficientnet_b0'
Comes from the timm library of models 
'''

class GalaxyImageClassifier(nn.Module):
    def __init__(self, num_classes=3):
        super(GalaxyImageClassifier, self).__init__()
        # Where we define all the parts of the model
        self.base_model = timm.create_model('efficientnet_b0', pretrained=True)
        # removing the last layer of the model
        self.features = nn.Sequential(*list(self.base_model.children())[:-1])

        enet_out_size = 1280
        # Make a classifier
        self.classifier = nn.Linear(enet_out_size, num_classes)


    def forward(self, x):
        # Connect these parts and return the output
        x = self.features(x)
       # x = x.view(x.size(0), -1)
        output = self.classifier(x)
        return output
