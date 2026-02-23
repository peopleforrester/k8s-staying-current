# RSS Setup for Kubernetes Feeds

RSS is the most reliable way to follow Kubernetes announcements without depending on algorithms, social media platforms, or newsletter services that might shut down.

---

## Essential Feeds

| Feed | URL | Content |
|------|-----|---------|
| Kubernetes Blog | `https://kubernetes.io/feed.xml` | Release announcements, deprecation notices, security advisories |
| CNCF Blog | `https://www.cncf.io/blog/feed/` | CNCF project news, event announcements, ecosystem updates |
| Kubernetes Enhancements | `https://github.com/kubernetes/enhancements/releases.atom` | KEP milestone updates |

---

## Recommended RSS Readers

### Desktop

| Reader | Platform | Cost | Notes |
|--------|----------|------|-------|
| **Thunderbird** | Windows, macOS, Linux | Free | Built-in RSS reader alongside email |
| **NetNewsWire** | macOS, iOS | Free, open source | Clean interface, iCloud sync |
| **Newsboat** | Linux, macOS (terminal) | Free, open source | For terminal users; keyboard-driven |

### Web-Based

| Reader | Cost | Notes |
|--------|------|-------|
| **Feedly** | Free tier available | Popular, good mobile apps, integrations |
| **Inoreader** | Free tier available | Powerful filtering and rules |
| **Miniflux** | Self-hosted (free) | Minimal, fast, self-hosted option |
| **Freshrss** | Self-hosted (free) | Full-featured, self-hosted with web UI |

### Mobile

| Reader | Platform | Cost |
|--------|----------|------|
| **NetNewsWire** | iOS | Free |
| **Reeder** | iOS | Paid |
| **Feedly** | iOS, Android | Free tier |
| **Inoreader** | iOS, Android | Free tier |

---

## Quick Setup: Feedly (5 minutes)

1. Go to [feedly.com](https://feedly.com) and create an account
2. Click **+ Add Content** → **Websites or Feeds**
3. Paste `https://kubernetes.io/feed.xml` and subscribe
4. Repeat for any additional feeds above
5. Optional: Create a folder called "Kubernetes" to group your feeds

---

## Quick Setup: Newsboat (Terminal)

```bash
# Install
brew install newsboat    # macOS
apt install newsboat     # Debian/Ubuntu

# Add feeds
mkdir -p ~/.newsboat
cat >> ~/.newsboat/urls << 'EOF'
https://kubernetes.io/feed.xml "~Kubernetes Blog" kubernetes
https://www.cncf.io/blog/feed/ "~CNCF Blog" cncf
https://github.com/kubernetes/enhancements/releases.atom "~K8s Enhancements" kubernetes
EOF

# Run
newsboat
```

Key bindings: `r` to refresh, `Enter` to open, `q` to quit.

---

## GitHub "Releases Only" Watch (Not RSS, but similar)

For the kubernetes/kubernetes repo release notifications:

1. Go to [github.com/kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)
2. Click the **Watch** dropdown (top right)
3. Select **Custom**
4. Check **Releases** only
5. Click **Apply**

Notifications will go to your GitHub email. You can also use the GitHub Atom feed:
```
https://github.com/kubernetes/kubernetes/releases.atom
```

---

## Tips

- **Check feeds weekly** as part of your [30-minute system](../checklists/developer-checklist.md)
- **Don't over-subscribe.** The three feeds above plus GitHub releases cover the essentials. Add SIG-specific feeds only if you're actively contributing to that SIG.
- **Use folders/tags** to separate Kubernetes feeds from other subscriptions
- **Set up mobile access** so you can scan during commute or downtime
