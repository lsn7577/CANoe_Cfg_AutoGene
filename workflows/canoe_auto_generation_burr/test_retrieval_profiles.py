import unittest

from workflows.canoe_auto_generation_burr.canoe_workflow import _coverage_report_from_state
from workflows.canoe_auto_generation_burr.canoe_workflow import _workflow_retrieval_profile


class RetrievalProfileTest(unittest.TestCase):
    def test_canoe_config_and_capl_profiles_are_scoped_apart(self) -> None:
        canoe_config = _workflow_retrieval_profile("canoe_config")
        capl = _workflow_retrieval_profile("capl_authoring")

        self.assertIn("canoe_config", canoe_config["topic_filters"])
        self.assertIn("com_automation", canoe_config["topic_filters"])
        self.assertIn("capl", canoe_config["blocked_topic_filters"])

        self.assertIn("capl", capl["topic_filters"])
        self.assertIn("canoe_config", capl["blocked_topic_filters"])
        self.assertIn("com_automation", capl["blocked_topic_filters"])

    def test_coverage_report_is_kb_profile_scoped(self) -> None:
        profile = _workflow_retrieval_profile("capl_authoring")
        structured = {
            "cases": [
                {
                    "case_id": "TC_001",
                    "requirement_ids": ["REQ_001", "REQ_002"],
                    "feature": "diagnostics",
                    "required_sources": ["cdd"],
                    "steps": [
                        {
                            "operation": {"type": "诊断服务请求"},
                            "condition": {"type": "诊断服务响应"},
                            "expected_result": {"type": "观测量变化"},
                        }
                    ],
                }
            ]
        }
        source_models = {"cdd": {"status": "parsed"}, "a2l": {"status": "parsed"}}
        evidence_bundle = {
            "required_symbols_by_case": {"TC_001": ["diagSendRequest", "TestWaitForSignalMatch"]},
            "pages": [{"symbol": "diagSendRequest"}],
            "gaps": [{"symbol": "TestWaitForSignalMatch", "reason": "not_found"}],
        }

        report = _coverage_report_from_state(structured, source_models, evidence_bundle, profile)

        self.assertEqual(report["retrieval_profile"], "capl_authoring")
        self.assertEqual(report["requirement_coverage"]["covered_requirement_count"], 2)
        self.assertEqual(report["domain_coverage"]["step_count_by_domain"]["diagnostics"], 1)
        self.assertEqual(report["capl_evidence_coverage"]["gap_count"], 1)
        self.assertEqual(report["status"], "warn")


if __name__ == "__main__":
    unittest.main()
