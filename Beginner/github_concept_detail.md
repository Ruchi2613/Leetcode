# 📘 Git & GitHub Essentials — Notebook Style

---

Git is a **version control system** that helps track changes in your code over time. It’s free, open-source, fast, and scalable, and is widely used by developers to collaborate and maintain project history efficiently. GitHub is a **web-based platform** where developers can store, manage, and share their Git repositories. It acts like a central place for hosting and collaborating on code, especially in teams.

---

Before working with Git, it’s important to set your identity using `git config --global user.name "Your Name"` and `git config --global user.email "your_email@example.com"`. You can check your settings with `git config --list`. Once configured, the typical workflow starts by **adding changes** to the staging area using `git add filename.txt` to add a specific file, or `git add .` to stage all modified files. After staging, you **commit** those changes with a message using `git commit -m "Your commit message"`. This creates a snapshot of your code history.

---

### 🔀 Difference Between `git clone` and `git remote`

A common point of confusion is the difference between `git clone` and `git remote`. While both are used to work with remote repositories (usually hosted on GitHub), they serve different purposes.

**`git clone`** is used when you want to **download an entire repository from a remote source (like GitHub) to your local machine**. It creates a complete copy of the repository — including its files, branches, and commit history — and automatically sets up the connection to the remote repo. For example, `git clone https://github.com/user/repository.git` will clone the project into a local folder and link it to the original GitHub repo. After cloning, you can run commands like `git push`, `git pull`, or `git fetch` because the remote connection is already established.

On the other hand, **`git remote`** is used to **manually link your local Git project to a remote repository**. If you’ve already initialized a Git repo locally using `git init`, but haven’t connected it to GitHub yet, you can do so using `git remote add origin https://github.com/user/repository.git`. This sets up the remote connection so that you can later push your code to GitHub with `git push`. You can verify the linked remote using `git remote -v`.

**In short:** `git clone` downloads a project and connects it automatically to the remote, while `git remote` is for manually linking a local project to a remote repository.

---

After cloning or setting the remote, you can push your code using `git push -u origin main`. The `-u` flag sets the upstream so that future pushes can be done simply with `git push`. Use `git status` to check the current state of your working directory — it tells you if files are modified, untracked, staged, or unstaged. You can switch between branches with `git checkout branch_name` or `git switch branch_name`, create new branches with `git checkout -b new_branch`, and delete them with `git branch -d branch_name`. List branches with `git branch`.

To view commit history, use `git log`. To compare changes, `git diff` shows the difference between your working directory and the staging area, between branches, or between commits — e.g., `git diff commit1 commit2` or `git diff main feature-branch`.

---

A **fork** on GitHub is like making your own copy of someone else’s repository. It lives in your GitHub account and lets you experiment with changes without affecting the original project. After forking, you can clone your fork (`git clone https://github.com/your-username/repo.git`), make changes locally, push to your fork (`git push origin main`), and then create a pull request to propose changes to the original repository.

---

### Self-Check & Troubleshooting

Make sure you're in the correct directory by running `pwd`, and check for the `.git` folder using `ls -a`. If the folder is missing or the clone is broken, you can delete it (`rm -rf folder_name`) and clone again using `git clone https://github.com/user/repository.git`. After that, go into the directory with `cd repo_name` and run `git status` to check if everything is working.

---

### Understanding File States in Git: Untracked, Staged, and Unstaged
In Git, every file in your working directory goes through different states based on what you’ve done with it — whether it's newly created, modified, or ready to be committed. When you create a new file in your project folder, Git doesn’t automatically track it. This is called an untracked file. It means Git sees the file in your folder, but it’s not yet part of version control. To start tracking it, you need to add it to the staging area using git add filename.

Once you run git add, the file enters the staged state. This means Git is now aware of your changes and is preparing to include them in the next commit. Think of the staging area like a “preview” of what will be committed. Only staged files are included when you run git commit.

Meanwhile, files that have already been tracked by Git (e.g., from previous commits) and have since been changed, but not yet staged, are called unstaged. Git sees the changes, but won’t include them in a commit unless you explicitly add them to the staging area again using git add.

To summarize: untracked files are new and ignored until added; unstaged files are modified but not yet prepared for commit; and staged files are ready to be committed to the repository. You can use git status to see all of these at any time and know exactly what’s going on with your files.


---
### Summary Table
State	                 Description	                                Action to Fix
Untracked	       New file not tracked by Git	                      git add filename
Staged	           File ready to be committed	                      git commit -m "message"
Unstaged	       File modified but not ready for commit	          git add filename to stage it
