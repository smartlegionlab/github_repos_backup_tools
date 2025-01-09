# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import sys
import argparse
from datetime import datetime, timedelta

from tools.app_manager import AppManager
from tools.parsers import ConfigParser


def main():
    project_root = os.path.abspath(os.path.dirname(__file__))
    config_file_path = os.path.join(project_root, '.config.ini')
    app_manager = AppManager()
    app_manager.show_head()
    config_parser = ConfigParser(config_file_path)
    github_token = config_parser.get_token()
    github_name = config_parser.get_github_name()

    if not github_name or not github_token:
        print('Please provide token and name')
        app_manager.show_footer()
        sys.exit(0)
    app_manager.name = github_name
    app_manager.token = github_token

    parser = argparse.ArgumentParser(description='GitHub Repositories Backup Tools')
    parser.add_argument('-r', action='store_true', help='Cloning repositories')
    parser.add_argument('-g', action='store_true', help='Cloning gists')
    parser.add_argument('--archive', action='store_true', help='Create archive')
    parser.add_argument('--no-auto', action='store_true', help='Disabling automatic mode')
    parser.add_argument('--shutdown',
                        action='store_true', help='Shutting down the system after finishing work')

    args = parser.parse_args()

    if args.r and args.g:
        app_manager.clone_repositories_and_gists(archive_flag=args.archive, auto_mode=not args.no_auto)
    elif args.r:
        app_manager.clone_repositories(archive_flag=args.archive, auto_mode=not args.no_auto)
    elif args.g:
        app_manager.clone_gists(archive_flag=args.archive, auto_mode=not args.no_auto)
    else:
        app_manager.main_menu()
    app_manager.show_footer()

    if args.shutdown:
        current_time = datetime.now()
        shutdown_time = current_time + timedelta(minutes=1)

        os.system(f'shutdown -h {shutdown_time.strftime("%H:%M")}')


if __name__ == '__main__':
    main()
