# Prompt Domain Knowledge

> NOTE: This file contains factual context about the user’s development environment and preferences.  
> Apply only if this file exists, and only after all other meta-prompt files.

## Environment Facts

- Local development is done on a laptop with **32 GB RAM** and a single **RTX 3070 GPU** with **8 GB VRAM**.
- Primary programming language is **Python**.
- Assume all Python development is being done in a **venv**.
- Tools requiring **Node.js** are acceptable; provide installation instructions when needed.
- When using Node.js, the package manager is **npm**.
- Primary editor is **Visual Studio Code (VSC)**.
- Preferred CLI editor is **vi/vim**, not nano.
- Default deployment platform is **Ubuntu 24.04 LTS**, for simple, bare-metal use.
- For robust production deployment, prefer **Docker** with `docker run`.  
  Use `docker compose` only if a multi-container workflow explicitly requires it.
