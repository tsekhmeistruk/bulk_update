#!/bin/bash

# Define variables
BASE_BRANCH="main"
NEW_BRANCH="feature/update-text"
FILE_PATH="path/to/file.yml"
ORIGINAL_TEXT="old text"
REPLACEMENT_TEXT="new text"
COMMIT_MESSAGE="Update text in file.yml"
PR_TITLE="Update Text in file.yml"
PR_BODY="This PR updates the text in file.yml. Please review."
REPOS_FILE="repos.txt"
REVIEWERS_FILE="reviewers.txt"
OUTPUT_FILE="pr_links.txt"

# Run the Python script with the provided arguments
py main.py \
  --base-branch "$BASE_BRANCH" \
  --new-branch "$NEW_BRANCH" \
  --file-path "$FILE_PATH" \
  --original-text "$ORIGINAL_TEXT" \
  --replacement-text "$REPLACEMENT_TEXT" \
  --commit-message "$COMMIT_MESSAGE" \
  --pr-title "$PR_TITLE" \
  --pr-body "$PR_BODY" \
  --repos-file "$REPOS_FILE" \
  --reviewers-file "$REVIEWERS_FILE" \
  --output-file "$OUTPUT_FILE"

echo "Script execution completed."
