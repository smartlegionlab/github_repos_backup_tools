# GitHub Repositories Backup Tools <sup>v0.7.1</sup>

---

> An application for automatic cloning of GitHub repositories (including private ones).

- Cloning repositories.
- Cloning gist.
- Creating an archive of the main folder with cloned repositories and gist.
- Shutting down the computer after cloning.

The folder and archive with cloned repositories are stored in your home directory.

***

Author and developer: ___A.A. Suvorov___

***

### **What's New:**

GitHub Repositories Backup Tools <sup>v0.7.1</sup>

- Added retry logic to all methods fetching data from GitHub API
- Implemented a max retries limit with a delay between attempts
- Improved error handling and logging for failed requests
- Ensured requests are retried until a 200 status is received or max retries are reached

***

```
************************************************************************************************************************************************************
------------------------------------------------------------- Github Repositories Backup Tools -------------------------------------------------------------
Getting a token from a .config.ini file...
✅ Token successfully received!
Token is valid: Yes
------------------------------------------------------------------------------------------------------------------------------------------------------------
Getting user login...
✅ Login: john_doe
------------------------------------------------------------------------------------------------------------------------------------------------------------
Parsing arguments:

✅ Clone repositories: Yes
✅ Clone gists: Yes
✅ Make archive: Yes
✅ Shutdown: No
------------------------------------------------------------------------------------------------------------------------------------------------------------
Forming a path to the directory:
Path: /home/john_doe/john_doe_github_backup

------------------------------------------------------------------ Cloning repositories:  ------------------------------------------------------------------
Target directory: /home/john_doe/john_doe_github_backup/repositories
Getting repositories...
Found 10 repositories.

------------------------------------------------------------------ Cloning repositories:  ------------------------------------------------------------------

--------------------------------------
1/10: Cloning: repo1
--------------------------------------
✅ Repository cloned successfully: /home/john_doe/john_doe_github_backup/repositories/repo1
--------------------------------------
2/10: Cloning: repo2
⚠ Pull operation timed out: 
/home/john_doe/john_doe_github_backup/repositories/repo2
⚠ Pull failed. Removing and recloning: 
/home/john_doe/john_doe_github_backup/repositories/ repo2
✅ Repository cloned successfully: 
/home/john_doe/john_doe_github_backup/repositories/repo2
--------------------------------------
```

## Help:

- `cd ~`
- Clone or download project
- `cd github_repos_backup_tools`
- Create file `.config.ini`:

### How to generate a token? 

- [Follow the link and create Personal access tokens (classic)](https://github.com/settings/tokens/new)
- Press 'Generate new token'. 
- Select "repo"
- Select "gist"
- Generate the token.
- Copy the token.


Example file`.config.ini`:
```ini
[github]
token = your_github_token
```


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

`python app.py` or `python app.py -r -g` - Perform automatic cloning of both repositories and gists.

- `-r` - Clone GitHub repositories.
- `-g` - Clone GitHub gists.
- `--archive` - Create archive.
- `--shutdown` - Turn off the device after completing all actions.

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
    Copyright © 2018-2025, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------