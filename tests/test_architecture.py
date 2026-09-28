from src.architecture.recommender import (
    ARCHITECTURE_OPTIONS,
    build_architecture_context,
    get_architecture_output_schema,
)


def test_architecture_options():
    assert "LLM" in ARCHITECTURE_OPTIONS
    assert "RAG" in ARCHITECTURE_OPTIONS
    assert "Agentic AI" in ARCHITECTURE_OPTIONS
    assert "Hybrid" in ARCHITECTURE_OPTIONS


def test_build_architecture_context():

    use_case = {
        "process_name": "Resume Screening",
        "industry": "Recruitment",
        "description": "Review resumes and shortlist candidates",
        "monthly_volume": 5000,
        "processing_time_minutes": 12,
        "data_type": ["PDF", "DOCX", "unstructured_text"],
        "current_automation": 0.10,
    }

    assessment_result = {
        "factor_scores": {
            "repetitiveness": 80,
            "volume": 60,
            "rule_based_nature": 60,
            "data_availability": 90,
            "human_effort": 80,
            "decision_complexity": 80,
            "ai_feasibility": 100,
        },
        "dimension_scores": {
            "ai_readiness": 90.5,
            "automation_readiness": 70.0,
            "business_impact": 70.0,
            "risk": 69.0,
        },
        "overall_opportunity_score": 54.27,
        "classification": "Moderate",
    }

    result = build_architecture_context(
        use_case=use_case,
        assessment_result=assessment_result,
    )

    assert result["assessment"]["ai_readiness"] == 90.5
    assert result["assessment"]["risk"] == 69.0
    assert result["process_factors"]["decision_complexity"] == 80
    assert result["use_case"]["data_type"] == [
        "PDF",
        "DOCX",
        "unstructured_text",
    ]


def test_architecture_output_schema():

    schema = get_architecture_output_schema()

    assert "recommended_architecture" in schema
    assert "reasoning" in schema
    assert "components" in schema
    assert "integrations" in schema
    assert "human_oversight" in schema
    assert "key_risks" in schema



from src.architecture.recommender import (
    build_architecture_context,
    build_architecture_prompt,
)


def test_architecture_prompt():

    use_case = {
        "process_name": "Resume Screening",
        "industry": "Recruitment",
        "description": "Review resumes and shortlist candidates",
        "monthly_volume": 5000,
        "processing_time_minutes": 12,
        "data_type": ["PDF", "DOCX", "unstructured_text"],
        "current_automation": 0.10,
    }

    assessment_result = {
        "factor_scores": {
            "repetitiveness": 80,
            "volume": 60,
            "rule_based_nature": 60,
            "data_availability": 90,
            "human_effort": 80,
            "decision_complexity": 80,
            "ai_feasibility": 100,
        },
        "dimension_scores": {
            "ai_readiness": 90.5,
            "automation_readiness": 70.0,
            "business_impact": 70.0,
            "risk": 69.0,
        },
        "overall_opportunity_score": 54.27,
        "classification": "Moderate",
    }

    context = build_architecture_context(
        use_case=use_case,
        assessment_result=assessment_result,
    )

    prompt = build_architecture_prompt(context)

    assert "Resume Screening" in prompt
    assert "AI Readiness: 90.5" in prompt
    assert "Automation Readiness: 70.0" in prompt
    assert "RAG" in prompt
    assert "Agentic AI" in prompt
    assert "Do not recommend unnecessary AI components." in prompt