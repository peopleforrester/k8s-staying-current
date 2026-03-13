# Trace a Feature: From Name to KEP to Release Notes

How to trace any Kubernetes feature back to its origin — who owns it, what stage it's at, and when it shipped. Four methods depending on what you start with.

---

## Method 1: Start from the Feature Name

**Example: "In-Place Pod Resize" (KEP-1287)**

1. **Search the KEP table** — [kubernetes.dev/resources/keps/](https://kubernetes.dev/resources/keps/)
   - Type "pod resize" in the search box
   - Find KEP-1287: "In-Place Update of Pod Resources"

2. **Read the kep.yaml** — Every KEP has a machine-readable metadata file
   - Path: `keps/sig-node/1287-in-place-update-pod-resources/kep.yaml`
   - Key fields:
     ```yaml
     owning-sig: sig-node
     status: implementable
     latest-milestone:
       alpha: v1.27
       beta: v1.32
       stable: v1.35
     feature-gate: InPlacePodVerticalScaling
     participating-sigs:
       - sig-autoscaling
       - sig-scheduling
     ```

3. **Check the tracking issue** — [kep.k8s.io/1287](https://kep.k8s.io/1287)
   - Redirects to the GitHub tracking issue
   - Labels show `sig/node`, `stage/stable`, and the current status
   - Comments track the feature through each release milestone

4. **Find it in release notes** — [relnotes.k8s.io](https://relnotes.k8s.io)
   - Filter by version (v1.35) and SIG (sig-node)
   - The entry describes what shipped and any caveats

---

## Method 2: Start from a Feature Gate

You see a feature gate in your cluster config and want to know what it does.

1. **Check the feature gates reference** — [kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
   - Search for the gate name (e.g., `InPlacePodVerticalScaling`)
   - Shows: default on/off, stage (Alpha/Beta/GA), and the version it was introduced

2. **Find the owning KEP** — The feature gates page links to the KEP number
   - Follow the link to the KEP tracking issue or the kep.yaml

---

## Method 3: Start from a Release

You want to know what shipped in a specific version.

1. **Release notes** — [relnotes.k8s.io](https://relnotes.k8s.io)
   - Select the version (e.g., v1.35)
   - Filter by kind: `feature`, `deprecation`, `bug`
   - Filter by SIG to narrow to your area of interest

2. **Release blog post** — [kubernetes.io/blog](https://kubernetes.io/blog)
   - Every minor release gets a detailed blog post
   - Lists major themes, notable features, deprecations, and removals
   - Worth reading in full — more context than the raw release notes

3. **Enhancements tracking sheet**
   - Each release has a tracking spreadsheet linked from [kubernetes.dev/resources/release/](https://kubernetes.dev/resources/release/)
   - Shows every KEP in the release with its status (tracked, at risk, removed)

> **Known issue:** relnotes.k8s.io has a v1.35 JSON parsing bug (trailing comma in response). Other versions work. Check if fixed before relying on v1.35 filters.

---

## Method 4: Start from a SIG

You follow a SIG and want to know what they're working on.

1. **SIG meeting notes** — Each SIG keeps meeting notes (usually a Google Doc linked from [kubernetes/community](https://github.com/kubernetes/community))
2. **SIG Slack channel** — Discussions about upcoming features happen in real time
3. **KEP table filtered by SIG** — [kubernetes.dev/resources/keps/](https://kubernetes.dev/resources/keps/) supports SIG filtering
4. **Release notes filtered by SIG** — [relnotes.k8s.io](https://relnotes.k8s.io) supports SIG filtering

---

## KEP URL Patterns

Every KEP has predictable URLs:

| What | URL Pattern |
|------|------------|
| KEP directory | `github.com/kubernetes/enhancements/tree/master/keps/sig-{name}/{number}-{description}/` |
| Tracking issue (shortcut) | `kep.k8s.io/{number}` |
| kep.yaml | `github.com/kubernetes/enhancements/blob/master/keps/sig-{name}/{number}-{description}/kep.yaml` |
| KEP searchable table | `kubernetes.dev/resources/keps/` |
| Release notes (filterable) | `relnotes.k8s.io` |

> See also: [`kep-url-patterns.md`](kep-url-patterns.md) for the full URL reference
