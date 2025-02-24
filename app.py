# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from utils.managers import AppManager
from utils.config import Config
from utils.github_tools import GitHubDataMaster
from utils.parsers import ConfigParser
from utils.printers import SmartPrinter


def main():
    config = Config()
    printer = SmartPrinter()
    config_parser = ConfigParser()
    github_data_master = GitHubDataMaster()
    app = AppManager(
        config=config,
        printer=printer,
        config_parser=config_parser,
        github_data_master=github_data_master
    )
    app.run()


if __name__ == '__main__':
    main()
