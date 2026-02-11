import streamlit as st
from datetime import datetime


st.set_page_config(
    page_title="Derrick | Portfolio",
    page_icon="💼",
    layout="wide"
)


st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to:",
    ["Home", "About Me", "Skills", "Projects", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.info("BSIT Student | CyberSecurity 🚀")


if section == "Home":
    st.title("👋 Hello, I'm Derrick")
    st.subheader("Welcome to My Professional Portfolio")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://via.placeholder.com/300", caption="Your Photo Here")

    with col2:
        st.write("""
        I am a passionate BSIT student interested in:
        - Software Development
        - Quality Assurance Testing
        - Web Technologies
        - Automation & CI/CD
        """)

    st.metric("Projects Completed", "5+")
    st.metric("Technologies Learned", "8+")


elif section == "About Me":
    st.header("📌 About Me")

    st.write("""
    I am currently pursuing a Bachelor of Science in Information Technology.
    I enjoy building web applications and learning about software testing.
    """)

    st.progress(80)
    st.write("Continuous Learning Progress: 80% 🚀")


elif section == "Skills":
    st.header("💻 Technical Skills")

    python_level = st.slider("Python", 0, 100, 85)
    django_level = st.slider("Django", 0, 100, 75)
    testing_level = st.slider("Software Testing", 0, 100, 70)

    st.write("### Skill Overview")
    st.write(f"Python Skill Level: {python_level}%")
    st.write(f"Django Skill Level: {django_level}%")
    st.write(f"Software Testing Level: {testing_level}%")


elif section == "Projects":
    st.header("📁 My Projects")

    with st.expander("Student Attendance Dashboard"):
        st.write("Built using Django framework.")
        st.success("Status: Completed")

    with st.expander("Windows Server Domain Setup"):
        st.write("Configured Active Directory and domain networking.")
        st.success("Status: Completed")

    with st.expander("QA Documentation & Testing"):
        st.write("Created test cases, test plans, and defect reports.")
        st.success("Status: Completed")

elif section == "Contact":
    st.header("📬 Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        st.success("Message sent successfully! ✅")
        st.balloons()

st.markdown("---")
st.caption(f"© {datetime.now().year} Derrick | Built with Streamlit")

import streamlit as st

st.set_page_config(page_title="My Autobiography", page_icon="👋", layout="centered")

st.title("👋 Hello! I'm Derrick")

st.header("📌 About Me")
st.write("""
Hi! I am a BSIT student passionate about software development and quality assurance.
I enjoy learning Python, Django, and Web Development.
""")

st.header("🎓 Education")
st.write("- Bachelor of Science in Information Technology")
st.write("- Interested in Software Testing & QA")

st.header("💻 Skills")
st.write("✔ Python")
st.write("✔ Django")
st.write("✔ HTML/CSS")
st.write("✔ Git & GitHub")

st.header("📁 Projects")
st.write("1. Student Attendance Dashboard (Django)")
st.write("2. Domain Network Setup (Windows Server)")
st.write("3. QA Documentation and Testing Activities")

st.success("Thank you for visiting my portfolio! 🚀")
