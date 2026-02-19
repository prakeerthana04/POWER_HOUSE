import streamlit as st
from PIL import Image
import os

# ----------------- CONFIG -----------------
st.set_page_config(page_title="Our Team Website", layout="wide")

# ----------------- SIDEBAR -----------------
st.sidebar.title("Team Navigation")
page = st.sidebar.radio("Go to", ["Home", "Team Members", "Team Moments"])

# ----------------- LOGO -----------------
logo_path = "logo.png"  # Place your team logo image in the same folder
if os.path.exists(logo_path):
    st.image(logo_path, width=180)

st.title("🌟 Our Amazing Team 🌟")

# ----------------- TEAM DATA -----------------
team_details = {
    "Team Name": "Your Team Name",
    "Department": "Artificial Intelligence & Machine Learning",
    "Institution": "Your College Name",
    "Project": "Your Project Name",
    "Guide": "Guide Name"
}

team_members = [
    {"name": "Member 1", "role": "Team Leader", "image": "member1.jpg"},
    {"name": "Member 2", "role": "Developer", "image": "member2.jpg"},
    {"name": "Member 3", "role": "Designer", "image": "member3.jpg"},
    {"name": "Member 4", "role": "Tester", "image": "member4.jpg"}
]

# ----------------- HOME PAGE -----------------
if page == "Home":
    st.subheader("📌 Team Details")
    col1, col2 = st.columns(2)

    for i, (key, value) in enumerate(team_details.items()):
        if i % 2 == 0:
            col1.markdown(f"**{key}:** {value}")
        else:
            col2.markdown(f"**{key}:** {value}")

    st.markdown("---")
    st.subheader("👥 Team Members Overview")

    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        if os.path.exists(member['image']):
            img = Image.open(member['image'])
            col.image(img, width=130)
        col.markdown(f"**{member['name']}**")
        col.caption(member['role'])

# ----------------- TEAM MEMBERS PAGE -----------------
elif page == "Team Members":
    st.subheader("🧑‍🤝‍🧑 Team Profiles")

    for member in team_members:
        col1, col2 = st.columns([1, 3])

        with col1:
            if os.path.exists(member['image']):
                img = Image.open(member['image'])
                st.image(img, width=150)
            else:
                st.warning("Image not found")

        with col2:
            st.markdown(f"### {member['name']}")
            st.markdown(f"**Role:** {member['role']}")
            st.markdown("**Description:** Passionate team member contributing to project success.")

        st.markdown("---")

# ----------------- TEAM MOMENTS PAGE -----------------
elif page == "Team Moments":
    st.subheader("📸 Team Moments Gallery")

    uploaded_files = st.file_uploader("Upload Team Moment Photos", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    if uploaded_files:
        cols = st.columns(3)
        for i, file in enumerate(uploaded_files):
            img = Image.open(file)
            cols[i % 3].image(img, use_container_width=True)

# ----------------- FOOTER -----------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center>✨ Designed with Streamlit | Your Team ✨</center>", unsafe_allow_html=True)
