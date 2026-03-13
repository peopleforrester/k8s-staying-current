# CLotributor: Find CNCF Contribution Opportunities

[CLotributor](https://clotributor.dev) is a search engine that indexes help-wanted issues across every CNCF project. It's the fastest way to find contribution opportunities beyond Kubernetes itself.

---

## What It Does

CLotributor crawls CNCF project repositories and surfaces issues tagged for contributors. It indexes:

- `good first issue` labels
- `help wanted` labels
- `mentor available` tags
- Project-specific contributor labels

All from a single searchable interface.

---

## How to Use It

1. Go to [clotributor.dev](https://clotributor.dev)
2. **Filter by project** — Kubernetes, Prometheus, Envoy, Argo, Falco, etc.
3. **Filter by difficulty** — Good first issue, help wanted, mentor available
4. **Filter by language** — Go, Rust, Python, TypeScript, etc.
5. **Filter by area** — Documentation, testing, bug fixes, features
6. Browse results and click through to the GitHub issue

---

## Why Use CLotributor Instead of GitHub Search

| Feature | CLotributor | GitHub Search |
|---------|-------------|---------------|
| Scope | All CNCF projects in one place | One repo at a time |
| Filtering | Project + difficulty + language | Labels only |
| Freshness | Indexes continuously | Real-time but harder to filter |
| Discovery | Find projects you didn't know about | Must know the repo |

GitHub's [go.k8s.io/good-first-issue](https://go.k8s.io/good-first-issue) is great for Kubernetes-specific issues. CLotributor is for when you want to explore the broader CNCF ecosystem.

---

## Tips

- **Start with your language.** If you write Go, filter by Go — most Kubernetes and CNCF projects use it.
- **Look for "mentor available."** These issues have someone committed to helping you through the PR process.
- **Don't limit yourself to Kubernetes.** Projects like Falco, Flux, Argo, and Backstage all have contributor-friendly issues and smaller communities where your PR gets reviewed faster.
- **Check the project's CONTRIBUTING.md** before starting. Contribution workflows vary between projects.

> See also: [`first-contribution.md`](first-contribution.md) for the Kubernetes-specific contribution path
