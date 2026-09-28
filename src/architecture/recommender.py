from typing import Any


ARCHITECTURE_OPTIONS = [
    "Rules Engine",
    "Traditional ML",
    "LLM",
    "RAG",
    "Agentic AI",
    "Fine-tuning",
    "Hybrid",
]


def build_architecture_context(
    use_case: dict[str, Any],
    assessment_result: dict[str, Any],
) -> dict[str, Any]:
    """
    Build a structured context for AI-based architecture recommendation.

    The deterministic assessment engine provides the quantitative signals.
    The original use-case information provides business/process context.
    """

    factor_scores = assessment_result["factor_scores"]
    dimension_scores = assessment_result["dimension_scores"]

    return {
        "use_case": {
            "process_name": use_case["process_name"],
            "industry": use_case["industry"],
            "description": use_case["description"],
            "monthly_volume": use_case["monthly_volume"],
            "processing_time_minutes": use_case["processing_time_minutes"],
            "data_type": use_case.get("data_type", []),
            "current_automation": use_case.get("current_automation", 0),
        },
        "assessment": {
            "ai_readiness": dimension_scores["ai_readiness"],
            "automation_readiness": dimension_scores["automation_readiness"],
            "business_impact": dimension_scores["business_impact"],
            "risk": dimension_scores["risk"],
            "overall_opportunity_score": assessment_result[
                "overall_opportunity_score"
            ],
            "classification": assessment_result["classification"],
        },
        "process_factors": {
            "repetitiveness": factor_scores["repetitiveness"],
            "volume": factor_scores["volume"],
            "rule_based_nature": factor_scores["rule_based_nature"],
            "data_availability": factor_scores["data_availability"],
            "human_effort": factor_scores["human_effort"],
            "decision_complexity": factor_scores["decision_complexity"],
            "ai_feasibility": factor_scores["ai_feasibility"],
        },
        "architecture_options": ARCHITECTURE_OPTIONS,
    }


def get_architecture_output_schema() -> dict[str, Any]:
    """
    Define the expected structured output from the AI architecture advisor.
    """

    return {
        "recommended_architecture": "",
        "alternative_architecture": "",
        "reasoning": [],
        "components": [],
        "data_sources": [],
        "integrations": [],
        "human_oversight": "",
        "key_risks": [],
        "governance_controls": [],
    }