# Khyathi.ai Scripts

## Main Setup Script

**`setup_khyathi.sh`** – Production-grade setup & phase runner.

### Usage

```bash
# Make executable (first time)
chmod +x scripts/setup_khyathi.sh

# Full setup (recommended first run)
./scripts/setup_khyathi.sh

# Only check current state
./scripts/setup_khyathi.sh --check

# Only install Python dependencies
./scripts/setup_khyathi.sh --install

# Prepare a specific phase
./scripts/setup_khyathi.sh --phase 0
./scripts/setup_khyathi.sh --phase 1
./scripts/setup_khyathi.sh --phase 2
# ... up to phase 5
```

### What the full run does

1. Verifies / creates the complete project structure (Phase 0)
2. Creates `.env` from `.env.example` if missing
3. Creates Python virtual environment (`.venv`)
4. Installs all dependencies from `requirements.txt`
5. Prepares backend package structure for Phase 1
6. Runs a health check and tells you the next steps

### Important

After the first run you **must** edit `.env` and add your real API keys before the agents can call LLMs.
