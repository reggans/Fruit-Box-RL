from ray.rllib.models.torch.torch_modelv2 import TorchModelV2
import torch
import torch.nn as nn

class CustomNetwork(TorchModelV2, nn.Module):
    def __init__