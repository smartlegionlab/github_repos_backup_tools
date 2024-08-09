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

from dotenv import load_dotenv

from tools.archive_creator import ArchiveCreator
from tools.repo_clone_master import RepoCloneMaster
from tools.config import Config
from tools.github_data_master import ReposDataMaster, GistsDataMaster
from tools.smart_printer import SmartPrinter


class AppManager:

    def __init__(self):
        self.smart_printer = SmartPrinter()
        self.repo_clone_master = RepoCloneMaster()
        self._name = None
        self._token = None

    def _init_data(self):
        load_dotenv()
        self._name = os.getenv("GITHUB_NAME")
        self._token = os.getenv("GITHUB_API_TOKEN")
        if not self._name or not self._token:
            print('Please provide token and name')
            self.exit_app()

    def main_menu(self):
        self.show_head()
        self._init_data()
        while True:
            self.smart_printer.print_center(text='Main Menu:')
            print('1: Clone repositories')
            print('2. Clone gists')
            print('3. Clone repositories + gists + create archive')
            print('0. Exit')
            choice = input('Enter a choice: ')
            self.smart_printer.print_center()
            if choice == '1':
                self.clone_repositories()
            elif choice == '2':
                self.clone_gists()
            elif choice == '3':
                self.clone_repositories_and_gists()
            elif choice == '0':
                self.exit_app()
            else:
                self.show_error('Invalid choice')

    @staticmethod
    def _continue():
        input('Press enter to continue... ')

    def show_error(self, msg):
        self.smart_printer.print_framed(msg)

    def show_head(self):
        self.smart_printer.show_head(text=Config.app_name)

    def show_footer(self):
        self.smart_printer.show_footer(url=Config.help_url, copyright_=Config.copyright_)

    def clone_repositories(self):
        self.smart_printer.print_center('Cloning repositories:')
        print('Please wait...')
        repo_data_master = ReposDataMaster(self._name, self._token)
        repos = repo_data_master.get_data()
        print(f'GitHub name: {self._name} | Repositories: {len(repos)}')
        self.repo_clone_master.clone_repo(name=self._name, repos=repos)

    def clone_gists(self):
        self.smart_printer.print_center('Cloning gists:')
        print('Please wait...')
        gists_data_master = GistsDataMaster(self._name, self._token)
        gists = gists_data_master.get_data()
        print(f'GitHub name: {self._name} | Gists: {len(gists)}')
        self.repo_clone_master.clone_repo(name=self._name, gists=gists)

    def clone_repositories_and_gists(self):
        self.smart_printer.print_center('Cloning repositories + gists + create archive:')
        self.clone_repositories()
        self.clone_gists()
        self.create_archive()

    def create_archive(self):
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{self._name}_github_backup')
        if os.path.exists(clone_path):
            archive_creator = ArchiveCreator(folder_path=clone_path)
            archive_creator.create_archive()
        else:
            print(f'Could not create archive. Path {clone_path} not found')

    def exit_app(self):
        self.show_footer()
        sys.exit(0)
