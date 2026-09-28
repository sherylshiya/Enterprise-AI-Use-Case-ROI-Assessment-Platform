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



def build_architecture_prompt(
    architecture_context: dict[str, Any],
) -> str:
    """
    Build the prompt that will be sent to the AI architecture advisor.
    """

    return f"""
You are an enterprise AI solution architect.

Design an appropriate solution architecture for the following business process.

Use the assessment scores as decision-support signals, but reason from the
complete business and technical context.

Do not assume that AI is always required.
Prefer the simplest architecture that can reliably solve the problem.

BUSINESS PROCESS
Process: {architecture_context["use_case"]["process_name"]}
Industry: {architecture_context["use_case"]["industry"]}
Description: {architecture_context["use_case"]["description"]}

PROCESS CONTEXT
Monthly Volume: {architecture_context["use_case"]["monthly_volume"]}
Processing Time: {architecture_context["use_case"]["processing_time_minutes"]} minutes
Data Types: {architecture_context["use_case"]["data_type"]}
Current Automation: {architecture_context["use_case"]["current_automation"]}

ASSESSMENT RESULTS
AI Readiness: {architecture_context["assessment"]["ai_readiness"]}
Automation Readiness: {architecture_context["assessment"]["automation_readiness"]}
Business Impact: {architecture_context["assessment"]["business_impact"]}
Risk: {architecture_context["assessment"]["risk"]}
Overall Opportunity Score: {
    architecture_context["assessment"]["overall_opportunity_score"]
}
Classification: {architecture_context["assessment"]["classification"]}

PROCESS FACTORS
Repetitiveness: {architecture_context["process_factors"]["repetitiveness"]}
Volume: {architecture_context["process_factors"]["volume"]}
Rule-Based Nature: {architecture_context["process_factors"]["rule_based_nature"]}
Data Availability: {architecture_context["process_factors"]["data_availability"]}
Human Effort: {architecture_context["process_factors"]["human_effort"]}
Decision Complexity: {architecture_context["process_factors"]["decision_complexity"]}
AI Feasibility: {architecture_context["process_factors"]["ai_feasibility"]}

AVAILABLE ARCHITECTURE OPTIONS
{architecture_context["architecture_options"]}

REQUIREMENTS

1. Select the most appropriate architecture.
2. Provide one alternative where appropriate.
3. Explain the reasoning using the assessment results.
4. Identify the major architecture components.
5. Identify required data sources.
6. Identify required enterprise integrations.
7. Define the appropriate level of human oversight.
8. Identify key risks.
9. Identify important governance controls.
10. Do not recommend unnecessary AI components.

Return the recommendation using the following structure:

Recommended Architecture
Alternative Architecture
Reasoning
Components
Data Sources
Integrations
Human Oversight
Key Risks
Governance Controls
""".strip()


def parse_architecture_response(
    response: dict[str, Any],
) -> dict[str, Any]:
    """
    Validate and normalize an AI-generated architecture recommendation.
    """

    required_fields = [
        "recommended_architecture",
        "alternative_architecture",
        "reasoning",
        "components",
        "data_sources",
        "integrations",
        "human_oversight",
        "key_risks",
        "governance_controls",
    ]

    result = {}

    for field in required_fields:
        result[field] = response.get(field)

    return result