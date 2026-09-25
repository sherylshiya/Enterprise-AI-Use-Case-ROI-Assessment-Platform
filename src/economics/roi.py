from src.economics.cost import (
    calculate_current_annual_cost,
    calculate_annual_operating_cost,
    calculate_total_first_year_cost,
    calculate_annual_savings,
    calculate_net_benefit,
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