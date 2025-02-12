# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from models.repo_clone_master import RepoCloneMaster
from models.github_data_master import ReposDataMaster, GistsDataMaster


class CloneController:
    def __init__(self, name: str, token: str):
        self.name = name
        self.token = token

    def clone_repositories(self, auto_mode: bool):
        data_master = ReposDataMaster(self.name, self.token)
        items = data_master.get_data()
        clone_master = RepoCloneMaster(self.name)
        clone_master.clone(items, 'repositories')

    def clone_gists(self, auto_mode: bool):
        data_master = GistsDataMaster(self.name, self.token)
        items = data_master.get_data()
        clone_master = RepoCloneMaster(self.name)
        clone_master.clone(items, 'gists')
