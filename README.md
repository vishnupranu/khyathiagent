# Khyathi.ai (khyathiagent)

**Production-grade Multi-Agent AI Orchestration System**

Khyathi Core sits at the center as the Orchestrator. It receives user requests, breaks them into sub-tasks, routes them to specialized agents running in parallel (or coordinated sequence), manages shared memory, and synthesizes the final result.

Inspired by advanced agentic systems, built for real production use: planning → design → code → marketing → automation & deployment.

---

## Vision

> A premium, multi-purpose AI agent platform that can take a high-level idea and deliver a complete package: Product Specs, UI/UX Design, Working Code, Go-to-Market Strategy, and real-world automation/deployment actions.

---

## High-Level Architecture

```
                       [ USER INTERFACE (Chat + Workspace) ]
                                        │
                                        ▼
                        ╔═══════════════════════════════╗
                        ║   KHYATHI CORE (Orchestrator) ║
                        ║  Intent Routing & Memory Hub  ║
                        ╚═══════════════════════════════╝
                                        │
        ┌───────────────┬───────────────┼───────────────┬───────────────┐
        │               │               │               │               │
  [SPEC AGENT]    [DESIGN AGENT]   [CODE AGENT]   [MARKETING AGENT] [WORK AGENT]
  - PRDs          - UI/UX Flows    - Full-Stack   - SEO & Copy      - Task Auto
  - Architecture  - Wireframes     - Debugging    - Ad Campaigns    - Scheduling
  - User Stories  - Image Gen      - Deployment   - Social Media    - Data Entry
        │               │               │               │               │
        └───────────────┴───────────────┴───────────────┴───────────────┘
                                        │
                 ╔════════════════════════════════════════════╗
                 ║        K-SKILLS & PLUGIN ECOSYSTEM          ║
                 ║  [GitHub] [Figma] [WebSearch] [Zapier] [DB] ║
                 ╚════════════════════════════════════════════╝
```

---

## Current Status

**Phase 0 – Foundation & Specs** → Complete  
**Complete executable project structure** is ready.  
Next: Phase 1 – Core Engine implementation.

---

## Documentation Map

| Document | Purpose |
|----------|---------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Full system design, components, data flow |
| [docs/AGENTS.md](docs/AGENTS.md) | Detailed specs for Core + all 5 specialist agents |
| [docs/WORKFLOWS.md](docs/WORKFLOWS.md) | How tasks are broken down, routed, and executed |
| [docs/SKILLS.md](docs/SKILLS.md) | K-Skills catalog, tools, webhooks mapping |
| [docs/PROMPTS.md](docs/PROMPTS.md) | System prompts for every agent + orchestrator |
| [docs/PHASES.md](docs/PHASES.md) | Complete phased delivery plan (AI vs Human) |
| [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) | **Complete executable project structure** |
| [docs/FILE_STRUCTURE.md](docs/FILE_STRUCTURE.md) | Earlier structure notes |

---

## Project Structure

Full ready-to-build layout is documented here:

**→ [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)**

Already created:
- `backend/` (core, agents, skills, config, utils)
- `docs/` (all specifications)
- `workspace/`, `scripts/`, `tests/`, `docker/`, `frontend/`
- `requirements.txt`, `.env.example`, `.gitignore`

---

## Tech Stack (Target)

| Layer | Technology | Purpose |
|-------|------------|---------|
| Orchestration | CrewAI (primary) / LangGraph (advanced control) | Multi-agent coordination |
| LLMs | Claude 3.5/4 Sonnet + GPT-4o + others | Role-specific model routing |
| Memory | ChromaDB (local) → Pinecone (production) | Long-term project & conversation memory |
| Frontend | Next.js + Tailwind + Vercel AI SDK | Streaming Chat + Workspace |
| Tools / Skills | LangChain Tools + Composio | 150+ app integrations |
| Backend Runtime | Python 3.11+ | Core engine |
| Deployment | Docker + Railway / Render / Vercel | Production hosting |

---

## How to Use This Documentation

1. Start with **ARCHITECTURE.md** and **AGENTS.md** to understand the system.
2. Review **PHASES.md** for the delivery roadmap and what you need to provide.
3. Use **PROMPTS.md** and **SKILLS.md** as the source of truth when we implement.
4. Everything is written to be **build-ready** — these specs will be turned directly into code.

---

## Next Step

Structure and specifications are ready.  
Say **“Start Phase 1”** and I will implement the full Core Engine + agents according to the specs.

---

*Built for production. Designed for premium quality.*
