import torch.nn as nn
import torch.nn.functional as F
import torch
class Net(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear (6, 64)
        self.fc2 = nn.Linear (64, 64)
        self.fc3 = nn.Linear (64, 64)
        self.fc4 = nn.Linear (64, 64)
        self.fc5 = nn.Linear (64, 1)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x =  self.fc5(x)
        return x
        

net = Net()
