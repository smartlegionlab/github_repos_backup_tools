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
    def get_action(cls, n, total, name):
        cls.printer.print_center()
        user_input = input(f'{n}/{total}. Cloning {name}? y|n: ')
        if user_input in ['y', 'Y', 'yes', 'Yes', '']:
            return True
        return False

    @classmethod
    def clone_repo(cls, name='anon', repos=None, gists=None, auto_mode=True):
        repos = repos or []
        gists = gists or []

        clone_path = cls._create_clone_directory(name)
        repositories_path = os.path.join(clone_path, 'repositories')
        gists_path = os.path.join(clone_path, 'gists')

        if repos:
            cls._prepare_directory(repositories_path)
            cls._clone_repositories(repos, repositories_path, auto_mode=auto_mode)

        if gists:
            cls._prepare_directory(gists_path)
            cls._clone_gists(gists, gists_path, auto_mode=auto_mode)

    @classmethod
    def _create_clone_directory(cls, name):
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{name}_github_backup')
        os.makedirs(clone_path, exist_ok=True)
        return clone_path

    @classmethod
    def _prepare_directory(cls, path):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)

    @classmethod
    def _clone_repositories(cls, repos, repositories_path, auto_mode=True):
        items_count = len(repos)
        for n, repo in enumerate(repos, 1):
            repo_name = repo['name']
            repo_ssh_url = repo['ssh_url']
            repo_path = os.path.join(repositories_path, repo_name)
            if not auto_mode:
                action = cls.get_action(n, items_count, repo_name)
                if not action:
                    print(f'NOT CLONED! Skip...')
                    continue
            cls._clone_git_repo(repo_ssh_url, repo_path, n, items_count, repo_name)

    @classmethod
    def _clone_gists(cls, gists, gists_path, auto_mode=True):
        items_count = len(gists)
        for n, gist in enumerate(gists, 1):
            gist_id = gist['id']
            gist_url = f'https://gist.github.com/{gist_id}.git'
            gist_path = os.path.join(gists_path, gist_id)
            if not auto_mode:
                action = cls.get_action(n, items_count, gist_id)
                if not action:
                    print(f'NOT CLONED! Skip...')
                    continue
            cls._clone_git_repo(gist_url, gist_path, n, items_count, f'Gist {gist_id}')

    @classmethod
    def _clone_git_repo(cls, git_url, path, n, total, name):
        msg = f'{n}/{total} Cloning {name}: '
        cls.printer.print_framed(text=msg)
        os.system(f'git clone {git_url} {path}')
