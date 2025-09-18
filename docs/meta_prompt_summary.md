# Meta-Prompt Kit: Summary

This document outlines the design of a reusable meta-prompt system for ChatGPT projects, with layered rules and conflict resolution.

## Core Concepts

- **Meta-Prompt Files**: Prompts stored as separate files that can be uploaded per project and used to define assistant style, tone, or rules.  
- **Conflict Resolution File (`meta-rules.md`)**: A central file that establishes consistent rules for handling conflicts between other meta-prompts.  
- **Process Once Guard**: Ensures `meta-rules.md` is only processed the first time it is called in a conversation. If other files reference it again, it is ignored on subsequent calls.  

## Rules in `meta-rules.md`

1. Specific instructions override general ones.  
2. When two rules directly conflict, the file named later in the user’s request takes priority.  
3. If conflicts remain unclear, the assistant pauses and asks the user to clarify instead of guessing.  

## Example Structure

### `meta-rules.md`
```markdown
# Meta-Prompt Conflict Resolution Rules

NOTE: Process this file only once per conversation. 
If already processed, return without action.

1. Specific instructions override general ones.
2. When two rules directly conflict, the file named later in the user’s request takes priority.
3. If conflicts remain unclear, pause and ask the user to clarify instead of guessing.
```

### `meta-prompt.md`
```markdown
Before applying these instructions, load and apply meta-rules.md.

# Meta-Prompt (Skeleton)

- Define assistant style, tone, or persona here.
- Add any formatting or output rules here.
- You can layer more rules by adding additional meta files.
```

### Example Additional Files

**file1.md**
```markdown
Before applying these instructions, load and apply meta-rules.md.

# File1 Rules

- All responses must be concise bullet points.
- Avoid long paragraphs unless explicitly requested.
- Keep tone neutral and professional.
```

**file2.md**
```markdown
Before applying these instructions, load and apply meta-rules.md.

# File2 Rules

- Every response must include at least one concrete example.
- Use plain English, avoid technical jargon unless asked for detail.
- If listing items, use numbered lists by default.
```

## Workflow

1. Upload the meta-prompt kit files into your project.  
2. Start a chat by instructing:  
   - “Use meta-prompt.md as the meta-prompt for this conversation.”  
   - Or: “Use meta-prompt.md and file2.md as the meta-prompt for this conversation.”  
3. The assistant will apply `meta-rules.md` only once, even if referenced by multiple files.  
4. Conflict resolution will follow the rules in `meta-rules.md`.  

## Index of Files

- **meta-rules.md** → Conflict resolution and one-time processing rules.  
- **meta-prompt.md** → Skeleton meta-prompt to customize.  
- **file1.md** → Example: concise bullet-point style.  
- **file2.md** → Example: examples + plain English.  
- **README.md** → Usage instructions.  
- **index.md** → File overview.  


---

# Appendix: Software Design Pattern Mapping

This appendix maps the meta-prompt kit to familiar software design patterns, so developers can relate prompt engineering to standard practices.

## `meta-rules.md` → Policy Engine / Config Precedence
- Acts like a rules engine or precedence framework.  
- Defines what happens when instructions conflict (specific > general, later > earlier, ask if unclear).  
- **Analogy**: CSS specificity, YAML config overrides.

## `meta-prompt.md` → Base Configuration / Skeleton Class
- Provides the default style, tone, and structure.  
- Serves as a base configuration extended by other files.  
- **Analogy**: Base Dockerfile, default app config, abstract class.

## `file1.md`, `file2.md`, etc. → Modules / Plug-ins
- Each file is a plug-in that modifies or extends behavior.  
- Files are composable and can be loaded in combination.  
- **Analogy**: Middleware in Express/Django, VS Code plug-ins.

## Process Once Guard → Idempotence
- Ensures `meta-rules.md` is applied only once per conversation.  
- Prevents duplication and redundant effects.  
- **Analogy**: `if not already_loaded: load_config()`.

## Whole Kit → Configuration Layering
- The system works like layered configs in many frameworks.  
- Defaults → Overrides → Conflict resolution → Final applied rules.  
- **Analogy**: Linux config cascades, Terraform modules, Ansible layered configs.

---

## Developer-Friendly Summary
The meta-prompt kit functions like a layered configuration system.  
- `meta-rules.md` is the policy engine.  
- `meta-prompt.md` is the base config.  
- Additional files are modules.  
- The process-once guard enforces idempotence.  

In effect, this treats **prompt engineering as heuristic programming in natural language**, with design principles drawn from established software configuration and policy systems.
