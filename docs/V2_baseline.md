# V2 Baseline Evaluation

## Evaluation Date
2026-09-23

## Purpose

V2 calibrates the initial scoring framework based on the V1 evaluation of three representative enterprise use cases.

The objective was to place greater emphasis on business value and automation potential while maintaining risk as a penalty.

---

## V2 Scoring Methodology

### Overall Opportunity Score

The V2 formula is:

Overall Opportunity =
    AI Readiness × 25%
    + Automation Readiness × 25%
    + Business Impact × 35%
    - Risk × 15%

### Dimension Weights

| Dimension | V1 | V2 |
|---|---:|---:|
| AI Readiness | 30% | 25% |
| Automation Readiness | 20% | 25% |
| Business Impact | 30% | 35% |
| Risk Penalty | 20% | 15% |

V2 places greater emphasis on business impact and automation while reducing the relative contribution of AI readiness and risk.

---

## V2 Factor Mapping

Categorical factors use the following normalized scores:

| Level | Score |
|---|---:|
| Low | 20 |
| Medium | 50 |
| High | 80 |
| Very High | 100 |

Volume continues to use volume-specific thresholds based on monthly process volume.

---

## V2 Evaluation Results

| Use Case | AI Readiness | Automation Readiness | Business Impact | Risk | Overall Opportunity | Classification |
|---|---:|---:|---:|---:|---:|---|
| Invoice Processing | 74.5 | 87.0 | 80.0 | 69.0 | 58.02 | Moderate |
| Resume Screening | 90.5 | 70.0 | 70.0 | 69.0 | 54.27 | Moderate |
| Customer Support | 94.0 | 79.0 | 85.0 | 69.0 | 62.65 | High |

---

## Use-Case Observations

### Invoice Processing

- Highest Automation Readiness among the three use cases.
- Strong Business Impact.
- AI Readiness is lower than Resume Screening and Customer Support.
- Overall Opportunity: 58.02.

### Resume Screening

- Very high AI Readiness.
- Moderate Automation Readiness.
- Business Impact is moderate-high.
- Risk was reduced from the original sample because the AI system is intended to support recruiter screening rather than make the final hiring decision.
- Overall Opportunity: 54.27.

### Customer Support

- Highest AI Readiness.
- Highest Business Impact.
- High Automation Readiness.
- Moderate Risk.
- Highest Overall Opportunity among the three V2 cases: 62.65.

---

## V1 → V2 Comparison

| Use Case | V1 Overall | V2 Overall | Change |
|---|---:|---:|---:|
| Invoice Processing | 58.95 | 58.02 | -0.93 |
| Resume Screening | 53.85 | 54.27 | +0.42 |
| Customer Support | 63.90 | 62.65 | -1.25 |

The V2 changes produce relatively small changes in overall opportunity scores while shifting the weighting toward business impact and automation.

---

## V2 Findings

1. The framework differentiates AI suitability from overall business opportunity.
2. Customer Support has the highest overall opportunity due to its combination of AI readiness, automation potential, and business impact.
3. Invoice Processing has particularly strong automation potential.
4. Resume Screening has high AI readiness while retaining human oversight in the decision process.
5. All three use cases currently receive the same Risk score of 69. This indicates that the current risk framework has limited differentiation for these sample cases.
6. Risk-factor granularity may need further calibration in a future version.

---

## V2 Status

V2 is the current scoring baseline for the platform.

The methodology is considered sufficiently stable for the next development stage.

Further calibration should be driven by additional representative business cases rather than repeated adjustment of the three initial samples.

## Next Step

Proceed to the cost and ROI assessment layer while retaining V2 as the scoring baseline.