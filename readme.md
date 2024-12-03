# BYOC Client Server Project

SERVER.PY is the file we wrote the server in, everything else is testing mess

### Notes:
* This file is written in markdown, which is a plain text editor with basic functions like headings.
* Once you have GitLens installed, you can click on the GitLens tab when your terminal is open (it's next to the Terminal tab)

himmytimmy 
this line of text is only on the uno branch
### Git Commands:

```bash
#basic tracking:
git add readme.md OR git add . #Stages the changes in either the specified file or all changes in the repo (git add .)
git commit -m "description of commit" #Saves the changes to version history LOCALLY
git pull #updates your local repo to what's on github
git push #updates the remote repo on github with what's on your computer

#branch control
git branch #show all branches in the repo
git checkout -b branch_name #creates a new branch and navigates to it
git push -u origin branch_name #pushes the branch to the remote (the cloud synced repo on github)

git checkout branch_name #moves you to the existing branch named branch_name

#After you finish your branch, create a pull request in github
```