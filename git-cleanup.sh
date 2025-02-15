#!/bin/bash
# This script will delete all branches that have been merged into develop and are not the current branch
git fetch --prune
git checkout develop
git pull
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d