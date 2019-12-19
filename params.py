
from utils import SampleExperiments

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

class Sample01Experiment(SampleExperiments):
    def __new__(cls, *args, **kwargs):
        cls.name = "Sample01"
        grid_params = []
        grid_params.append({
            'random_seed': random_seed,
        })
        cls.grid_params = grid_params
        return SampleExperiments.__new__(cls, *args, **kwargs)

