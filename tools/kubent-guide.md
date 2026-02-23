# kubent (Kube No Trouble) — Detect Deprecations in Running Clusters

kubent scans running Kubernetes clusters for resources using deprecated API versions. It collects manifests from kubectl annotations and Helm secrets, then checks them against known deprecation policies.

| | |
|---|---|
| **GitHub** | [github.com/doitintl/kube-no-trouble](https://github.com/doitintl/kube-no-trouble) |
| **Version** | 0.7.3 (August 30, 2024) |
| **License** | MIT |

---

## Installation

```bash
# Quick install script
sh -c "$(curl -sSL https://git.io/install-kubent)"

# Homebrew (macOS/Linux)
brew install kubent

# Scoop (Windows)
scoop install kubent

# Container image
# ghcr.io/doitintl/kube-no-trouble:0.7.3

# Binary download
# https://github.com/doitintl/kube-no-trouble/releases
```

---

## Key Commands

### Scan current cluster

```bash
kubent

# Output:
# >>> Deprecated APIs <<<
#
# KIND      NAMESPACE   NAME          API_VERSION                  REPLACE_WITH               REMOVED_IN
# Ingress   default     my-ingress    networking.k8s.io/v1beta1    networking.k8s.io/v1       v1.22.0
```

### Target a specific Kubernetes version

```bash
# Check what would break upgrading to v1.36
kubent -t 1.36
```

### Scan local manifest files

```bash
kubent -f ./deployment.yaml
kubent -f ./manifests/*.yaml
```

### Machine-readable output

```bash
kubent -o json
kubent -o csv
```

---

## Useful Flags

| Flag | Description |
|------|-------------|
| `-k`, `--kubeconfig` | Path to kubeconfig file |
| `-t`, `--target-version` | Target K8s version (overrides auto-detection) |
| `-o`, `--output` | Output: `text`, `json`, `csv` |
| `-e`, `--exit-error` | Exit code 200 when deprecations found (for CI) |
| `-f`, `--filename` | Local manifest file(s) to scan |

---

## Data Sources

kubent automatically collects manifests from three sources:
1. **kubectl** — Resources with `last-applied-configuration` annotations
2. **Helm v3** — Manifests stored in Helm release secrets
3. **Local files** — YAML/JSON files specified with `-f`

---

## CI/CD: GitHub Actions

```yaml
name: Pre-Upgrade Deprecation Check
on:
  schedule:
    - cron: '0 6 * * 1'  # Weekly Monday
  workflow_dispatch:

jobs:
  kubent:
    runs-on: ubuntu-latest
    steps:
      - name: Install kubent
        run: sh -c "$(curl -sSL https://git.io/install-kubent)"

      - name: Scan cluster
        run: kubent -k /tmp/kubeconfig -e
        # Exits 200 if deprecated APIs found
```

---

## Pluto vs kubent

| | Pluto | kubent |
|-|-------|--------|
| **Best for** | CI/CD on static manifests | Live cluster auditing |
| **CI exit codes** | Built-in (2=deprecated, 3=removed) | Opt-in (`-e`, code 200) |
| **Helm scanning** | `detect-helm` command | Automatic via Helm secrets |
| **GitHub Action** | Official action available | Install via script |

**Recommendation:** Use both. Pluto in CI to gate PRs. kubent against live clusters before upgrades.

---

## When to Use kubent

- **Before cluster upgrades** — Scan for resources that will break at the target version
- **Quarterly audit** — Part of the [30-minute weekly system](../checklists/developer-checklist.md)
- **Scheduled CI job** — Weekly scan to catch drift

See also: [`pluto-guide.md`](pluto-guide.md) for scanning static manifests and Helm charts.
