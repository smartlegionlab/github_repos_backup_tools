# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import os

from tools.config import Config
from tools.smart_printer import SmartPrinter


class AppManager:
    config = Config()
    printer = SmartPrinter()

    @classmethod
    def show_head(cls):
        cls.printer.echo()
        cls.printer.echo(cls.config.app_name)

    @classmethod
    def show_footer(cls):
        cls.printer.echo(cls.config.help_url)
        cls.printer.echo(cls.config.copyright_)
