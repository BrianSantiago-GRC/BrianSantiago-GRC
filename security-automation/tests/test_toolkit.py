import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path


TOOLKIT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLKIT_DIR))

import access_review_audit as access
import compliance_checker as compliance
import evidence_collector as evidence
import risk_scorer as risk


class RiskScorerTests(unittest.TestCase):
    def test_risk_boundaries(self):
        self.assertEqual(risk.classify_risk(4), "Low")
        self.assertEqual(risk.classify_risk(9), "Medium")
        self.assertEqual(risk.classify_risk(16), "High")
        self.assertEqual(risk.classify_risk(25), "Critical")

    def test_control_reduction(self):
        self.assertEqual(risk.calculate_residual_score(20, "High"), 12)
        self.assertEqual(risk.calculate_residual_score(3, "None"), 3)

    def test_sample_register_loads(self):
        risks = risk.load_risks(TOOLKIT_DIR / "sample_risk_register.csv")
        self.assertEqual(len(risks), 14)
        self.assertEqual(risks[0]["inherent_score"], 20)


class AccessReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.users = access.load_users(TOOLKIT_DIR / "sample_users.csv")
        cls.as_of = datetime(2026, 4, 1)

    def test_orphan_check_is_reproducible(self):
        findings = access.check_orphan_accounts(self.users, self.as_of)
        self.assertEqual([item["username"] for item in findings], ["jlee_old"])

    def test_access_policy_checks(self):
        self.assertEqual(len(access.check_mfa_compliance(self.users)), 2)
        self.assertEqual(len(access.check_privilege_ratio(self.users)), 1)
        self.assertEqual(len(access.check_separation_of_duties(self.users)), 0)
        self.assertEqual(len(access.check_service_accounts(self.users)), 1)


class EvidenceCollectorTests(unittest.TestCase):
    def test_access_summary(self):
        stats, findings = evidence.collect_access_evidence(
            evidence.generate_sample_users(), datetime(2026, 4, 1)
        )
        self.assertEqual(stats["total_users"], 10)
        self.assertEqual(stats["orphan_accounts"], 1)
        self.assertEqual(stats["mfa_rate"], "80.0%")
        self.assertEqual(len(findings), 3)

    def test_training_and_patch_summaries(self):
        training_stats, training_findings = evidence.collect_training_evidence(
            evidence.generate_sample_training()
        )
        patch_stats, patch_findings = evidence.collect_patch_evidence(
            evidence.generate_sample_patches()
        )
        self.assertEqual(training_stats["completion_rate"], "88.9%")
        self.assertEqual(len(training_findings), 2)
        self.assertEqual(patch_stats["compliance_rate"], "87.5%")
        self.assertEqual(len(patch_findings), 1)


class ComplianceCheckerTests(unittest.TestCase):
    def test_sample_control_analysis(self):
        controls = compliance.generate_sample_controls()
        stats, labels = compliance.analyze_controls(controls)
        self.assertEqual(stats["total"], 18)
        self.assertEqual(stats["implemented"], 13)
        self.assertEqual(len(stats["gaps"]), 5)
        self.assertEqual(labels["nist_csf"], "NIST CSF 2.0")


if __name__ == "__main__":
    unittest.main()
