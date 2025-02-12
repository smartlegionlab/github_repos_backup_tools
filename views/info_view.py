# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from views.smart_printer import SmartPrinter


class AppInfo:
    printer = SmartPrinter()
    app_name = 'GitHub Repositories Backup Tool'
    author = 'A.A. Suvorov'
    help_url = 'https://github.com/smartlegionlab/'
    copyright_ = 'Copyright © 2024, A.A. Suvorov. All rights reserved.'

    @classmethod
    def show_head(cls):
        cls.printer.print_center(symbol='*')
        cls.printer.print_center(text=cls.app_name)
        cls.printer.print_center(symbol='-')
        print()
        cls.printer.print_framed('Initializing, please wait...')
        print()

    @classmethod
    def show_footer(cls):
        print()
        cls.printer.print_center(symbol='-')
        cls.printer.print_center(text=cls.help_url, symbol='-')
        cls.printer.print_center(text=cls.copyright_, symbol='*')
