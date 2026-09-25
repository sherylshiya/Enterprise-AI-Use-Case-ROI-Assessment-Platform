def calculate_current_annual_cost(
    monthly_volume: int,
    processing_time_minutes: float,
    hourly_labor_cost: float,
) -> float:
    monthly_hours = (
        monthly_volume * processing_time_minutes
    ) / 60

    monthly_cost = monthly_hours * hourly_labor_cost

    annual_cost = monthly_cost * 12

    return round(annual_cost, 2)

def calculate_annual_operating_cost(
    monthly_operating_cost: float,
) -> float:
    """Calculate annual AI/automation operating cost."""
    return round(monthly_operating_cost * 12, 2)


def calculate_total_first_year_cost(
    implementation_cost: float,
    annual_operating_cost: float,
) -> float:
    """Calculate total first-year AI/automation cost."""
    return round(
        implementation_cost + annual_operating_cost,
        2,
    )

def calculate_annual_savings(
    current_annual_cost: float,
    annual_operating_cost: float,
) -> float:
    """Calculate annual savings after automation."""
    return round(
        current_annual_cost - annual_operating_cost,
        2,
    )


def calculate_net_benefit(
    annual_savings: float,
    implementation_cost: float,
) -> float:
    """Calculate first-year net financial benefit."""
    return round(
        annual_savings - implementation_cost,
        2,
    )