from nets import ResNet
import timm
from config import *


def get_model(model):
    if model == 'ResNet-18':
        return ResNet.resnet18(pretrained=True, t_num_classes=config['N_CLASSES'])  # initialize model
    elif model == 'ResNet-50':
        return ResNet.resnet50(pretrained=True, t_num_classes=config['N_CLASSES'])  # initialize model
    elif model == 'ResMLP-12':
        return timm.create_model('resmlp_12_224', pretrained=True, num_classes=config['N_CLASSES'])
    elif model == 'ResMLP-24':
        return timm.create_model('resmlp_24_224', pretrained=True, num_classes=config['N_CLASSES'])
    else:
        print('No required model')
        return None
