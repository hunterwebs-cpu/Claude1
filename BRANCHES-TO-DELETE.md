# Branches to delete

This branch exists only to list branches that still need to be manually deleted
via the GitHub UI — the agent proxy used in this session blocks `git push --delete`
(HTTP 403), and no GitHub MCP tool exposes ref deletion either, so these could
not be removed programmatically.

## In `hunterwebs-cpu/claude1`

Fully merged into `main` already — zero unique content, safe to delete:

- `claude/surviving-feds-site-5n4cmc`
- `claude/surviving-feds-site-cont-s2nyfw`
- `claude/subagents-launch-9lj81k`
- `claude/skills-inventory-95axy7`
- `claude/surviving-feds-redesign-discovery-42fbdg`

Superseded — their unique content was extracted and now lives in clean,
dedicated branches (`content/substack` here, and `legal/austin-appeal-25-1093`
/ `legal/in-re-mell` in `hunterwebs-cpu/legal-case-files`):

- `claude/austin-appeal-research-plan-0iw0eh`
- `claude/legal-citation-verification-m7ows0`
- `claude/subagents-research-task-3wbi8w`
- `claude/substack-prison-infrastructure-8zsync`

Once the branches above are deleted, this `delete` branch can be deleted too.

## In `hunterwebs-cpu/legal-case-files`

- `legal-citation-verification` — created by mistake during the split (wrong
  content, wrong repo). The correct content lives in `claude1`'s
  `content/substack` branch.
