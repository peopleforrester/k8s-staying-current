# Pluto — Detect Deprecated Kubernetes API Versions

Pluto scans static manifests, Helm releases, and live cluster resources for deprecated and removed Kubernetes API versions. Use it in CI/CD to catch issues before deployment, and locally before upgrades.

| | |
|---|---|
| **GitHub** | [github.com/FairwindsOps/pluto](https://github.com/FairwindsOps/pluto) |
| **Docs** | [pluto.docs.fairwinds.com](https://pluto.docs.fairwinds.com/) |
| **Version** | v5.22.7 (December 8, 2025) |
| **License** | Apache-2.0 |

---

## Installation

```bash
# Homebrew (macOS/Linux)
brew install FairwindsOps/tap/pluto

# Scoop (Windows)
scoop install pluto

# asdf
asdf plugin-add pluto
asdf install pluto 5.22.7

# Binary download
# https://github.com/FairwindsOps/pluto/releases/latest

# Container image
# us-docker.pkg.dev/fairwinds-ops/oss/pluto:v5
```

---

## Key Commands

### Scan manifest files

```bash
pluto detect-files -d ./manifests/

# Output:
# NAME        KIND         VERSION              REPLACEMENT   REMOVED   DEPRECATED
# utilities   Deployment   extensions/v1beta1   apps/v1       true      true
```

### Scan Helm releases in a cluster

```bash
pluto detect-helm -owide

# Single namespace
pluto detect-helm -n cert-manager -owide
```

### Scan all resources in a live cluster

```bash
pluto detect-all-in-cluster -o wide
```

### Pipe Helm template output

```bash
helm template my-chart ./charts/my-chart | pluto detect -
```

### Target a specific Kubernetes version

```bash
pluto detect-files -d ./manifests/ -t k8s=v1.31.0
```

---

## Useful Flags

| Flag | Description |
|------|-------------|
| `-d <dir>` | Directory to scan |
| `-o <format>` | Output: `wide`, `json`, `yaml`, `csv`, `markdown` |
| `-t <component=version>` | Target K8s version |
| `-r` / `--only-show-removed` | Show only removed APIs |
| `--no-headers` | Omit headers in output |

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | No issues |
| 1 | Error |
| 2 | Deprecated API found |
| 3 | Removed API found |

These exit codes make Pluto CI-friendly — non-zero exits fail pipeline steps automatically.

---

## CI/CD: GitHub Actions

```yaml
name: Check Deprecated APIs
on:
  pull_request:
    paths:
      - 'manifests/**'
      - 'charts/**'

jobs:
  pluto:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Download Pluto
        uses: FairwindsOps/pluto/github-action@master

      - name: Scan manifests
        run: pluto detect-files -d manifests/

      - name: Scan Helm charts
        run: helm template my-chart charts/my-chart | pluto detect -
```

---

## When to Use Pluto

- **In CI/CD** — Gate pull requests to catch deprecated APIs before they merge
- **Before upgrades** — Scan your manifests against the target K8s version
- **Quarterly audit** — Part of the [30-minute weekly system](../checklists/developer-checklist.md)

See also: [`kubent-guide.md`](kubent-guide.md) for scanning running clusters.
