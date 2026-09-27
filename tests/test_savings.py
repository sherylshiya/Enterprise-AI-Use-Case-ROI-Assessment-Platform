from src.economics.savings import calculate_automation_potential


def test_automation_potential():

    result = calculate_automation_potential(
        automation_readiness=87,
        repetitiveness=100,
        rule_based_nature=80,
        human_effort=80,
        ai_feasibility=80,
        decision_complexity=60,
        current_automation=10,
    )

    assert result > 70
    assert result <= 100
from src.economics.savings import (
    calculate_automation_potential,
    calculate_savings_scenarios,
)


def test_automation_potential():

    result = calculate_automation_potential(
        automation_readiness=87,
        repetitiveness=100,
        rule_based_nature=80,
        human_effort=80,
        ai_feasibility=80,
        decision_complexity=60,
        current_automation=10,
    )

    assert result > 70
    assert result <= 100


def test_savings_scenarios():

    result = calculate_savings_scenarios(
        current_annual_cost=500_000,
    )

    assert result["conservative"]["savings_rate"] == 30.0
    assert result["expected"]["savings_rate"] == 50.0
    assert result["optimistic"]["savings_rate"] == 70.0

    assert result["conservative"]["annual_savings"] == 150_000
    assert result["expected"]["annual_savings"] == 250_000
    assert result["optimistic"]["annual_savings"] == 350_000