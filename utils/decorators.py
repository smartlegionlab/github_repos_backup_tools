# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import shutil


class CenteredTextDecorator:
    @staticmethod
    def decorate(text: str = '', symbol: str = '-') -> str:
        columns = shutil.get_terminal_size().columns
        return text.center(columns, symbol)


class FramedTextDecorator:
    @staticmethod
    def decorate(text: str = '', symbol: str = '-') -> str:
        border = symbol * len(text)
        return f"{border}\n{text}\n{border}"
