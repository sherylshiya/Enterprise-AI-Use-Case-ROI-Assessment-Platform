import json

from src.assessment.scoring import assess_process


with open("data/sample_use_cases.json") as f:
    use_cases = json.load(f)


for use_case in use_cases:
    result = assess_process(use_case)

    print("\n" + "=" * 50)
    print(result["process_name"])
    print("=" * 50)

    print("AI Readiness:", result["dimension_scores"]["ai_readiness"])
    print("Automation Readiness:", result["dimension_scores"]["automation_readiness"])
    print("Business Impact:", result["dimension_scores"]["business_impact"])
    print("Risk:", result["dimension_scores"]["risk"])
    print("Overall Opportunity:", result["overall_opportunity_score"])
    print("Classification:", result["classification"])