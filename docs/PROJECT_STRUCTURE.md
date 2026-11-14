# Khyathi.ai – Complete Executable Project Structure

This is the **full production-oriented project layout**.  
All folders and key files listed below are now created (or will be filled in Phase 1).

```
khyathiagent/
│
├── README.md                          # Project overview & quick start
├── requirements.txt                   # Python dependencies
├── .env.example                       # Template for secrets (copy to .env)
├── .gitignore
│
├── docs/                              # SOURCE OF TRUTH – Specifications
│   ├── ARCHITECTURE.md
│   ├── AGENTS.md
│   ├── WORKFLOWS.md
│   ├── SKILLS.md
│   ├── PROMPTS.md
│   ├── PHASES.md
│   ├── FILE_STRUCTURE.md
│   └── PROJECT_STRUCTURE.md           # ← This file
│
├── backend/                           # Core Python engine
│   ├── __init__.py
│   ├── main.py                        # Entry point (CLI / API later)
│   │
│   ├── core/                          # Khyathi Core (Orchestrator)
│   │   ├── __init__.py
│   │   ├── config.py                  # Settings & environment loading
│   │   ├── orchestrator.py            # Main orchestration logic
│   │   ├── memory.py                  # Short + long-term memory
│   │   └── task_graph.py              # Task decomposition helpers
│   │
│   ├── agents/                        # Specialist Agents
│   │   ├── __init__.py
│   │   ├── base.py                    # Shared agent utilities
│   │   ├── spec_agent.py
│   │   ├── design_agent.py
│   │   ├── code_agent.py
│   │   ├── marketing_agent.py
│   │   └── work_agent.py
│   │
│   ├── skills/                        # K-Skills (Tools)
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── file_skills.py
│   │   ├── search_skills.py
│   │   ├── memory_skills.py
│   │   ├── github_skills.py           # Phase 2
│   │   ├── image_skills.py            # Phase 2
│   │   ├── webhook_skills.py          # Phase 2
│   │   └── composio_skills.py         # Phase 2
│   │
│   ├── prompts/                       # Loaded system prompts
│   │   └── (can load from docs/PROMPTS.md or individual .txt/.md)
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logging.py
│       └── helpers.py
│
├── workspace/                         # Runtime generated projects & artifacts
│   └── .gitkeep
│
├── scripts/
│   ├── run_khyathi.py                 # Simple CLI runner
│   └── sample_requests.py             # Test prompts
│
├── tests/
│   └── (unit + integration tests – Phase 4/5)
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml             # Phase 4
│
└── frontend/                          # Next.js Chat + Workspace (Phase 3)
    └── (created in Phase 3)
```

---

## How the Structure Maps to the System

| Folder / File              | Corresponds To                  | Phase |
|---------------------------|----------------------------------|-------|
| `backend/core/orchestrator.py` | Khyathi Core                    | 1     |
| `backend/agents/*.py`     | The 5 Specialist Agents          | 1     |
| `backend/skills/`         | K-Skills & Plugin system         | 1–2   |
| `docs/PROMPTS.md`         | All system prompts               | 0     |
| `docs/AGENTS.md`          | Role definitions                 | 0     |
| `workspace/`              | Generated code, specs, designs   | 1+    |
| `frontend/`               | Chat + Workspace UI              | 3     |
| `docker/`                 | Production packaging             | 4     |

---

## Execution Flow (How it runs)

1. User (or script) calls `scripts/run_khyathi.py "Build a cyberpunk Pomodoro app..."`
2. `backend/core/orchestrator.py` loads config + memory
3. Core analyzes request and creates tasks
4. Tasks are assigned to agents in `backend/agents/`
5. Agents use skills from `backend/skills/`
6. Outputs are saved into `workspace/<project_name>/`
7. Core synthesizes final response

---

## Current Status of Structure

- Directory tree: **Created**
- Documentation (docs/): **Complete**
- `requirements.txt` + `.env.example` + `.gitignore`: **Created**
- Actual Python implementation files: **Next (Phase 1)**

---

## Next Action

Once you confirm, I will fill the `backend/` folder with production-ready code according to the specs in `docs/`.

This structure is designed so that:
- Specs stay clean in `/docs`
- Code stays clean in `/backend`
- Generated user projects stay isolated in `/workspace`
- Frontend can grow independently

**This is the complete executable project structure.**
