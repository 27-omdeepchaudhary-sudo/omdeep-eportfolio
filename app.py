import streamlit as st
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Omdeep Chaudhary | E-Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .portfolio-name {
        font-size: 2.8rem;
        font-weight: 750;
        margin-bottom: 0.3rem;
    }

    .portfolio-subtitle {
        font-size: 1.25rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }

    .section-label {
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .project-card {
        padding: 1.6rem;
        border: 1px solid #dddddd;
        border-radius: 14px;
        margin-bottom: 1.2rem;
    }

    .featured-card {
        padding: 1.8rem;
        border: 2px solid #cccccc;
        border-radius: 16px;
        margin-bottom: 1.2rem;
    }

    .skill-tag {
        display: inline-block;
        padding: 0.45rem 0.8rem;
        margin: 0.25rem 0.2rem 0.25rem 0;
        border: 1px solid #d8d8d8;
        border-radius: 20px;
        font-size: 0.9rem;
    }

    .muted {
        color: #666666;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid #e5e5e5;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <div style="font-size:1.55rem; font-weight:750; line-height:1.15;">
        OMDEEP<br>CHAUDHARY
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.caption(
    "Operations | Process Improvement | Data Analytics"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "About",
        "Projects",
        "Experience",
        "Skills & Tools",
        "Certifications",
        "Achievements",
        "Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("New Delhi, India")


# =========================================================
# HOME
# =========================================================

if page == "Home":

    left, right = st.columns([1.65, 1], gap="large")

    with left:

        st.markdown(
            '<div class="portfolio-name">OMDEEP CHAUDHARY</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="portfolio-subtitle">'
            'Operations | Process Improvement | Data Analytics'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(
            "**PGDM Candidate | Operations Specialization | "
            "International Business Minor**"
        )

        st.write(
            "I am a PGDM candidate at Fortune Institute of International "
            "Business (FIIB), New Delhi, specializing in Operations with a "
            "minor in International Business. I have experience validating "
            "high-visibility election data at Kantar for Google’s Election "
            "Intelligence and leading a 2-member analyst team. I am skilled "
            "in data validation, process improvement, capacity analysis and "
            "data-driven decision-making, with working knowledge of MS Excel, "
            "Power BI and Python, along with Lean Six Sigma training. I am "
            "seeking an entry-level role in operations, supply chain, or "
            "business process improvement."
        )

        st.write("")

        button1, button2, button3 = st.columns(3)

        with button1:
            st.link_button(
                "GitHub",
                "https://github.com/27-omdeepchaudhary-sudo"
            )

        with button2:
            st.link_button(
                "LinkedIn",
                "https://www.linkedin.com/in/omdeep-chaudhary-8a8856373"
            )

        with button3:
            st.link_button(
                "Email",
                "mailto:27-omdeep.chaudhary@fiib.edu.in"
            )

    with right:

        photo_path = Path("assets/profile.jpg")

        if photo_path.exists():
            st.image(
                str(photo_path),
                width="stretch"
            )
        else:
            st.warning(
                "Profile photo not found. Please place profile.jpg "
                "inside the assets folder."
            )

    st.markdown("---")

    # -----------------------------------------------------
    # RESUME
    # -----------------------------------------------------

    st.header("Resume")

    st.write(
        "Upload your resume PDF below. After uploading, you can download "
        "the resume directly from the portfolio."
    )

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="resume_uploader"
    )

    if uploaded_resume is not None:

        st.success(
            f"Resume uploaded: {uploaded_resume.name}"
        )

        st.download_button(
            label="📄 Download Resume",
            data=uploaded_resume.getvalue(),
            file_name=uploaded_resume.name,
            mime="application/pdf",
            width="stretch"
        )

    else:
        st.info(
            "Upload your PDF resume to activate the Download Resume button."
        )

    st.markdown("---")

    # -----------------------------------------------------
    # CORE AREAS
    # -----------------------------------------------------

    st.header("Core Areas")

    areas = [
        "Operations Management",
        "Process Improvement",
        "Supply Chain",
        "Data Analytics"
    ]

    for area in areas:
        st.markdown(
            f'<span class="skill-tag">{area}</span>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -----------------------------------------------------
    # FEATURED PROJECT
    # -----------------------------------------------------

    st.header("Featured Project")

    st.markdown(
        """
        <div class="featured-card">
            <h3>AI Election Intelligence & Validation Dashboard</h3>
            <p><b>Kantar India</b></p>
            <p>
            Developed an AI-enabled election intelligence and validation
            solution focused on improving election-data reliability,
            monitoring and reporting. Worked on data validation,
            discrepancy identification, round-wise monitoring and
            dashboard-based visibility.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "View Project on GitHub →",
        "https://github.com/27-omdeepchaudhary-sudo/election-intelligence-dashboard"
    )


# =========================================================
# ABOUT
# =========================================================

elif page == "About":

    st.title("About Me")

    st.write(
        "I am an Operations-focused PGDM candidate interested in operations "
        "management, supply chain, process improvement and data-driven "
        "decision-making."
    )

    st.write(
        "My academic and professional experience has provided exposure to "
        "data validation, process analysis, dashboard development, "
        "root-cause analysis and structured process improvement."
    )

    st.write(
        "I am particularly interested in using analytical approaches and "
        "technology to understand operational problems, improve processes "
        "and support better business decisions."
    )

    st.markdown("---")

    st.header("Education")

    st.subheader("Fortune Institute of International Business (FIIB)")
    st.write("**PGDM | 2025–2027 | New Delhi**")
    st.write(
        "Specialization: Operations | Minor: International Business"
    )
    st.write("CGPA: **6.91**")

    st.subheader(
        "Raja Mahendra Pratap Singh State University"
    )
    st.write("**B.Sc. | 2021–2024 | Aligarh**")
    st.write("CGPA: **7.51**")


# =========================================================
# PROJECTS
# =========================================================

elif page == "Projects":

    st.title("Projects")

    st.caption(
        "Selected academic and professional work."
    )

    st.markdown("---")

    st.header("Featured Project")

    st.markdown(
        """
        <div class="featured-card">
            <h2>AI Election Intelligence & Validation Dashboard</h2>
            <p><b>Kantar India</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Developed an AI-enabled election intelligence and validation "
        "solution focused on improving election-data reliability, "
        "monitoring and reporting. Worked on data validation, discrepancy "
        "identification, round-wise monitoring and dashboard-based visibility."
    )

    st.subheader("My Contribution")

    st.markdown("""
    - Election data validation
    - Data-quality checks
    - Discrepancy identification
    - Round-wise monitoring
    - Dashboard development
    - Analyst/team coordination
    """)

    st.subheader("Tools")

    st.write(
        "Python • Pandas • SQLite • Streamlit"
    )

    st.link_button(
        "View Project on GitHub →",
        "https://github.com/27-omdeepchaudhary-sudo/election-intelligence-dashboard"
    )

    st.markdown("---")

    st.header("Additional Academic & Professional Work")

    st.markdown(
        """
        <div class="project-card">
            <h3>Kiran Auto Components — DMAIC / Six Sigma</h3>
            <p>
            Applied the DMAIC methodology to analyse a manufacturing
            process problem, identify root causes and develop improvement
            recommendations through structured process and data analysis.
            </p>
            <p>
            <b>Focus:</b> Six Sigma | Process Improvement |
            Root Cause Analysis | Data Analysis
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="project-card">
            <h3>CMP Redesign & Feedback Automation</h3>
            <p>
            Worked on redesigning the CMP mentoring workflow to address
            gaps in mentor–mentee feedback and process tracking, including
            workflow redesign, mapping, feedback mechanisms and
            dashboard-based monitoring.
            </p>
            <p>
            <b>Focus:</b> Project Management | Process Redesign |
            Dashboarding | Feedback Automation
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# EXPERIENCE
# =========================================================

elif page == "Experience":

    st.title("Experience")

    st.header("Kantar India")

    st.subheader("Research Analyst → Team Leader")
    st.caption("April 2026 – July 2026 | New Delhi")

    st.write(
        "Worked on live election-data validation by cross-checking "
        "Election Commission of India data with entered data and "
        "identifying discrepancies across election rounds."
    )

    st.write(
        "Progressed to Team Leader, coordinating a 2-member analyst team, "
        "reviewing validation work, assigning tasks and ensuring completion "
        "of multi-round validation activities."
    )

    st.markdown("---")

    st.header("Sakshi NGO")

    st.subheader("Survey / Field Data Work")
    st.caption("January 2026")

    st.write(
        "Worked on an UNSDG 5 household survey covering 200+ households "
        "and achieved 100% data accuracy. Managed case reporting over a "
        "10-day period while independently handling three concurrent "
        "field cases."
    )


# =========================================================
# SKILLS & TOOLS
# =========================================================

elif page == "Skills & Tools":

    st.title("Skills & Tools")

    left, right = st.columns(2, gap="large")

    with left:

        st.header("Skills")

        skills = [
            "Operations Management",
            "Supply Chain Management",
            "Process Improvement",
            "Root Cause Analysis",
            "Six Sigma Methodology",
            "Data Validation",
            "Process Analysis",
            "Data Presentation",
            "Data-Driven Decision Making",
            "Stakeholder Communication",
            "Team Coordination"
        ]

        for skill in skills:
            st.markdown(
                f'<span class="skill-tag">{skill}</span>',
                unsafe_allow_html=True
            )

    with right:

        st.header("Tools")

        tools = [
            "MS Excel",
            "Power BI",
            "Python",
            "RStudio",
            "Canva"
        ]

        for tool in tools:
            st.markdown(
                f'<span class="skill-tag">{tool}</span>',
                unsafe_allow_html=True
            )


# =========================================================
# CERTIFICATIONS
# =========================================================

elif page == "Certifications":

    st.title("Certifications")

    st.subheader("SQL for Data Science")

    st.write(
        "**University of California, Davis — Coursera**"
    )

    st.write(
        "Credential ID: **JLUN5EKWLSU6**"
    )

    st.link_button(
        "Verify Certificate →",
        "https://www.coursera.org/account/accomplishments/verify/JLUN5EKWLSU6"
    )

    st.markdown("---")

    st.subheader(
        "Lean Six Sigma Basics for Process Improvement"
    )
    st.write("EDUCBA / Coursera")

    st.subheader("Power BI Microsoft")
    st.write("LinkedIn Learning")

    st.subheader("Production Management")
    st.write("LinkedIn Learning")

    st.subheader("Supply Chain Management")
    st.write("LinkedIn Learning")

    st.subheader(
        "Data Visualization and Dashboards with Excel and Cognos"
    )
    st.write("IBM / Coursera")


# =========================================================
# ACHIEVEMENTS
# =========================================================

elif page == "Achievements":

    st.title("Achievements")

    st.header("Kantar India — Role Progression")

    st.write(
        "Progressed from Research Analyst to Team Leader, coordinating "
        "a 2-member analyst team."
    )

    st.markdown("---")

    st.header(
        "FIIB Rangbhoomi — Inter-Kabaddi Tournament"
    )

    st.write(
        "Won the tournament trophy as Vice Captain, contributing to "
        "match-day strategy for an 11-member team."
    )


# =========================================================
# CONTACT
# =========================================================

elif page == "Contact":

    st.title("Let's Connect")

    st.write(
        "I am open to opportunities in:"
    )

    st.markdown(
        "**Operations | Supply Chain | Business Process Improvement | "
        "Data Analytics**"
    )

    st.markdown("---")

    st.write(
        "📧 **Email:** 27-omdeep.chaudhary@fiib.edu.in"
    )

    st.write(
        "📱 **Phone:** +91 7300615359"
    )

    st.write(
        "📍 **Location:** New Delhi, India"
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.link_button(
            "Email Me",
            "mailto:27-omdeep.chaudhary@fiib.edu.in"
        )

    with col2:
        st.link_button(
            "LinkedIn",
            "https://www.linkedin.com/in/omdeep-chaudhary-8a8856373"
        )

    with col3:
        st.link_button(
            "GitHub",
            "https://github.com/27-omdeepchaudhary-sudo"
        )

    st.markdown("---")

    st.caption(
        "OMDEEP CHAUDHARY | Operations | Process Improvement | Data Analytics"
    )

    st.caption("© 2026 Omdeep Chaudhary")
