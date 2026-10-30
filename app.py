import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="John Ashley Loquillano | Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# PERSONAL DETAILS
# Edit the placeholder values below to match your details.
# ---------------------------------------------------------
NAME = "John Ashley G. Loquillano"
PROGRAM = "Bachelor of Science in Information Technology"
UNIVERSITY = "Cebu Institute of Technology - University"
SECTION = "CSIT 349(G01)"
EMAIL = "loquillanjohnashley3@gmail.com"
LOCATION = "Cebu, Philippines"

BIO = (
    "I am an Information Technology student at Cebu Institute of Technology - "
    "University. I enjoy learning how technology can solve practical problems "
    "and turning ideas into working applications. I am curious, collaborative, "
    "and hungry for improvement."
)

INTERESTS = ["Volleyball", "Basketball", "Online games"]

# These are editable self-assessment values, not test results.
skills = {
    "Python": 65,
    "Java": 75,
    "JavaScript / React": 65,
    "HTML / CSS": 75,
    "SQL / Database concepts": 65,
    "Problem solving": 70,
}

projects = [
    {
        "title": "CIT-U OJT Management System",
        "role": "Company Portal developer",
        "tools": "React, Java, Spring Boot, MySQL",
        "description": (
            "A university OJT management system concept connecting students, "
            "partner companies, and coordinators. My assigned work focuses on "
            "the Company Portal, including company profiles, verification, "
            "internship listings, applicant review, slots, messages, and certificates."
        ),
        "outcome": "A modular company-side workflow for managing internship opportunities and applicants.",
    },
    {
        "title": "Happy Meal - OOP2 Game",
        "role": "Java application developer",
        "tools": "Java, Java Swing, Object-Oriented Programming",
        "description": (
            "A desktop game project built around a tournament experience, "
            "with player setup, game modes, character selection, and gameplay "
            "mechanics."
        ),
        "outcome": "A Java Swing game prototype demonstrating OOP concepts and interactive screens.",
    },
    {
        "title": "LegacySupply Integration",
        "role": "Backend integration developer",
        "tools": "Java, Spring Boot, REST API, Postman, XML",
        "description": (
            "A modular-monolith integration lab connecting an inventory and "
            "ordering workflow to an external supplier API through an "
            "Anti-Corruption Layer."
        ),
        "outcome": "An integration workflow designed to keep external supplier formats separate from internal modules.",
    },
]

# ---------------------------------------------------------
# LIGHT THEME STYLING
# ---------------------------------------------------------
CSS = """
<style>
.stApp {
    background: #f7f9fc;
    color: #182230;
}
[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e7ebf2;
}
.hero {
    background: linear-gradient(135deg, #1d4ed8, #4f46e5);
    color: #ffffff;
    padding: 2.2rem 2.4rem;
    border-radius: 18px;
    margin-bottom: 1.5rem;
}
.hero h1 {
    margin: 0;
    padding: 0;
    color: #ffffff;
    font-size: 2.2rem;
}
.hero p {
    margin: 0.5rem 0 0 0;
    color: #e0e7ff;
    font-size: 1.05rem;
}
.card {
    background: #ffffff;
    border: 1px solid #e7ebf2;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
}
.card h4 {
    margin: 0 0 0.3rem 0;
    color: #182230;
}
.card .meta {
    color: #5b6678;
    font-size: 0.92rem;
    margin-bottom: 0.6rem;
}
.card p {
    color: #182230;
    margin: 0.4rem 0;
}
.chip {
    display: inline-block;
    background: #eef2ff;
    color: #3730a3;
    border-radius: 999px;
    padding: 0.25rem 0.8rem;
    margin: 0 0.4rem 0.4rem 0;
    font-size: 0.9rem;
}
.skill-row {
    margin-bottom: 0.9rem;
}
.skill-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.95rem;
    margin-bottom: 0.25rem;
}
.skill-track {
    background: #e7ebf2;
    border-radius: 999px;
    height: 10px;
    overflow: hidden;
}
.skill-fill {
    background: #4f46e5;
    height: 100%;
    border-radius: 999px;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(f"### {NAME}")
    st.caption(PROGRAM)
    st.caption(UNIVERSITY)
    st.divider()
    page = st.radio(
        "Go to",
        ["Home", "About", "Skills", "Projects", "Contact"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption(f"📍 {LOCATION}")


# ---------------------------------------------------------
# PAGE SECTIONS
# ---------------------------------------------------------
def render_hero():
    st.markdown(
        f"""
<div class="hero">
<h1>Hi, I'm {NAME} 👋</h1>
<p>{PROGRAM} · {UNIVERSITY}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def render_about():
    st.header("About me")
    st.write(BIO)
    st.subheader("Interests")
    chips = "".join(f'<span class="chip">{item}</span>' for item in INTERESTS)
    st.markdown(chips, unsafe_allow_html=True)

    st.subheader("Education")
    st.markdown(
        f"""
<div class="card">
<h4>{PROGRAM}</h4>
<div class="meta">{UNIVERSITY} · {SECTION}</div>
</div>
""",
        unsafe_allow_html=True,
    )


def render_skills():
    st.header("Skills")
    st.caption("Self-assessed levels out of 100. These are not test results.")

    left, right = st.columns([1, 1])

    with left:
        rows = ""
        for name, level in skills.items():
            rows += f"""
<div class="skill-row">
<div class="skill-label"><span>{name}</span><span>{level}%</span></div>
<div class="skill-track"><div class="skill-fill" style="width:{level}%"></div></div>
</div>
"""
        st.markdown(f'<div class="card">{rows}</div>', unsafe_allow_html=True)

    with right:
        df = pd.DataFrame(
            {"Skill": list(skills.keys()), "Level": list(skills.values())}
        ).set_index("Skill")
        st.bar_chart(df, horizontal=True)

    average = int(np.mean(list(skills.values())))
    strongest = max(skills, key=skills.get)
    c1, c2 = st.columns(2)
    c1.metric("Average level", f"{average}%")
    c2.metric("Strongest skill", strongest)


def render_projects():
    st.header("Projects")
    for project in projects:
        st.markdown(
            f"""
<div class="card">
<h4>{project['title']}</h4>
<div class="meta">{project['role']} · {project['tools']}</div>
<p>{project['description']}</p>
<p><strong>Outcome:</strong> {project['outcome']}</p>
</div>
""",
            unsafe_allow_html=True,
        )


def render_contact():
    st.header("Contact")
    st.markdown(
        f"""
<div class="card">
<h4>{NAME}</h4>
<div class="meta">{PROGRAM}</div>
<p><strong>Email:</strong> {EMAIL}</p>
<p><strong>Location:</strong> {LOCATION}</p>
<p><strong>Section:</strong> {SECTION}</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.subheader("Send me a message")
    with st.form("contact_form", clear_on_submit=True):
        sender = st.text_input("Your name")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send message")
    if submitted:
        if sender.strip() and message.strip():
            st.success(f"Thanks, {sender}! Your message was received.")
        else:
            st.warning("Please enter your name and a message.")


# ---------------------------------------------------------
# ROUTING
# ---------------------------------------------------------
if page == "Home":
    render_hero()
    render_about()
    render_skills()
    render_projects()
    render_contact()
elif page == "About":
    render_about()
elif page == "Skills":
    render_skills()
elif page == "Projects":
    render_projects()
elif page == "Contact":
    render_contact()