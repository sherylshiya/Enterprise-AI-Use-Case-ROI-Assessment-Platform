from src.economics.cost import (
    calculate_current_annual_cost,
    calculate_annual_operating_cost,
    calculate_total_first_year_cost,
    calculate_annual_savings,
    calculate_net_benefit,
)

from src.economics.savings import (
    calculate_automation_potential,
    calculate_savings_scenarios,
)


def calculate_roi(
    net_benefit: float,
    implementation_cost: float,
) -> float:
    """Calculate first-year ROI percentage."""
    if implementation_cost <= 0:
        return 0.0

    return round(
        (net_benefit / implementation_cost) * 100,
        2,
    )


def calculate_payback_period(
    implementation_cost: float,
    annual_savings: float,
) -> float:
    """Calculate payback period in months."""
    if annual_savings <= 0:
        return 0.0

    return round(
        (implementation_cost / annual_savings) * 12,
        2,
    )


def calculate_economics(
    monthly_volume: int,
    processing_time_minutes: float,
    hourly_labor_cost: float,
    monthly_operating_cost: float,
    implementation_cost: float,
) -> dict:
    """Calculate the complete financial assessment."""

    current_annual_cost = calculate_current_annual_cost(
        monthly_volume=monthly_volume,
        processing_time_minutes=processing_time_minutes,
        hourly_labor_cost=hourly_labor_cost,
    )

    annual_operating_cost = calculate_annual_operating_cost(
        monthly_operating_cost=monthly_operating_cost,
    )

    total_first_year_cost = calculate_total_first_year_cost(
        implementation_cost=implementation_cost,
        annual_operating_cost=annual_operating_cost,
    )

    annual_savings = calculate_annual_savings(
        current_annual_cost=current_annual_cost,
        annual_operating_cost=annual_operating_cost,
    )

    net_benefit = calculate_net_benefit(
        annual_savings=annual_savings,
        implementation_cost=implementation_cost,
    )

    roi = calculate_roi(
        net_benefit=net_benefit,
        implementation_cost=implementation_cost,
    )

    payback_period = calculate_payback_period(
        implementation_cost=implementation_cost,
        annual_savings=annual_savings,
    )

    return {
        "current_annual_cost": current_annual_cost,
        "annual_operating_cost": annual_operating_cost,
        "implementation_cost": implementation_cost,
        "total_first_year_cost": total_first_year_cost,
        "annual_savings": annual_savings,
        "net_benefit": net_benefit,
        "roi_percent": roi,
        "payback_period_months": payback_period,
    }


def calculate_scenario_roi(
    annual_savings: float,
    annual_operating_cost: float,
    implementation_cost: float,
) -> dict:
    """Calculate ROI for a single savings scenario."""

    realized_annual_benefit = (
        annual_savings - annual_operating_cost
    )

    net_benefit = (
        realized_annual_benefit - implementation_cost
    )

    roi = calculate_roi(
        net_benefit=net_benefit,
        implementation_cost=implementation_cost,
    )

    payback_period = calculate_payback_period(
        implementation_cost=implementation_cost,
        annual_savings=realized_annual_benefit,
    )

    return {
        "annual_savings": round(annual_savings, 2),
        "realized_annual_benefit": round(realized_annual_benefit, 2),
        "net_benefit": round(net_benefit, 2),
        "roi_percent": roi,
        "payback_period_months": payback_period,
    }


def calculate_scenario_economics(
    use_case: dict,
    assessment_result: dict,
) -> dict:
    """Calculate automation potential and scenario-based economics."""

    automation_potential = calculate_automation_potential(
        automation_readiness=assessment_result["dimension_scores"][
            "automation_readiness"
        ],
        repetitiveness=assessment_result["factor_scores"][
            "repetitiveness"
        ],
        rule_based_nature=assessment_result["factor_scores"][
            "rule_based_nature"
        ],
        human_effort=assessment_result["factor_scores"][
            "human_effort"
        ],
        ai_feasibility=assessment_result["factor_scores"][
            "ai_feasibility"
        ],
        decision_complexity=assessment_result["factor_scores"][
            "decision_complexity"
        ],
        current_automation=use_case["current_automation"] * 100,
    )

    current_annual_cost = calculate_current_annual_cost(
        monthly_volume=use_case["monthly_volume"],
        processing_time_minutes=use_case["processing_time_minutes"],
        hourly_labor_cost=use_case["hourly_labor_cost"],
    )

    annual_operating_cost = calculate_annual_operating_cost(
        monthly_operating_cost=use_case["monthly_operating_cost"]
    )

    implementation_cost = use_case["implementation_cost"]

    savings_scenarios = calculate_savings_scenarios(
        current_annual_cost=current_annual_cost,
    )

    scenarios = {}

    for scenario, values in savings_scenarios.items():

        scenarios[scenario] = calculate_scenario_roi(
            annual_savings=values["annual_savings"],
            annual_operating_cost=annual_operating_cost,
            implementation_cost=implementation_cost,
        )

        scenarios[scenario]["savings_rate"] = (
            values["savings_rate"]
        )

    return {
        "automation_potential": automation_potential,
        "scenarios": scenarios,
    }

def calculate_roi_sensitivity(
    current_annual_cost: float,
    annual_operating_cost: float,
    implementation_cost: float,
    savings_rates: list[float] | None = None,
) -> dict:
    """Calculate ROI across different savings assumptions."""

    if savings_rates is None:
        savings_rates = [
            10.0,
            20.0,
            30.0,
            40.0,
            50.0,
            60.0,
            70.0,
            80.0,
            90.0,
        ]

    sensitivity = {}

    for savings_rate in savings_rates:

        annual_savings = (
            current_annual_cost * (savings_rate / 100)
        )

        realized_annual_benefit = (
            annual_savings - annual_operating_cost
        )

        net_benefit = (
            realized_annual_benefit - implementation_cost
        )

        roi = calculate_roi(
            net_benefit=net_benefit,
            implementation_cost=implementation_cost,
        )

        payback = calculate_payback_period(
            implementation_cost=implementation_cost,
            annual_savings=realized_annual_benefit,
        )

        sensitivity[savings_rate] = {
            "annual_savings": round(annual_savings, 2),
            "net_benefit": round(net_benefit, 2),
            "roi_percent": roi,
            "payback_period_months": payback,
        }

    return sensitivity