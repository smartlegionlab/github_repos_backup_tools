# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
from typing import List, Dict
from views.main_view import MainView


class RepoCloneMaster:
    def __init__(self, name: str, token: str):
        self.name = name
        self.token = token
        self.view = MainView()
        self.clone_path = self._create_clone_directory()

    def _create_clone_directory(self) -> str:
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{self.name}_github_backup')
        os.makedirs(clone_path, exist_ok=True)
        return clone_path

    def clone(self, items: List[Dict], type_: str):
        path = os.path.join(self.clone_path, type_)
        os.makedirs(path, exist_ok=True)

        for index, item in enumerate(items, start=1):
            if 'ssh_url' in item:
                name, url = self._get_repo_info(item)
                item_path = os.path.join(path, name)

                if os.path.exists(item_path):
                    self.view.show_clone_progress(index, len(items), f"Updating {name}")
                    os.system(f'git -C {item_path} pull origin master')
                else:
                    self.view.show_clone_progress(index, len(items), f"Cloning {name}")
                    os.system(f'git clone https://{self.token}@github.com/{url} {item_path}')
            else:
                name, url = self._get_gist_info(item)
                item_path = os.path.join(path, name)

                if os.path.exists(item_path):
                    self.view.show_clone_progress(index, len(items), f"Updating {name}")
                    os.system(f'git -C {item_path} pull origin master')
                else:
                    self.view.show_clone_progress(index, len(items), f"Cloning {name}")
                    os.system(f'git clone https://{self.token}@gist.github.com/{url} {item_path}')

    @staticmethod
    def _get_repo_info(item: Dict) -> tuple:
        return item['name'], item['full_name']

    @staticmethod
    def _get_gist_info(item: Dict) -> tuple:
        return item['id'], item['id']
