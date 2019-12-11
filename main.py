from mkdir_p import mkdir_p

from package.variables import auto_var


def run_exp_name(auto_var):
    pass


def main():
    mkdir_p("./results/exp_name")
    auto_var.register_experiment('exp_name', run_exp_name,
                                 {'file_format': 'pickle', 'result_file_dir': './results/exp_name'})
    auto_var.parse_argparse()


if __name__ == '__main__':
    main()
