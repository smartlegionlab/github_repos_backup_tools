# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from utils.decorators import CenteredTextDecorator, FramedTextDecorator


class SmartPrinter:
    @staticmethod
    def print_center(text: str = '', symbol: str = '-'):
        print(CenteredTextDecorator.decorate(text, symbol))

    @staticmethod
    def print_framed(text: str = '', symbol: str = '-'):
        print(FramedTextDecorator.decorate(text, symbol))
