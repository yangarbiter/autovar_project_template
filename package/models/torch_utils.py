from torch import optim
import torch.nn as nn


def get_optimizer(model, optimizer: str, learning_rate: float, momentum, additional_vars=None):
    if additional_vars is None:
        parameters = model.parameters()
    else:
        parameters = [p for p in model.parameters()] + additional_vars

    if optimizer == 'adam':
        ret = optim.Adam(parameters, lr=learning_rate)
    elif optimizer == 'sgd':
        ret = optim.SGD(parameters, lr=learning_rate, momentum=momentum)
    else:
        raise ValueError(f"Not supported optimizer {optimizer}")
    return ret


def get_loss(loss_name: str, reduction):
    if 'ce' in loss_name:
        ret = nn.CrossEntropyLoss(reduction=reduction)
    elif 'mse' in loss_name:
        ret = nn.MSELoss(reduction=reduction)
    else:
        raise ValueError(f"Not supported loss {loss_name}")
    return ret
