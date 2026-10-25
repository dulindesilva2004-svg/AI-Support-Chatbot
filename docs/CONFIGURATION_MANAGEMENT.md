# Configuration Management Plan

## 1. Tool
We use **Git** for version control and **GitHub** to host the repository, review code (pull requests) and run automated tests (GitHub Actions). GitHub is linked to our Jira project (key `CHAT`) so commits and PRs show on the matching Jira issue.

## 2. Configuration items (what we control)
| Item | Location |
|---|---|
| Source code | `src/` |
| Intent / FAQ data | `data/` |
| Tests | `tests/` |
| Project documents | `docs/` |
| CI pipeline | `.github/workflows/ci.yml` |
| Dependencies | `requirements.txt` |

## 3. Branching strategy (simplified Git Flow)
- `main` – stable, released code only. Protected: no direct pushes.
- `develop` – integration branch for the current sprint.
- `feature/CHAT-<id>-<name>` – one branch per Jira task.
- `bugfix/CHAT-<id>-<name>` – fixes found in testing.
- `release/vX.Y.Z` – prepared at the end of a sprint, merged into `main` and tagged.

## 4. Commit conventions
- Start every message with the Jira key: `CHAT-15 Add delivery intent`
- Small, focused commits. Present tense.

## 5. Change control
1. Every change starts as a Jira issue.
2. Work happens on a feature branch.
3. A pull request into `develop` needs **1 approving review** and **passing CI**.
4. Merged at the end of the sprint into `main` through a release branch.

## 6. Versioning and releases
Semantic versioning (`vMAJOR.MINOR.PATCH`). Each milestone gets a tagged GitHub Release:
- `v0.1.0` – project setup / prototype
- `v0.5.0` – M3 working prototype
- `v1.0.0` – M5 go-live

## 7. Roles
| Role | Responsibility |
|---|---|
| CM owner (Member 2) | Sets up repo, branch protection, reviews release merges |
| All members | Follow branching/commit rules, review each other's PRs |
