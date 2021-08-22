
from utils import SampleExperiments

__all__ = ['sample_experiments']

random_seed = list(range(1))

class sample_experiments(SampleExperiments):
    def __new__(cls, *args, **kwargs):
        cls.name = "sample experiment"
        grid_params = []
        grid_params.append({
            'random_seed': random_seed,
        })
        cls.grid_params = grid_params
        return SampleExperiments.__new__(cls, *args, **kwargs)
