import os
import subprocess
import shutil

def clone_repo(repo_url, clone_dir):
    if not os.path.exists(clone_dir):
        print("Cloning...")
        subprocess.run(['git', 'clone', repo_url, clone_dir], check=True)


