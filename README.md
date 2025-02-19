# GitHub Repositories Backup Tool <sup>v0.6.0</sup>

---

> An application for automatic cloning of GitHub repositories (including private ones).

- Cloning repositories, including private ones.
- Cloning gist, including private ones.
- Creating an archive of the main folder with cloned repositories and gist.

The folder and archive with cloned repositories are stored in your home directory.

***

Author and developer: ___A.A. Suvorov___

***

## What's new:

- Cloning without pre-generating and adding an ssh key to GitHub.
- Cloning/Updating has become easier and faster.

***

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
github_name = your_github_username
```

### Use:

`python main.py` or `python main.py -r -g` - Perform automatic cloning of both repositories and gists.

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
    Copyright © 2024-2025, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------