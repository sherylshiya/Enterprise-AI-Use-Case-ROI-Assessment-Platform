import json

from src.assessment.scoring import assess_process
from src.economics.roi import calculate_economics


with open("data/sample_use_cases.json") as f:
    use_cases = json.load(f)


for use_case in use_cases:

    result = assess_process(use_case)

    economics = calculate_economics(
        monthly_volume=use_case["monthly_volume"],
        processing_time_minutes=use_case["processing_time_minutes"],
        hourly_labor_cost=use_case["hourly_labor_cost"],
        monthly_operating_cost=use_case["monthly_operating_cost"],
        implementation_cost=use_case["implementation_cost"],
    )

    print("\n" + "=" * 60)
    print(result["process_name"])
    print("=" * 60)

    # Assessment
    print("\n--- Assessment ---")
    print("AI Readiness:", result["dimension_scores"]["ai_readiness"])
    print("Automation Readiness:", result["dimension_scores"]["automation_readiness"])
    print("Business Impact:", result["dimension_scores"]["business_impact"])
    print("Risk:", result["dimension_scores"]["risk"])
    print("Overall Opportunity:", result["overall_opportunity_score"])
    print("Classification:", result["classification"])

    # Economics
    print("\n--- Economics ---")
    print("Current Annual Cost:", economics["current_annual_cost"])
    print("Annual Operating Cost:", economics["annual_operating_cost"])
    print("Implementation Cost:", economics["implementation_cost"])
    print("Total First-Year Cost:", economics["total_first_year_cost"])
    print("Annual Savings:", economics["annual_savings"])
    print("Net Benefit:", economics["net_benefit"])
    print("ROI:", economics["roi_percent"], "%")
    print("Payback Period:", economics["payback_period_months"], "months")