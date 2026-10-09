# Student Management System

Agile Software Development & DevOps Lab, Experiment 1: Agile project lifecycle using Jira
with a DevOps (GitHub Actions) CI pipeline.

- Work items (user stories and tasks) are planned and tracked in the Jira Scrum project
  **Student Management System** (key `SCRUM`).
- Each work item is developed on its own feature branch named after the Jira key
  (for example `SCRUM-<n>-short-description`) and merged into `main` through a Pull Request.
- The GitHub for Jira app links branches, commits and Pull Requests to the Jira work items.
- GitHub Actions (`.github/workflows/ci.yml`) lints the code and runs the unit tests on every
  push to `main` and on every Pull Request.

## Run locally

```
pip install -r requirements.txt
python student.py
pytest -v
```
