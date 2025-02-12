# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import platform
import argparse
from controllers.app_controller import AppController
from models.config import Config
from models.github_data_master import GitHubDataMaster
from utils.validators import Validators
from views.info_view import AppInfo


def main():
    config = Config()
    name = config.get_github_name()
    token = config.get_token()

    if not name or not token:
        print("Please provide GitHub name and token in the config file.")
        return

    data_master = GitHubDataMaster(name, token, url="https://api.github.com/user")
    data = {
        'token_is_valid': Validators.validate_token(token) and data_master.is_token_valid(),
        'name_is_valid': Validators.validate_name(name)
    }
    if not all(data.values()):
        print("Invalid or expired GitHub token. Please check your .config.ini file.")
        return

    parser = argparse.ArgumentParser(description="GitHub Repos Backup Tools")
    parser.add_argument("-r", action="store_true", help="Clone repositories")
    parser.add_argument("-g", action="store_true", help="Clone gists")
    parser.add_argument("--archive", action="store_true", help="Create archive")
    parser.add_argument("--shutdown", action="store_true", help="Shutdown after completion")

    args = parser.parse_args()

    controller = AppController(name, token)

    if args.r and args.g:
        controller.clone_repositories(args.archive)
        controller.clone_gists(args.archive)
    elif args.r:
        controller.clone_repositories(args.archive)
    elif args.g:
        controller.clone_gists(args.archive)
    else:
        controller.clone_repositories(args.archive)
        controller.clone_gists(args.archive)

    if args.shutdown and any([args.r, args.g]):
        print()
        if platform.system() == "Windows":
            os.system("shutdown /s /t 60")
        else:
            os.system("shutdown -h +1")
        print()


if __name__ == "__main__":
    AppInfo.show_head()
    main()
    AppInfo.show_footer()
