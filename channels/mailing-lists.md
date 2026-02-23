# Kubernetes Mailing Lists

Google Groups mailing lists are the official asynchronous communication channel for Kubernetes governance, SIG coordination, and security announcements.

---

## Essential Lists

| List | URL | Traffic | Why Subscribe |
|------|-----|---------|---------------|
| **kubernetes-security-announce** | [groups.google.com/g/kubernetes-security-announce](https://groups.google.com/g/kubernetes-security-announce) | Very low (CVEs only) | Security vulnerabilities — fires only when a CVE is disclosed |
| **kubernetes-announce** | [groups.google.com/g/kubernetes-announce](https://groups.google.com/g/kubernetes-announce) | Low | Official project announcements, release notifications |
| **kubernetes-dev** | [groups.google.com/g/kubernetes-dev](https://groups.google.com/g/kubernetes-dev) | Medium | Development discussions, KEP announcements, cross-SIG coordination |

---

## SIG Mailing Lists

Every SIG has a dedicated mailing list following a consistent pattern:

```
kubernetes-sig-<name>@googlegroups.com
```

**Examples:**
| SIG | Mailing List |
|-----|-------------|
| SIG Apps | [kubernetes-sig-apps](https://groups.google.com/g/kubernetes-sig-apps) |
| SIG Network | [kubernetes-sig-network](https://groups.google.com/g/kubernetes-sig-network) |
| SIG Node | [kubernetes-sig-node](https://groups.google.com/g/kubernetes-sig-node) |
| SIG Auth | [kubernetes-sig-auth](https://groups.google.com/g/kubernetes-sig-auth) |
| SIG Storage | [kubernetes-sig-storage](https://groups.google.com/g/kubernetes-sig-storage) |
| SIG CLI | [kubernetes-sig-cli](https://groups.google.com/g/kubernetes-sig-cli) |
| SIG Architecture | [kubernetes-sig-architecture](https://groups.google.com/g/kubernetes-sig-architecture) |
| SIG Release | [kubernetes-sig-release](https://groups.google.com/g/kubernetes-sig-release) |

For the complete list of all 24 SIGs and their mailing lists, see [`../reference/all-24-sigs.md`](../reference/all-24-sigs.md).

---

## By Role

### Everyone
- `kubernetes-security-announce` — Non-negotiable. Subscribe now.

### Developers
- `kubernetes-sig-apps`
- `kubernetes-sig-api-machinery`
- `kubernetes-sig-cli`

### Operators
- `kubernetes-sig-node`
- `kubernetes-sig-network`
- `kubernetes-sig-storage`
- `kubernetes-sig-auth`

### Architects
- `kubernetes-dev` — Cross-SIG development discussions
- `kubernetes-sig-architecture`

### Contributors
- `kubernetes-dev` — Development discussions and KEP announcements
- `kubernetes-sig-contribex` — Contributor experience and onboarding

---

## How to Subscribe

1. Go to the Google Group URL
2. Click **Ask to join group** (or **Join group** if open)
3. Choose your email delivery preference:
   - **Each email** — Every message as it's posted
   - **Digest** — Daily summary
   - **Abridged** — Daily summary with truncated messages
   - **No email** — Read on the web only
4. Click **Join**

**Tip:** For high-traffic lists like `kubernetes-dev`, use **Digest** or **No email** and check the web interface weekly. For `kubernetes-security-announce`, use **Each email** — you want CVEs immediately.

---

## Mailing Lists vs Slack

| | Mailing Lists | Slack |
|-|---------------|-------|
| **Best for** | Formal proposals, announcements, governance | Real-time discussion, quick questions |
| **Archive** | Permanent, searchable on Google Groups | Limited (Slack free tier limitations) |
| **Speed** | Async (hours to days) | Real-time |
| **Formality** | Higher — used for KEPs, elections, policy | Lower — casual discussion |

Both channels are active and serve different purposes. For staying current, subscribe to the security-announce list and 1–2 SIG lists for your role.
