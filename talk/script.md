# Talk Script: Every Channel You Need to Stay Current After Kubernetes Certification

**Event:** KubeCon EU 2026 — Cloud Native Theatre
**Date:** March 24, 2026 — Amsterdam
**Duration:** 20 minutes
**Speakers:** Mumshad Mannambeth & Michael Forrester (KodeKloud)
**Format:** Role-play conversation

---

## Format Notes

- **Mumshad** plays a recently certified Kubernetes engineer — just passed CKA, excited but overwhelmed, doesn't know where to go next. He asks the questions the audience is already thinking.
- **Michael** plays the CNCF educator — experienced guide who's been in the ecosystem for years and cuts through the noise.
- **Minimal slides.** Slides are backdrops — a few key visuals, a couple of reference tables, the QR code. The conversation IS the talk. Everything detailed goes in the GitHub repo.

---

## Story Arc

| Act | Theme | Time |
|-----|-------|------|
| **Act 1** — "I Passed. Now What?" | Mumshad sets up the problem. Certified, proud, immediately lost. Michael explains why — the cert is a snapshot, not a subscription. | 5 min |
| **Act 2** — "Show Me How This Works" | Progressively deeper questions. How does K8s ship? Who decides what goes in? How do I trace a feature? How do I report a bug? Each answer builds the mental model. | 10 min |
| **Act 3** — "Make It Actionable" | Mumshad gets practical. What do I subscribe to? I don't have time. I want to contribute. Michael gives the system, tools, and specific next steps — including events at KubeCon this week. | 5 min |
| **Close + QR Code** | Both speakers summarize. Everything goes in the repo. Audience scans the code. | 2 min |

---

## Scene-by-Scene Script

### SCENE 1: The Setup
**Time: 1:30**
**SLIDE:** Title card — talk name, speakers, KodeKloud logo, Cloud Native University

**Mumshad:** *(to audience)* Hey everyone! So, at KodeKloud we've trained over a million students for Kubernetes certifications. And the number one message we get after someone passes is — *"I passed. Now what?"*

That's what we're going to answer today. And we're going to do it a little differently.

I'm going to pretend I just passed my CKA. I'm confused, I'm overwhelmed, and I'm going to ask Michael every question I know you're thinking.

Michael — you ready?

**Michael:** Let's do it.

---

### SCENE 2: "My Cert Is Already Expiring?"
**Time: 2:00**
**SLIDE:** Release timeline — v1.33 through v1.36 with dates, "3 releases/year," "14 months of patch support"

```
HOW KUBERNETES SHIPS

3 releases/year | ~15-week cycles | 14 months of patch support

  v1.35  Timbernetes    Dec 17, 2025     EOL Feb 2027
  v1.34  Of Wind & Will Aug 2025         EOL Oct 2026
  v1.33  Octarine       Apr 2025         EOL Jun 2026
  v1.32  ⚠ END OF LIFE  Feb 28, 2026

  v1.36 -> Code Freeze: Mar 18 | Target: Apr 22, 2026
```

**Mumshad:** So I studied for months, I passed my CKA, and you're telling me the version I studied is already old?

**Michael:** Kubernetes ships three releases a year. Each release has about a 15-week cycle, and once it ships, you get 14 months of patch support. After that, it's end of life — no more security fixes.

v1.32? That went end of life February 28th. Three weeks ago. If you studied on v1.32, the APIs you used are still there — but some of them are deprecated, and if you're running v1.32 in production, you're unpatched.

**Mumshad:** So my certification is like a snapshot?

**Michael:** Exactly. It proves you understood Kubernetes at one point in time. But Kubernetes doesn't stop. v1.35 shipped December 17th. v1.36 is targeting April 22nd — that's less than a month from now. And here's the thing nobody tells you: the release blog post is worth more than any vendor webinar. Every release ships with a detailed blog listing what's new, what's deprecated, and what was removed.

---

### SCENE 3: "Who Actually Runs Kubernetes?"
**Time: 2:00**
**SLIDE:** SIG structure diagram — "24 SIGs Own Everything" with examples

```
24 SIGs OWN EVERYTHING

SIG Network    → all networking code
SIG Node       → the kubelet
SIG Auth       → RBAC, authentication
SIG Apps       → workload APIs (Deployments, StatefulSets)
SIG Release    → the release process
SIG etcd       → newest SIG (est. Nov 2023)
SIG Storage    → PVs, CSI drivers
SIG CLI        → kubectl

CNCF is the landlord. Kubernetes arranges its own furniture.
```

**Mumshad:** OK so if Kubernetes moves this fast, who's actually driving? Is it Google? Is it the CNCF?

**Michael:** Neither. It's 24 Special Interest Groups — SIGs. Each SIG owns a specific area of the project. SIG Network owns all the networking code. SIG Node owns the kubelet. SIG Auth owns RBAC and authentication.

And here's the mental model that matters: **CNCF is the landlord. Kubernetes arranges its own furniture.** The CNCF provides the infrastructure — the CI/CD, the legal entity, the conference you're sitting in right now. But it doesn't tell the SIGs what code to write.

**Mumshad:** Wait, I thought there were 21 SIGs?

**Michael:** Older docs are wrong. It's 24 now. The newest is SIG etcd, established November 2023. Every SIG — with Slack channels, meeting times, and current chairs — is in the repo.

---

### SCENE 4: "But Wait — What About TAGs?"
**Time: 1:30**
**SLIDE:** SIGs vs TAGs comparison

```
KUBERNETES SIGs ≠ CNCF TAGs

     K8s SIGs                  CNCF TAGs
     Own code                  Advisory only
     24 groups                 5 groups (restructured May 2025)
     Report to Steering        Report to TOC

THE 5 CNCF TAGs:
  Developer Experience | Infrastructure | Operational Resilience
  Security and Compliance | Workloads Foundation
```

**Mumshad:** Hold on. I keep seeing "TAGs" and "SIGs" and I'm getting confused. Are they the same thing?

**Michael:** No, and this trips everyone up. The CNCF originally called their advisory groups "SIGs" too — same name, completely different thing. They renamed them to TAGs — Technical Advisory Groups — specifically to fix this confusion.

And in May 2025, they restructured from 8 TAGs down to 5. TAG App Delivery, TAG Runtime, TAG Environmental Sustainability — gone. The old Slack channels got archived in June 2025. So if you're following a guide that mentions those, it's outdated.

The five current TAGs are: Developer Experience, Infrastructure, Operational Resilience, Security and Compliance, and Workloads Foundation.

And TAGs actually produce concrete things. TAG Security and Compliance, for example — they do security assessments for 50+ CNCF projects, they published the Cloud Native Security Whitepaper, and they're running the 2026 Security Slam right now through March 20th. SIGs write Go and merge PRs. TAGs write white papers and evaluate projects for the TOC.

---

### SCENE 5: "How Do Features Actually Ship?"
**Time: 1:00**
**SLIDE:** KEP lifecycle — Alpha → Beta → Stable

```
HOW FEATURES SHIP: THE KEP PROCESS

Kubernetes Enhancement Proposal (KEP)
  Alpha  → Off by default. Architects evaluating direction.
  Beta   → On by default. Operators plan for this.
  Stable → GA. Everyone — it's production-ready.

v1.35 shipped 60 enhancements:
  17 Stable | 19 Beta | 22 Alpha

Track them: github.com/kubernetes/enhancements
Shortcut: kep.k8s.io/{number}  |  Filter: relnotes.k8s.io
```

**Mumshad:** OK, so SIGs own the code. But how do new features actually get in?

**Michael:** Through KEPs — Kubernetes Enhancement Proposals. A KEP starts as an idea, goes through Alpha, Beta, then Stable — which is GA, production-ready. v1.35 shipped 60 enhancements: 17 went Stable, 19 Beta, 22 new Alphas. Let me show you how to trace one.

---

### SCENE 6: "Trace It — KEP-1287"
**Time: 1:30**
**SLIDE:** KEP-1287 In-Place Pod Resize walkthrough

```
TRACE IT: KEP-1287
In-Place Update of Pod Resources

1  Search the KEP table
   kubernetes.dev/resources/keps/ → search "pod resize"

2  Read the kep.yaml
   keps/sig-node/1287-in-place-update-pod-resources/kep.yaml

3  Check the tracking issue
   kep.k8s.io/1287 → labels show sig/node + stage

4  Find it in release notes
   relnotes.k8s.io → filter v1.35 + sig-node

kep.yaml:
  owning-sig:     sig-node
  alpha:          v1.27
  beta:           v1.32
  stable:         v1.35 (GA!)
  feature-gate:   InPlacePodVerticalScaling
  participating:  sig-autoscaling, sig-scheduling
```

**Michael:** In-Place Pod Resize — being able to change resource limits without restarting the pod — went GA in v1.35. Big deal. Here's how you trace it.

Step one: Search the KEP table at kubernetes.dev/resources/keps. Step two: Every KEP has a kep.yaml that tells you the owning SIG, what version it hit each stage, and the feature gate name. Step three: kep.k8s.io/1287 — that shortcut takes you straight to the tracking issue. Step four: relnotes.k8s.io — filter by version and SIG to see exactly what shipped.

Every major feature has a paper trail. The URL is predictable. The data is machine-readable.

**Mumshad:** OK, so I can track features. But what if I find something broken?

---

### SCENE 7: "I Found a Bug"
**Time: 1:30**
**SLIDE:** File a Bug — exact steps with bot commands

```
FILE A BUG: THE EXACT STEPS

1  Go to the issue template
   github.com/kubernetes/kubernetes/issues/new/choose
   → select Bug Report

2  Fill the structured form
   What happened? How to reproduce?
   K8s version, runtime, OS

3  Submit — bot labels automatically
   kind/bug + needs-triage applied by @k8s-ci-robot (Prow)

4  SIG picks it up
   Triager comments /sig node → routes to the right team

KEY BOT COMMANDS:
  /sig node          Route to a SIG
  /assign            Self-assign
  /kind bug          Label as bug
  /good-first-issue  Mark for newcomers
  /lgtm + /approve   PR merge flow

Full command ref: go.k8s.io/bot-commands
⚠ Security bugs → kubernetes.io/security (NEVER public issues)
```

**Michael:** Go to the kubernetes/kubernetes repo, click "New Issue," and pick "Bug Report." There's a structured form — what happened, how to reproduce, your Kubernetes version. When you submit, the Prow bot automatically labels it.

Then a SIG triager routes it. They comment `/sig node` and the bot assigns it to the right team. If you want to fix it yourself, comment `/assign` — it's yours.

And here's the important one: if it's a security vulnerability, it **never** goes through public issues. Go to kubernetes.io/security. That's a private disclosure process.

**Mumshad:** So the entire project runs on bot commands and structured processes?

**Michael:** Exactly. And the full command reference is at go.k8s.io/bot-commands. It's all documented, all automatable.

---

### SCENE 8: "Half My Bookmarks Are Broken"
**Time: 2:00**
**SLIDE:** "What Changed in 2025"

```
THE 2025 LANDSCAPE SHIFT

✗ KubeWeekly newsletter    → Dead. Last issue May 2025 (#434)
✗ Ship It podcast          → Dead. Now "Fork Around and Find Out"
✗ Old CNCF TAG Slack       → Archived. 8 TAGs became 5.

⚠ Kubernetes Slack         → Downgrade threatened, then CANCELLED
                              Still on Slack. Future uncertain.

✓ Bluesky                  → NOW the official social channel
                              v1.35 blog: "Follow us on Bluesky @kubernetes.io"
✓ Wisdom of the Cloud      → Replaced KubeWeekly (monthly, cncf.io/newsletter)
✓ LWKD                     → Still the best weekly digest (lwkd.info)
```

**Mumshad:** OK so I go to Google, I search "how to stay current with Kubernetes," and half the links I find recommend things that don't exist anymore.

**Michael:** Yeah, 2025 was a landscape shift. KubeWeekly — the newsletter everyone used to recommend — is dead. Last issue was number 434, May 2025. The replacement is "Wisdom of the Cloud," a monthly newsletter from CNCF.

"Ship It" — the podcast — rebranded to "Fork Around and Find Out." The old CNCF TAG Slack channels got archived when they restructured.

And then there was the Slack scare. In June 2025, Salesforce threatened to downgrade the Kubernetes Slack workspace — we're talking about 300,000+ members. The community mobilized, and the downgrade was cancelled. Slack is still the primary real-time channel. But the future is uncertain.

**Mumshad:** What about social media?

**Michael:** Bluesky. That's the official channel now. When v1.35 shipped, the release blog post said "Follow us on Bluesky @kubernetes.io." X is deprioritized. If you're following the Kubernetes account on Twitter and wondering why it's quiet — that's why.

---

### SCENE 9: "What Do I Actually Subscribe To?"
**Time: 1:30**
**SLIDE:** "The Non-Negotiable Five"

```
THE NON-NEGOTIABLE FIVE

1. kubernetes-security-announce    (Google Group — fires on CVEs only)
2. LWKD                           (lwkd.info — weekly dev digest)
3. Kubernetes Blog RSS             (kubernetes.io/feed.xml)
4. GitHub "Releases Only" watch    (kubernetes/kubernetes repo)
5. Official CVE JSON feed          (k8s.io/docs/reference/issues-security/
                                    official-cve-feed/)
```

**Mumshad:** OK Michael, just tell me — what do I actually subscribe to?

**Michael:** Five things. Non-negotiable.

One: kubernetes-security-announce. It's a Google Group. Low traffic — it only fires on CVEs. But when it fires, you need to know. Remember IngressNightmare? The CVE cluster that hit Ingress NGINX? If you were on this list, you knew before the blog posts started flying.

Two: LWKD — Last Week in Kubernetes Development. A weekly digest at lwkd.info. Best signal-to-noise ratio in the ecosystem.

Three: The Kubernetes Blog RSS feed. kubernetes.io/feed.xml. Release announcements, deprecation notices, security advisories — they all land here.

Four: GitHub "Releases Only" watch on the kubernetes/kubernetes repo. You'll get notified for every patch and minor release.

Five: The official CVE JSON feed. Machine-readable, automatable, and it's the source of truth for Kubernetes vulnerabilities.

These five cover security, releases, and deprecations — the three things that will actually break your production clusters.

---

### SCENE 10: "I Don't Have Time For This"
**Time: 1:30**
**SLIDE:** "30 Minutes/Week" system + role filters

```
THE 30-MINUTE WEEKLY SYSTEM

WEEKLY (20 min):  Read LWKD + scan 1-2 SIG Slack channels for your role
MONTHLY (30 min): Wisdom of the Cloud + Kubernetes blog scan
QUARTERLY (1 hr): Run pluto + kubent + review upcoming release KEPs

SUBSCRIBE ONCE:   security-announce, GitHub releases, CVE feed

BY ROLE:
  Developers  → SIG Apps, SIG API Machinery, SIG CLI
  Operators   → SIG Node, SIG Network, SIG Storage, SIG Auth
  Architects  → SIG Architecture, CNCF TOC notes, Alpha-stage KEPs
```

**Mumshad:** Five subscriptions, SIGs, TAGs, blogs, podcasts — Michael, I have a day job. I can't spend hours on this every week.

**Michael:** You don't need to. Here's the system.

Weekly: 20 minutes. Read LWKD and scan one or two SIG Slack channels relevant to your role.

Monthly: 30 minutes. Read Wisdom of the Cloud and do a quick scan of the Kubernetes blog.

Quarterly: One hour. Run pluto and kubent against your clusters — pluto checks your manifests for deprecated API versions, kubent checks your running cluster. Then review the KEPs for the upcoming release.

And the five subscriptions? Subscribe once. They come to you.

**Mumshad:** What about filtering by role?

**Michael:** If you're a developer — follow SIG Apps, SIG API Machinery, and SIG CLI. If you're an operator — SIG Node, SIG Network, SIG Storage, SIG Auth. If you're an architect — SIG Architecture, CNCF TOC meeting notes, and watch the Alpha-stage KEPs — that's where the future direction lives.

---

### SCENE 11: "I Want to Contribute. Where Do I Start?"
**Time: 2:00**
**SLIDE:** "Your First Contribution" — 5-step path

```
YOUR FIRST CONTRIBUTION

1. Join Slack NOW → slack.k8s.io
   #kubernetes-contributors | #sig-contribex | your SIG's channel

2. SIG Meet & Greet → happening THIS WEEK at KubeCon
   Lunch session, Project Pavilion — just walk up

3. Claim a good first issue → go.k8s.io/good-first-issue
   Comment /assign | Mentor included | Practice at
   github.com/kubernetes-sigs/contributor-playground

4. Monthly New Contributor Orientation → kubernetes.dev/docs/orientation/
   3rd Tuesday of every month

5. Structured programs:
   Release Team Shadow → watch #sig-release on Slack
   LFX Mentorship      → mentoring.cncf.io
   GSoC / Outreachy     → annual Kubernetes projects

Find Josh Berkus — Red Hat's K8s Community Architect, co-chairs SIG ContribEx. Slack: jberkus
```

**Mumshad:** *(genuinely interested)* What if I don't just want to follow along? What if I actually want to contribute?

**Michael:** Then the path exists and it's clear.

Step one: Join Slack. Right now. slack.k8s.io. Join #kubernetes-contributors, join #sig-contribex, and join the channel for whatever SIG interests you.

Step two: The SIG Meet & Greet. It happens at every KubeCon — it's a lunch session in the Project Pavilion. Just walk up. It's happening this week.

Step three: Claim a good first issue. go.k8s.io/good-first-issue — comment `/assign` and it's yours. Practice the mechanics first at the contributor playground.

Step four: Monthly New Contributor Orientation. Third Tuesday of every month. Self-paced course at kubernetes.dev/docs/onboarding.

Step five: Structured programs — Release Team Shadow, LFX Mentorship at mentoring.cncf.io, GSoC, Outreachy.

And find Josh Berkus — Red Hat's Kubernetes Community Architect, co-chairs SIG ContribEx. They build the onboarding infrastructure and curate those good first issues. Slack username: jberkus.

One more thing — the old "Contributor Summit" is now the Maintainer Summit. Happens Sunday before co-located events. If you contribute long enough, you'll get there.

---

### SCENE 12: Close + QR Code
**Time: 2:00**
**SLIDE:** QR code + repo URL + key takeaways

```
EVERYTHING IS IN THE REPO

[LARGE QR CODE]

github.com/peopleforrester/k8s-staying-current

- All links from this talk, verified and maintained
- Role-based subscription checklists
- All 24 SIGs — names, Slack channels, meeting times
- Governance reference (Steering, TOC, 5 TAGs, 11 WGs)
- Tool guides (pluto, kubent, RSS setup)
- "What Changed in 2025" summary
- First contribution path with direct links
```

**Mumshad:** *(drops character, addresses audience directly)* Alright, let's land this.

Everything we just talked about — every link, every tool, every checklist — is in a GitHub repo that we're going to maintain. Scan that QR code or go to github.com/peopleforrester/k8s-staying-current.

**Michael:** Five things to remember:

One: Your cert is a snapshot. Kubernetes ships three times a year.

Two: SIGs own everything. Follow the SIG, not the vendor blog.

Three: The information landscape changed in 2025. Update your bookmarks.

Four: Thirty minutes a week. That's all it takes.

Five: If you want to contribute, the path exists and it starts today.

**Mumshad:** Thank you all. Enjoy the rest of KubeCon.

---

## Timing Summary

| Scene | Topic | Time |
|-------|-------|------|
| 1 | Setup / Hook | 1:30 |
| 2 | Release cadence — "my cert is expiring?" | 2:00 |
| 3 | 24 SIGs — "who runs Kubernetes?" | 2:00 |
| 4 | TAGs vs SIGs (+ Security Slam) | 1:30 |
| 5 | KEP process — "how features ship" | 1:00 |
| 6 | Trace It: KEP-1287 — "show me the paper trail" | 1:30 |
| 7 | File a Bug — "I found something broken" | 1:30 |
| 8 | 2025 landscape shift — "half my bookmarks are broken" | 2:00 |
| 9 | The Non-Negotiable Five — "what do I subscribe to?" | 1:30 |
| 10 | 30 min/week system — "I don't have time" | 1:30 |
| 11 | First contribution path — "I want to contribute" | 2:00 |
| 12 | Close + QR code | 2:00 |
| | **TOTAL** | **20:00** |

**Buffer:** Zero — tight 20 minutes. Mumshad controls pacing by adjusting follow-up questions.

---

## Handoff Mechanics

- No formal handoffs. Mumshad asks, Michael answers.
- **Scene 1 → 2:** Mumshad explicitly sets up the role-play.
- **Scene 11 → 12:** Mumshad drops character. "Alright, let's land this." Shifts to direct address.
- Michael stays in educator mode throughout.

---

## Speaker Prep Notes

### What Mumshad Needs to Prep
1. The 10 questions (internalized, not memorized)
2. Reactive energy — surprise, frustration, mirroring audience
3. The close — drops character, drives audience to QR code
4. Timing awareness — zero buffer, so pace control is critical. Accelerate/decelerate by adjusting follow-ups.

### What Michael Needs to Prep
1. Facts cold: 24 SIGs, 5 TAGs, 7 Steering, 11 TOC, v1.35 Dec 17, v1.36 Apr 22, KubeWeekly died May 2025, Bluesky official
2. KEP-1287 walkthrough (4 steps, smooth and confident)
3. Bug filing flow + bot commands (`/sig`, `/assign`, `/kind bug`)
4. Security Slam 2026 mention (through March 20)
5. Pivot lines that set up the next question
6. Josh Berkus reference (delivered casually)
7. SIG Meet & Greet — check kccnceu2026.sched.com morning-of for exact day/time/location

---

## Facts to Re-Verify Week-Of (March 23–26, 2026)

<!-- VERIFY WEEK-OF -->

| Fact | Why It Might Change | Where to Check |
|------|---------------------|----------------|
| SIG Meet & Greet day/time | Not yet on schedule | kccnceu2026.sched.com |
| CNCF TOC membership | 6 of 11 seats expired Feb–Mar 2026 | github.com/cncf/toc README |
| v1.36 release schedule | Code Freeze is Mar 18, can slip | kubernetes.dev/resources/release/ |
| v1.35 latest patch level | New patches ship monthly | kubernetes.io/releases/ |
| K8s Podcast status | Last episode Dec 22, 2025 | kubernetespodcast.com |
| v1.32 EOL | Should be dead by March — confirm | kubernetes.io/releases/patch-releases/ |
