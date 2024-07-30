# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import os
import shutil


class RepoCloneMaster:

    @classmethod
    def clone_repo(cls, repos=None):
        if repos is None:
            repos = []

        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, 'github_repositories')
        num_of_repo = len(repos)
        for n, repo in enumerate(repos, 1):
            repo_name = repo['name']
            repo_ssh_url = repo['ssh_url']
            repo_path = os.path.join(clone_path, repo_name)

            if os.path.exists(repo_path):
                shutil.rmtree(repo_path)

            os.makedirs(repo_path, exist_ok=True)
            os.system(f'git clone --mirror {repo_ssh_url} {repo_path} ')
            print('-' * 30)
            msg = f'{n}/{num_of_repo}. Cloned {repo_name} successfully! [ok]'
            length = len(msg)
            print('-' * length)
            print(msg)
            print('-' * length)
