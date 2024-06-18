# GitHub Repositories Backup Tool

---

> Application for creating backup copies of repositories on GitHub.
> Creates a github_repositories folder in the user's home folder and clones repositories into it.

***

Author and developer: ___A.A. Suvorov___

***

## Help:

> ATTENTION! Before running the application, you must generate an ssh key for GitHub on your system and add it to your GitHub account.

- `ssh-keygen -t ed25519 -C "email@gmail.com"` Replace with your email
- `eval "$(ssh-agent -s)"`
- `ssh-add ~/.ssh/id_ed25519`

Copy the key from the `.ssh/id_ed25519.pub` file and add it to your GitHub account.

- `ssh -T git@github.com`
- `ssh-keyscan github.com >> ~/.ssh/known_host`

The check should be successful.

- Download project.
- Unzip the project.
- Go to your project folder.
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- Create file .env
- Add keys and values to the file, where the value are your GitHub api token and GitHub username:

```python
GITHUB_API_TOKEN=TOKEN
GITHUB_NAME=USERNAME
```
- `python app.py`

***

## In the plans:

1. Archiving the folder with cloned repositories.
2. Uploading the created archive to Google Disk.

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------