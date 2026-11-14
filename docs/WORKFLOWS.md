# Khyathi.ai – Workflows & Task Orchestration

This document defines how requests move through the system, how tasks are created, dependencies are handled, and results are synthesized.

---

## 1. High-Level Request Lifecycle

1. **User sends message** → Frontend streams it to Backend
2. **Khyathi Core receives** the message + conversation history + relevant project memory
3. **Intent Analysis**  
   - Is this a simple chat / question? → Answer directly  
   - Is this a new project / complex build request? → Full multi-agent workflow  
   - Is this a follow-up on an existing project? → Load project memory and continue
4. **Task Decomposition**  
   Core creates a Task Graph with clear dependencies
5. **Agent Execution**  
   Agents run (sequential where needed, parallel where possible)
6. **Result Collection & Synthesis**  
   Core gathers all outputs, resolves conflicts, creates final coherent response
7. **Persistence**  
   Everything important is saved to Project Memory + Workspace files
8. **Response to User**  
   Streaming final answer + links to generated artifacts

---

## 2. Standard Full Project Workflow

This is the default path for requests like:  
“Build a SaaS Pomodoro Timer with cyberpunk theme and prepare its launch.”

```
[Core] Analyze request
        ↓
[Spec Agent]     →  PRD + Architecture + User Stories
        ↓
[Design Agent]   →  Design System + Flows + Image Prompts     (can start once Spec is partially ready)
        ↓
[Code Agent]     →  Working code + project structure          (depends on Spec + Design)
        ↓
[Marketing Agent]→  Landing copy + Launch plan + Social      (can run in parallel with Code)
        ↓
[Work Agent]     →  Create GitHub repo, push code, notify, trigger any automations
        ↓
[Core] Synthesize everything into final package for user
```

---

## 3. Task Dependency Rules

| Task                        | Depends On              | Can Run In Parallel With |
|----------------------------|-------------------------|--------------------------|
| Spec                       | Nothing                 | —                        |
| Design                     | Spec (at least partial) | Marketing (sometimes)    |
| Code                       | Spec + Design           | Marketing                |
| Marketing                  | Spec                    | Code, Design             |
| Work (side-effect actions) | Usually Code + others   | — (runs late)            |

Core is responsible for enforcing these dependencies.

---

## 4. Parallelism Strategy

- **Early phases**: Spec runs alone.
- **Middle phases**: Design + Marketing can often run together once Spec is done.
- **Late phases**: Code runs, then Work.
- Core may decide to run multiple instances of the same agent type in the future.

---

## 5. Error & Recovery Workflow

1. Agent fails or times out
2. Core receives error + partial output
3. Core decides:
   - Retry the same agent (with more context)
   - Re-assign to a different agent
   - Ask user for clarification
   - Degrade gracefully (deliver what is available)
4. All failures are logged with full context for debugging

---

## 6. Simple Chat / Non-Project Workflow

Not every message needs the full 5-agent pipeline.

Examples of direct Core handling:
- “What is the status of my last project?”
- “Explain this code to me”
- “Change the color palette of the previous design”
- General knowledge questions

Core should be smart enough to route simple requests itself.

---

## 7. Webhook & External Trigger Workflow (Work Agent)

When Work Agent needs to perform side effects:

1. Core or Work Agent prepares payload
2. Work Agent calls the appropriate K-Skill (Composio or custom webhook)
3. Result (success / failure / response data) is returned
4. Core records the action in Project Memory
5. User is informed of what was executed

Safety rule (early versions):  
Destructive or public actions should require explicit user confirmation.

---

## 8. Memory Write Points

Important moments when memory is updated:
- After Spec is completed
- After Design is completed
- After Code is generated
- After any Work Agent side-effect
- At the end of a full workflow (final synthesis)

---

*This workflow document is the operational playbook for the Orchestrator.*
