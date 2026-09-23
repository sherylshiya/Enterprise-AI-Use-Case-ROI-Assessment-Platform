"""
Core scoring engine for the Enterprise AI Use-Case & ROI Assessment Platform.

This module converts business-process characteristics into normalized
0-100 scores and derives higher-level assessments.
"""


# ============================================================
# CONSTANTS
# ============================================================

SCORE_BANDS = {
    "low": (0, 39),
    "moderate": (40, 59),
    "high": (60, 79),
    "very_high": (80, 100),
}


# ============================================================
# BASIC FEATURE SCORING
# ============================================================

def score_repetitiveness(level: str) -> float:
    """
    Score how repetitive the process is.

    Higher score = more repetitive = greater automation opportunity.
    """
    scores = {
        "low": 20,
        "medium": 50,
        "high": 80,
        "very_high": 100,
    }

    return scores.get(level.lower(), 0)


def score_volume(monthly_volume: int) -> float:
    """
    Score process volume based on monthly transaction/task count.
    """
    if monthly_volume < 1_000:
        return 20
    elif monthly_volume < 5_000:
        return 40
    elif monthly_volume < 10_000:
        return 60
    elif monthly_volume < 50_000:
        return 80
    else:
        return 100


def score_rule_based_nature(level: str) -> float:
    """
    Score how strongly the process follows explicit business rules.

    Higher score = more deterministic.
    """
    scores = {
        "low": 20,
        "medium": 50,
        "high": 80,
        "very_high": 100,
    }

    return scores.get(level.lower(), 0)


def score_data_availability(level: str) -> float:
    """
    Score availability of usable process data.
    """
    scores = {
        "low": 20,
        "medium": 50,
        "high": 90,
        "very_high": 100,
    }

    return scores.get(level.lower(), 0)


def score_human_effort(level: str) -> float:
    """
    Score the amount of human effort involved.

    Higher score = more human effort = greater automation opportunity.
    """
    scores = {
        "low": 20,
        "medium": 50,
        "high": 80,
        "very_high": 100,
    }

    return scores.get(level.lower(), 0)


def score_decision_complexity(level: str) -> float:
    """
    Score the complexity of decisions made during the process.

    Higher score = more contextual / complex human reasoning.
    """
    scores = {
        "low": 20,
        "medium": 50,
        "high": 80,
        "very_high": 100,
    }

    return scores.get(level.lower(), 0)


def score_ai_feasibility(level: str) -> float:
    """
    Score whether AI is technically and practically suitable
    for the process.
    """
    scores = {
        "low": 20,
        "medium": 50,
        "high": 80,
        "very_high": 100,
    }

    return scores.get(level.lower(), 0)


# ============================================================
# AI READINESS
# ============================================================

def calculate_ai_readiness(
    data_availability: float,
    decision_complexity: float,
    ai_feasibility: float,
) -> float:
    """
    Calculate AI Readiness.

    AI Readiness focuses on whether the process has:
    - sufficient data
    - meaningful decision complexity
    - a genuine use case for AI

    Weights:
        Data Availability: 35%
        Decision Complexity: 30%
        AI Feasibility: 35%
    """

    score = (
        data_availability * 0.35
        + decision_complexity * 0.30
        + ai_feasibility * 0.35
    )

    return round(score, 2)


# ============================================================
# AUTOMATION READINESS
# ============================================================

def calculate_automation_readiness(
    repetitiveness: float,
    volume: float,
    rule_based_nature: float,
    human_effort: float,
) -> float:
    """
    Calculate Automation Readiness.

    Automation Readiness focuses on how suitable the process is
    for removing repetitive manual work.

    Weights:
        Repetitiveness: 35%
        Volume: 20%
        Rule-based Nature: 20%
        Human Effort: 25%
    """

    score = (
        repetitiveness * 0.35
        + volume * 0.20
        + rule_based_nature * 0.20
        + human_effort * 0.25
    )

    return round(score, 2)


# ============================================================
# OVERALL AI / AUTOMATION OPPORTUNITY
# ============================================================

def calculate_opportunity_score(
    ai_readiness: float,
    automation_readiness: float,
    business_impact: float,
    risk: float,
) -> float:
    score = (
        ai_readiness * 0.25
        + automation_readiness * 0.25
        + business_impact * 0.35
        - risk * 0.15
    )

    return round(score, 2)
# ============================================================
# CLASSIFICATION
# ============================================================

def classify_score(score: float) -> str:
    """
    Convert a 0-100 score into a business-friendly classification.
    """

    if score < 40:
        return "Low"
    elif score < 60:
        return "Moderate"
    elif score < 80:
        return "High"
    else:
        return "Very High"


def score_financial_impact(level: str) -> float:
    scores = {
        "low": 20,
        "medium": 60,
        "high": 80,
        "very_high": 100,
    }
    return scores.get(level.lower(), 0)


def score_time_savings(level: str) -> float:
    scores = {
        "low": 20,
        "medium": 60,
        "high": 80,
        "very_high": 100,
    }
    return scores.get(level.lower(), 0)


def score_strategic_importance(level: str) -> float:
    scores = {
        "low": 20,
        "medium": 60,
        "high": 80,
        "very_high": 100,
    }
    return scores.get(level.lower(), 0)


def calculate_business_impact(
    financial_impact: float,
    time_savings: float,
    volume: float,
    strategic_importance: float,
) -> float:

    score = (
        financial_impact * 0.30
        + time_savings * 0.25
        + volume * 0.20
        + strategic_importance * 0.25
    )

    return round(score, 2)

def score_decision_criticality(level: str) -> float:
    scores = {
        "low": 20,
        "medium": 60,
        "high": 80,
        "very_high": 100,
    }
    return scores.get(level.lower(), 0)


def score_accuracy_requirement(level: str) -> float:
    scores = {
        "low": 20,
        "medium": 60,
        "high": 80,
        "very_high": 100,
    }
    return scores.get(level.lower(), 0)


def score_compliance_sensitivity(level: str) -> float:
    scores = {
        "low": 20,
        "medium": 60,
        "high": 80,
        "very_high": 100,
    }
    return scores.get(level.lower(), 0)


def score_human_oversight(level: str) -> float:
    scores = {
        "low": 20,
        "medium": 60,
        "high": 80,
        "very_high": 100,
    }
    return scores.get(level.lower(), 0)

def calculate_risk(
    decision_criticality: float,
    accuracy_requirement: float,
    compliance_sensitivity: float,
    human_oversight: float,
) -> float:

    score = (
        decision_criticality * 0.30
        + accuracy_requirement * 0.25
        + compliance_sensitivity * 0.25
        + human_oversight * 0.20
    )

    return round(score, 2)
# ============================================================
# FULL ASSESSMENT
# ============================================================

def assess_process(process: dict) -> dict:
    # Factor scores
    repetitiveness = score_repetitiveness(process["repetitiveness"])
    volume = score_volume(process["monthly_volume"])
    rule_based_nature = score_rule_based_nature(
        process["rule_based_nature"]
    )
    data_availability = score_data_availability(
        process["data_availability"]
    )
    human_effort = score_human_effort(process["human_effort"])
    decision_complexity = score_decision_complexity(
        process["decision_complexity"]
    )
    ai_feasibility = score_ai_feasibility(
        process["ai_feasibility"]
    )

    financial_impact = score_financial_impact(
        process["financial_impact"]
    )
    time_savings = score_time_savings(
        process["time_savings"]
    )
    strategic_importance = score_strategic_importance(
        process["strategic_importance"]
    )

    decision_criticality = score_decision_criticality(
        process["decision_criticality"]
    )
    accuracy_requirement = score_accuracy_requirement(
        process["accuracy_requirement"]
    )
    compliance_sensitivity = score_compliance_sensitivity(
        process["compliance_sensitivity"]
    )
    human_oversight = score_human_oversight(
        process["human_oversight"]
    )

    # Dimension scores
    ai_readiness = calculate_ai_readiness(
        data_availability=data_availability,
        decision_complexity=decision_complexity,
        ai_feasibility=ai_feasibility,
    )

    automation_readiness = calculate_automation_readiness(
        repetitiveness=repetitiveness,
        volume=volume,
        rule_based_nature=rule_based_nature,
        human_effort=human_effort,
    )

    business_impact = calculate_business_impact(
        financial_impact=financial_impact,
        time_savings=time_savings,
        volume=volume,
        strategic_importance=strategic_importance,
    )

    risk = calculate_risk(
        decision_criticality=decision_criticality,
        accuracy_requirement=accuracy_requirement,
        compliance_sensitivity=compliance_sensitivity,
        human_oversight=human_oversight,
    )

    opportunity_score = calculate_opportunity_score(
        ai_readiness=ai_readiness,
        automation_readiness=automation_readiness,
        business_impact=business_impact,
        risk=risk,
    )

    return {
        "process_name": process.get("process_name"),

        "factor_scores": {
            "repetitiveness": repetitiveness,
            "volume": volume,
            "rule_based_nature": rule_based_nature,
            "data_availability": data_availability,
            "human_effort": human_effort,
            "decision_complexity": decision_complexity,
            "ai_feasibility": ai_feasibility,
            "financial_impact": financial_impact,
            "time_savings": time_savings,
            "strategic_importance": strategic_importance,
            "decision_criticality": decision_criticality,
            "accuracy_requirement": accuracy_requirement,
            "compliance_sensitivity": compliance_sensitivity,
            "human_oversight": human_oversight,
        },

        "dimension_scores": {
            "ai_readiness": ai_readiness,
            "automation_readiness": automation_readiness,
            "business_impact": business_impact,
            "risk": risk,
        },

        "overall_opportunity_score": opportunity_score,
        "classification": classify_score(opportunity_score),
    }
