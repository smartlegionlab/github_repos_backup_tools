# GitHub Repositories Backup Tool <sup>v0.2.0</sup>

---

> Application for creating backup copies of repositories and gists on GitHub.
> Creates a "your_name_github_backup" folder in the user's home folder and clones repositories and gists into it.

***


## Images:

![logo](https://github.com/smartlegionlab/github_repos_backup_tools/raw/master/data/images/github_repos_backup_tools.png)

***

Author and developer: ___A.A. Suvorov___

***

## What's new:

github_repos_backup_tools v0.2.0

- Completely rewritten application code
- Fixed bugs
- Improved performance
- Added the ability to clone gists
- Added main menu with the ability to select cloning (repositories, gists, repositories + gists)
- Renamed the main folder for storing repositories
- Gists and repositories are stored in different folders inside the main folder
- Cloning a repository + gists will create an archive of the main folder.

***

## Help:

> ATTENTION! Before running the application, you must generate an ssh key for GitHub on your system and add it to your GitHub account.

> You can use a ready-made tool: [github-ssh-key](https://github.com/smartlegionlab/github-ssh-key/) or:

- `ssh-keygen -t ed25519 -C "email@gmail.com"` Replace with your email.
- `eval "$(ssh-agent -s)"`
- `ssh-add ~/.ssh/id_ed25519`

Copy the key from the `/home/name/.ssh/id_ed25519.pub` file and add it to your GitHub account.
- View and copy the key: `cat /home/name/.ssh/id_ed25519.pub`
- [Link to adding a key to GitHub](https://github.com/settings/keys)

- `ssh-keyscan github.com >> ~/.ssh/known_host`
- `ssh -T git@github.com`

The check should be successful.

- `cd ~`
- [Download project in HOME dir](https://github.com/smartlegionlab/github_repos_backup_tools/archive/refs/heads/master.zip) or: `wget -P https://github.com/smartlegionlab/github_repos_backup_tools/archive/refs/heads/master.zip` 
- Create a folder "github_repos_backup_tools" and unzip the archive with the project into it. For example: `unzip master.zip -d github_repos_backup_tools`.
- Go to your project folder. Or: `cd github_repos_backup_tools`
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- Create file .env or `echo -e "GITHUB_API_TOKEN=TOKEN\nGITHUB_NAME=USERNAME" > .env`
- Add keys and values to the file, where the value are your GitHub api token and GitHub username:

> How to generate a token? [Follow the link and create Personal access tokens (classic)](https://github.com/settings/tokens/new). Press 'Generate new token'. Select "repo", select "gist", generate and copy the token.

Exemple file`.env`:
```text
GITHUB_API_TOKEN=<YOUR TOKEN>
GITHUB_NAME=<YOUR USERNAME>
```
- `python app.py`

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
    Copyright © 2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------