## Welcome To Git Guide Beginner!

- I am muhammed, adding this from `for-conflict`
- I love programming especially `Java`
- I am adding this from `for-conflict2`

// git branch new-branch-name source-branch : This command lets you to create a branch that it inherited from the source (You selected by source-branch) branch.

/\*

Useful git commands:

git init -> To initialize git repo on local

git log -> To see all commits

git status -> To see repository state (commits, merges) etc.

git add -> To stage the changes

git commit -m 'Some messege' -> To apply staged changes with a explentation messege

git remote add origin <Repo Link> -> To link local repo with github repo

git push -> To add changes to github after commiting

git pull -> To get all changes from github that you don't have on local

git merge <branch-name> -> To merge branches (if you are working on different branch and you wanna pull changes from another branch)

git fetch origin main -> Fetches changes from 'main' on remote 'origin' but does NOT merge automatically

git branch <branch-name> -> To create new branch

git branch -d branch_name -> To delete branch on local

git branch --set-upstream-to=origin/main main -> Set up a branch to track local changes

git push origin --delete <branch-name> -> To delete branch on github

git branch -u origin/<branch-name> -> Sets the upstream (remote tracking) branch for your local branch

git checkout <branch-name> -> To switch to another branch or commit

git checkout -b <branch-name> -> To create branch and imedietly switch to it

git push --set-upstream origin <branch-name> -> To add remote on new branch (Connecting to main) and push or pull the chenges

git push -u origin <branch-name> -> Same as git push/pull --set-upstream origin <branch-name>

git pull origin main -> Fetch the main branch from the remote origin and merge it into your current local branch. fetch + merge

git reset --soft <commit-hash> -> Soft Reset (Explained at line 85)

git reset <commit hash> -> Mixed Reset (Explained at line 89)

git reset --hard <commit hash> -> Hard Reset (Explained at line 93)

git revert -> (Explained at line 98)

git stash -> (Explained at line 107)

git stash list -> To see all stash names

git stash apply <stash-name> -> To restore a stash

git stash pop <stash-name> -> To restore a stash and deleting it

git stash drop <stash-name> -> To delete a specific stash

git stash clear -> Deletes all stashes at once

git blame <file> -> Shows who last modified each line in a file

git clean -f -> Deletes untracked files in the working directory

git cherry-pick <commit-hash> -> Applies a specific commit from another branch onto the current branch.

Rule: add -> commit -> push

Practices:

1. Create Repo, commit changes, push to github.

- Create new Repository
- Commit some changes to it and write commit massage
- Try to commit everything
- Explore previous commits
- Lastly remote local project to github repo and push the changes.

2. Branching and Merging

- Create new branch and do it with this ways (create and move to it, create and move to it in same time, create new branch under specific branch)
- Modify some code, commit and push it to new branch
- Publish the new branch to github
- Let's say someone else commited some code on branch so you wanna see it in your ide (vscode) so get and look to the changes
- Merge the modified branch to main branch and look to new code features

3. Merge conflict

- Try to make merge conflict by using two different branch
- Resolve the merge conflict problem

4. Fix some mess ups

- Read the NOTES before practicing this step
- Write some broken codes and commit it over and over
- Try to comeback to the version that doesn't has any broken codes
- Apply that by showing everyone the mess up and with hiding all breaks that you do :D
- Fix some bugs without commiting your workout right now and after return to actuall work

Note:

---

- Version = commit \*

---

Reset Types:

1. Soft reset: You will be able to comeback to specific version with keep -
   the changes after this version staged and the meaning of staged is you can commit -
   again whatever version you want. // After git add .

2. Mixed reset: You will be able to comeback to specific version with keep -
   the changes after this version but it is not staged. If you want later to -
   stage them you can by adding, commiting etc. // Before git add . return to start point

3. Hard reset: You will be able to comeback to specific version -
   this will delete immediately all the changes/versions after this version.

Note 2:

Difference Between Reset and Revert:
If you wanna hide the mistake that you made you'll use reset to hide everything and delete -
the mess up from the git log but if you wanna to show everyone the mistakes that you made -
you can use revert by using revert everything, every commit and every mistake will appear -
in git log and everyone will be able to see this changes or broken codes :) So choose wisely -
which one are you going to use.

Note 3:

Fix Before Commit (git stash):
Let's say you are working on one feature and your friend makes a mistake -
that brought a bug and yours boss said "Fix that bug now before doing anything" -
now you don't know what to do, do i continue to add my feature or i will be getting -
fired, so you decided to fix the bug but you didn't commit your changes yet so you -
need to keep your changes in somewhere to fix the bug and after return to your actuall -
work that you was doing here when 'git stash' comes into play so with this command you -
can make your changes staged or unstaged without commiting so you can fix the bug and -
after you can continue to add your main feature. What a good friend :D

Git & Github Video Link:
https://youtu.be/S7XpTAnSDL4?si=cnRRCIzHQou56qbH

\*/
