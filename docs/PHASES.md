# Khyathi.ai – Complete Phased Delivery Plan

This is the master delivery plan. Every phase has clear ownership.

**Legend**  
- **AI Side**: What I will design, code, and deliver  
- **Human Side**: What you need to provide, decide, or approve  
- **Where to get it**: Exact places to create accounts / get keys

---

## Phase 0 – Foundation & Specifications (Current)
**Status:** Complete

**AI Side:**
- Create full documentation set (Architecture, Agents, Workflows, Skills, Prompts, File Structure)
- Organize all system roles and build-ready specs

**Human Side:**
- Review and approve the specifications
- Confirm any changes to roles, priorities, or constraints

**Exit Criteria:** You approve the specs and say “Start Phase 1”.

---

## Phase 1 – Core Engine (Backend Brain)

**Goal:** A working multi-agent system that can take a request and produce real Spec + Design + Code + Marketing + Work outputs.

**AI Side:**
- Project structure
- Clean `khyathi_core.py` with proper environment handling
- All 5 agents + Core defined according to specs
- Basic K-Skills (file, search, memory foundation)
- Hierarchical orchestration
- Logging and basic error handling
- Sample end-to-end test run
- Clear instructions how to run

**Human Side:**
| Item | Purpose | Where to get it | Notes |
|------|---------|-----------------|-------|
| OpenAI API Key | Main LLM | https://platform.openai.com/api-keys | Required |
| Serper API Key | Web search | https://serper.dev | Free tier available |
| Anthropic API Key (recommended) | Better code & specs | https://console.anthropic.com | Strongly recommended |
| Decision: Real keys or mock mode first | — | Tell me | Prefer real keys |

**Exit Criteria:** Successful full multi-agent run that generates usable files.

---

## Phase 2 – K-Skills & Real Capabilities

**Goal:** Agents gain real power (GitHub, images, memory, external actions).

**AI Side:**
- Composio integration
- Image generation skill
- Vector memory (ChromaDB first)
- Improved Code Agent (multi-file quality)
- GitHub create + push skills
- Webhook skill
- Better tool error handling

**Human Side:**
| Item | Purpose | Where to get it | Notes |
|------|---------|-----------------|-------|
| Composio account | 150+ app integrations | https://composio.dev | Free tier + paid |
| GitHub Personal Access Token | Code Agent can push repos | GitHub → Settings → Developer settings → Tokens | Free |
| Optional: Pinecone | Cloud vector DB | https://www.pinecone.io | Free tier available |
| OpenAI / Replicate for images | Design Agent | Already covered by OpenAI key | — |

**Exit Criteria:** System can create a real GitHub repo and use external tools successfully.

---

## Phase 3 – Frontend (Chat + Workspace)

**Goal:** Beautiful, usable product interface.

**AI Side:**
- Next.js + Tailwind application
- Streaming chat with Khyathi Core
- Live agent progress visualization
- Project / Workspace view
- Connection to backend
- Premium dark UI

**Human Side:**
| Item | Purpose | Where to get it | Notes |
|------|---------|-----------------|-------|
| Vercel account | Deploy frontend | https://vercel.com | Excellent free tier |
| Design preference | Visual direction | Tell me (cyberpunk / clean premium / other) | I will implement |
| Optional domain | Professional URL | Namecheap, Cloudflare, etc. | Later |

**Exit Criteria:** You can chat with Khyathi in the browser and watch agents work.

---

## Phase 4 – Production Hardening

**Goal:** Stable, secure, deployable, observable system.

**AI Side:**
- Docker + docker-compose
- Proper configuration management
- Logging, retries, cost tracking
- Basic security & rate limiting
- Observability foundations
- Multi-user readiness (structure)
- Elite Mode features
- Simple CI

**Human Side:**
| Item | Purpose | Where to get it | Notes |
|------|---------|-----------------|-------|
| Hosting choice | Where backend runs | Railway.app / Render.com / Fly.io | Free tiers + cheap paid |
| Optional monitoring | Error tracking | Sentry.io etc. | Free tiers exist |
| Decision on multi-user priority | Affects scope | Tell me | Recommended later |

**Exit Criteria:** System can be deployed with Docker and runs reliably.

---

## Phase 5 – Polish & Launch Ready

**Goal:** High-quality, documented, shippable product.

**AI Side:**
- End-to-end testing of major flows
- Full documentation
- Example projects / templates
- Final UI polish
- Performance & cost optimization
- Deployment guide

**Human Side:**
- Thorough testing and feedback
- Final branding decisions (logo, name, colors)
- Decision: private tool first or public launch

**Exit Criteria:** Ready for real daily use or soft launch.

---

## Recommended Starting Order of Keys

1. OpenAI API key  
2. Serper API key  
3. Anthropic API key (highly recommended)  
4. Composio account  
5. GitHub token  

You can begin Phase 1 with only OpenAI + Serper. We will add the rest as we go.

---

*This document is the single source of truth for delivery ownership and sequence.*
