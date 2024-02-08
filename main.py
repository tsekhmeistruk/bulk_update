import argparse
from github import Github
from dotenv import load_dotenv
import os


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Batch update files across GitHub repositories.")
    parser.add_argument("--base-branch", required=True, help="Base branch for pull requests.")
    parser.add_argument("--new-branch", required=True, help="New branch for changes.")
    parser.add_argument("--file-path", required=True, help="File path to update.")
    parser.add_argument("--original-text", required=True, help="Text to replace.")
    parser.add_argument("--replacement-text", required=True, help="Replacement text.")
    parser.add_argument("--commit-message", required=True, help="Commit message.")
    parser.add_argument("--pr-title", required=True, help="Pull request title.")
    parser.add_argument("--pr-body", required=True, help="Pull request body.")
    parser.add_argument("--repos-file", required=True, help="File containing repository list.")
    parser.add_argument("--reviewers-file", required=True, help="File containing reviewers list.")
    parser.add_argument("--output-file", required=True, help="File to write PR links to.")
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Load the GitHub token from .env
    load_dotenv()
    token = os.getenv('GITHUB_TOKEN')
    github_client = Github(token)

    # Load repositories and reviewers from files
    with open(args.repos_file, "r") as file:
        repos = [line.strip() for line in file]

    with open(args.reviewers_file, "r") as file:
        reviewers = [line.strip() for line in file]

    pr_links = []

    for repo_name in repos:
        try:
            repo = github_client.get_repo(repo_name)
            default_branch = repo.get_branch(args.base_branch)
            repo.create_git_ref(ref=f"refs/heads/{args.new_branch}", sha=default_branch.commit.sha)
            contents = repo.get_contents(args.file_path, ref=args.new_branch)
            updated_content = contents.decoded_content.decode().replace(args.original_text, args.replacement_text)
            repo.update_file(contents.path, args.commit_message, updated_content, contents.sha, branch=args.new_branch)
            pull = repo.create_pull(title=args.pr_title, body=args.pr_body, head=args.new_branch, base=args.base_branch)

            for reviewer in reviewers:
                try:
                    pull.create_review_request(reviewers=[reviewer])
                except Exception as e:
                    print(f"Warning: Could not add {reviewer} as a reviewer to {repo_name}: {e}")

            pr_links.append(pull.html_url)
            print(f"PR created successfully for {repo_name}")
        except Exception as e:
            print(f"Failed to process {repo_name}: {e}")

    # Save the PR links to the specified output file
    with open(args.output_file, "w") as output_file:
        output_file.write("Please review the PRs:\n")
        output_file.writelines(f"{link}\n" for link in pr_links)


if __name__ == "__main__":
    main()
