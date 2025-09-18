# Meta-Prompt Formatting Rules

NOTE: Process this file only once per conversation.
If already processed, return without action.

## Chat Rules

When rendering example markdown in chats, always ensure that they are in fenced code blocks, with the markdown language tag, to avoid code getting split on formatting.

## Markdown Formatting Rules

These rules should be applied to all markdown presented as a markdown example, and when writing markdown files. It is not necessary to use these rules for general responses, which are only being passed for HTML formatting.

**Note:** These rules are derived from [markdownlint rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md).

1. **Headings**
   - Use `#` for top-level title, then `##`, then `###` for sub-sections.
   - Do not skip heading levels.

2. **Lists**
   - Use `-` for unordered lists.
   - Use `1.`, `2.`, etc. for ordered lists.
   - Nested lists must be indented with 2 spaces.

3. **Code Blocks**
   - Always use fenced code blocks with language tags:
     - Example: "```python" or "```markdown"
   - Do not use inline backticks for multi-line code.

4. **Links**
   - Always format links as `[text](url)`.
   - Do not output bare URLs.

5. **Text Emphasis**
   - Use `**bold**` for strong emphasis.
   - Use `*italics*` for mild emphasis.
   - Do not use underscores for emphasis.

6. **Tables**
   - Use standard Markdown pipe `|` syntax.
   - Always include header separators (`---`).

7. **General Rules**
   - Do not insert HTML tags unless explicitly requested.
   - Keep line width reasonable (≤ 80–100 characters).
   - Avoid trailing spaces at line ends.
   - Always close fenced code blocks properly.
