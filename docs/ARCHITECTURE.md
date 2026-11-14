# Khyathi.ai – System Architecture

## 1. Core Design Principles

1. **Orchestrator-Centric**  
   Khyathi Core is the single entry point and decision maker. All specialist agents report to it.

2. **Specialist Agents**  
   Each agent has a narrow, deep responsibility. They do not talk to each other directly — only through the Core (or shared memory).

3. **Shared Memory Hub**  
   All agents read/write to a common memory layer so context is never lost.

4. **Skill / Plugin Layer**  
   Capabilities (tools) are externalized into K-Skills so new powers can be added without rewriting agents.

5. **Production First**  
   Every component is designed with logging, error recovery, observability, and cost control from day one.

---

## 2. Component Overview

### 2.1 User Interface Layer
- **Chat Interface** – Streaming conversation with Khyathi Core
- **Workspace** – Project files, agent outputs, history, status of running tasks
- **Live Agent View** – Visual progress of Spec → Design → Code → Marketing → Work

Technology: Next.js + Tailwind CSS + Vercel AI SDK

### 2.2 Khyathi Core (Orchestrator)
Responsibilities:
- Receive user request
- Analyze intent and complexity
- Break request into ordered / parallel sub-tasks
- Assign tasks to the correct specialist agents
- Manage shared context and memory
- Collect results and synthesize final response
- Decide when to stop, retry, or ask clarifying questions
- Route to different LLMs based on task type (model routing)

### 2.3 Specialist Agents

| Agent | Primary Responsibility | Typical Outputs |
|-------|------------------------|-----------------|
| **Spec Agent** | Product thinking & technical planning | PRD, Architecture, User Stories, Tech Stack decisions, Data models |
| **Design Agent** | UI/UX & visual identity | Wireframes descriptions, Design system, Color palette, Typography, Image generation prompts |
| **Code Agent** | Implementation | Production-ready code, multi-file projects, basic tests, deployment configs |
| **Marketing Agent** | Growth & communication | Landing page copy, SEO plan, social posts, launch strategy, ad concepts |
| **Work Agent** | Real-world execution | Trigger webhooks, schedule tasks, push to GitHub, send notifications, data entry, external API calls |

### 2.4 K-Skills & Plugin Ecosystem
A unified tool layer that any agent can call.  
Examples:
- Web Search
- File System (read/write/version)
- GitHub (create repo, push code, issues)
- Image Generation
- Composio-powered apps (Slack, Notion, Linear, Gmail, etc.)
- Deployment (Vercel, Docker hooks)
- Database connectors
- Custom webhooks

### 2.5 Memory System
- **Short-term**: Current conversation + active project context
- **Long-term**: Vector store of past projects, decisions, and learnings
- **Project Memory**: Structured storage of specs, designs, code versions per project

---

## 3. Data & Control Flow (Simplified)

```
User Message
    ↓
Khyathi Core (Intent Analysis + Task Decomposition)
    ↓
Create Task Graph (with dependencies)
    ↓
┌─────────────────────────────────────────────┐
│  Parallel / Sequential Agent Execution      │
│  Spec ──→ Design ──→ Code                   │
│       ↘         ↘                           │
│         Marketing   Work (can run later)    │
└─────────────────────────────────────────────┘
    ↓
Results collected by Core
    ↓
Synthesis + Final Response to User
    ↓
All artifacts saved to Project Memory + Workspace
```

---

## 4. Model Routing Strategy (Premium)

| Task Type              | Preferred Model          | Reason                     |
|------------------------|--------------------------|----------------------------|
| Orchestration / Chat   | GPT-4o                   | Fast, good reasoning       |
| Specs & Architecture   | Claude 3.5/4 Sonnet      | Superior structured thinking |
| Code Generation        | Claude 3.5/4 Sonnet      | Best code quality          |
| Design & Creative      | GPT-4o + Image models    | Strong creative output     |
| Marketing Copy         | GPT-4o                   | Excellent writing          |
| Work / Tool Use        | GPT-4o or Claude         | Reliable tool calling      |

---

## 5. Error Handling & Reliability Principles

- Every agent task has timeout + retry policy
- Core can re-plan if an agent fails
- All tool calls are logged
- Cost is tracked per agent and per project
- Sensitive actions (deploy, external write) require confirmation in early versions

---

## 6. Security Boundaries

- API keys never hard-coded
- Tool execution runs in controlled environment (sandbox for code)
- User data isolation (especially when multi-user is added)
- Rate limiting on expensive tools

---

*This architecture is the source of truth for all implementation decisions.*
