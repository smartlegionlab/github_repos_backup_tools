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


class Validators:
    @staticmethod
    def validate_token(token: str) -> bool:
        return bool(token) and len(token) == 40

    @staticmethod
    def validate_name(name: str) -> bool:
        return bool(name) and len(name) > 0

    @classmethod
    def is_token_valid(cls, token: str) -> bool:
        url = "https://api.github.com/user"
        headers = {
            "Authorization": f"token {token}",
            "User-Agent": "Python"
        }

        request = urllib.request.Request(url, headers=headers)

        try:
            with urllib.request.urlopen(request) as response:
                return response.status == 200
        except urllib.error.HTTPError as e:
            if e.code == 401:
                print('WARNING! The token is invalid or expired.')
                return False
            else:
                print(f"Error: {e.code} - {e.reason}")
                return False
