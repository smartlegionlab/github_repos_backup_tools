# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import urllib.request
import urllib.error
import json


class GitHubDataMaster:
    def __init__(self, token=None):
        self._token = token
        self.login = None
        self.repositories = {}
        self.gists = {}

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def headers(self) -> dict:
        return {'Authorization': f'token {self._token}'}

    def fetch_user_data(self):
        url = "https://api.github.com/user"
        req = urllib.request.Request(url, headers=self.headers)
        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    self.login = data.get('login')
                else:
                    raise Exception(f"Error: {response.status} - {response.read().decode('utf-8')}")
        except urllib.error.HTTPError as e:
            print(f"HTTP error occurred: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            print(f"URL error occurred: {e.reason}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def fetch_repositories(self):
        url = "https://api.github.com/user/repos"
        self.repositories = self._fetch_data(url, is_repo=True)

    def fetch_gists(self):
        url = "https://api.github.com/gists"
        self.gists = self._fetch_data(url, is_repo=False)

    def _fetch_data(self, url: str, is_repo: bool) -> dict:
        data_dict = {}
        page = 1
        per_page = 100

        while True:
            paginated_url = f"{url}?page={page}&per_page={per_page}"
            req = urllib.request.Request(paginated_url, headers=self.headers)
            try:
                with urllib.request.urlopen(req) as response:
                    if response.status == 200:
                        data = json.loads(response.read().decode('utf-8'))
                        if not data:
                            break
                        for item in data:
                            if is_repo:
                                data_dict[item['full_name']] = item['ssh_url']
                            else:
                                data_dict[item['id']] = item['git_pull_url']
                        page += 1
                    else:
                        raise Exception(f"Error: {response.status} - {response.read().decode('utf-8')}")
            except urllib.error.HTTPError as e:
                print(f"HTTP error occurred: {e.code} - {e.reason}")
                break
            except urllib.error.URLError as e:
                print(f"URL error occurred: {e.reason}")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                break

        return data_dict

    def is_token_valid(self) -> bool:
        url = "https://api.github.com/user"
        req = urllib.request.Request(url, headers=self.headers)
        try:
            with urllib.request.urlopen(req) as response:
                return response.status == 200
        except urllib.error.HTTPError as e:
            if e.code == 401:
                return False
            raise
        except urllib.error.URLError as e:
            print(f"URL error occurred: {e.reason}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return False
