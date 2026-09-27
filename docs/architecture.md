                         ┌──────────────────────────┐
                         │        USER / CLIENT      │
                         │  Business Process Input   │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │      STREAMLIT UI         │
                         │  Process Assessment Form  │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                    ┌──────────────────────────────────┐
                    │       ASSESSMENT ENGINE           │
                    │                                  │
                    │  ┌────────────┐ ┌─────────────┐ │
                    │  │ Scoring    │ │ Applicability│ │
                    │  │ Engine     │ │ / AI Fit     │ │
                    │  └────────────┘ └─────────────┘ │
                    │          │             │         │
                    │          └──────┬──────┘         │
                    │                 ▼                │
                    │       Risk Assessment            │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │       OPPORTUNITY ASSESSMENT      │
                    │                                  │
                    │  AI Readiness                    │
                    │  Automation Readiness            │
                    │  Business Impact                 │
                    │  Risk                            │
                    │  Overall Opportunity Score       │
                    │  Automation Potential            │
                    └────────────────┬─────────────────┘
                                     │
                    ┌────────────────┴─────────────────┐
                    ▼                                  ▼
       ┌─────────────────────────┐       ┌─────────────────────────┐
       │   ECONOMICS ENGINE      │       │ ARCHITECTURE ENGINE     │
       │                         │       │                         │
       │ Current Cost            │       │ Architecture Selection  │
       │ Operating Cost          │       │ Component Selection     │
       │ Implementation Cost     │       │ Integration Requirements│
       │ Savings                 │       │ Human-in-the-Loop       │
       │ ROI                     │       │ Governance              │
       │ Payback                 │       └────────────┬────────────┘
       │ Scenario Analysis       │                    │
       │ Sensitivity Analysis    │                    │
       └────────────┬────────────┘                    │
                    │                                 │
                    └──────────────┬──────────────────┘
                                   ▼
                    ┌──────────────────────────────────┐
                    │       RECOMMENDATION ENGINE      │
                    │                                  │
                    │  Business Recommendation         │
                    │  Architecture Recommendation     │
                    │  Economic Recommendation         │
                    │  Risks / Constraints              │
                    │  Implementation Considerations   │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │        ASSESSMENT OUTPUT          │
                    │                                  │
                    │  Opportunity Score               │
                    │  ROI & Payback                   │
                    │  Scenarios                       │
                    │  Recommended Architecture        │
                    │  Risks & Governance              │
                    │  Human Oversight                 │
                    └──────────────────────────────────┘


Architecture boundaries:

                    ┌─────────────────────┐
                    │   Business Process  │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │  ASSESSMENT LAYER   │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │  ECONOMICS LAYER    │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ ARCHITECTURE LAYER  │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ RECOMMENDATION      │
                    │ LAYER               │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │   FINAL DECISION    │
                    └─────────────────────┘