# Batch File Update Script for GitHub Repositories

This Python script automates the process of updating a specific file across multiple GitHub repositories.
It allows for the batch replacement of text within a specified file, commits the changes to a new branch, creates a pull request, and assigns reviewers.

## Features

- Updates a specified file in multiple repositories with text replacement.
- Creates a new branch for the changes.
- Commits the updated file with a custom message.
- Opens a pull request against a specified base branch.
- Assigns designated reviewers to the pull request.

## Prerequisites

- Python 3.x
- GitHub Personal Access Token with `repo` scope
- `PyGithub` and `python-dotenv` libraries

## Setup Instructions

1. **Install Python Dependencies**

   Run the following command to install the necessary libraries:

   ```bash
   pip install -r requirements.txt
   ```
2. **Configure Environment Variables**

   Create a `.env` file in the root directory of your project and add your GitHub Personal Access Token:
   ```bash
   GITHUB_TOKEN=your_token_here
   ```
   Replace your_token_here with your actual token.
3. **Prepare Configuration Files**

   - Repositories List: Create a file listing the repositories to update (e.g., repos.txt), with one repository per line in the format org/repo.
   - Reviewers List: Create a file listing the GitHub usernames of the reviewers (e.g., reviewers.txt), one per line.

## Running the Script
   ### Using the Shell Script
   To simplify running the Python script with all necessary arguments, a shell script run_update.sh is provided.
   Before running this script, ensure you have made it executable:
   ```bash
   chmod +x run_update.sh
   ```
   Then, run the script by executing:
   ```bash
   ./run_update.sh
   ```

   ### Direct Usage
   Alternatively, you can run the Python script directly using the following command format:
   ```bash
   python main.py \
  --base-branch "main" \
  --new-branch "feature/update-text" \
  --file-path "path/to/file.yml" \
  --original-text "old text" \
  --replacement-text "new text" \
  --commit-message "Update text in file.yml" \
  --pr-title "Update Text in file.yml" \
  --pr-body "This PR updates the text in file.yml. Please review." \
  --repos-file "repos.txt" \
  --reviewers-file "reviewers.txt" \
  --output-file "pr_links.txt"
   ```
   Replace the argument values with your specific update requirements.

## Use-cases
1. #### Update .gitignore Files
   Automatically add new rules or remove outdated entries across all `.gitignore` files.

2. #### Fix Typos
   Effortlessly correct common typos or mistakes that have been replicated across documentation, comments, or code.

3. #### Update Configuration Files
   Uniformly apply updates to various configuration files such as `.editorconfig`, `Dockerfile`, and CI/CD pipeline configurations.

4. #### Revise Legal License Text or Copyright Headers
   Batch update legal notices, license text, or copyright headers in source files across all repositories to comply with legal requirements and reflect current information.

5. #### Update URLs Organization-wide
   Synchronize updates of crucial URLs like API endpoints, Nexus URLs, etc. 

## Customization
   You can customize the script for different files, text replacements, or repositories by adjusting the command-line arguments or editing run_update.sh.

## Security Note
   Ensure your .env file and personal access token are kept secure and not exposed publicly.

## Contributing
   Contributions to improve the script or add new features are welcome. Please submit a pull request or issue on GitHub.