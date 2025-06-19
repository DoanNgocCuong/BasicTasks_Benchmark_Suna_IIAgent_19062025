# Pika Gamification V1 – Consulting Deck Outline (DRAFT)

## 1. Executive Summary

This execution plan delivers a focused, expert-powered pathway to launch a robust V1 gamification layer for Pika—the English-speaking robot for Vietnamese children aged 5–10—within 8–10 weeks. Leveraging both in-house and external expertise, the plan sharpens the current BRD by aligning it with Pika’s developmental, technical, and engagement principles, as well as hardware and bandwidth constraints. The approach emphasizes rapid, iterative prototyping and validation, with clear roles, deliverables, and checkpoints. It ensures that all gamification mechanics reinforce learning, drive daily engagement, and foster meaningful child-parent interaction, while remaining feasible for a small core team. The result is a shippable, measurable, and extensible gamification system that sets the foundation for future growth.

## 2. Expert-Contribution Map

| Role                        | Skill Profile                                      | Key Artefacts Delivered                                 |
|-----------------------------|----------------------------------------------------|---------------------------------------------------------|
| Reward-Economy Designer     | Gamification, child motivation, reward systems      | Reward system spec, XP/streak/badge logic, reward maps  |
| UX Motion Artist            | Animation, UI/UX for children, micro-interactions   | Animated feedback prototypes, motion spec sheets        |
| Child-Psychology Researcher | Developmental psych, play-test, child engagement    | Play-test protocol, observation reports, delight metrics|
| Unity/Canvas Prototyper     | Rapid prototyping, interactive UI, game engines     | Playable paper & digital prototypes, asset handoff      |
| Edtech Play-Test Facilitator| User research, child testing, parent engagement     | Play-test session plans, feedback synthesis             |
| (Optional) Localization/Story Expert | Narrative, cultural adaptation, child storytelling | Story arcs, dialogue samples, cultural review notes     |

## 3. End-to-End Workflow

**Phase 1: Gap Audit (Week 1–2)**
- Review BRD vs. Design Framework with core team and external experts
- Identify misalignments, missing mechanics, and technical blockers
- Output: Gap analysis doc, prioritized action list

**Phase 2: Co-Creation Sprints (Week 2–6)**
- Sprint 1: Concept & Paper Prototype (reward logic, feedback, progression)
- Sprint 2: Motion/UX Prototyping (animated feedback, micro-interactions)
- Sprint 3: Playable Prototype (Unity/Canvas, basic reward loop)
- Output: Playable prototype, reward system spec, motion assets

**Phase 3: Play-Test Loops (Week 5–7)**
- Play-test with target children (5–10 yrs) and parents
- Collect delight, engagement, and learning data
- Iterate on reward/feedback mechanics and visuals
- Output: Play-test report, refined prototype, delight/retention metrics

**Phase 4: Implementation Support & Handoff (Week 7–10)**
- Finalize V1 reward system, badge logic, and progression
- Code handoff, KPI handshake, and dev support
- Output: Shippable gamification layer, KPI dashboard, demo review


## 4. RACI Matrix

| Phase                | Task/Decision                  | Product Lead | Dev Team | Reward Designer | UX Motion Artist | Child Psych Researcher | Prototyper | Play-Test Facilitator |
|----------------------|-------------------------------|--------------|----------|-----------------|------------------|-----------------------|------------|----------------------|
| Gap Audit            | Review, gap analysis          | A/R          | C        | R               | C                | C                     | C          | C                    |
| Co-Creation Sprints  | Reward logic, prototyping     | A            | C        | R               | R                | C                     | R          | C                    |
| Play-Test Loops      | Play-test, feedback           | C            | C        | C               | C                | R                     | C          | R                    |
| Implementation/Handoff| Finalize, code handoff, KPI  | A/R          | R        | C               | C                | C                     | C          | C                    |

A = Accountable, R = Responsible, C = Consulted

## 5. I/O Contract Table

| Phase                | Inputs                                 | Outputs                                 | Acceptance Criteria                        | Tools/Formats                |
|----------------------|----------------------------------------|------------------------------------------|---------------------------------------------|------------------------------|
| Gap Audit            | BRD, Design Framework, expert input    | Gap analysis doc, action list            | All gaps/risks identified, prioritized      | FigJam, Google Docs          |
| Co-Creation Sprints  | Gap list, reward concepts, motion refs | Paper & digital prototypes, reward spec   | Playable prototype, feedback-ready assets   | Figma, Unity/Canvas, JSON    |
| Play-Test Loops      | Prototype, test protocol, user pool    | Play-test report, delight/retention data  | 10+ child sessions, clear delight metrics   | Video, survey, observation   |
| Implementation/Handoff| Final spec, code, KPI list            | Shippable gamification layer, KPI board   | Passes QA, demoable, KPI dashboard live    | Git, MQTT demo, KPI dashboard|

## 6. Lean-Execution Guardrails

- **Hardware/Bandwidth:**
  - All visuals/animations optimized for 480×320 TFT, 20fps max
  - Audio assets compressed for 0.8 Mbps download speed
  - Memory footprint for all assets < 16MB Flash, 8MB PSRAM
- **Interaction:**
  - All core loops must be operable via buttons, touch sensors, and ASR (no touchscreen required)
  - Feedback and rewards must be multi-modal (visual, audio, physical)
  - No feature may require more than 3 concurrent input types
- **Scope:**
  - Only mechanics that reinforce learning and habit (XP, streaks, badges, surprise rewards, parent loop)
  - No “game for game’s sake” features; all must tie to learning or engagement
  - All prototypes must be playable and testable within 1 sprint
  - Team size: ≤5 core devs, with external expert input as mapped


## 7. Reward-System Design Kit

- **Core Mechanics:**
  - XP (Star Fuel): Earned for every learning action, with bonus for streaks and effort
  - Gems: Collectible for completing micro-loops (words/phrases)
  - Topic Badges: For finishing all content in a topic, displayed in a collection
  - Streaks: Daily learning streaks, with freeze option (earned or bought)
  - Pika Customization: Unlockable accessories, moods, and outfits
  - Journey Map: Visualizes progress, unlocks new worlds/chapters
  - Surprise Rewards: Mystery bags, spin-to-win, puzzle reveals, random drops
  - Parent Loop: Notifies parents, enables co-rewarding, celebrates milestones
- **Tuning for 5–10 yrs:**
  - Instant, expressive feedback (animation, sound, voice)
  - Tangible, visual progress (maps, sticker books, badges)
  - Nurturing and autonomy (let kids help/teach Pika, choose rewards)
  - Story-driven rewards (Pika’s journey, emotional unlocks)
  - Surprise and delight (unboxing, mystery, randomization)
  - All rewards reinforce learning, not just engagement
- **References:**
  - Night Zookeeper, Duolingo Kids, Pokémon badge showcases, Tamagotchi mood meters, surprise egg mechanics


## 8. External-Resource Channels

- **Specialist Communities:**
  - Gamification: GamFed Slack, Octalysis Prime, Gamification Hub (Facebook)
  - UX/Motion: Dribbble, Behance, Motion Design Slack, Upwork (filter: children’s UX, animation)
  - Child Psychology: Academic partnerships (local universities), LinkedIn, ResearchGate
  - Edtech Play-Test: EdSurge, EdtechX, local teacher networks
- **Talent Platforms:**
  - Upwork (filter: gamification, child UX, Unity prototyping)
  - Toptal (for rapid prototyping, animation)
  - Fiverr (for quick asset creation)
- **Briefing Tips:**
  - Share BRD, Design Framework, and this execution plan
  - Use clear deliverable checklists and sprint timelines
  - Prioritize candidates with proven edtech/child product experience


## 9. Timeline & Milestones

| Week | Phase                  | Key Activities/Checkpoints                | Demoable Output         | Risks & Mitigations                                 |
|------|------------------------|-------------------------------------------|------------------------|-----------------------------------------------------|
| 1    | Gap Audit              | BRD/Framework review, expert onboarding   | Gap analysis doc       | Misalignment: daily sync, expert Q&A                |
| 2-3  | Co-Creation Sprint 1   | Reward logic, paper prototype             | Paper prototype demo   | Slow start: pre-schedule expert sessions            |
| 3-4  | Co-Creation Sprint 2   | Motion/UX prototyping, asset creation     | Animated feedback demo | Asset lag: use placeholder art, parallelize tasks   |
| 4-6  | Co-Creation Sprint 3   | Playable prototype, reward loop           | Playable prototype     | Tech blockers: dev check-ins, fallback to paper     |
| 5-7  | Play-Test Loops        | User testing, feedback, iteration         | Play-test report       | Low delight: rapid iteration, extra test sessions   |
| 7-9  | Implementation Support | Finalize logic, code handoff, KPI setup   | Shippable V1 build     | Dev overload: stagger handoff, focus on core loop   |
| 9-10 | Demo & Review          | KPI review, parent/child feedback         | Demo, KPI dashboard    | Missed KPIs: scope cut, extra bugfix sprint         |


## 10. Success Metrics

- **Quantitative:**
  - Daily active learning minutes per user (target: +20% vs. baseline)
  - 7-day and 30-day streak retention rates
  - % of users earning at least 1 badge per week
  - Parent engagement rate (noti open, reward sent)
  - Play-test delight score (target: 4.5/5 avg)
- **Qualitative:**
  - Child-reported enjoyment and favorite reward moments
  - Parent feedback on child motivation and learning
  - Observed delight reactions (laughter, pride, surprise)
  - Play-test session notes (engagement, confusion, boredom)

