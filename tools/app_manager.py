# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from tools.config import Config
from tools.smart_printer import SmartPrinter


class AppManager:
    _config = Config()
    _printer = SmartPrinter()

    @classmethod
    def show_head(cls):
        cls._printer.echo()
        cls._printer.echo(cls._config.app_name)

    @classmethod
    def show_footer(cls):
        cls._printer.echo(cls._config.help_url)
        cls._printer.echo(cls._config.copyright_)
