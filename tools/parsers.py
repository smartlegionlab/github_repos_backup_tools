# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import configparser


class ConfigParser:
    def __init__(self, file_path):
        self.file_path = self.get_file_path(file_path)
        self.config = self.load_config()

    @staticmethod
    def get_file_path(file_name):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        return os.path.join(project_root, file_name)

    def load_config(self):
        config = configparser.ConfigParser()
        try:
            config.read(self.file_path, encoding='utf-8')
        except FileNotFoundError:
            raise Exception(f"File {self.file_path} not found.")
        return config

    def get_token(self):
        return self.config.get('github', 'token', fallback='')

    def get_github_name(self):
        return self.config.get('github', 'github_name', fallback='')
