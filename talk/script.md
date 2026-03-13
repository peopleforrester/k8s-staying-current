# Talk Script: How Kubernetes Actually Ships

**Event:** KubeCon EU 2026 — Cloud Native Theater (Cloud Native University block)
**Date:** Tuesday, March 24, 2026 | 12:37–12:57 CET | Hall 1-5, Tram Zone
**Duration:** 20 minutes (17:00 scripted + 3:00 buffer)
**Speakers:** Mumshad Mannambeth & Michael Forrester (KodeKloud)
**Format:** Role-play conversation
**Slides:** 20 (thin — question/answer rhythm)

> **NOTE:** The working title "Every Channel You Need to Stay Current After Kubernetes Certification" was the internal/CFP title. The official scheduled title is "How Kubernetes Actually Ships: An Educator's Guide to Core Releases, SIGs, and Staying Current."

---

## Format Notes

Mumshad plays a recently certified Kubernetes engineer — the guy who just passed his CKA, is excited but overwhelmed, and doesn't know where to go next. He asks the questions the audience is already thinking.

Michael plays the CNCF educator — the experienced guide who's been in the ecosystem for years and can cut through the noise to show what actually matters.

The audience sees themselves in Mumshad. They get the answers from Michael. The role-play makes it conversational, memorable, and way more engaging than two guys reading slides at a room full of engineers who've been in sessions all day.

The deck has 20 slides but they're thin — each slide shows either Mumshad's question (gold italic text on dark background) or one anchor visual for Michael's answer. The conversation IS the talk. Slides track the question → answer rhythm. Everything detailed goes in the GitHub repo.

---

## Story Arc

| Act | Theme | Time |
|-----|-------|------|
| **Act 1** — "I Passed. Now What?" | Mumshad sets up the problem. Certified, proud, immediately lost. Michael explains why — the cert is a snapshot, not a subscription. He explains who actually runs Kubernetes. | 4 min |
| **Act 2** — "Show Me How This Works" | Progressively deeper questions. What are TAGs? How do features ship? Walk me through a real feature. I found a bug — how do I report it? Where do I find out what changed? Each answer builds on the last, constructing the mental model and giving the audience practical walkthroughs. | 10 min |
| **Act 3** — "Make It Actionable" | Mumshad gets practical. What do I subscribe to? I don't have time. I want to contribute. Where do I go RIGHT NOW at this conference? Michael gives him the system, the tools, and the specific next steps — including events happening this week at KubeCon EU. | 5 min |
| **Close + QR Code** | Both speakers summarize. Everything goes in the repo. Audience scans the code. | 1 min |

---

## Scene-by-Scene Script

### SCENE 1: The Setup
**Time: 1:00**

**SLIDE 1:** Title card — "How Kubernetes Actually Ships," speakers, KodeKloud logo, Cloud Native Theater

MUMSHAD: (to audience) So Michael and I have trained over a million students at KodeKloud. We've helped more people pass Kubernetes certifications than almost anyone. And you know what the number one message we get the week after someone passes their exam is?

(beat)

"I passed. Now what?"

That's literally it. "Now what." So today we're going to answer that question. I'm going to play the guy who just passed his CKA — because I remember exactly what that feels like — and Michael is going to be the guide I wish I'd had. Ready?

MICHAEL: Let's do it.

---

### SCENE 2: "My Cert Is Already Expiring?"
**Time: 1:30**

**SLIDE 2:** Question — *"I passed my CKA. How long before what I learned is out of date?"*

**SLIDE 3:** Release timeline — version table (v1.32–v1.35), stat boxes (3/year, ~15 weeks, 14 months), v1.36 callout, punchline: "Your cert is a snapshot."

MUMSHAD: Okay so I passed my CKA. I studied hard. I know my stuff. How long before what I learned is out of date?

MICHAEL: Honestly? Parts of it are already out of date. Kubernetes ships three releases a year on roughly 15-week cycles. v1.35, codenamed "Timbernetes," shipped December 17th. v1.36 is targeting April 22nd — that's less than a month from now. Each release can deprecate APIs, graduate features, or change default behaviors.

Here's a real example: v1.32 — end of life was February 28th. That's three weeks ago. If you passed your cert on v1.32, that version is already unsupported. And here's one that's going to affect a lot of people in this room: Ingress NGINX is being archived after March 2026. Gateway API is the replacement. If you learned Ingress for your cert, you need to learn Gateway API now. Your cert is a snapshot. The ecosystem is a moving target.

MUMSHAD: So how do I track that? I can't re-study every four months.

MICHAEL: You don't need to. You need a system. But first, let me show you how the machine works — because once you understand the structure, you'll know exactly where to look.

---

### SCENE 3: "Who Actually Runs Kubernetes?"
**Time: 2:00**

**SLIDE 4:** Question — *"Is CNCF in charge of Kubernetes?"*

**SLIDE 5:** 24 SIGs grid — 8 key SIGs in cards, landlord/tenant tagline

MUMSHAD: Here's something that always confused me. Is CNCF in charge of Kubernetes? Like, does CNCF decide what goes into the next release?

MICHAEL: No. This is the single most common misconception in the entire ecosystem. Kubernetes is governed by 24 Special Interest Groups — SIGs. Every line of code, every API, every feature belongs to a SIG. SIG Network owns all networking. SIG Node owns the kubelet. SIG Auth owns RBAC. SIG Apps owns your Deployments and StatefulSets.

MUMSHAD: Twenty-four. Not 21? I've seen older docs say 21.

MICHAEL: Twenty-four. The newest is SIG etcd, established November 2023. If your reference material says 21, it's out of date. This is exactly the kind of thing that changes quietly while people aren't looking.

Think of it like a landlord and tenant. CNCF provides the house — the trademark, the infrastructure, the events, this conference. Kubernetes is a tenant with a very detailed lease. Three bodies you need to know: the Steering Committee — 7 elected members, handles Kubernetes governance, disputes, community policy. The Technical Oversight Committee — that's the TOC, 11 members on the CNCF side — they handle which projects get accepted and at what maturity level. And the 24 SIGs — they own the actual code. The TOC doesn't tell Kubernetes what code to write. If you ever want to know who's in each body: github.com/kubernetes/steering and github.com/cncf/toc.

MUMSHAD: So if I want to know what's changing in networking, I don't read the CNCF blog. I follow SIG Network.

MICHAEL: Exactly. The signal is at the SIG level.

---

### SCENE 4: "But Wait — What About TAGs?"
**Time: 1:30**

**SLIDE 6:** Question — *"What are TAGs? Are they the same as SIGs?"*

**SLIDE 7:** SIGs ≠ TAGs comparison — big SIGs/TAGs headers, all 5 TAG boxes, "WHAT DOES A TAG ACTUALLY DO?" section with concrete examples, punchline

MUMSHAD: I keep seeing "TAGs" mentioned too. Are those the same as SIGs?

MICHAEL: No, and this confuses everyone. CNCF originally called their groups SIGs too. They renamed them TAGs — Technical Advisory Groups — specifically to avoid confusion. It didn't work.

The key difference: SIGs own code. TAGs advise. In May 2025, CNCF restructured from 8 TAGs to 5. If your docs mention TAG App Delivery, TAG Runtime, or TAG Environmental Sustainability — those don't exist anymore. Old Slack channels were archived last June.

MUMSHAD: So what does a TAG actually produce? If they don't write code, what do they do?

MICHAEL: Real things. TAG Security and Compliance — which is probably the most active — has run security assessments on over 50 CNCF projects. Falco, Harbor, OPA, Kyverno — they've all gone through the process. They published the Cloud Native Security Whitepaper, now on version 2, translated into five languages. The Software Supply Chain Best Practices guide. And here's one that's happening right now: the 2026 Security Slam. It runs through March 20th — that's during this conference. For the first time this year it's open to all open-source projects, not just CNCF. That's a TAG producing real, tangible work.

The one-liner is this: SIGs write Go and merge PRs. TAGs write white papers and evaluate projects for the Technical Oversight Committee.

MUMSHAD: Okay. So how does a feature actually get into Kubernetes?

---

### SCENE 5: "How Do Features Actually Ship?"
**Time: 1:30**

**SLIDE 8:** Question — *"How does a feature actually get into Kubernetes?"*

**SLIDE 9:** KEP pipeline — Alpha/Beta/Stable boxes with color bars, v1.35 stat (60 enhancements: 17/19/22), KEP URL pattern, kep.k8s.io shortcut, relnotes.k8s.io

MUMSHAD: Who decides "this goes in v1.36"?

MICHAEL: Every significant change goes through a KEP — Kubernetes Enhancement Proposal. It lives in the kubernetes/enhancements repo on GitHub. A KEP starts at alpha — off by default, experimental. Then beta — on by default. Then stable — GA, production-ready.

v1.35 shipped with 60 enhancements. 17 hit stable.

And here's the thing most people don't know: every KEP lives at a predictable URL. It's `github.com/kubernetes/enhancements/tree/master/keps/sig-{name}/{number}-{description}`. And there's a shortcut — `kep.k8s.io` slash the number. That jumps straight to the tracking issue. And relnotes.k8s.io lets you filter release notes by version, SIG, and kind.

MUMSHAD: Can we trace a real one?

MICHAEL: Let's do it.

---

### SCENE 6: "Trace a Feature"
**Time: 1:30**

**SLIDE 10:** Question — *"I heard about In-Place Pod Resize. Where did it come from?"*

**SLIDE 11:** Trace walkthrough — 4-step path (search KEP table → read kep.yaml → check tracking issue → find in release notes) + kep.yaml metadata card showing sig-node, v1.27 alpha, v1.32 beta, v1.35 stable (GA!)

MUMSHAD: I heard about In-Place Pod Resize — it lets you change CPU and memory on a running pod without restarting it. That sounds huge. Where did it come from?

MICHAEL: Let me trace it for you. Step one: go to kubernetes.dev/resources/keps — that's a searchable table of every KEP. Search "pod resize."

Step two: you land on KEP-1287. Open the kep.yaml file. It tells you everything. Owning SIG: sig-node. Alpha in v1.27. Beta in v1.32. Stable — GA — in v1.35. Feature gate: InPlacePodVerticalScaling. Participating SIGs: sig-autoscaling and sig-scheduling.

Step three: kep.k8s.io/1287 takes you straight to the tracking issue. Labels show sig/node and the current stage.

Step four: go to relnotes.k8s.io, filter by v1.35 and sig-node, and there it is.

Every major feature has a paper trail. The URL is predictable. The data is machine-readable. You don't need insider access. You just need to know where to look.

MUMSHAD: Okay, that's features. What about bugs?

---

### SCENE 7: "I Found a Bug"
**Time: 1:30**

**SLIDE 12:** Question — *"I found a bug in Kubernetes. How do I report it?"*

**SLIDE 13:** Bug filing walkthrough — 4 steps (issue template → fill form → bot labels automatically → SIG picks it up) + key bot commands card (/sig, /triage, /assign, /kind, /lgtm, /approve) + security warning

MUMSHAD: Say I hit something weird in kubelet. Where do I even file it?

MICHAEL: github.com/kubernetes/kubernetes/issues/new/choose. Blank issues are disabled — you have to pick a template. Select "Bug Report." Fill out the form: what happened, how to reproduce it, your kubectl version, runtime, OS.

The moment you click submit, @k8s-ci-robot — that's the Prow automation bot — applies two labels: `kind/bug` and `needs-triage`. If you didn't specify a SIG, it also adds `needs-sig`.

Then a triager routes it. They comment `/sig node` and the bot moves it to SIG Node's queue. The SIG reviews it: `/triage accepted`, then `/priority important-soon`, then someone comments `/assign` to take ownership. When the fix PR is ready, a reviewer comments `/lgtm`, an approver comments `/approve`, and Tide — the merge bot — merges it automatically.

The full bot command reference is at go.k8s.io/bot-commands.

One critical thing: security vulnerabilities NEVER go through public issues. Those go through kubernetes.io/security. Private disclosure only.

MUMSHAD: So even bug reporting is structured. It's not chaos.

MICHAEL: It's an assembly line with bots. And speaking of things that changed while you weren't looking...

---

### SCENE 8: "Half My Bookmarks Are Broken"
**Time: 1:30**

**SLIDE 14:** Question — *"I subscribed to KubeWeekly while studying. Am I good?"*

**SLIDE 15:** Dead/alive channels — red/amber/green status rows: KubeWeekly (dead), Ship It (dead), Old TAG Slack (dead), K8s Slack (warning), Bluesky (alive), LWKD (alive), Wisdom of the Cloud (alive)

MUMSHAD: Let me test you. I subscribed to KubeWeekly while studying. Am I good?

MICHAEL: KubeWeekly is dead. Issue 434 was the last one — May 2025. Replaced by Wisdom of the Cloud, a CNCF monthly newsletter. Monthly, not weekly. That's a big gap.

Ship It from Changelog — gone. Replaced by "Fork Around and Find Out."

Kubernetes Slack almost died. Salesforce threatened a free-tier downgrade last June — would've killed message history. Community panicked. Salesforce reversed at the last minute. Still on Slack, but the long-term platform is uncertain.

And Bluesky is now an official Kubernetes social channel — @kubernetes.io, domain-verified. The kubernetes.io community page lists it before X, and the homepage embeds a live Bluesky feed. X still exists but it's deprioritized. If you want real-time cloud native conversation, the community moved to Bluesky.

MUMSHAD: (to audience) So in the last year: my newsletter died, my Slack almost died, and my social media feed moved platforms. And nobody sent me a memo.

MICHAEL: Nobody sends memos in open source. That's why you need a system.

---

### SCENE 9: "What Do I Actually Subscribe To?"
**Time: 1:30**

**SLIDE 16:** Question — *"I'm overwhelmed. What do I actually need?"*

**SLIDE 17:** Non-Negotiable Five (left) + 30 min/week cadence (right) + role filters (bottom)

MUMSHAD: There are a million channels. What do I actually need?

MICHAEL: Five things. Non-negotiable. Miss any and you're flying blind.

One: kubernetes-security-announce. Google Group. Fires on CVEs only.

Two: LWKD — Last Week in Kubernetes Development. Weekly digest. The single most efficient channel in the ecosystem.

Three: Kubernetes blog RSS. kubernetes.io/feed.xml. Every release, every deprecation.

Four: GitHub "Releases Only" watch on kubernetes/kubernetes. Zero noise.

Five: Official CVE JSON feed. Machine-readable. Point your automation at it.

That covers security, releases, and deprecations — the three things that break production clusters.

MUMSHAD: And the time commitment?

MICHAEL: Thirty minutes a week. Weekly: read LWKD plus one or two SIG Slack channels for your role. Monthly: Wisdom of the Cloud plus blog scan. Quarterly: run deprecation scanners against your clusters. Pluto — v5.22.7, actively maintained by Fairwinds — scans your manifests for deprecated API versions. kubent is the other common tool, but fair warning: the last release was August 2024 and the project has maintenance issues — only covers deprecations through v1.32. KubePug is an alternative that uses live API specs as a kubectl plugin. Any of these take seconds to run and save you hours after a botched upgrade.

Filter by role. Developers: SIG Apps, CLI. Operators: SIG Node, Network, Auth. Architects: SIG Architecture, Alpha KEPs.

MUMSHAD: That's it? Thirty minutes?

MICHAEL: Put it on your calendar. It's a habit, not a project.

---

### SCENE 10: "I Want to Contribute. Where Do I Start?"
**Time: 2:00**

**SLIDE 18:** Question — *"I want to go deeper. How do I start contributing?"*

**SLIDE 19:** 5-step contribution path with numbered circles + Josh Berkus callout

MUMSHAD: Last question. This is a contributor conference. I want to go deeper than consuming information. I want to contribute. But it feels intimidating.

MICHAEL: It is intimidating. And the community knows that, which is why they've built an actual onboarding path.

Step one: Join Kubernetes Slack. slack.k8s.io. Join #kubernetes-contributors and #sig-contribex.

Step two — the one I really want you to hear — SIG Meet & Greet. It happens at every KubeCon. It's likely happening this week — check the KubeCon app. SIG representatives sit at tables. You walk up. No registration. No credentials. You say "I'm new and I want to help."

And look for Josh Berkus while you're here — Red Hat's Kubernetes Community Architect, co-chairs SIG ContribEx. Find him on Slack as jberkus. He is the connector.

Step three: go.k8s.io/good-first-issue. Issues curated for first-time contributors. Each one has a mentor. Comment /assign and it's yours. And if you want to explore beyond Kubernetes to any CNCF project, check out clotributor.dev — it's a search engine that indexes help-wanted issues across every CNCF project. Filter by difficulty, language, project. Whitney Lee turned me on to that one.

Step four: monthly New Contributor Orientation. Third Tuesday. kubernetes.dev/docs/orientation.

Step five: structured programs. Release Team Shadow — no experience required, watch #sig-release. LFX Mentorship — 187 successful projects in 2025, and 25 mentee alumni have gone on to become CNCF project maintainers. That's the flywheel. And here's a timely one: CNCF is a GSoC 2026 mentoring organization. Contributor applications open March 16th — that's this week. You could literally apply from this conference.

MUMSHAD: (to audience) So there's no excuse.

MICHAEL: There really isn't.

---

### SCENE 11: Close + QR Code
**Time: 1:00**

**SLIDE 20:** QR code (large) + repo URL + 5 takeaway checkmarks

MUMSHAD: (dropping character, speaking as himself) Alright, let's land this. Everything Michael just walked me through — every link, every SIG, every tool, every subscribe button — is in this repo. Take a photo. Star it. We keep it updated.

MICHAEL: Five things to remember.

One: your cert is a snapshot. Kubernetes ships three times a year.

Two: SIGs own everything. Follow the SIG, not the vendor blog.

Three: the information landscape changed in 2025. Update your bookmarks.

Four: thirty minutes a week. That's all it takes.

Five: the path to contribute exists. It starts today.

MUMSHAD: Thank you.

---

## Timing Summary

| Scene | Topic | Time |
|-------|-------|------|
| 1 | Setup / Hook | 1:00 |
| 2 | Release cadence — "my cert is expiring?" | 1:30 |
| 3 | 24 SIGs — "who runs Kubernetes?" | 2:00 |
| 4 | TAGs vs SIGs — "what do TAGs actually do?" | 1:30 |
| 5 | KEP process — "how features ship" | 1:30 |
| 6 | Trace a feature — "where did In-Place Pod Resize come from?" | 1:30 |
| 7 | File a bug — "I found a bug, how do I report it?" | 1:30 |
| 8 | 2025 landscape shift — "half my bookmarks are broken" | 1:30 |
| 9 | Non-Negotiable Five + 30 min/week — "what do I subscribe to?" | 1:30 |
| 10 | First contribution path — "I want to contribute" | 2:00 |
| 11 | Close + QR code | 1:00 |
| | **TOTAL** | **17:00** |

**Buffer: 3 minutes** for audience reaction, natural pauses, Mumshad's beat moments, and minor overruns. Target in rehearsal: under 18 minutes.

---

## Slide Deck (20 slides)

| Slide | Type | Content |
|-------|------|---------|
| 1 | Title | "How Kubernetes Actually Ships," speakers, KodeKloud, Cloud Native Theater |
| 2 | **Question** | *"I passed my CKA. How long before what I learned is out of date?"* |
| 3 | Answer | Release table (v1.32–v1.35), stat boxes, v1.36 callout |
| 4 | **Question** | *"Is CNCF in charge of Kubernetes?"* |
| 5 | Answer | 24 SIGs grid (8 key SIGs), governance key (Steering/TOC/SIGs), landlord/tenant |
| 6 | **Question** | *"What are TAGs? Are they the same as SIGs?"* |
| 7 | Answer | SIGs ≠ TAGs comparison, all 5 TAGs, concrete TAG output, Technical Oversight Committee spelled out |
| 8 | **Question** | *"How does a feature actually get into Kubernetes?"* |
| 9 | Answer | KEP pipeline (Alpha→Beta→Stable), v1.35 breakdown, URL patterns |
| 10 | **Question** | *"I heard about In-Place Pod Resize. Where did it come from?"* |
| 11 | Answer | KEP-1287 trace: 4-step walkthrough + kep.yaml metadata card |
| 12 | **Question** | *"I found a bug in Kubernetes. How do I report it?"* |
| 13 | Answer | Bug filing: 4 steps + bot commands card + security warning |
| 14 | **Question** | *"I subscribed to KubeWeekly while studying. Am I good?"* |
| 15 | Answer | Dead/alive channel status rows (red/amber/green), Bluesky as official (listed before X) |
| 16 | **Question** | *"I'm overwhelmed. What do I actually need?"* |
| 17 | Answer | Non-Negotiable Five + 30 min/week cadence + pluto/kubent/kubepug + role filters |
| 18 | **Question** | *"I want to go deeper. How do I start contributing?"* |
| 19 | Answer | 5-step contribution path + Josh Berkus callout |
| 20 | Close | QR code + repo URL + 5 takeaways |

---

## Handoff Mechanics

There are no formal handoffs in this format. Mumshad asks, Michael answers. Three structural transitions need to feel deliberate:

**Scene 1 → 2:** Mumshad explicitly sets up the role-play. "I'm going to play the guy who just passed his CKA." This signals to the audience what's happening.

**Scene 5 → 6:** Michael says "Let's do it" and walks through a live trace. This shifts from conceptual to practical — the audience feels the gear change.

**Scene 10 → 11:** Mumshad drops character. "Alright, let's land this." He shifts from role-play to direct address for the close. This signals the talk is wrapping up.

Michael stays in educator mode throughout. He doesn't need to break character because his character IS his real self.

---

## Speaker Prep Notes

### What Mumshad Needs to Prep

**The questions.** Mumshad needs to internalize the 10 questions, not memorize them word-for-word. The questions should feel natural, like a real conversation. If he can hit the general topic of each question, Michael can steer the answer.

**Reactive energy.** The role-play works because Mumshad reacts authentically — surprise at the 24 SIG count, frustration at dead bookmarks, "so there's no excuse" at the contribution path. These reactions mirror the audience.

**The close.** Mumshad owns the close. He drops character, speaks directly to the audience, and drives them to the QR code. This is the most important 60 seconds — it's the last thing they remember.

**Timing awareness.** If a scene runs long, Mumshad can accelerate by asking shorter follow-ups or cutting to the next question. If a scene runs short, he can ask a natural follow-up. The role-play format is inherently more flexible than slides.

### What Michael Needs to Prep

**The facts cold.** Michael needs these committed to memory:

- 24 SIGs (newest: SIG etcd, Nov 2023)
- 5 TAGs (restructured May 2025)
- 7 Steering Committee members (elected Nov 2025) — github.com/kubernetes/steering
- 11 Technical Oversight Committee (TOC) members (6 seats expired Feb–Mar 2026) — github.com/cncf/toc
- v1.35 shipped Dec 17, 2025
- v1.36 targets Apr 22, 2026
- v1.32 EOL Feb 28, 2026
- KubeWeekly died May 2025
- Bluesky @kubernetes.io is official K8s social channel (listed before X on kubernetes.io/community — NOT "primary," both are listed)
- 60 enhancements in v1.35 (17 Stable, 19 Beta, 22 Alpha)
- KEP-1287: In-Place Pod Resize, sig-node, alpha v1.27, beta v1.32, GA v1.35
- Prow bot commands: /sig, /triage accepted, /assign, /lgtm, /approve
- go.k8s.io/bot-commands for full reference
- Security Slam 2026 runs through March 20 (during KubeCon)
- pluto v5.22.7 (actively maintained, Dec 2025)
- kubent v0.7.3 (last release Aug 2024, project effectively unmaintained — maintainer quit per Issue #732, only covers through v1.32) — mention on stage WITH caveat or just say "kubent" without version
- KubePug (kubectl deprecations plugin) — alternative to kubent, uses live API specs
- CLotributor.dev — CNCF contribution finder (Whitney Lee rec)
- GSoC 2026 contributor applications open March 16, close March 31 (during KubeCon week)
- LFX Mentorship: 187 projects in 2025, 25 alumni became maintainers, Term 1 running now
- Outreachy: CNCF not currently active (last was Dec 2024–Mar 2025) — do NOT mention on stage
- Kubernetes Podcast from Google: last episode #264 was Dec 22, 2025 — appears silently ended (Apple shows "2018–2025")
- relnotes.k8s.io: known v1.35 JSON parsing bug (trailing comma) — test before demoing live; other versions work
- Maintainer Summit (NOT "Contributor Summit") — happened Sunday March 22 at RAI Amsterdam

**The walkthrough flows.** Scenes 6 and 7 are mini-demos. Michael should be able to narrate the KEP trace and bug filing steps without hesitation. If there's a live browser on stage, these can be shown — but the slides carry the content if not.

**The pivot lines.** Each answer ends with a natural setup for the next question. "That's why you need a system" → Mumshad asks about subscriptions. "Things move" → broken bookmarks. "Let's do it" → feature trace. "Even bug reporting is structured" → landscape shift. Michael controls pacing through these pivots.

**Josh Berkus reference.** Delivered casually, not as a scripted plug. "Look for Josh Berkus while you're here — Red Hat's Kubernetes Community Architect..." Should feel like a genuine recommendation, because it is.

**The SIG Meet & Greet reference.** Michael should check kccnceu2026.sched.com the morning of the talk to confirm exact day/time/location. At past KubeCons it's been a lunch session (~12:00–2:30 PM) in the Project Pavilion. If confirmed, name the specific day and room. If not yet listed, say "check your KubeCon app — it's coming."

---

## Speaker Prep Checklist

- [ ] Mumshad has internalized the 10 questions (not memorized — internalized)
- [ ] Michael has the key numbers cold (24 SIGs, 5 TAGs, v1.35 Dec 17, KEP-1287 trace, bot commands, etc.)
- [ ] Michael can narrate the KEP-1287 trace and bug filing walkthrough without notes
- [ ] Michael can explain Steering Committee / TOC / SIGs governance in one breath
- [ ] Michael knows CLotributor.dev one-liner and GSoC application dates (Mar 16–31)
- [ ] Michael knows kubent maintenance caveat (v0.7.3 Aug 2024, maintainer quit, covers through v1.32 only)
- [ ] Michael knows KubePug as the kubent alternative
- [ ] QR code generated and tested (resolves to correct repo)
- [ ] Repo is public with all content live (especially walkthroughs/ and contributing/ directories)
- [ ] Full run-through done conversationally (not from script — talk naturally)
- [ ] Timed at under 18 min in rehearsal
- [ ] relnotes.k8s.io tested live for v1.35 — known JSON parsing bug, may or may not be fixed
- [ ] SIG Meet & Greet day/time confirmed from kccnceu2026.sched.com morning-of
- [ ] Security Slam 2026 confirmed still running (ends Mar 20)
- [ ] GSoC 2026 application window confirmed open (opens Mar 16)
- [ ] CLotributor.dev confirmed live and indexing
- [ ] TOC membership re-checked (6 seats expiring, roster may have changed)
- [ ] LWKD latest issue checked — reference current week's issue, not a stale one
- [ ] Josh Berkus confirmed attending (check #sig-contribex on Slack)
- [ ] v7 stage deck loaded and tested on venue AV — **Hall 1-5, Tram Zone** (NOT Hall 8 Room G)
- [ ] Water for both speakers
- [ ] Timer visible to both speakers (phone on podium)

---

## Facts to Re-Verify Week-Of (March 23–26, 2026)

<!-- VERIFY WEEK-OF -->

| Fact | Why It Might Change | Where to Check |
|------|---------------------|----------------|
| SIG Meet & Greet day/time | Not yet on schedule | kccnceu2026.sched.com |
| CNCF TOC membership | 6 of 11 seats expired Feb–Mar 2026 | github.com/cncf/toc README |
| v1.36 release schedule | Code Freeze is Mar 18, can slip | kubernetes.dev/resources/release/ |
| v1.35 latest patch level | New patches ship monthly | kubernetes.io/releases/ |
| K8s Podcast status | Last episode #264 Dec 22, 2025 — appears ended | kubernetespodcast.com |
| v1.32 EOL | Should be dead by March — confirm | kubernetes.io/releases/patch-releases/ |
| Security Slam 2026 status | Confirm still running through Mar 20 | cncf.io blog |
| KEP-1287 stage | Verify still listed as stable in v1.35 | kep.k8s.io/1287 |
| GSoC 2026 application window | Opens Mar 16, closes Mar 31 — confirm | summerofcode.withgoogle.com |
| CLotributor.dev | Confirm site is live and indexing | clotributor.dev |
| relnotes.k8s.io v1.35 bug | Trailing comma JSON parsing error reported Dec 2025 — may be fixed | relnotes.k8s.io (try v1.35) |
| kubent maintenance status | Last release Aug 2024, maintainer quit — confirm still usable | github.com/doitintl/kube-no-trouble/issues/732 |
| LWKD latest issue | Publishing weekly — check morning-of for most current | lwkd.info |
| Maintainer Summit schedule | Happening March 22 — confirm rooms/sessions | maintainersummiteu2026.sched.com |
