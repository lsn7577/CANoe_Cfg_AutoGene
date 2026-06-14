{
  "metadata": {
    "title": "Agent KB Rules",
    "schema_version": "1.0",
    "default_mode": "agent_first_bm25_grounded",
    "model_dependency": "none",
    "default_version": "v15",
    "description": "Machine-readable retrieval rules and answer gate for deterministic lookup, constrained candidate search, and grounded synthesis."
  },
  "tool_order": [
    {
      "name": "capability_manifest",
      "surface": "agent_kb/capability_manifest.md",
      "required_when": "starting a new domain or capability question"
    },
    {
      "name": "query_routing",
      "surface": "agent_kb/query_routing.md",
      "required_when": "choosing topic, version, or collection"
    },
    {
      "name": "resolve_symbol",
      "surface": "agent_kb/kb_lookup.py:resolve_symbol",
      "required_when": "a named symbol, API, event, selector, control, or project helper is present"
    },
    {
      "name": "load_page",
      "surface": "agent_kb/kb_lookup.py:load_page",
      "required_when": "a symbol was resolved or a generated API call is planned"
    },
    {
      "name": "match_scenario",
      "surface": "agent_kb/kb_lookup.py:match_scenario",
      "required_when": "the request is a common test-generation or workflow intent"
    },
    {
      "name": "load_scenario_pages",
      "surface": "agent_kb/kb_lookup.py:load_scenario_pages",
      "required_when": "a scenario matched"
    },
    {
      "name": "search",
      "surface": "agent_kb/kb_lookup.py:search",
      "required_when": "exact lookup and scenario lookup are insufficient"
    },
    {
      "name": "team_overrides",
      "surface": "extras/team/*.json",
      "required_when": "generating code, tests, panel bindings, CI configuration, or project-specific guidance"
    }
  ],
  "query_plan_schema": {
    "type": "object",
    "required": ["intent", "version", "topic"],
    "properties": {
      "intent": {
        "type": "string",
        "examples": [
          "generate_capl_test",
          "explain_api",
          "debug_code",
          "compare_versions",
          "panel_binding",
          "dbc_authoring",
          "diagnostics"
        ]
      },
      "version": {
        "type": "string",
        "default": "v15",
        "enum": ["v12", "v15", "v17", "v18", "extras"]
      },
      "topic": {
        "type": "string",
        "enum": ["capl", "panel", "dbc", "xcp", "diagnostics", "extras"]
      },
      "page_type": {
        "type": ["string", "null"],
        "enum": ["function", "method", "event", "selector", "concept", "notes", null]
      },
      "known_symbols": {
        "type": "array",
        "items": {"type": "string"}
      },
      "scenario_candidates": {
        "type": "array",
        "items": {"type": "string"}
      },
      "team_override_required": {
        "type": "boolean",
        "default": false
      },
      "fallback_searches": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["query"],
          "properties": {
            "query": {"type": "string"},
            "version": {"type": "string"},
            "topic": {"type": "string"},
            "page_type": {"type": ["string", "null"]},
            "top_n": {"type": "integer", "minimum": 1, "maximum": 20}
          }
        }
      }
    }
  },
  "search_constraints": {
    "default_top_n": 5,
    "max_top_n": 20,
    "require_version_filter_by_default": true,
    "default_version": "v15",
    "prefer_topic_filter": true,
    "search_hit_status": "candidate_until_grounded",
    "allowed_topics": ["capl", "panel", "dbc", "xcp", "diagnostics", "extras"],
    "allowed_page_types": ["function", "method", "event", "selector", "concept", "notes"],
    "default_vector_backend": "disabled",
    "semantic_understanding_owner": "calling_agent"
  },
  "combined_retrieval": {
    "required_for": [
      "generated_capl_tests",
      "panel_binding_generation",
      "diagnostics_workflows",
      "project_specific_code",
      "multi_step_debugging"
    ],
    "lanes": [
      "scenario_pages",
      "exact_symbol_pages",
      "constrained_search_candidates",
      "team_override_pages"
    ],
    "source_boundary_rule": "Keep generic Vector facts and project override facts separately attributable until synthesis."
  },
  "answer_gate": {
    "all_symbols_must_be_resolved_or_marked_unknown": true,
    "generated_api_calls_require_loaded_page": true,
    "syntax_must_come_from_grounded_facts": true,
    "parameters_must_come_from_grounded_facts": true,
    "team_overrides_checked_for_code_generation": true,
    "search_hits_require_page_loading_before_fact_use": true,
    "version_claims_require_version_filter": true,
    "missing_evidence_blocks_confident_code_generation": true,
    "allow_explicit_assumptions": true
  },
  "failure_policy": {
    "retry_normalized_symbol": true,
    "retry_narrower_topic": true,
    "retry_narrower_page_type": true,
    "fallback_to_scenario": true,
    "fallback_to_search": true,
    "fabricate_unresolved_syntax": false
  }
}
