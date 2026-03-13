# KEP URL Patterns

How to construct URLs for any Kubernetes Enhancement Proposal. Every KEP follows predictable URL patterns — once you know the KEP number, you can navigate directly.

---

## Quick Reference

| What You Want | URL | Example |
|---------------|-----|---------|
| Tracking issue (shortcut) | `kep.k8s.io/{number}` | [kep.k8s.io/1287](https://kep.k8s.io/1287) |
| Searchable KEP table | `kubernetes.dev/resources/keps/` | [kubernetes.dev/resources/keps/](https://kubernetes.dev/resources/keps/) |
| KEP directory | `github.com/kubernetes/enhancements/tree/master/keps/sig-{name}/{number}-{description}/` | [KEP-1287 dir](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/1287-in-place-update-pod-resources/) |
| kep.yaml metadata | `github.com/kubernetes/enhancements/blob/master/keps/sig-{name}/{number}-{description}/kep.yaml` | [KEP-1287 yaml](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/1287-in-place-update-pod-resources/kep.yaml) |
| Enhancements repo | `github.com/kubernetes/enhancements` | [enhancements repo](https://github.com/kubernetes/enhancements) |
| Release notes (filterable) | `relnotes.k8s.io` | [relnotes.k8s.io](https://relnotes.k8s.io) |
| Feature gates reference | `kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/` | [feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) |

---

## The kep.k8s.io Shortcut

The fastest way to find any KEP:

```
kep.k8s.io/{number}
```

This redirects to the GitHub tracking issue. From the tracking issue, labels and links take you to the KEP directory, the owning SIG, and the current stage.

**Examples:**
- [kep.k8s.io/1287](https://kep.k8s.io/1287) — In-Place Pod Resize (sig-node)
- [kep.k8s.io/4639](https://kep.k8s.io/4639) — OCI VolumeSource (sig-storage)
- [kep.k8s.io/3960](https://kep.k8s.io/3960) — Sleep Action for PreStop Hook (sig-node)

---

## The kep.yaml File

Every KEP directory contains a `kep.yaml` with structured metadata:

```yaml
title: "In-Place Update of Pod Resources"
kep-number: 1287
owning-sig: sig-node
status: implementable
creation-date: 2019-06-19
latest-milestone:
  alpha: v1.27
  beta: v1.32
  stable: v1.35
feature-gates:
  - name: InPlacePodVerticalScaling
participating-sigs:
  - sig-autoscaling
  - sig-scheduling
```

Key fields:
- **owning-sig** — Which SIG owns this feature
- **latest-milestone** — Which version each stage shipped in
- **feature-gates** — The flag to enable/disable the feature
- **participating-sigs** — Other SIGs involved

---

## Release Notes Filtering

[relnotes.k8s.io](https://relnotes.k8s.io) supports filtering by:

- **Version** — e.g., v1.35
- **SIG** — e.g., sig-node
- **Kind** — feature, bug, deprecation, cleanup, documentation
- **Area** — specific component areas

This is the fastest way to answer "what changed for my SIG in the latest release?"

> **Known issue:** relnotes.k8s.io has a v1.35 JSON parsing bug (trailing comma in response). Other versions work. Check if fixed before relying on v1.35 filters.

---

## Enhancements Tracking Sheet

Each release has a tracking spreadsheet linked from [kubernetes.dev/resources/release/](https://kubernetes.dev/resources/release/). The sheet shows every KEP targeting that release, with status:

- **Tracked** — On schedule
- **At risk** — May not make the release
- **Removed** — Pushed to next release

This is useful during the release cycle to see what's likely to ship.
