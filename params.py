
from autovar_utils import Experiments

__all__ = ['SampleExperiments']

random_seed = list(range(1))

class SampleExperiments(Experiments):
    def __new__(cls, *args, **kwargs):
        cls.name = "sample experiment"
        cls.experiment_fn = 'train_vae_manifold'
        grid_params = []

        datasets = [f"sample-dataset_{dim}" for dim in [2, 3, 10]]

        grid_params.append({
            'dataset': datasets,
            'batch_size': [1024],
            'epochs': [30],
            'optimizer': ['adam'],
            'momentum': [0.0],
            'learning_rate': [0.001],
            'random_seed': list(range(1)),
        })

        cls.grid_params = grid_params
        return Experiments.__new__(cls, *args, **kwargs)
