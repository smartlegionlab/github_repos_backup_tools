# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import urllib.request
import urllib.error
import json


class GitHubDataMaster:
    def __init__(self, name: str, token: str, url: str):
        self._name = name
        self._token = token
        self._url = url

    @property
    def headers(self) -> dict:
        return {'Authorization': f'token {self._token}'}

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

    def get_data(self) -> list:
        clone_urls = []
        page = 1
        per_page = 100

        while True:
            url = f"{self._url}?page={page}&per_page={per_page}"
            req = urllib.request.Request(url, headers=self.headers)
            try:
                with urllib.request.urlopen(req) as response:
                    if response.status == 200:
                        data = json.loads(response.read().decode('utf-8'))
                        if not data:
                            break
                        clone_urls.extend(data)
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

        return clone_urls


class ReposDataMaster(GitHubDataMaster):
    def __init__(self, name: str, token: str):
        super().__init__(name, token, url='https://api.github.com/user/repos')


class GistsDataMaster(GitHubDataMaster):
    def __init__(self, name: str, token: str):
        super().__init__(name, token, url='https://api.github.com/gists')
