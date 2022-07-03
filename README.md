# Loan Prediction Backend

## Stack
- Python
- Flask
- Scikit Learn

---

## Getting started
- Clone this repository to your preferred working directory
- Create a virtual environment `python3 -m venv otehrvenv` will create a virtual env
- Source the env, assuming you on zsh/bash `source venv/bin/activate`
- Install dependencies `pip3 install -r requirements.txt`

## Deployment & Build Server
- You have already done this on the Git & Github Quiz assignment
- The CircleCI config is on this repo.
- Setup your project on Heroku and on CircleCI
- Refer to [https://github.com/africacodeacademy/aca-erp2022-2-Quiz](https://github.com/africacodeacademy/aca-erp2022-2-Quiz)

## Installing other Dependencies
- Should you need other dependencies, Add them to your requirements.txt

# ACA Git Workflow 

<https://guides.github.com/introduction/flow/>

## Branch Naming Convention:

Here’s the branch naming convention that we should enforce for the devs.

### Feature Branch

Feature requests should have a naming convention of (where XXX is the Shortcut ticket number). For example:
feature-XXX-<feature-description> eg.
feature-1234-add-logout-button

### Bug fix branch

Bugs are similar with the “bug-” prefix.

_bug-XXX-<bug-description>_

eg.

_bug-1235-fix-crash-on-logout_

### Hotfix branches

In the event we have hotfixes (haha!), they can also have its own branch of the following form, where VVV is the hotfix version number:

_hotfix-VVV_

eg.

_hotfix-1.0.1_

## Commit Messages Convention

Add ticket number and concise message. Why?

## Version Tags

We’ll be using tags in the main branch to specify releases.

# Pre-commit & PR Merge Checks

## Merging to ‘main’:

As mentioned above, there’s only one rule: anything in the `main` branch is always deployable.

Before a branch is merged back to main the following this must have happened with the branch code:

**Commits:** Code changes, atomic and often.  
**Pull Request:** Which is followed by a …  
**Code Review:** The code is reviewed.  
**Tests:** The is deployed to a test server and tested.  
**Merge to main:** Finally, the tested code is merged into the main branch.  
