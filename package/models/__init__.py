import os

from autovar.base import RegisteringChoiceType, VariableClass, register_var


DEBUG = int(os.getenv("DEBUG", 0))

class ModelVarClass(VariableClass, metaclass=RegisteringChoiceType):
    """Model Variable Class"""
    var_name = "model"

    @register_var(argument=r'(?P<loss>[a-zA-Z0-9]+)-lig-(?P<arch>[a-zA-Z0-9_]+)(?P<hyper>-[a-zA-Z0-9\.]+)?')
    @staticmethod
    def torch_lightning(auto_var, loss, arch, hyper, n_features, n_classes):
        from .lightning_model import TorchLightningModel

        hyper = hyper[1:] if hyper is not None else None

        params = {}
        params['n_features'] = n_features
        params['n_classes'] = n_classes

        params['loss_name'] = loss
        params['arch'] = arch

        params['epochs'] = auto_var.get_var("epochs")
        params['learning_rate'] = auto_var.get_var("learning_rate")
        params['momentum'] = auto_var.get_var("momentum")
        params['optimizer'] = auto_var.get_var("optimizer")

        model = TorchLightningModel(**params)

        return model
