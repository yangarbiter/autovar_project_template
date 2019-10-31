from mkdir_p import mkdir_p



def main():
    mkdir_p("./results/exp_name")
    auto_var.register_experiment('exp_name', run_exp_name,
                                 {'result_file_dir': './results/exp_name'})
    auto_var.parse_argparse(


if __name__ == '__main__':
    main()
