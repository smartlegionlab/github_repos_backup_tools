# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from views.smart_printer import SmartPrinter


class MainView:
    def __init__(self):
        self.printer = SmartPrinter()

    def show_error(self, message: str):
        self.printer.print_framed(f"Error: {message}")

    def get_user_choice(self) -> str:
        return input("Enter your choice: ")

    def confirm_action(self, message: str) -> bool:
        response = input(f"{message} (y/n): ").lower()
        return response == 'y'

    def show_clone_progress(self, current: int, total: int, name: str):
        self.printer.print_framed(f"{current}/{total}. Cloning: {name}")
