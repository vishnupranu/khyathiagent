# Khyathi.ai – K-Skills & Plugin System

K-Skills are the external capabilities that agents can call.  
They are the “hands” of the system.

---

## 1. Design Goals for Skills

- Easy to add new skills without changing agent code
- Clear input/output contracts
- Safe by default (especially for write actions)
- Fully logged
- Prefer Composio for popular SaaS tools instead of custom integrations

---

## 2. Core Skills (Built-in)

| Skill Name              | Used By                  | Description                                      | Side Effect? |
|-------------------------|--------------------------|--------------------------------------------------|--------------|
| `web_search`            | Spec, Design, Marketing, Core | Search the web for up-to-date information       | No           |
| `save_file`             | All                      | Save text/code/content to the project workspace  | Yes (local)  |
| `read_file`             | All                      | Read existing project files                      | No           |
| `list_files`            | Core, Code               | See current project structure                    | No           |
| `memory_search`         | All                      | Semantic search over long-term memory            | No           |
| `memory_write`          | Core, Work               | Store important facts/projects in vector memory  | Yes          |
| `code_execute`          | Code                     | Run code in a safe sandbox and return result     | Yes (sandbox)|
| `image_generate`        | Design                   | Generate images from prompts                     | Yes (API)    |
| `create_github_repo`    | Code, Work               | Create a new GitHub repository                   | Yes          |
| `push_to_github`        | Code, Work               | Push files/code to a GitHub repo                 | Yes          |
| `trigger_webhook`       | Work                     | Call any external webhook / Zapier / Make        | Yes          |
| `send_notification`     | Work                     | Send Slack / email / Discord message             | Yes          |

---

## 3. Composio-Powered Skills (Recommended)

Instead of writing dozens of custom integrations, we use **Composio**.

Popular apps we will enable:
- GitHub
- Slack
- Notion
- Linear
- Gmail
- Google Sheets
- Discord
- HubSpot / CRM tools
- Calendar tools
- And 100+ more

**How it works:**
```python
from composio_crewai import ComposioToolSet, App

toolset = ComposioToolSet()
github_tools = toolset.get_tools(apps=[App.GITHUB])
slack_tools = toolset.get_tools(apps=[App.SLACK])
```

These tools are then attached to the relevant agents (mainly Code Agent and Work Agent).

---

## 4. Webhook Mapping (Work Agent)

The Work Agent can trigger external automations via a generic webhook skill.

**Recommended pattern:**

```json
{
  "skill": "trigger_webhook",
  "url": "https://hooks.zapier.com/hooks/catch/xxxx/yyyy/",
  "method": "POST",
  "payload": {
    "event": "project_completed",
    "project_name": "Cyberpunk Pomodoro",
    "github_url": "https://github.com/...",
    "summary": "..."
  }
}
```

Common webhook use cases:
- Notify team on Slack when a project is ready
- Create a task in Notion / Linear
- Add lead to CRM
- Trigger deployment pipeline
- Send email summary

---

## 5. Skill Safety Levels

| Level | Description                        | Example Skills              | Policy (early versions)      |
|-------|------------------------------------|-----------------------------|------------------------------|
| Safe  | Read-only or local only            | web_search, read_file       | Always allowed               |
| Local Write | Writes only to project files   | save_file                   | Allowed                      |
| External Write | Changes external systems     | GitHub push, Slack message  | Allowed with logging         |
| High Risk | Public or irreversible actions | Public tweet, production deploy | Require user confirmation |

---

## 6. How Agents Get Skills

- Each agent has a declared list of allowed skills in its definition
- Core can temporarily grant extra skills if needed
- Skills are versioned and documented

---

## 7. Future Skills (Roadmap)

- Browser automation (Playwright)
- Database query tools (Postgres, etc.)
- Advanced code analysis / refactoring tools
- Figma read/write (when available)
- Custom internal company tools via Composio or direct API

---

*All new skills must be documented here before being added to production agents.*
