# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import shutil


class SmartPrinter:

    @classmethod
    def echo(cls, text='', char='-', show=True):
        columns = cls._get_term_width()
        symbol = ' ' if not char else char
        msg = (f' {text} ' if text else '').center(columns, symbol[0])
        if show:
            print(msg)
        return msg

    @classmethod
    def _get_term_width(cls):
        return shutil.get_terminal_size()[0]
