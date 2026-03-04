import streamlit as st
import pandas as pd
import plotly.express as px
import networkx as nx

# PDF generation
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# Temporary files
import tempfile

# Chart generation for PDF
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Governance Intelligence Platform", layout="wide")

# ---------------- CUSTOM STYLE ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
}

[data-testid="stSidebar"] {
    background-color:#111c24;
}

h1,h2,h3 {
    color:#F0F2F6;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("AI Governance Intelligence Platform")

st.caption(
"Integrated AI Governance Platform based on **India AI Governance Framework, "
"NIST AI Risk Management Framework, and Unified Control Framework**"
)

st.write("""
This platform demonstrates how organizations can design and implement a **comprehensive AI governance system**.

The objective of this project is to build an **integrated AI governance playbook** that combines:

• **India AI Governance Framework** – ethical and regulatory guidelines  
• **NIST AI Risk Management Framework** – structured risk management lifecycle  
• **Unified Control Framework (UCF)** – enterprise governance controls  

Together they form a **complete governance architecture for responsible AI deployment**.
""")

# ---------------- SESSION STATE ----------------

if "systems" not in st.session_state:
    st.session_state.systems = []

systems = st.session_state.systems

# ---------------- SIDEBAR NAVIGATION ----------------

st.sidebar.title("Platform Modules")

modules = [
"Governance Dashboard",
"AI System Assessment",
"Risk Register",
"Governance Lifecycle",
"Responsible AI Principles",
"Governance Control Library",
"Framework Comparison",
"Integrated Governance Playbook",
"AI Governance Stress Testing",
"AI Governance Roadmap",
"Governance KPI Monitor",
"AI Incident Response",
"AI Deployment Compliance Gates",
"AI Risk Matrix",
"Responsible AI Checklist",
"Cross Framework Mapping",       
"Governance Analytics Center",    
"Executive Governance Summary", 
"AI Governance Scorecard",
"Governance Maturity Radar",
"Framework Control Mapping",
"AI Governance Policies",
"AI Governance Architecture",
"AI Risk Heatmap",
"Governance Reporting",
]

if "page" not in st.session_state:
    st.session_state.page = modules[0]

for m in modules:
    if st.sidebar.button(m):
        st.session_state.page = m

page = st.session_state.page


# =====================================================
# GOVERNANCE DASHBOARD
# =====================================================

if page == "Governance Dashboard":

    st.header("AI Governance Analytics Dashboard")

    st.write("""
The **Governance Dashboard** provides a centralized overview of the organization's AI ecosystem.

It enables governance teams to monitor:

• Total AI systems under governance  
• Risk classification distribution  
• Sector-wise AI adoption  
• Deployment lifecycle visibility  
• Overall governance maturity
""")

    systems = st.session_state.systems

    st.subheader("Governance Overview")

    total = len(systems)

    high = len([s for s in systems if s["risk"] == "High Risk"])
    medium = len([s for s in systems if s["risk"] == "Medium Risk"])
    low = len([s for s in systems if s["risk"] == "Low Risk"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total AI Systems", total)
    c2.metric("High Risk Systems", high)
    c3.metric("Medium Risk Systems", medium)
    c4.metric("Low Risk Systems", low)

    # ---------------------------------------------------

    if total > 0:

        df = pd.DataFrame(systems)

        # Risk Distribution
        st.subheader("AI Risk Distribution")

        fig1 = px.pie(
            df,
            names="risk",
            title="AI Risk Classification Distribution"
        )

        st.plotly_chart(fig1, width="stretch")

        # Sector Distribution
        st.subheader("Sector Adoption of AI Systems")

        fig2 = px.histogram(
            df,
            x="sector",
            title="AI Systems Across Industry Sectors",
            color="sector"
        )

        st.plotly_chart(fig2, width="stretch")

        # Deployment Stage
        st.subheader("AI Deployment Lifecycle")

        if "deployment" in df.columns:

            fig3 = px.bar(
                df,
                x="deployment",
                title="AI Systems by Deployment Stage",
                color="deployment"
            )

            st.plotly_chart(fig3, width="stretch")

        # Governance Risk Exposure
        st.subheader("Governance Risk Exposure")

        avg_score = sum([s["score"] for s in systems]) / total

        st.metric(
            "Average Risk Exposure Score",
            round(avg_score, 2)
        )

        # Governance Maturity
        st.subheader("AI Governance Maturity Index")

        maturity = min(100, 35 + total * 7)

        st.progress(maturity)

        st.write(f"Current Governance Maturity Score: **{maturity}%**")

        if maturity < 50:

            st.warning("Governance maturity is still developing.")

        elif maturity < 80:

            st.info("Governance program is moderately developed.")

        else:

            st.success("Governance maturity is strong.")

        # Governance Alerts
        st.subheader("Governance Alerts")

        if high > 0:

            st.error(f"{high} high-risk AI systems require immediate governance attention.")

        elif medium > 0:

            st.warning("Some AI systems require governance monitoring.")

        else:

            st.success("No critical governance issues detected.")

    else:

        st.info("No AI systems registered yet. Run assessments to populate governance analytics.")


# =====================================================
# AI SYSTEM GOVERNANCE RISK ASSESSMENT
# =====================================================


elif page == "AI System Assessment":

    st.header("AI System Governance Risk Assessment")

    st.write("""
This module evaluates the **governance risk profile of an individual AI system**.

The assessment analyzes several governance factors including:

• Sector risk exposure  
• Data sensitivity level  
• Automation capability  
• Deployment maturity  

These indicators help determine whether an AI system falls under **low, medium or high governance risk categories**.
""")

    # ---------------------------------------------------
    # INPUT SECTION
    # ---------------------------------------------------

    st.subheader("AI System Details")

    system_name = st.text_input("AI System Name")

    owner = st.text_input("System Owner")

    sector = st.selectbox(
        "Sector",
        ["Healthcare","Finance","Education","Retail","Manufacturing","Government"]
    )

    data = st.selectbox(
        "Data Sensitivity",
        ["Public Data","Internal Data","Personal Data","Sensitive Personal Data"]
    )

    automation = st.selectbox(
        "Automation Level",
        ["Decision Support","Human-in-the-loop","Fully Autonomous"]
    )

    deployment = st.selectbox(
        "Deployment Stage",
        ["Development","Testing","Production"]
    )

    run = st.button("Run Governance Assessment")

    # ---------------------------------------------------
    # RISK CALCULATION
    # ---------------------------------------------------

    if run:

        # Sector scoring
        sector_scores = {
            "Healthcare":3,
            "Finance":3,
            "Government":3,
            "Education":2,
            "Retail":2,
            "Manufacturing":1
        }

        sector_score = sector_scores[sector]

        # Data scoring
        data_scores = {
            "Public Data":1,
            "Internal Data":2,
            "Personal Data":3,
            "Sensitive Personal Data":4
        }

        data_score = data_scores[data]

        # Automation scoring
        auto_scores = {
            "Decision Support":1,
            "Human-in-the-loop":2,
            "Fully Autonomous":3
        }

        auto_score = auto_scores[automation]

        # Deployment scoring
        deploy_scores = {
            "Development":1,
            "Testing":2,
            "Production":3
        }

        deploy_score = deploy_scores[deployment]

        # Final risk score
        risk_score = sector_score + data_score + auto_score + deploy_score

        # ---------------------------------------------------
        # RISK CLASSIFICATION
        # ---------------------------------------------------

        if risk_score >= 10:
            risk_level = "High Risk"

        elif risk_score >= 7:
            risk_level = "Medium Risk"

        else:
            risk_level = "Low Risk"

        # Governance audit score
        audit_score = 100 - (risk_score * 5)

        # ---------------------------------------------------
        # RESULTS
        # ---------------------------------------------------

        st.success("Assessment Complete")

        # =====================================================
        # SAVE SYSTEM FOR DASHBOARD
        # =====================================================

        system_record = {
            "name": system_name,
            "owner": owner,
            "sector": sector,
            "risk": risk_level,
            "score": risk_score,
            "deployment": deployment
        }

        st.session_state.systems.append(system_record)

        # ---------------------------------------------------
        # METRICS
        # ---------------------------------------------------

        c1,c2,c3 = st.columns(3)

        c1.metric("Risk Score",risk_score)
        c2.metric("Risk Classification",risk_level)
        c3.metric("Governance Audit Score",audit_score)

        # ---------------------------------------------------
        # SYSTEM GOVERNANCE SUMMARY
        # ---------------------------------------------------

        st.subheader("System Governance Summary")

        summary = pd.DataFrame({

            "Attribute":[
                "System Name",
                "System Owner",
                "Sector",
                "Data Sensitivity",
                "Automation Level",
                "Deployment Stage",
                "Risk Classification"
            ],

            "Value":[
                system_name,
                owner,
                sector,
                data,
                automation,
                deployment,
                risk_level
            ]

        })

        st.table(summary)

        # ---------------------------------------------------
        # FRAMEWORK ALIGNMENT
        # ---------------------------------------------------

        st.subheader("Framework Governance Alignment")

        framework = pd.DataFrame({

        "Framework":[
        "India AI Governance Framework",
        "NIST AI Risk Management Framework",
        "Unified Control Framework"
        ],

        "Relevant Governance Requirement":[
        "Responsible AI deployment and societal impact monitoring",
        "Risk identification and risk management lifecycle",
        "Enterprise governance controls and compliance monitoring"
        ]

        })

        st.table(framework)

        # ---------------------------------------------------
        # GOVERNANCE RECOMMENDATIONS
        # ---------------------------------------------------

        st.subheader("Governance Recommendations")

        if risk_level == "High Risk":

            st.error("High Governance Risk AI System")

            st.write("""
Recommended governance actions:

• Conduct bias and fairness testing  
• Implement human oversight mechanisms  
• Perform regulatory compliance assessment  
• Deploy continuous model monitoring  
• Maintain model documentation and audit logs
""")

        elif risk_level == "Medium Risk":

            st.warning("Moderate Governance Risk")

            st.write("""
Recommended governance actions:

• Establish monitoring controls  
• Improve model transparency documentation  
• Conduct periodic AI governance reviews
""")

        else:

            st.success("Low Governance Risk")

            st.write("""
Recommended governance actions:

• Maintain documentation  
• Conduct periodic governance monitoring
""")

# =====================================================
# RISK REGISTER
# =====================================================

elif page == "Risk Register":

    st.header("AI Governance Risk Register")

    st.write("""
The risk register stores **all evaluated AI systems** along with their governance risk levels.
It acts as a **central repository for governance monitoring**.
""")

    if systems:

        df=pd.DataFrame(systems)

        st.dataframe(df)

        st.download_button(
            "Download Governance Report",
            df.to_csv(index=False),
            "ai_governance_report.csv"
        )

    else:
        st.info("No AI systems recorded.")


# =====================================================
# GOVERNANCE LIFECYCLE
# =====================================================

elif page == "Governance Lifecycle":

    st.header("AI Risk Management Lifecycle")

    st.write("""
The **AI Risk Management Lifecycle** describes the structured process used by organizations
to manage risks associated with artificial intelligence systems throughout their lifecycle.

This lifecycle approach is aligned with **NIST AI Risk Management Framework** principles and
ensures that AI systems are designed, deployed, and monitored responsibly.

The lifecycle consists of five major stages.
""")

    lifecycle = pd.DataFrame({
        "Stage":[
            "Identify",
            "Assess",
            "Evaluate",
            "Mitigate",
            "Monitor"
        ],

        "Description":[
            "Identify AI systems, stakeholders, operational environment, and potential societal impacts",
            "Assess potential ethical, technical, operational, and regulatory risks",
            "Evaluate system fairness, reliability, transparency, and security",
            "Implement governance safeguards and risk mitigation strategies",
            "Continuously monitor AI performance, compliance, and emerging risks"
        ]
    })

    st.dataframe(lifecycle)

    st.subheader("Lifecycle Explanation")

    st.markdown("""
**1. Identify**

Organizations must identify all AI systems being developed or deployed.  
This includes defining the **system purpose, stakeholders, operational environment,
and potential societal impacts**.

**2. Assess**

Once AI systems are identified, organizations must analyze potential risks including:

• algorithmic bias  
• privacy risks  
• operational failures  
• cybersecurity threats  
• regulatory non-compliance

**3. Evaluate**

Technical evaluation of AI models is performed to ensure:

• fairness across demographic groups  
• robustness against adversarial attacks  
• explainability of model decisions  
• reliability of outputs

**4. Mitigate**

Risk mitigation strategies are implemented including:

• bias mitigation techniques  
• model validation procedures  
• human oversight mechanisms  
• governance control implementation

**5. Monitor**

AI systems must be continuously monitored after deployment to detect:

• model drift  
• performance degradation  
• ethical risks  
• compliance violations
""")


# =====================================================
# RESPONSIBLE AI PRINCIPLES
# =====================================================

elif page == "Responsible AI Principles":

    st.header("Responsible AI Principles")

    st.write("""
Responsible AI ensures that artificial intelligence systems are designed,
developed, and deployed in a manner that is **ethical, transparent,
and aligned with societal values**.

These principles guide organizations in building trustworthy AI systems.
""")

    principles = {
        "Human Centricity":
        "AI systems must prioritize human welfare and ensure that technology benefits society while minimizing harm.",

        "Transparency":
        "AI decisions should be explainable and understandable to stakeholders to maintain trust.",

        "Fairness":
        "AI models must avoid discriminatory outcomes and ensure equal treatment across demographic groups.",

        "Privacy Protection":
        "Personal data used by AI systems must be protected through secure data governance and privacy-preserving techniques.",

        "Security":
        "AI systems must be resilient to cyber threats and adversarial attacks.",

        "Accountability":
        "Organizations must take responsibility for AI decisions and maintain governance oversight.",

        "Reliability":
        "AI systems should operate consistently and produce accurate outputs across different scenarios.",

        "Continuous Monitoring":
        "AI models must be monitored after deployment to detect risks, failures, and unintended consequences."
    }

    for p,desc in principles.items():

        st.subheader(p)

        st.write(desc)

        st.markdown("---")

# =====================================================
# CONTROL LIBRARY
# =====================================================

# =====================================================
# AI GOVERNANCE CONTROL LIBRARY
# =====================================================

elif page == "Governance Control Library":

    st.header("AI Governance Control Library")

    st.write("""
The **AI Governance Control Library** defines the organizational safeguards required
to manage risks associated with AI systems.

The controls listed below are aligned with:

• **India AI Governance Framework**  
• **NIST AI Risk Management Framework (RMF)**  
• **Unified Control Framework (UCF)**  

Together these controls provide a **structured governance architecture for responsible AI deployment**.
""")

    # -------------------------------------------------
    # CONTROL LIBRARY DATA
    # -------------------------------------------------

    control_data = {

        "Control ID":[
            "AIGC-01",
            "AIGC-02",
            "AIGC-03",
            "AIGC-04",
            "AIGC-05",
            "AIGC-06",
            "AIGC-07",
            "AIGC-08"
        ],

        "Control":[
            "AI Governance Policy Framework",
            "AI Risk Assessment Procedure",
            "Algorithmic Bias Testing",
            "Data Governance Controls",
            "Model Performance Monitoring",
            "AI Incident Response Plan",
            "AI Security Hardening",
            "Audit Logging and Traceability"
        ],

        "Category":[
            "Governance",
            "Risk Management",
            "Ethical AI",
            "Data Governance",
            "Monitoring",
            "Operational Risk",
            "Security",
            "Accountability"
        ],

        "Framework Alignment":[
            "India AI + NIST Govern + UCF",
            "NIST Measure + Manage",
            "India AI Ethical Principles",
            "UCF Data Governance",
            "NIST Manage",
            "NIST Respond",
            "UCF Security Controls",
            "India AI Accountability"
        ],

        "Description":[
            "Defines enterprise level policies governing responsible AI development and usage.",
            "Standardized methodology for identifying, assessing, and mitigating AI risks.",
            "Testing procedures to detect unfair bias or discrimination in AI models.",
            "Controls ensuring high quality, secure, and compliant data usage.",
            "Continuous monitoring of AI model performance and drift detection.",
            "Operational procedures for responding to AI incidents and failures.",
            "Security safeguards protecting AI models from adversarial attacks.",
            "Maintains transparency through detailed logging and audit trails."
        ],

        "Maturity Level":[
            "Advanced",
            "Advanced",
            "Intermediate",
            "Advanced",
            "Intermediate",
            "Intermediate",
            "Advanced",
            "Advanced"
        ]

    }

    df = pd.DataFrame(control_data)

    # -------------------------------------------------
    # DISPLAY CONTROL LIBRARY
    # -------------------------------------------------

    st.subheader("Enterprise AI Governance Control Catalogue")

    st.dataframe(df, width='stretch')

    # -------------------------------------------------
    # CONTROL CATEGORY VISUALIZATION
    # -------------------------------------------------

    st.subheader("Control Distribution by Governance Domain")

    fig = px.histogram(
        df,
        x="Category",
        title="AI Governance Control Coverage",
        color="Category"
    )

    st.plotly_chart(fig, width='stretch')

    # -------------------------------------------------
    # MATURITY VISUALIZATION
    # -------------------------------------------------

    st.subheader("Control Maturity Distribution")

    maturity_chart = px.pie(
        df,
        names="Maturity Level",
        title="AI Governance Control Maturity"
    )

    st.plotly_chart(maturity_chart, width='stretch')

    # -------------------------------------------------
    # CONTROL EXPLANATION SECTION
    # -------------------------------------------------

    st.subheader("Control Implementation Guidance")

    selected_control = st.selectbox(
        "Select Control for Detailed Explanation",
        df["Control"]
    )

    control_info = df[df["Control"] == selected_control].iloc[0]

    st.write("### Control Description")
    st.write(control_info["Description"])

    st.write("### Governance Category")
    st.write(control_info["Category"])

    st.write("### Framework Alignment")
    st.write(control_info["Framework Alignment"])

    st.write("### Control Maturity Level")
    st.write(control_info["Maturity Level"])

# =====================================================
# FRAMEWORK COMPARISON
# =====================================================

elif page == "Framework Comparison":

    st.header("AI Governance Framework Comparison")

    st.write("""
Organizations rely on multiple governance frameworks to manage AI risks effectively.

This module compares three major governance frameworks:

• **India AI Governance Framework**  
• **NIST AI Risk Management Framework (RMF)**  
• **Unified Control Framework (UCF)**  

Each framework provides a different perspective on responsible AI governance and risk management.
""")

    # -------------------------------------------------
    # FRAMEWORK COMPARISON DATA
    # -------------------------------------------------

    data = {

        "Governance Dimension":[
            "Governance Structure",
            "Risk Identification",
            "Risk Assessment",
            "Risk Mitigation",
            "Transparency",
            "Accountability",
            "Continuous Monitoring"
        ],

        "India AI Governance Framework":[
            "Government oversight and ethical AI guidelines",
            "Identification of AI risks and societal impacts",
            "Evaluation of deployment risks",
            "Responsible AI safeguards",
            "Transparency in automated decisions",
            "Regulatory accountability mechanisms",
            "Continuous regulatory monitoring"
        ],

        "NIST AI RMF":[
            "GOVERN function defining governance roles",
            "MAP function identifying AI risks",
            "MEASURE function evaluating risk severity",
            "MANAGE function implementing risk controls",
            "Explainability and transparency principles",
            "Organizational accountability",
            "Continuous monitoring of AI systems"
        ],

        "Unified Control Framework":[
            "Enterprise governance architecture",
            "Risk control identification",
            "Control evaluation procedures",
            "Implementation of governance safeguards",
            "Audit documentation and traceability",
            "Compliance accountability",
            "Continuous control monitoring"
        ]

    }

    df = pd.DataFrame(data)

    # -------------------------------------------------
    # DISPLAY COMPARISON TABLE
    # -------------------------------------------------

    st.subheader("Framework Comparison Table")

    st.dataframe(df, width='stretch')

    # -------------------------------------------------
    # FRAMEWORK CAPABILITY SCORES
    # -------------------------------------------------

    st.subheader("Framework Capability Analysis")

    score_data = pd.DataFrame({

        "Framework":[
            "India AI Framework",
            "NIST AI RMF",
            "Unified Control Framework"
        ],

        "Governance Strength":[85,90,88],
        "Risk Management":[80,95,90],
        "Operational Controls":[70,85,95],
        "Compliance":[88,85,92],
        "Monitoring":[75,90,88]

    })

    radar = px.line_polar(
        score_data.melt(id_vars="Framework"),
        r="value",
        theta="variable",
        color="Framework",
        line_close=True,
        title="Governance Capability Comparison"
    )

    radar.update_traces(fill="toself")

    st.plotly_chart(radar, width='stretch')

    # -------------------------------------------------
    # FRAMEWORK STRENGTHS
    # -------------------------------------------------

    st.subheader("Framework Strengths Analysis")

    framework = st.selectbox(
        "Select Framework for Detailed Analysis",
        [
            "India AI Governance Framework",
            "NIST AI RMF",
            "Unified Control Framework"
        ]
    )

    if framework == "India AI Governance Framework":

        st.write("""
### India AI Governance Framework

Strengths:

• Focus on **ethical AI and societal impact**  
• Strong emphasis on **transparency and accountability**  
• Supports **national AI policy alignment**  
• Encourages **responsible innovation and citizen protection**
""")

    elif framework == "NIST AI RMF":

        st.write("""
### NIST AI Risk Management Framework

Strengths:

• Provides a **structured lifecycle for AI risk management**  
• Strong emphasis on **risk measurement and monitoring**  
• Widely adopted across global enterprises  
• Supports **continuous governance processes**
""")

    else:

        st.write("""
### Unified Control Framework

Strengths:

• Integrates **multiple regulatory control frameworks**  
• Provides **enterprise-level governance controls**  
• Enables **standardized compliance monitoring**  
• Supports large-scale governance implementations
""")

    # -------------------------------------------------
    # FRAMEWORK VISUAL COMPARISON
    # -------------------------------------------------

    st.subheader("Framework Coverage Across Governance Domains")

    coverage = pd.DataFrame({

        "Framework":[
            "India AI Framework",
            "NIST AI RMF",
            "Unified Control Framework"
        ],

        "Policy":[90,80,85],
        "Risk":[80,95,90],
        "Controls":[70,85,95],
        "Transparency":[92,88,85],
        "Monitoring":[75,90,88]

    })

    heatmap = px.imshow(
        coverage.set_index("Framework"),
        text_auto=True,
        color_continuous_scale="Blues",
        title="AI Governance Framework Coverage"
    )

    st.plotly_chart(heatmap, width='stretch')


# =====================================================
# PLAYBOOK
# =====================================================

elif page == "Integrated Governance Playbook":

    st.header("Integrated AI Governance Playbook")

    st.write("""
The integrated governance playbook demonstrates how **India AI governance guidelines,
the NIST AI Risk Management Framework (RMF), and the Unified Control Framework (UCF)**
can be combined to create a unified governance architecture.

This integrated approach ensures that AI systems are:

• ethically designed  
• operationally reliable  
• compliant with regulatory expectations  
• continuously monitored after deployment
""")

    st.subheader("Integrated Governance Mapping")

    playbook = pd.DataFrame({

        "Governance Phase":[
        "AI System Identification",
        "Risk Mapping",
        "Risk Assessment",
        "Control Implementation",
        "Compliance Review",
        "Continuous Monitoring"
        ],

        "India Framework":[
        "Identify AI systems and societal context",
        "Recognize ethical and regulatory risks",
        "Evaluate AI impact on stakeholders",
        "Apply responsible AI safeguards",
        "Ensure regulatory compliance",
        "Monitor societal and economic impact"
        ],

        "NIST AI RMF":[
        "MAP – Understand AI context",
        "MAP – Identify risks",
        "MEASURE – Assess risk levels",
        "MANAGE – Implement mitigation",
        "GOVERN – Organizational oversight",
        "MANAGE – Continuous monitoring"
        ],

        "Unified Control Framework":[
        "AI asset inventory",
        "Risk control mapping",
        "Control evaluation",
        "Control implementation",
        "Compliance verification",
        "Continuous control monitoring"
        ]

    })

    st.dataframe(playbook)

    st.subheader("Integrated Governance Workflow")

    st.markdown("""
**Step 1 — AI System Identification**

Organizations must identify all AI systems in development or deployment,
including their intended use, stakeholders, and potential societal impact.

**Step 2 — Risk Mapping**

Potential risks are mapped using governance frameworks such as
ethical risks, operational risks, security risks, and compliance risks.

**Step 3 — Risk Assessment**

AI models are evaluated for bias, reliability, transparency, and security.

**Step 4 — Control Implementation**

Governance safeguards such as human oversight, bias mitigation,
and data governance policies are implemented.

**Step 5 — Compliance Verification**

Regulatory and internal governance requirements are verified before deployment.

**Step 6 — Continuous Monitoring**

AI systems are continuously monitored for performance degradation,
ethical risks, and regulatory compliance.
""")


# =====================================================
# STRESS TESTING
# =====================================================

elif page == "AI Governance Stress Testing":

    st.header("AI Governance Stress Testing Engine")

    st.write("""
This module simulates potential **AI failure scenarios** to evaluate
whether governance safeguards are sufficient.

Stress testing helps organizations understand how AI systems behave
under adverse conditions.
""")

    scenario = st.selectbox(
        "Select Stress Test Scenario",
        [
            "Algorithmic Bias",
            "Data Leakage",
            "Model Drift",
            "Adversarial Attack",
            "Incorrect Prediction"
        ]
    )

    if st.button("Run Stress Test"):

        if scenario == "Algorithmic Bias":

            st.error("Risk Type: Ethical Risk")

            st.write("Potential Impact:")

            st.write("• Discrimination in automated decisions")
            st.write("• Legal and regulatory consequences")
            st.write("• Loss of public trust")

            st.write("Recommended Governance Controls:")

            st.write("• Bias testing and fairness metrics")
            st.write("• Dataset auditing")
            st.write("• Human oversight mechanisms")

        elif scenario == "Data Leakage":

            st.error("Risk Type: Privacy Risk")

            st.write("Potential Impact:")

            st.write("• Exposure of sensitive personal data")
            st.write("• Regulatory penalties")
            st.write("• Reputation damage")

            st.write("Recommended Governance Controls:")

            st.write("• Data encryption")
            st.write("• Access control policies")
            st.write("• Privacy impact assessments")

        elif scenario == "Model Drift":

            st.warning("Risk Type: Operational Risk")

            st.write("Potential Impact:")

            st.write("• Reduced prediction accuracy")
            st.write("• Operational disruption")
            st.write("• Incorrect decisions")

            st.write("Recommended Governance Controls:")

            st.write("• Continuous model monitoring")
            st.write("• Model retraining")
            st.write("• Performance evaluation")

        elif scenario == "Adversarial Attack":

            st.error("Risk Type: Security Risk")

            st.write("Potential Impact:")

            st.write("• Manipulated AI outputs")
            st.write("• System compromise")
            st.write("• Security vulnerabilities")

            st.write("Recommended Governance Controls:")

            st.write("• Adversarial robustness testing")
            st.write("• AI security audits")
            st.write("• Cybersecurity safeguards")

        elif scenario == "Incorrect Prediction":

            st.warning("Risk Type: Reliability Risk")

            st.write("Potential Impact:")

            st.write("• Financial losses")
            st.write("• Incorrect decision outcomes")
            st.write("• Customer dissatisfaction")

            st.write("Recommended Governance Controls:")

            st.write("• Model validation")
            st.write("• Human review processes")
            st.write("• Performance monitoring")


# =====================================================
# AI GOVERNANCE IMPLEMENTATION ROADMAP
# =====================================================

if page == "AI Governance Roadmap":

    st.header("AI Governance Implementation Roadmap")

    st.write("""
This module presents a **structured multi-phase roadmap** for implementing an 
enterprise-grade AI governance program.

The roadmap aligns with:

• India AI Governance Framework  
• NIST AI Risk Management Framework (AI RMF)  
• Unified Control Framework (UCF)

The goal is to guide organizations through a **governance maturity journey**
from initial governance setup to advanced AI risk oversight.
""")

    # --------------------------------------------
    # ROADMAP DATA
    # --------------------------------------------

    roadmap = [
        ["Phase 1", "Establish AI Governance Committee", "Critical", "Day 7"],
        ["Phase 1", "Appoint Chief AI Risk Officer (CARO)", "Critical", "Day 14"],
        ["Phase 1", "Define Responsible AI Governance Charter", "High", "Day 21"],

        ["Phase 2", "Create AI System Inventory", "Critical", "Day 45"],
        ["Phase 2", "Implement AI Risk Classification Framework", "High", "Day 60"],

        ["Phase 3", "Deploy Model Monitoring Infrastructure", "High", "Month 4"],
        ["Phase 3", "Implement Bias & Fairness Evaluation Framework", "High", "Month 5"],

        ["Phase 4", "Automate AI Incident Response Procedures", "Medium", "Month 7"],
        ["Phase 4", "Implement Continuous Compliance Monitoring", "Medium", "Month 8"],

        ["Phase 5", "Enterprise AI Governance Optimization Program", "Low", "Month 12"]
    ]

    df = pd.DataFrame(
        roadmap,
        columns=["Phase", "Action Item", "Priority", "Timeline"]
    )

    st.subheader("Governance Implementation Plan")

    st.dataframe(df, width="stretch")

    # --------------------------------------------
    # TIMELINE CONVERSION
    # --------------------------------------------

    timeline_days = {
        "Day 7":7,
        "Day 14":14,
        "Day 21":21,
        "Day 45":45,
        "Day 60":60,
        "Month 4":120,
        "Month 5":150,
        "Month 7":210,
        "Month 8":240,
        "Month 12":365
    }

    df["Implementation Day"] = df["Timeline"].map(timeline_days)

    # --------------------------------------------
    # TIMELINE VISUALIZATION
    # --------------------------------------------

    st.subheader("Governance Implementation Timeline")

    fig = px.bar(
        df,
        x="Implementation Day",
        y="Action Item",
        orientation="h",
        color="Priority",
        title="AI Governance Roadmap Timeline"
    )

    fig.update_layout(
        xaxis_title="Implementation Timeline (Days)",
        yaxis_title="Governance Activities",
        height=500
    )

    st.plotly_chart(fig, width="stretch")

    # --------------------------------------------
    # PRIORITY DISTRIBUTION
    # --------------------------------------------

    st.subheader("Governance Action Priority Distribution")

    fig2 = px.pie(
        df,
        names="Priority",
        title="Distribution of Governance Action Priorities"
    )

    st.plotly_chart(fig2, width="stretch")

    # --------------------------------------------
    # PHASE PROGRESS TRACKER
    # --------------------------------------------

    st.subheader("Governance Implementation Progress")

    progress = {
        "Phase 1 – Governance Setup":80,
        "Phase 2 – Risk Management":60,
        "Phase 3 – Monitoring Systems":40,
        "Phase 4 – Operational Automation":25,
        "Phase 5 – Governance Optimization":10
    }

    for phase,value in progress.items():

        st.write(f"**{phase}**")

        st.progress(value/100)

    # --------------------------------------------
    # ROADMAP SUMMARY
    # --------------------------------------------

    st.subheader("Roadmap Summary")

    st.info("""
The AI Governance roadmap provides a **step-by-step strategic plan** to help
organizations gradually build mature AI governance capabilities.

Early phases focus on **governance structure and risk classification**, while
later phases emphasize **monitoring, compliance automation, and enterprise
optimization**.
""")

# =====================================================
# GOVERNANCE KPI MONITOR
# =====================================================

if page == "Governance KPI Monitor":

    st.header("AI Governance KPI Monitoring")

    st.write("""
This module tracks **key performance indicators (KPIs)** used to evaluate 
the effectiveness of an organization's AI governance program.

The KPIs are derived from:
• NIST AI RMF MEASURE Function  
• India AI Governance Assurance Metrics  
• UCF Monitoring Controls
""")

    kpis = {
        "Safety Compliance Rate": 98.7,
        "Bias Detection Rate": 96.2,
        "Model Explainability Score": 91.5,
        "Security Incident Detection": 97.3,
        "Privacy Compliance Score": 94.6,
        "Operational Stability": 95.8
    }

    cols = st.columns(3)

    for i,(k,v) in enumerate(kpis.items()):
        cols[i%3].metric(k, f"{v}%")

    df = pd.DataFrame({
        "Metric": list(kpis.keys()),
        "Score": list(kpis.values())
    })

    fig = px.bar(
        df,
        x="Metric",
        y="Score",
        title="AI Governance KPI Performance",
        color="Score"
    )

    st.plotly_chart(fig, width="stretch")

    fig2 = px.line(
        df,
        x="Metric",
        y="Score",
        title="Governance Performance Trend"
    )

    st.plotly_chart(fig2, width="stretch")


# =====================================================
# AI INCIDENT RESPONSE
# =====================================================

if page == "AI Incident Response":

    st.header("AI Incident Response Playbook")

    st.write("""
This module defines the **AI incident management process** for handling 
AI system failures, ethical violations, or security breaches.

The workflow aligns with:
• CERT-In reporting guidelines
• NIST AI RMF MANAGE function
• Enterprise AI risk escalation protocols
""")

    response_steps = [
        ["Detection", "AI monitoring system detects anomaly"],
        ["Triage", "Security team assesses severity"],
        ["Containment", "Model or system access temporarily restricted"],
        ["Investigation", "Root cause analysis performed"],
        ["Remediation", "Corrective fixes applied"],
        ["Reporting", "Regulatory reporting (CERT-In if required)"],
        ["Recovery", "System restored and monitoring increased"]
    ]

    df = pd.DataFrame(response_steps, columns=["Stage","Description"])

    st.dataframe(df, use_container_width=True)

    fig = px.funnel(
        df,
        x="Stage",
        y=[1,1,1,1,1,1,1],
        title="AI Incident Response Workflow"
    )

    st.plotly_chart(fig, width="stretch")

    st.warning("Critical AI incidents must be reported to regulatory authorities within defined timeframes.")


# =====================================================
# AI DEPLOYMENT COMPLIANCE GATES
# =====================================================

# =====================================================
# AI DEPLOYMENT COMPLIANCE GATES
# =====================================================

if page == "AI Deployment Compliance Gates":

    st.header("AI Deployment Compliance Gates")

    st.write("""
Before any AI system is deployed to production, it must pass a **structured
governance compliance evaluation**.

This evaluation ensures the AI system satisfies requirements across:

• Safety  
• Security  
• Privacy  
• Fairness  
• Performance  

The checks align with the **India AI Governance Framework, NIST AI RMF,
and Unified Control Framework (UCF)**.
""")

    # -----------------------------------------
    # SAFETY CHECKS
    # -----------------------------------------

    st.subheader("Gate 1: Safety Evaluation")

    safety_checks = {
        "Harmful Content Generation Testing": True,
        "Jailbreak Resistance Evaluation": True,
        "Edge Case Stress Testing": True,
        "Human Oversight Enabled": True,
        "Model Output Validation": True,
        "Tool Misuse Prevention": False
    }

    safety_df = pd.DataFrame(
        list(safety_checks.items()),
        columns=["Safety Check", "Status"]
    )

    st.dataframe(safety_df, width="stretch")

    # -----------------------------------------
    # SECURITY CHECKS
    # -----------------------------------------

    st.subheader("Gate 2: Security Evaluation")

    security_checks = {
        "Model Access Control Implemented": True,
        "API Authentication Enabled": True,
        "Adversarial Testing Completed": True,
        "Prompt Injection Protection": True,
        "Data Encryption Implemented": True,
        "Secrets Management Configured": True,
        "Security Logging Enabled": False
    }

    security_df = pd.DataFrame(
        list(security_checks.items()),
        columns=["Security Check", "Status"]
    )

    st.dataframe(security_df, width="stretch")

    # -----------------------------------------
    # PRIVACY CHECKS
    # -----------------------------------------

    st.subheader("Gate 3: Privacy Evaluation")

    privacy_checks = {
        "Data Minimization Applied": True,
        "PII Detection Implemented": True,
        "Consent Mechanisms Enabled": False,
        "Data Retention Policies Defined": True,
        "Privacy Impact Assessment Completed": True,
        "User Data Anonymization": True
    }

    privacy_df = pd.DataFrame(
        list(privacy_checks.items()),
        columns=["Privacy Check", "Status"]
    )

    st.dataframe(privacy_df, width="stretch")

    # -----------------------------------------
    # FAIRNESS CHECKS
    # -----------------------------------------

    st.subheader("Gate 4: Fairness & Bias Evaluation")

    fairness_checks = {
        "Bias Detection Testing": True,
        "Demographic Bias Analysis": True,
        "Fairness Metrics Evaluation": True,
        "Model Explainability Assessment": True,
        "Fairness Documentation": False,
        "Independent Audit Review": False
    }

    fairness_df = pd.DataFrame(
        list(fairness_checks.items()),
        columns=["Fairness Check", "Status"]
    )

    st.dataframe(fairness_df, width="stretch")

    # -----------------------------------------
    # PERFORMANCE CHECKS
    # -----------------------------------------

    st.subheader("Gate 5: Performance Evaluation")

    performance_checks = {
        "Accuracy Benchmark Validation": True,
        "Latency Performance Testing": True,
        "System Load Testing": True,
        "Failure Recovery Testing": True,
        "Monitoring Metrics Configured": True,
        "Model Drift Detection": False
    }

    performance_df = pd.DataFrame(
        list(performance_checks.items()),
        columns=["Performance Check", "Status"]
    )

    st.dataframe(performance_df, width="stretch")

    # -----------------------------------------
    # COMBINED COMPLIANCE ANALYSIS
    # -----------------------------------------

    all_checks = (
        list(safety_checks.values())
        + list(security_checks.values())
        + list(privacy_checks.values())
        + list(fairness_checks.values())
        + list(performance_checks.values())
    )

    passed = sum(all_checks)
    total = len(all_checks)

    score = round((passed/total)*100,2)

    st.subheader("AI Deployment Readiness Score")

    st.metric("Compliance Score", f"{score}%")

    # -----------------------------------------
    # DECISION ENGINE
    # -----------------------------------------

    if score >= 90:
        st.success("AI System Approved for Deployment")

    elif score >= 70:
        st.warning("Conditional Approval — Governance improvements required")

    else:
        st.error("Deployment Blocked — Compliance requirements not met")

    # -----------------------------------------
    # VISUALIZATION
    # -----------------------------------------

    st.subheader("Compliance Gate Performance")

    categories = [
        "Safety",
        "Security",
        "Privacy",
        "Fairness",
        "Performance"
    ]

    scores = [
        sum(safety_checks.values())/len(safety_checks)*100,
        sum(security_checks.values())/len(security_checks)*100,
        sum(privacy_checks.values())/len(privacy_checks)*100,
        sum(fairness_checks.values())/len(fairness_checks)*100,
        sum(performance_checks.values())/len(performance_checks)*100
    ]

    chart_df = pd.DataFrame({
        "Category": categories,
        "Score": scores
    })

    fig = px.bar(
        chart_df,
        x="Category",
        y="Score",
        color="Score",
        title="Compliance Gate Evaluation Scores"
    )

    st.plotly_chart(fig, width="stretch")


# =====================================================
# RISK MATRIX
# =====================================================

elif page == "AI Risk Matrix":

    st.header("AI Risk Matrix (Impact vs Likelihood)")

    st.write("""
The **AI Risk Matrix** is a governance tool used to prioritize AI risks
based on two critical dimensions:

• **Impact** – the severity of consequences if the AI failure occurs  
• **Likelihood** – the probability that the risk will occur

This approach is widely used in **enterprise risk management frameworks**
including NIST AI RMF and ISO risk assessment methodologies.

The purpose of this matrix is to help organizations determine
**which AI risks require stronger governance controls**.
""")

    impact = st.selectbox(
        "Select Impact Level",
        ["Low","Medium","High"]
    )

    likelihood = st.selectbox(
        "Select Likelihood Level",
        ["Low","Medium","High"]
    )

    if st.button("Evaluate Risk"):

        if impact == "High" and likelihood == "High":
            risk = "Critical Risk"

        elif impact == "High" and likelihood == "Medium":
            risk = "High Risk"

        elif impact == "Medium" and likelihood == "High":
            risk = "High Risk"

        elif impact == "Medium" and likelihood == "Medium":
            risk = "Medium Risk"

        else:
            risk = "Low Risk"

        st.subheader("Risk Evaluation Result")

        st.write(f"Impact Level: **{impact}**")
        st.write(f"Likelihood Level: **{likelihood}**")

        if risk == "Critical Risk":

            st.error("""
Critical Risk – Immediate governance intervention required.

Recommended actions:

• immediate mitigation measures  
• executive governance oversight  
• deployment suspension if required  
• regulatory compliance verification
""")

        elif risk == "High Risk":

            st.warning("""
High Risk – Strong governance controls required.

Recommended actions:

• enhanced model validation  
• bias testing procedures  
• increased monitoring frequency
""")

        elif risk == "Medium Risk":

            st.info("""
Medium Risk – Monitoring and mitigation required.

Recommended actions:

• periodic model review  
• governance documentation  
• operational monitoring
""")

        else:

            st.success("""
Low Risk – Standard governance controls sufficient.

Recommended actions:

• standard monitoring  
• documentation maintenance
""")


# =====================================================
# RESPONSIBLE AI CHECKLIST
# =====================================================

elif page == "Responsible AI Checklist":

    st.header("Responsible AI Governance Checklist")

    st.write("""
This checklist helps organizations verify whether key **Responsible AI
governance safeguards** are implemented before deploying AI systems.

The checklist aligns with **ethical AI guidelines, NIST AI RMF,
and enterprise governance frameworks**.
""")

    bias = st.checkbox("Bias testing performed")
    transparency = st.checkbox("Transparency documentation available")
    privacy = st.checkbox("Privacy protection implemented")
    security = st.checkbox("Security safeguards implemented")
    oversight = st.checkbox("Human oversight enabled")

    score = sum([bias,transparency,privacy,security,oversight]) * 20

    st.progress(score/100)

    st.subheader(f"Compliance Score: {score}%")

    if score >= 80:
        st.success("Strong responsible AI governance readiness")

    elif score >= 60:
        st.warning("Moderate governance readiness – improvements recommended")

    else:
        st.error("Low governance readiness – significant controls missing")

    st.markdown("""
**Checklist Explanation**

• Bias testing ensures AI models do not produce discriminatory outcomes  
• Transparency documentation explains how AI decisions are generated  
• Privacy protection safeguards sensitive user data  
• Security safeguards protect AI systems against cyber threats  
• Human oversight ensures that automated decisions can be reviewed
""")

# =====================================================
# CROSS FRAMEWORK MAPPING
# =====================================================

elif page == "Cross Framework Mapping":

    st.header("AI Governance Cross-Framework Mapping")

    st.write("""
This module demonstrates **integration between major AI governance frameworks**.

It maps:

• India AI Governance Principles  
• NIST AI Risk Management Framework functions  
• Unified Control Framework controls

This ensures organizations maintain **alignment across multiple governance standards simultaneously**.
""")

    mapping_data = {

        "India Principle":[
            "Human Centric AI",
            "Safety and Reliability",
            "Privacy Protection",
            "Transparency",
            "Accountability"
        ],

        "NIST RMF Function":[
            "Govern",
            "Measure",
            "Manage",
            "Map",
            "Govern"
        ],

        "UCF Control":[
            "UCF-AI-001",
            "UCF-AI-014",
            "UCF-AI-022",
            "UCF-AI-031",
            "UCF-AI-045"
        ]

    }

    df = pd.DataFrame(mapping_data)

    st.dataframe(df,width='stretch')

    st.subheader("Framework Integration Visualization")

    fig = px.parallel_categories(
        df,
        dimensions=[
            "India Principle",
            "NIST RMF Function",
            "UCF Control"
        ],
        title="Cross Framework Governance Alignment"
    )

    st.plotly_chart(fig,width='stretch')

# =====================================================
# GOVERNANCE ANALYTICS CENTER
# =====================================================

elif page == "Governance Analytics Center":

    st.header("AI Governance Analytics Center")

    st.write("""
This analytics center provides **advanced governance intelligence insights** across the AI ecosystem.

It helps governance teams monitor:

• Risk exposure trends  
• Sector adoption patterns  
• Governance maturity distribution  
• AI trustworthiness indicators
""")

    if systems:

        df = pd.DataFrame(systems)

        st.subheader("AI Systems by Sector")

        fig_sector = px.bar(
            df,
            x="sector",
            color="risk",
            title="Sector Level AI Risk Distribution"
        )

        st.plotly_chart(fig_sector,width='stretch')

        st.subheader("Risk Exposure Distribution")

        fig_risk = px.histogram(
            df,
            x="score",
            nbins=10,
            title="AI Risk Exposure Distribution"
        )

        st.plotly_chart(fig_risk,width='stretch')

        st.subheader("AI Governance Trustworthiness Radar")

        trust_data = pd.DataFrame({
            "Dimension":[
                "Safety",
                "Security",
                "Privacy",
                "Transparency",
                "Accountability",
                "Fairness",
                "Reliability"
            ],
            "Score":[
                80,
                75,
                70,
                65,
                78,
                72,
                76
            ]
        })

        radar = px.line_polar(
            trust_data,
            r="Score",
            theta="Dimension",
            line_close=True,
            title="AI Trustworthiness Assessment"
        )

        radar.update_traces(fill="toself")

        st.plotly_chart(radar,width='stretch')

    else:

        st.info("No AI systems available for analytics.")

# =====================================================
# EXECUTIVE GOVERNANCE SUMMARY
# =====================================================

elif page == "Executive Governance Summary":

    st.header("Executive AI Governance Summary")

    st.write("""
This executive dashboard provides a **strategic overview of the organization's AI governance posture**.

It summarizes:

• AI system deployment  
• Governance risk exposure  
• Compliance readiness  
• Governance maturity level  
• Sector level AI adoption
""")

    if systems:

        df = pd.DataFrame(systems)

        total_systems = len(df)
        high_risk = len(df[df["risk"] == "High Risk"])
        medium_risk = len(df[df["risk"] == "Medium Risk"])
        low_risk = len(df[df["risk"] == "Low Risk"])

        col1,col2,col3,col4 = st.columns(4)

        col1.metric("Total AI Systems",total_systems)
        col2.metric("High Risk Systems",high_risk)
        col3.metric("Medium Risk Systems",medium_risk)
        col4.metric("Low Risk Systems",low_risk)

        st.subheader("AI Risk Distribution")

        fig = px.pie(
            df,
            names="risk",
            title="Enterprise AI Risk Profile",
            color="risk",
            color_discrete_map={
                "High Risk":"red",
                "Medium Risk":"orange",
                "Low Risk":"green"
            }
        )

        st.plotly_chart(fig,width='stretch')

        st.subheader("Sector Level AI Adoption")

        sector_fig = px.histogram(
            df,
            x="sector",
            color="risk",
            title="AI Systems by Industry Sector"
        )

        st.plotly_chart(sector_fig,width='stretch')

        avg_score = df["score"].mean()

        st.metric("Average Risk Exposure", round(avg_score,2))

        maturity = min(100,40 + total_systems*7)

        st.subheader("Governance Maturity Index")

        st.progress(maturity)

        st.write(f"Overall Governance Maturity: **{maturity}%**")

    else:

        st.info("No AI systems registered yet.")


# =====================================================
# SCORECARD
# =====================================================

elif page == "AI Governance Scorecard":

    st.header("AI Governance Scorecard")

    st.write("""
The **AI Governance Scorecard** measures the maturity of governance
controls across key responsible AI dimensions.

This evaluation framework helps organizations assess
their governance readiness across multiple domains.
""")

    transparency = st.slider("Transparency",0,100,70)
    fairness = st.slider("Fairness",0,100,75)
    security = st.slider("Security",0,100,80)
    compliance = st.slider("Compliance",0,100,85)

    overall = (transparency + fairness + security + compliance)/4

    st.subheader("Overall Governance Score")

    st.metric("Governance Score",round(overall,1))

    if overall > 80:

        st.success("""
Governance maturity is strong.
The organization demonstrates robust governance safeguards
and responsible AI practices.
""")

    elif overall > 60:

        st.warning("""
Governance maturity is moderate.
Certain governance areas require improvement.
""")

    else:

        st.error("""
Governance maturity is weak.
Significant improvements in governance controls are required.
""")


# =====================================================
# RADAR
# =====================================================

elif page == "Governance Maturity Radar":

    st.header("AI Governance Maturity Radar")

    st.write("""
The **AI Governance Maturity Radar** provides a visual representation of an organization's
capability to manage and govern artificial intelligence systems responsibly.

The radar model evaluates maturity across five critical governance domains that are
aligned with global governance frameworks such as the **NIST AI Risk Management Framework**
and enterprise governance best practices.

These domains represent the key building blocks of responsible AI governance.
""")

    st.subheader("Governance Domains Evaluated")

    st.markdown("""
**1. Governance**

Represents the presence of formal policies, governance structures,
and leadership oversight for AI systems.

Organizations with strong governance ensure accountability,
clear decision-making processes, and regulatory alignment.

**2. Risk Management**

Measures how effectively organizations identify, assess,
and mitigate risks associated with AI systems.

This includes ethical risks, operational risks,
security threats, and compliance risks.

**3. Data Governance**

Evaluates how well organizations manage AI training data,
including data quality, privacy protection,
and regulatory compliance.

Proper data governance is essential for trustworthy AI.

**4. Model Validation**

Measures the robustness and reliability of AI models.

This includes fairness testing, bias detection,
model accuracy validation, and explainability.

**5. Continuous Monitoring**

Assesses the organization's ability to monitor AI systems
after deployment to detect model drift, failures,
and emerging risks.
""")

    st.subheader("Evaluate Governance Maturity")

    governance = st.slider("Governance Maturity",0,100,80)
    risk = st.slider("Risk Management Maturity",0,100,70)
    data = st.slider("Data Governance Maturity",0,100,75)
    validation = st.slider("Model Validation Maturity",0,100,65)
    monitoring = st.slider("Monitoring Capability",0,100,85)

    radar_data = pd.DataFrame({
        "Dimension":[
            "Governance",
            "Risk Management",
            "Data Governance",
            "Model Validation",
            "Monitoring"
        ],
        "Score":[
            governance,
            risk,
            data,
            validation,
            monitoring
        ]
    })

    fig = px.line_polar(
        radar_data,
        r="Score",
        theta="Dimension",
        line_close=True,
        range_r=[0,100]
    )

    fig.update_traces(fill='toself')

    st.plotly_chart(fig, use_container_width=True)

    overall_maturity = (
        governance + risk + data + validation + monitoring
    ) / 5

    st.subheader("Overall Governance Maturity Score")

    st.metric("Maturity Score", round(overall_maturity,1))

    if overall_maturity > 80:

        st.success("""
Governance maturity is **advanced**.

The organization demonstrates strong governance structures,
risk management capabilities, and continuous monitoring of AI systems.
""")

    elif overall_maturity > 60:

        st.warning("""
Governance maturity is **developing**.

The organization has implemented several governance mechanisms,
but additional improvements are needed in certain domains.
""")

    else:

        st.error("""
Governance maturity is **early stage**.

The organization should establish stronger governance policies,
risk management processes, and monitoring mechanisms.
""")


# =====================================================
# AI GOVERNANCE CONTROL MAPPING
# =====================================================

elif page == "Framework Control Mapping":

    st.header("AI Governance Control Mapping")

    st.write("""
AI governance frameworks provide structured guidance for managing risks associated with
artificial intelligence systems. However, organizations often struggle to integrate multiple
governance standards into a unified governance program.

This module demonstrates how **three major AI governance frameworks** can be aligned:

• **India AI Governance Framework** – focuses on ethical, societal, and regulatory responsibility  
• **NIST AI Risk Management Framework (AI RMF)** – provides a structured lifecycle for AI risk management  
• **Unified Control Framework (UCF)** – defines enterprise governance controls for operational implementation  

By mapping these frameworks together, organizations can create a **comprehensive AI governance playbook**
that ensures regulatory compliance, operational accountability, and responsible AI deployment.
""")

    st.subheader("Framework Alignment Matrix")

    mapping = pd.DataFrame({

        "Governance Activity":[
        "AI System Identification",
        "Risk Mapping",
        "Risk Assessment",
        "Control Implementation",
        "Compliance Monitoring"
        ],

        "India AI Governance Framework":[
        "Identify AI systems, their operational context, and societal impact",
        "Recognize ethical, legal, and regulatory risks associated with AI deployment",
        "Evaluate potential impacts of AI systems on individuals, organizations, and society",
        "Apply responsible AI principles including fairness, transparency, and accountability",
        "Monitor societal impact and regulatory compliance of AI systems"
        ],

        "NIST AI RMF":[
        "MAP – Understand AI system purpose, context, and stakeholders",
        "MAP – Identify potential risks across the AI lifecycle",
        "MEASURE – Assess reliability, bias, security, and performance risks",
        "MANAGE – Implement mitigation strategies and governance controls",
        "MANAGE – Continuous monitoring and risk reassessment"
        ],

        "Unified Control Framework":[
        "AI asset identification and system documentation",
        "Risk control mapping and governance planning",
        "Control evaluation and risk scoring",
        "Implementation of enterprise governance controls",
        "Continuous control monitoring and audit reporting"
        ]
    })

    st.dataframe(mapping)

    st.write("""
This integrated mapping helps organizations translate **high-level governance principles into
practical enterprise controls**, ensuring that AI systems remain compliant, transparent,
and aligned with global governance standards.
""")

# =====================================================
# AI GOVERNANCE POLICY FRAMEWORK
# =====================================================

elif page == "AI Governance Policies":

    st.header("AI Governance Policy Framework")

    st.write("""
AI governance policies define the **organizational rules, principles, and operational standards**
that guide the responsible design, development, deployment, and monitoring of artificial intelligence systems.

These policies ensure that AI systems operate within **ethical, legal, and operational boundaries**
while minimizing risks related to bias, privacy violations, security breaches, and regulatory non-compliance.

A comprehensive AI governance policy framework typically includes multiple policy domains
covering data management, model risk management, ethical AI principles, and security governance.
""")

    st.subheader("Core AI Governance Policies")

    policies = pd.DataFrame({

        "Policy":[
        "Responsible AI Policy",
        "Data Governance Policy",
        "Model Risk Management Policy",
        "AI Security Policy",
        "AI Audit & Compliance Policy"
        ],

        "Description":[
        "Defines ethical principles such as fairness, transparency, accountability, and human oversight in AI systems.",
        "Establishes rules for data collection, storage, access, quality management, and privacy protection.",
        "Provides governance procedures for model development, validation, monitoring, and risk assessment.",
        "Protects AI systems against cyber threats, adversarial attacks, and unauthorized system access.",
        "Ensures regulatory compliance through documentation, internal audits, and external regulatory reporting."
        ],

        "Governance Objective":[
        "Ensure ethical and socially responsible AI usage",
        "Protect sensitive personal and organizational data",
        "Manage risks associated with machine learning models",
        "Maintain security and system resilience",
        "Ensure transparency and regulatory compliance"
        ]
    })

    st.dataframe(policies)

    st.subheader("Why AI Governance Policies Are Important")

    st.write("""
AI governance policies form the **foundation of enterprise AI governance programs**.

They help organizations:

• Ensure compliance with emerging **AI regulations and ethical standards**  
• Establish **clear accountability and governance responsibilities**  
• Protect **user privacy and sensitive organizational data**  
• Reduce risks associated with **biased or unreliable AI models**  
• Maintain **trust and transparency with stakeholders**

Strong governance policies enable organizations to deploy AI systems responsibly
while maintaining operational efficiency and regulatory readiness.
""")

# =====================================================
# AI GOVERNANCE ARCHITECTURE
# =====================================================


elif page == "AI Governance Architecture":

    st.header("AI Governance System Architecture")

    st.write("""
The **AI Governance System Architecture** illustrates how governance mechanisms
interact across the AI lifecycle.

This architecture integrates governance principles from:

• **India AI Governance Framework**  
• **NIST AI Risk Management Framework (RMF)**  
• **Unified Control Framework (UCF)**  

The architecture ensures that AI systems remain **transparent, accountable,
secure, and compliant throughout their lifecycle**.
""")


    # --------------------------------------------------
    # CREATE GOVERNANCE GRAPH
    # --------------------------------------------------

    G = nx.DiGraph()

    nodes = [

        "AI Systems",

        "Risk Assessment",

        "Governance Controls",

        "Compliance Gates",

        "Monitoring & KPIs",

        "Incident Response",

        "Governance Reporting"

    ]

    G.add_nodes_from(nodes)

    edges = [

        ("AI Systems","Risk Assessment"),

        ("Risk Assessment","Governance Controls"),

        ("Governance Controls","Compliance Gates"),

        ("Compliance Gates","Monitoring & KPIs"),

        ("Monitoring & KPIs","Incident Response"),

        ("Incident Response","Governance Reporting")

    ]

    G.add_edges_from(edges)

    # --------------------------------------------------
    # LAYERED ARCHITECTURE LAYOUT
    # --------------------------------------------------

    pos = {

        "AI Systems":(0,0),

        "Risk Assessment":(2,1),

        "Governance Controls":(4,2),

        "Compliance Gates":(6,2),

        "Monitoring & KPIs":(8,1),

        "Incident Response":(6,0),

        "Governance Reporting":(4,-1)

    }

    # --------------------------------------------------
    # DRAW ARCHITECTURE
    # --------------------------------------------------

    fig, ax = plt.subplots(figsize=(12,7))

    # Draw nodes
    nx.draw_networkx_nodes(

        G,
        pos,
        node_size=4200,
        node_color="#6bb3d6",
        edgecolors="black"

    )

    # Draw labels
    nx.draw_networkx_labels(

        G,
        pos,
        font_size=11,
        font_weight="bold"

    )

    # Draw edges
    nx.draw_networkx_edges(

        G,
        pos,
        arrowstyle="->",
        arrowsize=22,
        width=2

    )

    ax.set_title(
        "Enterprise AI Governance Lifecycle Architecture",
        fontsize=14,
        fontweight="bold"
    )

    ax.axis("off")

    st.pyplot(fig)

    # --------------------------------------------------
    # GOVERNANCE LAYERS EXPLANATION
    # --------------------------------------------------

    st.subheader("Governance Architecture Layers")

    st.write("""
The architecture is organized into **three major governance layers**:

### 1️⃣ AI Operational Layer
This layer contains the **AI systems deployed within the organization**.

• Machine learning models  
• Decision automation systems  
• AI analytics platforms  

These systems generate outputs that must be monitored and governed.

---

### 2️⃣ AI Governance Control Layer
This layer implements governance safeguards:

• **Risk Assessment** – evaluates AI risks including bias, security vulnerabilities, and operational impact.  
• **Governance Controls** – implements safeguards such as fairness testing, explainability, and policy enforcement.  
• **Compliance Gates** – ensures that AI deployments meet regulatory and organizational requirements before release.

---

### 3️⃣ Governance Oversight Layer
This layer provides continuous monitoring and oversight:

• **Monitoring & KPIs** – tracks AI performance, drift, and governance metrics.  
• **Incident Response** – addresses AI failures, ethical violations, or security incidents.  
• **Governance Reporting** – generates reports for regulators, auditors, and executives.

Together these layers ensure **responsible AI lifecycle governance**.
""")

    # --------------------------------------------------
    # GOVERNANCE FLOW DESCRIPTION
    # --------------------------------------------------

    st.subheader("Governance Lifecycle Flow")

    st.write("""
The AI governance lifecycle follows a **continuous oversight loop**:

1️⃣ **AI Systems**  
AI applications operate in production environments.

2️⃣ **Risk Assessment**  
Risks related to bias, privacy, security, and reliability are evaluated.

3️⃣ **Governance Controls**  
Policies, safeguards, and monitoring mechanisms are implemented.

4️⃣ **Compliance Gates**  
AI systems undergo regulatory and governance validation before deployment.

5️⃣ **Monitoring & KPIs**  
Continuous monitoring ensures AI systems remain compliant and performant.

6️⃣ **Incident Response**  
Governance teams respond to AI incidents or unexpected outcomes.

7️⃣ **Governance Reporting**  
Insights and compliance reports are generated for management and regulators.

This lifecycle ensures **continuous governance of AI systems**.
""")

# =====================================================
# AI GOVERNANCE RISK HEATMAP
# =====================================================

elif page == "AI Risk Heatmap":

    st.header("AI Governance Risk Heatmap")

    st.write("""
The **AI Governance Risk Heatmap** visualizes AI risks based on their **likelihood of occurrence**
and **potential organizational impact**.

This tool helps governance teams:

• Prioritize high-risk AI issues  
• Identify areas requiring stronger governance controls  
• Support risk mitigation decisions  

The heatmap follows a **5×5 risk matrix commonly used in enterprise risk management**.
""")

    # --------------------------------------------------
    # SAMPLE AI RISK DATA
    # --------------------------------------------------

    risk_data = pd.DataFrame({

        "Risk":[
            "Algorithmic Bias",
            "Data Privacy Violation",
            "Model Drift",
            "Adversarial Attack",
            "Regulatory Non-Compliance",
            "Explainability Failure",
            "Operational AI Failure",
            "Data Quality Issues"
        ],

        "Likelihood":[
            4,
            3,
            4,
            2,
            3,
            2,
            3,
            4
        ],

        "Impact":[
            5,
            5,
            3,
            4,
            5,
            3,
            4,
            3
        ]

    })

    # --------------------------------------------------
    # CALCULATE RISK SCORE
    # --------------------------------------------------

    risk_data["Risk Score"] = risk_data["Likelihood"] * risk_data["Impact"]

    # --------------------------------------------------
    # CLASSIFY RISK LEVEL
    # --------------------------------------------------

    def classify_risk(score):

        if score >= 20:
            return "Critical"

        elif score >= 12:
            return "High"

        elif score >= 6:
            return "Medium"

        else:
            return "Low"

    risk_data["Risk Level"] = risk_data["Risk Score"].apply(classify_risk)

    # --------------------------------------------------
    # DISPLAY RISK TABLE
    # --------------------------------------------------

    st.subheader("AI Risk Register")

    st.dataframe(risk_data, width='stretch')

    # --------------------------------------------------
    # CREATE HEATMAP SCATTER PLOT
    # --------------------------------------------------

    st.subheader("AI Risk Matrix Visualization")

    fig = px.scatter(

        risk_data,

        x="Likelihood",
        y="Impact",
        text="Risk",
        color="Risk Level",
        size="Risk Score",

        title="AI Governance Risk Matrix",

        color_discrete_map={

            "Low":"green",
            "Medium":"yellow",
            "High":"orange",
            "Critical":"red"

        }

    )

    fig.update_traces(

        textposition="top center"

    )

    fig.update_layout(

        xaxis=dict(

            title="Likelihood",
            range=[0,5],
            dtick=1

        ),

        yaxis=dict(

            title="Impact",
            range=[0,5],
            dtick=1

        )

    )

    st.plotly_chart(fig, width='stretch')

    # --------------------------------------------------
    # RISK DISTRIBUTION ANALYSIS
    # --------------------------------------------------

    st.subheader("Risk Distribution by Severity")

    severity_chart = px.histogram(

        risk_data,

        x="Risk Level",
        color="Risk Level",
        title="AI Risk Severity Distribution",

        color_discrete_map={

            "Low":"green",
            "Medium":"yellow",
            "High":"orange",
            "Critical":"red"

        }

    )

    st.plotly_chart(severity_chart, width='stretch')

    # --------------------------------------------------
    # GOVERNANCE INTERPRETATION
    # --------------------------------------------------

    st.subheader("Risk Governance Interpretation")

    st.write("""

**Critical Risks (Red Zone)**  
Immediate governance intervention required.  
Examples include regulatory violations, severe bias issues, or security breaches.

**High Risks (Orange Zone)**  
Require mitigation planning and monitoring controls.

**Medium Risks (Yellow Zone)**  
Moderate risks requiring governance oversight.

**Low Risks (Green Zone)**  
Acceptable risks that can be monitored periodically.

""")

# =====================================================
# AI GOVERNANCE REPORTING
# =====================================================

elif page == "Governance Reporting":

    st.title("AI Governance Reporting")

    st.write("""
Governance reporting provides **visibility into AI system risks, performance, and compliance readiness across the organization.**

It allows organizations to monitor AI systems and generate governance reports for **internal stakeholders, auditors, and regulators**.
""")

    if systems:

        df = pd.DataFrame(systems)

        # ------------------------------
        # REPORTING DASHBOARD
        # ------------------------------

        st.header("Governance Reporting Dashboard")

        st.write("""
The table below displays all AI systems registered in the governance platform along with their attributes.
""")

        st.dataframe(df, use_container_width=True)

        # ------------------------------
        # METRICS SUMMARY
        # ------------------------------

        st.header("Governance Metrics Summary")

        total = len(df)
        high = len(df[df["risk"]=="High Risk"])
        medium = len(df[df["risk"]=="Medium Risk"])
        low = len(df[df["risk"]=="Low Risk"])

        c1,c2,c3,c4 = st.columns(4)

        c1.metric("Total AI Systems", total)
        c2.metric("High Risk Systems", high)
        c3.metric("Medium Risk Systems", medium)
        c4.metric("Low Risk Systems", low)

        # ------------------------------
        # RISK DISTRIBUTION
        # ------------------------------

        st.header("Risk Distribution")

        fig = px.pie(df, names="risk", title="AI Risk Distribution")
        st.plotly_chart(fig, use_container_width=True)

        # ------------------------------
        # SECTOR DISTRIBUTION
        # ------------------------------

        st.header("Sector Distribution")

        fig2 = px.bar(df, x="sector", title="AI Systems Across Sectors")
        st.plotly_chart(fig2, use_container_width=True)

        # ------------------------------
        # GOVERNANCE MATURITY
        # ------------------------------

        st.header("Governance Maturity")

        maturity = min(100, 40 + total*6)

        st.progress(maturity)

        st.write(f"Governance Maturity Score: **{maturity}%**")

        # ------------------------------
        # PDF EXPORT
        # ------------------------------

        st.header("Export Governance Report")

        if st.button("Generate Full Governance Report"):

            styles = getSampleStyleSheet()

            elements = []

            elements.append(Paragraph("AI Governance Intelligence Platform", styles["Title"]))
            elements.append(Spacer(1,20))

            elements.append(Paragraph(
                "This report summarizes the AI governance posture of the organization including system registry, risk distribution, and governance maturity.",
                styles["BodyText"]
            ))

            elements.append(Spacer(1,20))

            # -----------------------
            # SYSTEM TABLE
            # -----------------------

            table_data = [df.columns.tolist()] + df.values.tolist()

            table = Table(table_data)

            elements.append(Paragraph("AI Systems Registry", styles["Heading2"]))
            elements.append(table)

            elements.append(Spacer(1,20))

            # -----------------------
            # GOVERNANCE METRICS
            # -----------------------

            elements.append(Paragraph("Governance Metrics Summary", styles["Heading2"]))

            elements.append(Paragraph(f"Total AI Systems: {total}", styles["BodyText"]))
            elements.append(Paragraph(f"High Risk Systems: {high}", styles["BodyText"]))
            elements.append(Paragraph(f"Medium Risk Systems: {medium}", styles["BodyText"]))
            elements.append(Paragraph(f"Low Risk Systems: {low}", styles["BodyText"]))
            elements.append(Paragraph(f"Governance Maturity Score: {maturity}%", styles["BodyText"]))

            elements.append(Spacer(1,20))

            # -----------------------
            # RISK CHART (Matplotlib)
            # -----------------------

            risk_chart = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name

            risk_counts = df["risk"].value_counts()

            plt.figure()
            risk_counts.plot.pie(autopct='%1.0f%%')
            plt.title("Risk Distribution")
            plt.ylabel("")
            plt.savefig(risk_chart)
            plt.close()

            elements.append(Paragraph("Risk Distribution", styles["Heading2"]))
            elements.append(Image(risk_chart, 5*inch, 4*inch))

            elements.append(Spacer(1,20))

            # -----------------------
            # SECTOR CHART
            # -----------------------

            sector_chart = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name

            sector_counts = df["sector"].value_counts()

            plt.figure()
            sector_counts.plot(kind="bar")
            plt.title("AI Systems Across Sectors")
            plt.xlabel("Sector")
            plt.ylabel("Number of Systems")
            plt.savefig(sector_chart)
            plt.close()

            elements.append(Paragraph("Sector Distribution", styles["Heading2"]))
            elements.append(Image(sector_chart, 5*inch, 4*inch))

            # -----------------------
            # CREATE PDF
            # -----------------------

            pdf_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

            doc = SimpleDocTemplate(pdf_file.name, pagesize=letter)

            doc.build(elements)

            with open(pdf_file.name,"rb") as f:

                st.download_button(
                    label="Download AI Governance Report (PDF)",
                    data=f,
                    file_name="AI_Governance_Report.pdf",
                    mime="application/pdf"
                )

    else:

        st.info("No AI systems registered yet.")