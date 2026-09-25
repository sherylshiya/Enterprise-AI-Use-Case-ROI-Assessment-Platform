from src.economics.cost import calculate_current_annual_cost
from src.economics.cost import (
    calculate_annual_operating_cost,
    calculate_total_first_year_cost,
)

from src.economics.roi import calculate_economics
from src.economics.roi import (
    calculate_roi,
    calculate_payback_period,
)

def test_current_annual_cost():
    cost = calculate_current_annual_cost(
        monthly_volume=10000,
        processing_time_minutes=10,
        hourly_labor_cost=25,
    )

    assert cost == 500000




def test_annual_operating_cost():
    cost = calculate_annual_operating_cost(
        monthly_operating_cost=2000,
    )

    assert cost == 24000


def test_total_first_year_cost():
    cost = calculate_total_first_year_cost(
        implementation_cost=30000,
        annual_operating_cost=24000,
    )

    assert cost == 54000

from src.economics.cost import (
    calculate_annual_savings,
    calculate_net_benefit,
)


def test_annual_savings():
    savings = calculate_annual_savings(
        current_annual_cost=500000,
        annual_operating_cost=24000,
    )

    assert savings == 476000


def test_net_benefit():
    benefit = calculate_net_benefit(
        annual_savings=476000,
        implementation_cost=30000,
    )

    assert benefit == 446000


def test_roi():
    roi = calculate_roi(
        net_benefit=446000,
        implementation_cost=30000,
    )

    assert roi == 1486.67


def test_payback_period():
    payback = calculate_payback_period(
        implementation_cost=30000,
        annual_savings=476000,
    )

    assert payback == 0.76



def test_economics_assessment():
    result = calculate_economics(
        monthly_volume=10000,
        processing_time_minutes=10,
        hourly_labor_cost=25,
        monthly_operating_cost=2000,
        implementation_cost=30000,
    )

    assert result["current_annual_cost"] == 500000
    assert result["annual_operating_cost"] == 24000
    assert result["implementation_cost"] == 30000
    assert result["annual_savings"] == 476000
    assert result["net_benefit"] == 446000
    assert result["roi_percent"] == 1486.67
    assert result["payback_period_months"] == 0.76