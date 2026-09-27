def calculate_automation_potential(
    automation_readiness: float,
    repetitiveness: float,
    rule_based_nature: float,
    human_effort: float,
    ai_feasibility: float,
    decision_complexity: float,
    current_automation: float,
) -> float:

    score = (
        automation_readiness * 0.30
        + repetitiveness * 0.15
        + rule_based_nature * 0.15
        + human_effort * 0.15
        + ai_feasibility * 0.15
        + (100 - decision_complexity) * 0.05
        + (100 - current_automation) * 0.05
    )

    return round(score, 2)

CONSERVATIVE_SAVINGS_RATE = 0.30
EXPECTED_SAVINGS_RATE = 0.50
OPTIMISTIC_SAVINGS_RATE = 0.70


def calculate_savings_scenarios(
    current_annual_cost: float,
) -> dict:

    return {
        "conservative": {
            "savings_rate": 30.0,
            "annual_savings": round(
                current_annual_cost * CONSERVATIVE_SAVINGS_RATE,
                2,
            ),
        },
        "expected": {
            "savings_rate": 50.0,
            "annual_savings": round(
                current_annual_cost * EXPECTED_SAVINGS_RATE,
                2,
            ),
        },
        "optimistic": {
            "savings_rate": 70.0,
            "annual_savings": round(
                current_annual_cost * OPTIMISTIC_SAVINGS_RATE,
                2,
            ),
        },
    }