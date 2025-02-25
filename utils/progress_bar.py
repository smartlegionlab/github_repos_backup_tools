# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import sys


class ProgressBar:
    @staticmethod
    def _clear_line():
        sys.stdout.write('\r\033[K')
        sys.stdout.flush()

    @staticmethod
    def _move_cursor_to_end():
        sys.stdout.write('\033[999C')
        sys.stdout.flush()

    @staticmethod
    def _progress_bar(current, total, failed, message=""):
        percent = (current / total) * 100
        bar_length = 50
        filled_length = int(bar_length * current // total)
        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        line = f'\r[{bar}] {percent:.2f}% | {current}/{total} | Failed: {failed} | {message}'
        sys.stdout.write(line.ljust(120))
        sys.stdout.flush()

    def __init__(self):
        pass

    def update(self, current, total, failed, message=""):
        self._clear_line()
        self._progress_bar(current, total, failed, message)
        self._move_cursor_to_end()

    def finish(self, message='Progress completed!'):
        # self._clear_line()
        print()
        print(f"\n✅{message}\n")
        print()
