# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os

from tools.archive_creator import ArchiveCreator
from tools.config import Config
from tools.github_data_master import ReposDataMaster, GistsDataMaster
from tools.repo_clone_master import RepoCloneMaster
from tools.smart_printer import SmartPrinter


class AppManager:
    def __init__(self):
        self.smart_printer = SmartPrinter()
        self.repo_clone_master = RepoCloneMaster()
        self._name = None
        self._token = None

    @staticmethod
    def _to_continue():
        input('Press enter to continue... ')

    @staticmethod
    def get_action(title):
        action = input(title)
        if action == 'y':
            return True
        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("The name must be a string.")
        self._name = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        if not isinstance(value, str):
            raise ValueError("The token must ba a string.")
        self._token = value

    def show_head(self):
        self.smart_printer.show_head(text=Config.app_name)

    def show_footer(self):
        self.smart_printer.show_footer(url=Config.help_url, copyright_=Config.copyright_)

    def show_error(self, msg):
        self.smart_printer.print_framed(msg)
        self._to_continue()

    def main_menu(self):
        while True:
            self.smart_printer.print_center(text='Main Menu:')
            print('1: Clone repositories')
            print('2. Clone gists')
            print('3. Clone repositories + gists')
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
                break
            else:
                self.show_error('Invalid choice')

    def _clone(self, archive_flag, auto_mode, type_):
        print('Please wait...')
        if type_ == 'repositories':
            repo_data_master = ReposDataMaster(self._name, self._token)
            items = repo_data_master.get_data()
            repo_type = 'Repositories'
        else:
            gists_data_master = GistsDataMaster(self._name, self._token)
            items = gists_data_master.get_data()
            repo_type = 'Gists'
        self.smart_printer.print_center()
        self.smart_printer.print_center(f'GitHub name: {self._name} | {repo_type}: {len(items)}')
        if auto_mode is None:
            self.smart_printer.print_center()
            auto_mode = self.get_action('Automatic cloning? y|n: ')
        if archive_flag is None:
            self.smart_printer.print_center()
            archive_flag = self.get_action('Create archive? y|n: ')
        if type_ == 'repositories':
            self.repo_clone_master.clone(name=self._name, items=items, auto_mode=auto_mode, type_=type_)
        else:
            self.repo_clone_master.clone(name=self._name, items=items, auto_mode=auto_mode, type_=type_)
        if archive_flag:
            self.smart_printer.print_center()
            self.create_archive()

    def clone_repositories(self, archive_flag=None, auto_mode=None):
        self.smart_printer.print_center('Cloning repositories:')
        self._clone(archive_flag, auto_mode, type_='repositories')

    def clone_gists(self, archive_flag=None, auto_mode=None):
        self.smart_printer.print_center('Cloning gists:')
        self._clone(archive_flag, auto_mode, type_='gists')

    def clone_repositories_and_gists(self, archive_flag=None, auto_mode=None):
        self.smart_printer.print_center('Cloning repositories + gists:')
        self.clone_repositories(archive_flag=False, auto_mode=auto_mode)
        self.clone_gists(archive_flag=False, auto_mode=auto_mode)
        if archive_flag is None:
            self.smart_printer.print_center()
            archive_flag = self.get_action('Create archive? y|n: ')
        if archive_flag:
            self.smart_printer.print_center()
            self.create_archive()

    def create_archive(self):
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{self._name}_github_backup')
        if os.path.exists(clone_path):
            archive_creator = ArchiveCreator(folder_path=clone_path)
            archive_creator.create_archive()
        else:
            print(f'Could not create archive. Path {clone_path} not found')
