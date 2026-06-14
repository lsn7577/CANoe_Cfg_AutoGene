# Agent KB Rules

This document is the agent-facing retrieval protocol for this knowledge base.
It defines how an agent must look up CANoe, CAPL, Panel, DBC, XCP,
diagnostics, and project-convention facts before answering or generating code.

The default mode is model-free and agent-first. The knowledge base supplies
deterministic lookup, BM25 candidate recall, and grounded structured facts.
The calling agent is responsible for semantic interpretation and synthesis.

## Required Retrieval Order

Agents must use this order unless a narrower step already proves the answer.

1. Read the capability surface.
   Use `agent_kb/capability_manifest.md` and `agent_kb/query_routing.md` to
   confirm the topic, version, and candidate collection.

2. Build a query plan.
   Convert the user request into a small structured plan:
   `intent`, `version`, `topic`, `page_type`, `known_symbols`,
   `scenario_candidates`, and `team_override_required`.

3. Resolve exact symbols first.
   If the request contains a named API, symbol, event, selector, control, or
   project helper, call `agent_kb.kb_lookup.resolve_symbol()` and
   `agent_kb.kb_lookup.load_page()` before free-form search.

4. Match common scenarios.
   For test-generation intents, call `match_scenario()` and load every primary
   page with `load_scenario_pages()`. Related pages are required when they
   affect code generation, validation, version behavior, or project style.

5. Use constrained candidate search.
   For free-form or mixed-language questions, call `search(query, version,
   topic, page_type, top_n)` with the narrowest safe filters. The search result
   is only a candidate. Any fact used in a final answer must come from
   `grounded_facts` or a loaded source page.

6. Check team overrides.
   Before generating code, tests, CI configuration, or panel bindings, load the
   relevant `extras/team/*.json` pages. These project conventions override
   generic Vector examples.

7. Grounded synthesis.
   Compose the answer only from loaded pages, scenario context, grounded search
   facts, and explicitly marked assumptions. If a required symbol or parameter
   cannot be resolved, say it is unknown instead of inventing syntax.

## Answer Gate

Before answering, especially before generating CAPL or configuration artifacts,
the agent must pass these checks:

- Every generated API call has a loaded page or is explicitly marked unknown.
- Syntax comes from `syntax[]` or `grounded_facts.syntax`.
- Parameters come from `parameters`, `sections`, `tables`, or grounded facts.
- Version-specific claims name the version used for retrieval.
- Team overrides have been checked for generated code and CI/panel guidance.
- Search hits are treated as candidates until their pages are loaded or their
  grounded facts are directly used.
- Conflicting pages are resolved by exact symbol lookup, scenario primary pages,
  then narrower version/topic filters.
- Missing evidence blocks confident code generation.

## Combined Retrieval Protocol

Some requests require more than one retrieval lane. For example, "create a
CAPL test that sets a signal, waits for a value, and follows our team style"
requires:

1. Scenario matching for `set_signal_value` and
   `wait_for_signal_condition`.
2. Exact page loading for `setSignal`, `TestWaitForSignalMatch`, and any
   additional helper used by the generated code.
3. Team override loading for `CAPL_Internal_Coding_Standards`,
   `Common_Gotchas`, or `canSetSignalDword` when applicable.
4. Optional constrained search if the scenario pages do not answer a detail.
5. Grounded synthesis using only the collected facts.

Combined retrieval must preserve source boundaries. Do not merge generic Vector
syntax with project-specific wrappers unless both pages were loaded and the
relationship is stated.

## Grounded Fact Rules

`search()` returns `grounded_facts` for each hit. These fields are safe to use:

- `name`
- `page_type`
- `syntax`
- `parameters`
- `return`
- `description`
- `sections`
- `selectors`
- `property_references`
- `example_code`
- `availability`
- `source`

If a final answer depends on a field that is not present in grounded facts,
load the page directly with `load_page()` or `_load_page_by_id()`.

## Failure Handling

If lookup fails:

1. Retry with normalized symbol spelling and the requested version.
2. Retry with a narrower topic or page type.
3. Use scenario pages when the natural-language intent is known.
4. Use search as a fallback candidate source.
5. If still unresolved, mark the fact unknown and do not generate syntax for it.

No agent may fabricate CAPL calls, selector names, Panel properties, DBC
keywords, or diagnostics service details from memory when this knowledge base is
being used as the source of truth.
