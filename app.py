# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import os
from dotenv import load_dotenv
from tools.app_manager import AppManager
from tools.githib_api_manager import GitHubAPI


def main():
    load_dotenv()
    app_manager = AppManager()
    app_manager.show_head()
    print('Please wait...')
    token = os.getenv("GITHUB_API_TOKEN")
    name = os.getenv("GITHUB_NAME")
    github_api_manager = GitHubAPI(
        name=name,
        token=token
    )
    repos = github_api_manager.get_repos_names()
    app_manager.printer.echo()
    print(f'Name: {github_api_manager.name} | Repositories: {len(repos)}')
    app_manager.printer.echo()
    app_manager.show_footer()


if __name__ == '__main__':
    main()
