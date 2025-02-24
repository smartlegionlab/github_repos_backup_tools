# GitHub Repositories Backup Tools <sup>v0.7.0</sup>

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

GitHub Repositories Backup Tools <sup>v0.7.0</sup>

#### **1. Enhanced Repository Cloning Mechanism**
   - **Problem:** 
     - Cloning repositories occasionally failed due to network timeouts, unstable connections, or large repository sizes. This led to incomplete or corrupted clones, requiring manual intervention.
   - **Solution:**
     - Implemented a robust retry mechanism for cloning and updating repositories. If a clone operation fails due to a timeout or other errors, the application automatically retries the operation after a short delay.
     - Added a fallback mechanism: if a repository cannot be cloned after multiple attempts, it is marked as failed, and the user is notified.
     - Improved the `git pull` functionality to ensure that existing repositories are updated correctly, even in cases of merge conflicts or network issues.

#### **2. Error Handling and Recovery**
   - **Problem:**
     - The application previously lacked proper error handling, which made it difficult to diagnose and recover from failures during cloning or updating.
   - **Solution:**
     - Added comprehensive error handling for Git operations (e.g., `git clone`, `git pull`). Errors are now logged and displayed to the user with clear messages.
     - Implemented a cleanup mechanism: if a repository or gist fails to clone or update, the application removes any partially cloned files to avoid leaving the system in an inconsistent state.
     - Added a retry loop for failed operations, ensuring that transient issues (e.g., network glitches) do not cause permanent failures.

#### **3. Improved User Interface**
   - **Problem:**
     - The previous user interface lacked clarity and did not provide sufficient feedback during long-running operations, making it difficult for users to understand the application's progress.
   - **Solution:**
     - Enhanced the console output with detailed progress updates, including the current step, the number of repositories/gists processed, and the status of each operation (e.g., "Cloning repository X/Y").
     - Added visual indicators (e.g., success/failure icons) to make it easier to identify which operations completed successfully and which failed.
     - Improved the formatting of messages and added separators (e.g., `---`) to make the output more readable and structured.

#### **4. Timeout Management**
   - **Problem:**
     - Git operations sometimes hung indefinitely due to network issues or large repositories, causing the application to become unresponsive.
   - **Solution:**
     - Added configurable timeouts for Git operations (`git clone`, `git pull`). If an operation exceeds the timeout, it is automatically aborted, and the application retries or marks it as failed.

#### **5. Code Refactoring and Maintainability**
   - **Problem:**
     - The codebase had significant duplication and did not fully adhere to SOLID principles, making it difficult to maintain and extend.
   - **Solution:**
     - Refactored the code to reduce duplication and improve modularity. For example, the logic for cloning repositories and gists was consolidated into a single method with reusable components.
     - Improved adherence to SOLID principles by separating concerns (e.g., moving Git operations into a dedicated utility class) and using dependency injection for better testability.

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
1/10: Cloning: repo2
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