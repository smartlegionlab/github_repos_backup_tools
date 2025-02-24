# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import argparse
import os
import platform
import shutil
import subprocess
from typing import Dict

from utils.archive_creator import ArchiveCreator
from utils.config import Config
from utils.github_tools import GitHubDataMaster
from utils.parsers import ConfigParser
from utils.smart_printer import SmartPrinter


class AppManager:
    def __init__(self):
        self.config = Config()
        self.printer = SmartPrinter()
        self.config_parser = ConfigParser()
        self.github_data_master = GitHubDataMaster()

    @staticmethod
    def get_yes_no(arg):
        return 'Yes' if arg else 'No'

    def start(self):
        self.printer.show_head(text=self.config.name)
        print(f'Getting a token from a .config.ini file...')
        token = self.config_parser.get_token()

        if not token:
            print("ERROR! Please provide GitHub token in the config file.")
            return
        else:
            print(f'Token successfully received!')

        self.github_data_master.token = token

        is_token_valid = self.github_data_master.is_token_valid()

        print(f'Token is valid: {self.get_yes_no(is_token_valid)}')

        self.printer.print_center()

        print(f'Getting user login...')

        self.github_data_master.fetch_user_data()

        login = self.github_data_master.login

        if login:
            print(f'Login: {login}')
        else:
            print('Login failed.')
            return

        self.printer.print_center()

        print(f'Parsing arguments:\n')

        parser = argparse.ArgumentParser(description="GitHub Repos Backup Tools")
        parser.add_argument("-r", action="store_true", help="Clone repositories")
        parser.add_argument("-g", action="store_true", help="Clone gists")
        parser.add_argument("--archive", action="store_true", help="Create archive")
        parser.add_argument("--shutdown", action="store_true", help="Shutdown after completion")
        args = parser.parse_args()

        clone_repos = args.r
        clone_gists = args.g
        make_archive = args.archive
        exec_shutdown = args.shutdown

        print(f'Clone repositories: {self.get_yes_no(clone_repos)}')
        print(f'Clone gists: {self.get_yes_no(clone_gists)}')
        print(f'Make archive: {self.get_yes_no(make_archive)}')
        print(f'Shutdown: {self.get_yes_no(exec_shutdown)}')

        self.printer.print_center()
        print(f'Forming a path to the directory:\n')

        path = self._create_clone_directory(login)

        print(f'Path: {path}')

        if clone_repos:
            repos_target_dir = os.path.join(path, "repositories")
            self.clone_repositories(repos_target_dir)

        if clone_gists:
            gists_target_dir = os.path.join(path, "gists")
            self.clone_gists(gists_target_dir)

        if make_archive:
            self._create_archive(login)

    def clone_repositories(self, target_dir: str) -> Dict[str, bool]:
        self.printer.print_center(text='Cloning repositories: ')
        os.makedirs(target_dir, exist_ok=True)
        print(f'Target directory: {target_dir}')
        print(f'Getting repositories...')

        self.github_data_master.fetch_repositories()
        repositories = self.github_data_master.repositories
        count = len(repositories)

        if not count:
            print('No repositories found.')
            return {}
        else:
            print(f'Found {count} repositories.')

        status_dict = {}

        for index, (name, url) in enumerate(repositories.items(), start=1):
            self.printer.print_framed(f'{index}/{count}: Cloning: {name}')
            item_path = os.path.join(target_dir, name)

            if os.path.exists(item_path):
                success = self._git_pull(item_path)
                if not success:
                    print(f"Pull failed. Removing and recloning: \n{item_path}")
                    shutil.rmtree(item_path)
                    success = self._git_clone(url, item_path)
            else:
                success = self._git_clone(url, item_path)

            if not success and os.path.exists(item_path):
                print(f"Removing incomplete repository: \n{item_path}")
                shutil.rmtree(item_path)

            status_dict[name] = success

        while True:
            failed_repos = {name: url for name, url in repositories.items() if not status_dict.get(name, False)}

            if not failed_repos:
                break

            self.printer.print_framed(f"Retrying failed repositories: {len(failed_repos)} remaining")

            for name, url in failed_repos.items():
                self.printer.print_framed(f'Retrying: {name}')
                item_path = os.path.join(target_dir, name)

                if os.path.exists(item_path):
                    success = self._git_pull(item_path)
                    if not success:
                        print(f"Pull failed. Removing and recloning: \n{item_path}")
                        shutil.rmtree(item_path)
                        success = self._git_clone(url, item_path)
                else:
                    success = self._git_clone(url, item_path)

                if not success and os.path.exists(item_path):
                    print(f"Removing incomplete repository: \n{item_path}")
                    shutil.rmtree(item_path)

                status_dict[name] = success

        return status_dict

    def _git_clone(self, url: str, item_path: str) -> bool:
        try:
            result = subprocess.run(
                ['git', 'clone', url, item_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=20
            )
            if result.returncode == 0:
                print(f"Repository cloned successfully: \n{item_path}")
                return True
            else:
                print(f"Failed to clone repository: \n{item_path}")
                print(result.stderr)
                return False
        except subprocess.TimeoutExpired:
            print(f"Clone operation timed out: \n{item_path}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while cloning {item_path}: {str(e)}")
            return False

    def _git_pull(self, item_path: str) -> bool:
        try:
            result = subprocess.run(
                ['git', '-C', item_path, 'pull', 'origin', 'master'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=20
            )
            if result.returncode == 0:
                print(f"Repository updated successfully: \n{item_path}")
                return True
            else:
                print(f"Failed to update repository: \n{item_path}")
                print(result.stderr)
                return False
        except subprocess.TimeoutExpired:
            print(f"Pull operation timed out: \n{item_path}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while updating {item_path}: {str(e)}")
            return False

    def clone_gists(self, target_dir):
        self.printer.print_center(text='Cloning gists: ')
        os.makedirs(target_dir, exist_ok=True)
        print(f'Target directory: {target_dir}')
        print(f'Getting gists...')

        self.github_data_master.fetch_gists()
        gists = self.github_data_master.gists
        count = len(gists)

        if not count:
            print('No gists found.')
            return {}
        else:
            print(f'Found {count} gists.')

        status_dict = {}

        for index, (name, url) in enumerate(gists.items(), start=1):
            self.printer.print_framed(f'{index}/{count}: Cloning: {name}')
            item_path = os.path.join(str(target_dir), str(name))

            if os.path.exists(item_path):
                success = self._git_pull(item_path)
                if not success:
                    print(f"Pull failed. Removing and recloning: \n{item_path}")
                    shutil.rmtree(item_path)
                    success = self._git_clone(url, item_path)
            else:
                success = self._git_clone(url, item_path)

            if not success and os.path.exists(item_path):
                print(f"Removing incomplete gist: \n{item_path}")
                shutil.rmtree(item_path)

            status_dict[name] = success

        while True:
            failed_repos = {name: url for name, url in gists.items() if not status_dict.get(name, False)}

            if not failed_repos:
                break

            print(f"Retrying failed gists: {len(failed_repos)} remaining")

            for name, url in failed_repos.items():
                self.printer.print_framed(f'Retrying: {name}')
                item_path = os.path.join(str(target_dir), str(name))

                if os.path.exists(item_path):
                    success = self._git_pull(item_path)
                    if not success:
                        print(f"Pull failed. Removing and recloning: \n{item_path}")
                        shutil.rmtree(item_path)
                        success = self._git_clone(url, item_path)
                else:
                    success = self._git_clone(url, item_path)

                if not success and os.path.exists(item_path):
                    print(f"Removing incomplete gist: \n{item_path}")
                    shutil.rmtree(item_path)

                status_dict[name] = success

        return status_dict

    def _create_archive(self, login):
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{login}_github_backup')
        if os.path.exists(clone_path):
            archive_creator = ArchiveCreator(clone_path)
            archive_creator.create_archive()
        else:
            self.printer.print_framed("Clone path not found")

    def show_error(self, message: str):
        self.printer.print_framed(f"Error: {message}")

    def show_clone_progress(self, current: int, total: int, name: str):
        self.printer.print_framed(f"{current}/{total}. Cloning: {name}")

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

    def stop(self, shutdown=False):
        self.printer.show_footer(url=self.config.url, copyright_=self.config.info)
        if shutdown:
            self.shutdown()

    def run(self):
        self.start()
        self.stop()
