# File a Bug: From Discovery to Merge

How to report a bug in Kubernetes — the full lifecycle from issue template to merged fix.

---

## Step 1: Open the Issue Template

Go to: [github.com/kubernetes/kubernetes/issues/new/choose](https://github.com/kubernetes/kubernetes/issues/new/choose)

Blank issues are disabled. Select **"Bug Report"** from the template list.

---

## Step 2: Fill the Structured Form

The template asks for:

| Field | What to Write |
|-------|--------------|
| **What happened?** | Clear description of the unexpected behavior |
| **What did you expect to happen?** | The correct behavior |
| **How can we reproduce it?** | Step-by-step instructions (the more specific, the faster the fix) |
| **Anything else we need to know?** | Cluster setup, cloud provider, CNI, etc. |
| **Kubernetes version** | Output of `kubectl version` |
| **Cloud provider or hardware** | GKE, EKS, AKS, bare metal, etc. |
| **OS** | Output of `cat /etc/os-release` |
| **Install tools** | kubeadm, kops, etc. |
| **Container runtime and version** | containerd, CRI-O, etc. |

---

## Step 3: Submit — Bot Labels Automatically

When you click submit, **@k8s-ci-robot** (the Prow automation bot) immediately applies:

- `kind/bug` — identifies this as a bug report
- `needs-triage` — flags it for human review

If you didn't specify a SIG in the issue body, the bot also adds `needs-sig`.

---

## Step 4: SIG Picks It Up

A triager (human) reads the issue and routes it:

1. **Route to SIG:** Triager comments `/sig node` → bot adds `sig/node` label and assigns to SIG Node's triage queue
2. **Accept triage:** SIG member comments `/triage accepted` → issue is acknowledged
3. **Set priority:** `/priority important-soon` or `/priority critical-urgent`
4. **Assign owner:** Someone comments `/assign` to take ownership (you can self-assign too)

---

## Step 5: The Fix (PR Lifecycle)

When a fix PR is submitted:

1. **CI runs automatically** — Tests, linting, conformance checks
2. **Review:** A reviewer comments `/lgtm` ("looks good to me")
3. **Approve:** An approver (different person) comments `/approve`
4. **Merge:** Tide (the merge bot) merges it automatically once both labels are present and CI passes

---

## Security Vulnerabilities — NEVER Public Issues

If the bug is a **security vulnerability**, it **MUST NOT** go through public GitHub issues.

Go to: [kubernetes.io/security](https://kubernetes.io/security)

This is a private disclosure process. The Security Response Committee handles triage, patch development, and coordinated disclosure. Public CVE announcements go to kubernetes-security-announce after a fix is available.

---

## Key Bot Commands

| Command | What It Does |
|---------|-------------|
| `/sig node` | Route issue to a SIG |
| `/assign` | Self-assign the issue |
| `/assign @username` | Assign to someone else |
| `/kind bug` | Label as bug |
| `/kind feature` | Label as feature request |
| `/triage accepted` | Accept for triage |
| `/priority important-soon` | Set priority |
| `/good-first-issue` | Mark as suitable for newcomers |
| `/lgtm` | Reviewer approves the code |
| `/approve` | Approver approves for merge |
| `/hold` | Prevent merge (add a hold) |
| `/hold cancel` | Remove hold |

Full command reference: [go.k8s.io/bot-commands](https://go.k8s.io/bot-commands)

---

## Tips

- **Be specific.** Vague bugs get `needs-more-information` and stall.
- **Include versions.** The exact `kubectl version` output matters.
- **Reproduce minimally.** Strip your reproduction to the fewest steps possible.
- **Check existing issues first.** Search the repo before filing — your bug may already be tracked.
- **Don't @ SIG leads directly.** Use `/sig` to route — the bot handles assignment to the right queue.

> See also: [`bot-commands-cheatsheet.md`](bot-commands-cheatsheet.md) for the quick reference card
