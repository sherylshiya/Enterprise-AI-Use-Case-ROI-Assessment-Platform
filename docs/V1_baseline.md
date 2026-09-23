# V1 Baseline Evaluation

## Evaluation Date
2026-09-23

## Purpose

This evaluation establishes the first baseline output of the Enterprise AI Use-Case & ROI Assessment Platform using the initial deterministic scoring engine.

The purpose is to validate whether the scoring framework produces differentiated and interpretable results across representative business processes.

## Scoring Dimensions

The V1 engine evaluates:

- AI Readiness
- Automation Readiness
- Business Impact
- Risk
- Overall Opportunity

## Baseline Results

| Use Case | AI Readiness | Automation Readiness | Business Impact | Risk | Overall Opportunity | Classification |
|---|---:|---:|---:|---:|---:|---|
| Invoice Processing | 78.5 | 87.0 | 80.0 | 69.0 | 58.95 | Moderate |
| Resume Screening | 91.5 | 72.0 | 70.0 | 84.0 | 53.85 | Moderate |
| Customer Support | 95.0 | 81.0 | 85.0 | 69.0 | 63.90 | High |

## Initial Observations

### Invoice Processing
- High automation readiness.
- High business impact.
- Moderate risk.
- AI readiness is lower than Customer Support and Resume Screening.

### Resume Screening
- Very high AI readiness.
- High risk due to decision criticality, accuracy requirements, compliance sensitivity, and human oversight.
- Overall opportunity is reduced by the risk penalty.

### Customer Support
- Highest AI readiness among the three use cases.
- High automation readiness and business impact.
- Moderate risk.
- Highest overall opportunity score in the V1 baseline.

## V1 Status

This is the **initial baseline**, not the final calibrated scoring methodology.

Future iterations should compare their results against this baseline rather than replacing it.

## Next Validation

The next step is to evaluate whether these results are logically consistent with the intended business characteristics and determine whether the scoring weights, factor mappings, or thresholds require calibration.