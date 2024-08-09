# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import requests


class GitHubDataMaster:
    def __init__(self, name, token, url):
        self._name = name
        self._token = token
        self._url = url

    @property
    def headers(self):
        return {'Authorization': f'token {self._token}'}

    def get_data(self):
        clone_urls = []
        page = 1
        per_page = 100

        while True:
            params = {'page': page, 'per_page': per_page}
            response = requests.get(self._url, headers=self.headers, params=params)
            data = response.json()
            if not data:
                break

            for repo in data:
                clone_urls.append(repo)

            page += 1
        return clone_urls


class ReposDataMaster(GitHubDataMaster):
    def __init__(self, name, token):
        super().__init__(name, token, url=f'https://api.github.com/user/repos')


class GistsDataMaster(GitHubDataMaster):
    def __init__(self, name, token):
        super().__init__(name, token, url=f'https://api.github.com/gists')
