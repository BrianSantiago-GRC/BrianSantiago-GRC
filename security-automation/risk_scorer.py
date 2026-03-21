"""
GRC Risk Scoring Automation Tool
Reads a risk register CSV, calculates inherent and residual risk scores,
classifies risk levels, and generates a summary report with a text-based heat map.

Methodology: NIST SP 800-30 (Guide for Conducting Risk Assessments)
Scoring: Likelihood (1-5) x Impact (1-5) = Risk Score (1-25)

Author: Brian Santiago
"""

import csv
import sys
import os
from datetime import datetime


# ---------------------------------------------------------------------------
# Scoring tables aligned to NIST SP 800-30
# ---------------------------------------------------------------------------

LIKELIHOOD_LABELS = {1: "Very Low", 2: "Low", 3: "Moderate", 4: "High", 5: "Very High"}
IMPACT_LABELS = {1: "Very Low", 2: "Low", 3: "Moderate", 4: "High", 5: "Very High"}

RISK_LEVEL_THRESHOLDS = [
    (0, 4, "Low", "green"),
    (5, 9, "Medium", "yellow"),
    (10, 16, "High", "orange"),
    (17, 25, "Critical", "red"),
]

CONTROL_EFFECTIVENESS_REDUCTION = {
    "High": 0.40,
    "Medium": 0.25,
    "Low": 0.10,
    "None": 0.00,
}


def classify_risk(score):
    """Return the risk level label for a given numeric score."""
    for low, high, label, _ in RISK_LEVEL_THRESHOLDS:
        if low <= score <= high:
            return label
    return "Unknown"


def calculate_residual_score(inherent_score, control_effectiveness):
    """
    Reduce inherent risk by the control effectiveness percentage.
    Result is rounded to the nearest integer and floored at 1.
    """
    reduction = CONTROL_EFFECTIVENESS_REDUCTION.get(control_effectiveness, 0.0)
    residual = inherent_score * (1 - reduction)
    return max(1, round(residual))


def load_risks(filepath):
    """Load risks from a CSV file and return a list of enriched risk dicts."""
    risks = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            likelihood = int(row["likelihood"])
            impact = int(row["impact"])
            inherent_score = likelihood * impact
            control_eff = row.get("control_effectiveness", "None").strip()
            residual_score = calculate_residual_score(inherent_score, control_eff)

            risks.append({
                "id": row["risk_id"],
                "name": row["risk_name"],
                "category": row["category"],
                "threat_source": row["threat_source"],
                "affected_asset": row["affected_asset"],
                "likelihood": likelihood,
                "impact": impact,
                "inherent_score": inherent_score,
                "control_description": row["control_description"],
                "control_effectiveness": control_eff,
                "residual_score": residual_score,
                "inherent_level": classify_risk(inherent_score),
                "residual_level": classify_risk(residual_score),
                "status": row.get("status", ""),
                "owner": row.get("owner", ""),
            })
    return risks


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_divider(char="-", width=90):
    print(char * width)


def print_risk_table(risks):
    """Print a formatted table of all risks with scores."""
    header = f"{'ID':<10} {'Risk Name':<42} {'L':>2} {'I':>2} {'Inherent':>9} {'Residual':>9} {'Level':>9}"
    print_divider("=")
    print(header)
    print_divider("=")
    for r in risks:
        print(
            f"{r['id']:<10} {r['name']:<42} {r['likelihood']:>2} {r['impact']:>2} "
            f"{r['inherent_score']:>5} ({r['inherent_level']:<8}) "
            f"{r['residual_score']:>3} ({r['residual_level']:<8})"
        )
    print_divider("=")


def print_heat_map(risks):
    """
    Print a 5x5 text-based risk heat map showing how many risks fall
    into each likelihood/impact cell based on residual scores.
    """
    grid = {}
    for r in risks:
        # Use residual-adjusted likelihood for placement
        res_likelihood = max(1, round(r["residual_score"] / r["impact"])) if r["impact"] > 0 else r["likelihood"]
        key = (res_likelihood, r["impact"])
        grid[key] = grid.get(key, 0) + 1

    print("\n  RESIDUAL RISK HEAT MAP (count of risks per cell)")
    print_divider()
    print(f"  {'':>14}", end="")
    for imp in range(1, 6):
        print(f"  Impact {imp} ", end="")
    print()
    print_divider()

    for lik in range(5, 0, -1):
        label = f"Likelihood {lik}"
        print(f"  {label:>14}", end="")
        for imp in range(1, 6):
            count = grid.get((lik, imp), 0)
            score = lik * imp
            level = classify_risk(score)
            if count > 0:
                marker = f"[{count:^3}]"
            else:
                marker = "  .  "
            # Add risk-level indicator
            indicator = {"Low": " ", "Medium": "*", "High": "#", "Critical": "!"}
            print(f"  {indicator.get(level, ' ')}{marker}  ", end="")
        print()

    print_divider()
    print("  Legend:  . = no risks   [ n ] = count of risks in cell")
    print("          (space) = Low   * = Medium   # = High   ! = Critical\n")


def print_summary_stats(risks):
    """Print high-level statistics about the risk register."""
    total = len(risks)
    inherent_counts = {}
    residual_counts = {}
    for r in risks:
        inherent_counts[r["inherent_level"]] = inherent_counts.get(r["inherent_level"], 0) + 1
        residual_counts[r["residual_level"]] = residual_counts.get(r["residual_level"], 0) + 1

    avg_inherent = sum(r["inherent_score"] for r in risks) / total if total else 0
    avg_residual = sum(r["residual_score"] for r in risks) / total if total else 0
    overall_reduction = ((avg_inherent - avg_residual) / avg_inherent * 100) if avg_inherent else 0

    print("\n  RISK SUMMARY")
    print_divider()
    print(f"  Total risks assessed:  {total}")
    print(f"  Average inherent score: {avg_inherent:.1f}")
    print(f"  Average residual score: {avg_residual:.1f}")
    print(f"  Overall risk reduction: {overall_reduction:.1f}%")
    print()

    print("  Risk distribution (inherent -> residual):")
    for level in ["Critical", "High", "Medium", "Low"]:
        inh = inherent_counts.get(level, 0)
        res = residual_counts.get(level, 0)
        arrow = "v" if res < inh else ("^" if res > inh else "=")
        print(f"    {level:<10}  {inh:>2} -> {res:>2}  {arrow}")
    print()


def print_top_risks(risks, n=5):
    """Print the top N risks by residual score for prioritization."""
    sorted_risks = sorted(risks, key=lambda r: r["residual_score"], reverse=True)
    print(f"\n  TOP {n} RISKS BY RESIDUAL SCORE (prioritize treatment)")
    print_divider()
    for i, r in enumerate(sorted_risks[:n], 1):
        print(f"  {i}. [{r['residual_level']}] {r['id']} - {r['name']}")
        print(f"     Score: {r['residual_score']} | Owner: {r['owner']} | Asset: {r['affected_asset']}")
        print(f"     Control: {r['control_description'][:80]}")
        print()


def generate_report(risks, output_path=None):
    """Generate the full risk scoring report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{'='*90}")
    print(f"  GRC RISK SCORING REPORT")
    print(f"  Generated: {timestamp}")
    print(f"  Methodology: NIST SP 800-30")
    print(f"  Scoring: Likelihood (1-5) x Impact (1-5) = Inherent Risk (1-25)")
    print(f"  Residual: Inherent score reduced by control effectiveness")
    print(f"{'='*90}\n")

    print_risk_table(risks)
    print_summary_stats(risks)
    print_heat_map(risks)
    print_top_risks(risks)

    # Write to file if output path provided
    if output_path:
        import io
        from contextlib import redirect_stdout

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print(f"GRC RISK SCORING REPORT")
            print(f"Generated: {timestamp}")
            print(f"Methodology: NIST SP 800-30\n")
            print_risk_table(risks)
            print_summary_stats(risks)
            print_heat_map(risks)
            print_top_risks(risks)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(buffer.getvalue())
        print(f"  Report saved to: {output_path}")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        # Default to sample file in same directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "sample_risk_register.csv")
    else:
        csv_path = sys.argv[1]

    if not os.path.exists(csv_path):
        print(f"Error: File not found: {csv_path}")
        sys.exit(1)

    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    risks = load_risks(csv_path)
    generate_report(risks, output_path)


if __name__ == "__main__":
    main()
