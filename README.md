# GitHub Repositories Backup Tool <sup>v0.4.0</sup>

---

> An application for creating backup copies of repositories and GitHub (including private ones).

- Cloning repositories, including closed ones. (Automatic/Manual).
- Cloning gists, including closed ones. (Automatic/Manual).
- Creating an archive of the main folder with cloned repositories and gists (Automatic/Manual).
- Launch in "Menu mode"/"Launch in console with additional parameters".

The folder and archive with cloned repositories are stored in your home directory.

***


## Images:

![logo](https://github.com/smartlegionlab/github_repos_backup_tools/raw/master/data/images/github_repos_backup_tools.png)

***

Author and developer: ___A.A. Suvorov___

***

## What's new:

github_repos_backup_tools v0.4.0

- Removed all dependencies, project is now self-contained and does not require any external libraries to be installed.

***

## Help:

> ATTENTION! Before running the application, you must generate an ssh key 
> for GitHub on your system and add it to your GitHub account.

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
- Create file `.config.ini`:

> How to generate a token? [Follow the link and create Personal access tokens (classic)](https://github.com/settings/tokens/new). Press 'Generate new token'. Select "repo", select "gist", generate and copy the token.


Example file`.config.ini`:
```ini
[github]
token = your_github_token
github_name = your_github_username
```

### Use:

- `python app.py`. Show main menu.
- `python app.py -r` - Automatically clone GitHub repositories without creating an archive.
- `python app.py -r --no-auto` - Manually select GitHub repositories to clone without creating an archive.
- `python app.py -r --archive` - Automatically clone GitHub repositories with the creation of an archive.
- `python app.py -r --archive --no-auto` - Manually select GitHub repositories to clone with archive creation.
- `python app.py -g` - Automatically clone GitHub gists without creating an archive.
- `python app.py -g --no-auto` - Manually select GitHub gists to clone without creating an archive.
- `python app.py -g --archive` - Automatically clone GitHub gists with the creation of an archive.
- `python app.py -g --archive --no-auto` - Manually select GitHub gists to clone with archive creation.
- `python app.py -r -g` - Automatically clone GitHub repositories and gists without creating an archive.
- `python app.py -r -g --no-auto` - Manually select GitHub repositories and gists to clone without creating an archive.
- `python app.py -r -g --archive` - Automatically clone GitHub repositories and gists, and create archive.
- `python app.py -r -g --archive --no-auto` - Manually select GitHub repositories and gists to clone with archive creation.

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