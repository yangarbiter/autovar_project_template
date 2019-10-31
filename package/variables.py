import logging

from autovar import AutoVar
from autovar.base import RegisteringChoiceType, VariableClass, register_var
from autovar.hooks import (
    check_result_file_exist, save_result_to_file,
)

auto_var = AutoVar(
    logging_level=logging.INFO,
    before_experiment_hooks=[check_result_file_exist],
    after_experiment_hooks=[save_result_to_file],
    settings={
        'server_url': '',
        'result_file_dir': './results/'
    }
)

#class ExampleVarClass(VariableClass, metaclass=RegisteringChoiceType):
#    """Example Variable Class"""
#    var_name = "example"
#
#    @register_var()
#    @staticmethod
#    def exp(auto_var):
#        pass

#auto_var.add_variable_class(ExampleVarClass())
