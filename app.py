# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import argparse
import os
import sys

from dotenv import load_dotenv

from tools.app_manager import AppManager


def main():
    app_manager = AppManager()
    app_manager.show_head()
    load_dotenv()
    name = os.getenv("GITHUB_NAME")
    token = os.getenv("GITHUB_API_TOKEN")
    if not name or not token:
        print('Please provide token and name')
        app_manager.show_footer()
        sys.exit(0)
    app_manager.name = name
    app_manager.token = token
    parser = argparse.ArgumentParser(description='GitHub Repositories Backup Tools')
    parser.add_argument('-r', action='store_true', help='Cloning repositories')
    parser.add_argument('-g', action='store_true', help='Cloning gists')
    parser.add_argument('--no-archive', action='store_true', help='Do not create archive')
    args = parser.parse_args()
    if args.r and args.g:
        app_manager.clone_repositories_and_gists()
    elif args.r:
        app_manager.clone_repositories()
    elif args.g:
        app_manager.clone_gists()
    else:
        app_manager.main_menu()
    if not args.no_archive:
        app_manager.create_archive()
    app_manager.show_footer()


if __name__ == '__main__':
    main()
