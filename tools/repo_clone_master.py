import os
import shutil
import subprocess


class RepoCloneMaster:

    @classmethod
    def clone_repo(cls, repos=None):
        if repos is None:
            repos = []

        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, 'github_repositories')

        for n, repo in enumerate(repos, 1):
            repo_name = repo['name']
            repo_ssh_url = repo['ssh_url']
            repo_path = os.path.join(clone_path, repo_name)

            if os.path.exists(repo_path):
                shutil.rmtree(repo_path)

            os.makedirs(repo_path, exist_ok=True)
            # subprocess.run(['git', 'clone', repo_ssh_url, repo_path])
            os.system(f'git clone {repo_ssh_url} {repo_path}')
            print('-' * 30)
            print(f'{n}) Cloned {repo_name} successfully! [ok]')
