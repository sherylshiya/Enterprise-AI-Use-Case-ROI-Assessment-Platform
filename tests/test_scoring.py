from src.assessment.scoring import (
    calculate_business_impact,
    calculate_risk,
    score_volume,
    score_repetitiveness,
    calculate_ai_readiness,
    calculate_automation_readiness,
    calculate_opportunity_score,
    classify_score,
    assess_process,
)


def test_volume_score():
    assert score_volume(10000) == 80


def test_repetitiveness_score():
    assert score_repetitiveness("very_high") == 100


def test_ai_readiness():
    score = calculate_ai_readiness(
        data_availability=90,
        decision_complexity=80,
        ai_feasibility=100,
    )

    assert score == 91.5


def test_automation_readiness():
    score = calculate_automation_readiness(
        repetitiveness=100,
        volume=80,
        rule_based_nature=80,
        human_effort=80,
    )

    assert score == 87


def test_opportunity_score():
    score = calculate_opportunity_score(
        ai_readiness=91.5,
        automation_readiness=88,
        business_impact=81,
        risk=75,
    )

    assert score == 62.5


def test_classification():
    assert classify_score(89.75) == "Very High"


def test_full_assessment():

    process = {
    "process_name": "Invoice Processing",
    "monthly_volume": 10000,

    "repetitiveness": "very_high",
    "rule_based_nature": "high",
    "data_availability": "high",
    "human_effort": "high",
    "decision_complexity": "medium",
    "ai_feasibility": "high",

    "financial_impact": "high",
    "time_savings": "very_high",
    "strategic_importance": "high",

    "decision_criticality": "medium",
    "accuracy_requirement": "high",
    "compliance_sensitivity": "medium",
    "human_oversight": "high",

    }

    result = assess_process(process)

    assert "factor_scores" in result
    assert "dimension_scores" in result
    assert "overall_opportunity_score" in result
    assert "classification" in result

    assert 0 <= result["overall_opportunity_score"] <= 100

def test_business_impact():
    score = calculate_business_impact(
        financial_impact=80,
        time_savings=100,
        volume=60,
        strategic_importance=80,
    )

    assert score == 81
def test_risk():
    score = calculate_risk(
        decision_criticality=80,
        accuracy_requirement=80,
        compliance_sensitivity=60,
        human_oversight=80,
    )

    assert score == 75

def test_opportunity_score_with_risk():
    score = calculate_opportunity_score(
        ai_readiness=90,
        automation_readiness=80,
        business_impact=85,
        risk=60,
    )

    assert score == 63.5