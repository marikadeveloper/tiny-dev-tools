#!/bin/bash
CHANGED_FILES=$(git diff --name-only --staged)

if [[ -z "$CHANGED_FILES" ]]; then
    echo "No staged changes detected."
    exit 1
fi

echo "Suggested commit messages:"
echo "1. Update ${CHANGED_FILES%% *}"
echo "2. Fix bug in ${CHANGED_FILES%% *}"
echo "3. Add feature related to ${CHANGED_FILES%% *}"

read -p "Choose a message (or enter your own): " MSG
if [[ -z "$MSG" ]]; then
    MSG="Update ${CHANGED_FILES%% *}"
fi

git commit -m "$MSG"
