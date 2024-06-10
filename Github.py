import subprocess

# Initialize a new Git repository
# git init
subprocess.run(["git", "init"])

# Clone a repository from GitHub
# git clone https://github.com/username/repository.git
subprocess.run(["git", "clone", "https://github.com/username/repository.git"])

# Stage changes for commit
# git add .
subprocess.run(["git", "add", "."])

# Commit changes with a descriptive message
# git commit -m "Initial commit"
subprocess.run(["git", "commit", "-m", "Initial commit"])

# Push changes to a remote repository
# git push origin main
subprocess.run(["git", "push", "origin", "main"])

# List branches
# git branch
subprocess.run(["git", "branch"])

# Switch to a different branch
# git checkout feature-branch
subprocess.run(["git", "checkout", "feature-branch"])

# Merge changes from one branch to another
# git merge feature-branch
subprocess.run(["git", "merge", "feature-branch"])

# Pull changes from a remote repository
# git pull origin main
subprocess.run(["git", "pull", "origin", "main"])


git clone https://github.com/username/repository.git
git branch feature-branch
git checkout feature-branch
git add .
git commit -m "Add new feature"
git push origin feature-branch
