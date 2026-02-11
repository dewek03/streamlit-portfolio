import streamlit as st

st.set_page_config(page_title="My Autobiography", page_icon="👋", layout="centered")

st.title("👋 Hello! I'm Derrick Estopace")

st.header("📌 About Me")
st.write("""
Hi! I am a BSIT student passionate about software development and cybersecurity.
I enjoy learning Python, Django, and Web Development.
""")

st.header("🎓 Education")
st.write("- Bachelor of Science in Information Technology")
st.write("- Interested in Software Testing & CyberSecurity")

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
