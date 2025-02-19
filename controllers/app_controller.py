# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os

from models.github_data_master import ReposDataMaster, GistsDataMaster
from models.repo_clone_master import RepoCloneMaster
from models.archive_creator import ArchiveCreator
from views.main_view import MainView


class AppController:
    def __init__(self, name: str, token: str):
        self.name = name
        self.token = token
        self.view = MainView()

    def clone_repositories(self, archive: bool):
        data_master = ReposDataMaster(self.name, self.token)
        items = data_master.get_data()
        clone_master = RepoCloneMaster(self.name, self.token)
        clone_master.clone(items, 'repositories')
        if archive:
            self._create_archive()

    def clone_gists(self, archive: bool):
        data_master = GistsDataMaster(self.name, self.token)
        items = data_master.get_data()
        clone_master = RepoCloneMaster(self.name, self.token)
        clone_master.clone(items, 'gists')
        if archive:
            self._create_archive()

    def _create_archive(self):
        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, f'{self.name}_github_backup')
        if os.path.exists(clone_path):
            archive_creator = ArchiveCreator(clone_path)
            archive_creator.create_archive()
        else:
            self.view.show_error("Clone path not found")
