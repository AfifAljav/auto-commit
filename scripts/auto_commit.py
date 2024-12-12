import os
import random
import subprocess
from datetime import datetime

REPO_DIR = "."
LOG_FILE = os.path.join(REPO_DIR, "logs", "commit_log.txt")

def make_commits(min_commits=100, max_commits=200):
    """Create a random number of commits between min_commits and max_commits."""
    commit_count = random.randint(min_commits, max_commits)
    print(f"Creating {commit_count} commits.")
    with open(LOG_FILE, "a") as log_file:
        for i in range(commit_count):
            dummy_file_path = os.path.join(REPO_DIR, "dummy.txt")
            with open(dummy_file_path, "a") as dummy_file:
                dummy_file.write(f"Commit {i+1} at {datetime.now()}\n")
            subprocess.run(["git", "add", dummy_file_path], cwd=REPO_DIR)
            commit_message = f"Auto commit #{i+1}"
            subprocess.run(["git", "commit", "-m", commit_message], cwd=REPO_DIR)
            log_file.write(f"{datetime.now()}: {commit_message}\n")
    return commit_count

def push_changes():
    """Push all commits to the remote repository."""
    subprocess.run(["git", "push"], cwd=REPO_DIR)

if __name__ == "__main__":
    # Convert environment variables to integers
    min_commits = int(os.getenv("MIN_COMMITS", "100"))
    max_commits = int(os.getenv("MAX_COMMITS", "200"))
    make_commits(min_commits, max_commits)
    push_changes()
