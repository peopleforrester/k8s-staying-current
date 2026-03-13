# Prow Bot Commands Cheatsheet

Quick reference for Kubernetes GitHub bot commands. These are typed as comments on issues and PRs. The Prow bot (@k8s-ci-robot) processes them automatically.

Full reference: [go.k8s.io/bot-commands](https://go.k8s.io/bot-commands)

---

## Issue Triage

| Command | Effect |
|---------|--------|
| `/sig node` | Route to SIG Node (works for any SIG: `/sig network`, `/sig apps`, etc.) |
| `/triage accepted` | Mark as triaged and accepted |
| `/triage not-reproducible` | Close as not reproducible |
| `/kind bug` | Label as bug |
| `/kind feature` | Label as feature request |
| `/kind cleanup` | Label as cleanup/tech debt |
| `/kind documentation` | Label as docs issue |
| `/priority critical-urgent` | P0 — drop everything |
| `/priority important-soon` | P1 — fix this release |
| `/priority important-longterm` | P2 — fix eventually |
| `/priority backlog` | P3 — nice to have |
| `/good-first-issue` | Mark for first-time contributors |
| `/help` | Mark as "help wanted" |

---

## Issue Assignment

| Command | Effect |
|---------|--------|
| `/assign` | Assign the issue to yourself |
| `/assign @username` | Assign to someone else |
| `/unassign` | Remove yourself from assignment |
| `/cc @username` | Request review from someone |
| `/uncc @username` | Remove review request |

---

## PR Review & Merge

| Command | Effect |
|---------|--------|
| `/lgtm` | Reviewer approves — adds `lgtm` label |
| `/lgtm cancel` | Retract approval |
| `/approve` | Approver approves for merge — adds `approved` label |
| `/approve cancel` | Retract approval |
| `/hold` | Prevent merge (adds `do-not-merge/hold`) |
| `/hold cancel` | Allow merge again |
| `/retest` | Re-run failed CI tests |
| `/ok-to-test` | Allow CI to run on external contributor PRs |
| `/cherry-pick release-1.35` | Request cherry-pick to release branch |

**Merge requirements:** Tide (the merge bot) merges automatically when:
1. `lgtm` label is present (from a reviewer)
2. `approved` label is present (from an approver — must be a different person)
3. CI tests pass
4. No `do-not-merge/*` labels

---

## Labels & Metadata

| Command | Effect |
|---------|--------|
| `/area etcd` | Add area label |
| `/remove-area etcd` | Remove area label |
| `/milestone v1.36` | Set milestone |
| `/remove-milestone v1.36` | Remove milestone |
| `/lifecycle stale` | Mark as stale |
| `/lifecycle rotten` | Mark as rotten (will be closed) |
| `/lifecycle frozen` | Prevent auto-close |
| `/close` | Close the issue |
| `/reopen` | Reopen a closed issue |

---

## How It Works

All Kubernetes repos use **Prow** — a CI/CD system built on Kubernetes itself. When you type a command in a comment:

1. Prow detects the command
2. Checks your permissions (are you a member? a reviewer? an approver?)
3. Applies the appropriate label or action
4. Comments back confirming the action

You don't need special access to use most commands. Anyone can `/assign` themselves to an issue or comment `/kind bug`. Review and approval commands (`/lgtm`, `/approve`) require membership in the OWNERS file for that directory.

---

## Common Workflows

### "I want to fix this bug"
```
/assign
```
Then open a PR. In the PR description, add `Fixes #12345` to auto-close the issue on merge.

### "This is a good issue for newcomers"
```
/good-first-issue
/help
```

### "This PR looks good and should merge"
```
/lgtm        (reviewer)
/approve     (approver — different person)
```

### "Hold this PR, not ready yet"
```
/hold
```
When ready: `/hold cancel`
