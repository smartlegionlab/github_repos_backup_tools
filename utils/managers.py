# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import shutil
import subprocess
import argparse
from typing import Dict
import platform

from utils.archive_creator import ArchiveCreator


class AppManager:
    def __init__(self, config, printer, config_parser, github_data_master):
        self.config = config
        self.printer = printer
        self.config_parser = config_parser
        self.github_data_master = github_data_master

    @staticmethod
    def _parse_arguments():
        parser = argparse.ArgumentParser(description="GitHub Repos Backup Tools")
        parser.add_argument("-r", action="store_true", help="Clone repositories")
        parser.add_argument("-g", action="store_true", help="Clone gists")
        parser.add_argument("--archive", action="store_true", help="Create archive")
        parser.add_argument("--shutdown", action="store_true", help="Shutdown after completion")
        return parser.parse_args()

    @staticmethod
    def _create_clone_directory(login) -> str:
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{login}_github_backup')
        os.makedirs(clone_path, exist_ok=True)
        return clone_path

    @staticmethod
    def shutdown():
        print()
        if platform.system() == "Windows":
            os.system("shutdown /s /t 60")
        else:
            os.system("shutdown -h +1")
        print()

    @staticmethod
    def get_yes_no(arg):
        return '✅' if arg else '⚠️'

    @staticmethod
    def create_item_path(target_dir: str, item_name: str) -> str:
        return os.path.join(target_dir, item_name)

    @staticmethod
    def _git_clone(url: str, item_path: str) -> bool:
        try:
            result = subprocess.run(
                ['git', 'clone', url, item_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=20
            )
            if result.returncode == 0:
                print(f"✅ Repository cloned successfully: \n{item_path}")
                return True
            else:
                print(f"⚠️ Failed to clone repository: \n{item_path}")
                print(result.stderr)
                return False
        except subprocess.TimeoutExpired:
            print(f"⚠️ Clone operation timed out: \n{item_path}")
            return False
        except Exception as e:
            print(f"⚠️ An unexpected error occurred while cloning {item_path}: {str(e)}")
            return False

    @staticmethod
    def _git_pull(item_path: str) -> bool:
        try:
            result = subprocess.run(
                ['git', '-C', item_path, 'pull', 'origin', 'master'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=20
            )
            if result.returncode == 0:
                print(f"✅ Repository updated successfully: \n{item_path}")
                return True
            else:
                print(f"⚠️ Failed to update repository: \n{item_path}")
                print(result.stderr)
                return False
        except subprocess.TimeoutExpired:
            print(f"⚠️ Pull operation timed out: \n{item_path}")
            return False
        except Exception as e:
            print(f"⚠️ An unexpected error occurred while updating {item_path}: {str(e)}")
            return False

    def start(self):
        self.printer.show_head(text=self.config.name)
        self.printer.print_center()
        print('Getting a token from a .config.ini file:\n')
        token = self.config_parser.get_token()

        if not token:
            print("⚠️ ERROR! Please provide GitHub token in the config file.")
            return
        else:
            print('✅ Token successfully received!')

        self.github_data_master.token = token

        self.printer.print_center()
        print(f'Checking the token for validity: \n')
        is_token_valid = self.github_data_master.is_token_valid()

        if is_token_valid:
            print(f'✅ Token is valid: {self.get_yes_no(is_token_valid)}')

        self.printer.print_center()

        print('Getting user login:\n')
        self.github_data_master.fetch_user_data()
        login = self.github_data_master.login

        if login:
            print(f'✅ Login: {login}')
        else:
            print('⚠️ Login failed.')
            return

        self.printer.print_center()

        print('Parsing arguments:\n')
        args = self._parse_arguments()

        clone_repos = args.r
        clone_gists = args.g
        make_archive = args.archive
        exec_shutdown = args.shutdown

        print(f'Clone repositories: {self.get_yes_no(clone_repos)}')
        print(f'Clone gists: {self.get_yes_no(clone_gists)}')
        print(f'Make archive: {self.get_yes_no(make_archive)}')
        print(f'Shutdown: {self.get_yes_no(exec_shutdown)}')

        self.printer.print_center()
        print('Forming a path to the directory:\n')

        path = self._create_clone_directory(login)
        print(f'✅ Path: {path}')

        if clone_repos:
            repos_target_dir = os.path.join(path, "repositories")
            self.clone_items(repos_target_dir, self.github_data_master.fetch_repositories, "repositories")

        if clone_gists:
            gists_target_dir = os.path.join(path, "gists")
            self.clone_items(gists_target_dir, self.github_data_master.fetch_gists, "gists")

        if make_archive:
            self._create_archive(login)

        if exec_shutdown:
            self.shutdown()

    def clone_items(self, target_dir: str, fetch_method, item_type: str) -> Dict[str, bool]:
        print()
        self.printer.print_center()
        self.printer.print_center(text=f'Cloning {item_type}: ')
        self.printer.print_center()
        print()
        os.makedirs(target_dir, exist_ok=True)
        print(f'Target directory: {target_dir}')
        self.printer.print_center()
        print(f'Getting {item_type}:\n')

        fetch_method()
        items = getattr(self.github_data_master, item_type)
        count = len(items)

        if not count:
            self.printer.print_framed(f'⚠️ No {item_type} found.')
            return {}
        else:
            self.printer.print_framed(f'✅ Found {count} {item_type}.')
        print()
        failed_dict = {}
        failed_count = 0

        for index, (name, url) in enumerate(items.items(), start=1):
            self.printer.print_framed(f'{index}/{count}/{failed_count}: Cloning: {name}')
            item_path = self.create_item_path(target_dir, name)

            if os.path.exists(item_path):
                success = self._git_pull(item_path)
                if not success:
                    print(f"⚠️ Pull failed. Removing and re-cloning: \n{item_path}")
                    shutil.rmtree(item_path)
                    success = self._git_clone(url, item_path)
            else:
                success = self._git_clone(url, item_path)

            if not success:
                print(f"⚠️ Removing incomplete {item_type}: \n{item_path}")
                if os.path.exists(item_path):
                    shutil.rmtree(item_path)
                failed_dict[name] = url
                failed_count += 1

        if not failed_dict:
            return failed_dict

        while failed_dict:
            self.printer.print_center()
            print()
            self.printer.print_framed(f"Retrying failed {item_type}: {len(failed_dict)} remaining")
            print()
            self.printer.print_center()

            current_failed = failed_dict.copy()
            failed_dict.clear()

            for index, (name, url) in enumerate(current_failed.items(), start=1):
                self.printer.print_framed(f'{index}/{len(current_failed)}/{failed_count}: Retrying: {name}')
                item_path = self.create_item_path(target_dir, name)

                if os.path.exists(item_path):
                    success = self._git_pull(item_path)
                    if not success:
                        print(f"⚠️ Pull failed. Removing and re-cloning: \n{item_path}")
                        shutil.rmtree(item_path)
                        success = self._git_clone(url, item_path)
                else:
                    success = self._git_clone(url, item_path)

                if not success:
                    print(f"⚠️ Removing incomplete {item_type}: \n{item_path}")
                    if os.path.exists(item_path):
                        shutil.rmtree(item_path)
                    failed_dict[name] = url
                else:
                    failed_count -= 1

        return failed_dict

    def _create_archive(self, login):
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{login}_github_backup')
        if os.path.exists(clone_path):
            archive_creator = ArchiveCreator(clone_path)
            archive_creator.create_archive()
        else:
            self.printer.print_framed("⚠️ Clone path not found")

    def stop(self, shutdown=False):
        self.printer.print_center()
        self.printer.show_footer(url=self.config.url, copyright_=self.config.info)
        if shutdown:
            self.shutdown()

    def run(self):
        self.start()
        self.stop()
