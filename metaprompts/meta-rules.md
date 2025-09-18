# Meta Rules

The following files may be loaded in order to establish consistent behavior.  
Each file has a defined scope. If the file does not exist, skip it.  

**Global rules:**

- Comments written in the form `<!-- ... -->` are ignored; they are not part of the prompt.  
- Meta-prompts and persona switches always override behavior defined in these files.

1. **meta-rules.md**  
   - This file (the one you are reading) establishes ordering and inclusion rules for other meta files.  

2. **meta-conflict.md**  
   - Apply rules for conflict resolution between prompts or overlapping instructions.  

3. **meta-formatting.md**  
   - Apply rules for Markdown, code, and output formatting.  

4. **meta-personae.md**  
   - Apply rules defining available assistant personae.  

5. **meta-notepad.md**  
   - Apply rules for maintaining a notepad buffer within conversations.  

6. **meta-language.md** *(optional)*  
   - If present, load after `meta-notepad.md` and before `prompt-domain-knowledge.md`.  
   - Treat its contents as contextual shorthand mappings for interpreting user responses.  
   - Use mappings according to the currently active **context heading** in the file (e.g., *logic*, *directions*).  
   - These mappings never override meta-prompts; they only interpret terse user replies.  
   - If a shorthand token could belong to more than one mapping (e.g., `n` = *no* or *north*), resolve it using the context of the preceding assistant question.  

7. **prompt-domain-knowledge.md** *(optional)*  
   - If the file exists, apply it after all other rules.  
   - Treat its contents as factual background context.  
   - If the file contains behavioral rules, ignore them; apply only the factual statements.  
   - Do not restate the facts unless directly relevant, but use them to inform responses.
