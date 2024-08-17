# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import shutil

from tools.smart_printer import SmartPrinter


class RepoCloneMaster:
    printer = SmartPrinter()

    @classmethod
    def clone(cls, name='anon', items=None, auto_mode=True, type_='repositories'):
        items = items or []
        clone_path = cls._create_clone_directory(name)
        path = os.path.join(clone_path, type_)

        cls._prepare_subdirectory(path)

        if type_ == 'repositories':
            cls._clone_items(items, path, auto_mode, cls._get_repo_info)
        else:
            cls._clone_items(items, path, auto_mode, cls._get_gist_info)

    @classmethod
    def _create_clone_directory(cls, name):
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{name}_github_backup')
        os.makedirs(clone_path, exist_ok=True)
        return clone_path

    @classmethod
    def _prepare_subdirectory(cls, path):
        os.makedirs(path, exist_ok=True)

    @classmethod
    def _get_action(cls, n, total, name):
        cls.printer.print_center()
        user_input = input(f'{n}/{total}. Cloning {name}? y|n|s: ')
        if user_input in ['y', 'Y', 'yes', 'Yes', '']:
            return True
        elif user_input in ['n', 'N', 'no', 'No']:
            return False
        elif user_input == 's':
            return None
        else:
            return

    @classmethod
    def _clone_items(cls, items, base_path, auto_mode, get_info_func):
        items_count = len(items)
        for n, item in enumerate(items, 1):
            name, url = get_info_func(item)
            item_path = os.path.join(base_path, name)

            if os.path.exists(item_path):
                shutil.rmtree(item_path)

            if not auto_mode:
                action = cls._get_action(n, items_count, name)
                if action is None:
                    print(f'Cloning stopped.')
                    break
                elif not action:
                    print(f'NOT CLONED! Skip...')
                    continue
            else:
                msg = f'{n}/{items_count} Cloning {name}: '
                cls.printer.print_framed(text=msg)
            os.system(f'git clone {url} {item_path}')

    @classmethod
    def _get_repo_info(cls, repo):
        return repo['name'], repo['ssh_url']

    @classmethod
    def _get_gist_info(cls, gist):
        gist_id = gist['id']
        return gist_id, f'https://gist.github.com/{gist_id}.git'
