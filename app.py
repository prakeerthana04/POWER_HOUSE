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
    "Team Name": "POWER HOUSE",
    "Department": "MECHANICAL ENGINEERING",
    "Institution": "VIDYA ACADEMY OF SCIENCE AND TECNOLOGY",
    "Instagram Id": "https://www.instagram.com/_power_house08?igsh=Y295bWJxOWV5ajFv"
}

team_members = [
    {"name": "Godwin C Baiju", "role": "Captain of House", "image": "godwin.png"},
    {"name": "Vishnudev M S", "role": "Vice Captain", "image": "vishnu.png"},
    {"name": "Vinayak", "role": "Designer", "image": "vinayak.png"},
    {"name": "Goutham K V", "role": "Tester", "image": "goutham.png"},
    {"name": "Rohith K R", "role": "Tester", "image": "rohith.png"},
    {"name": "Athul T Santhosh", "role": "Tester", "image": "athul.png"},
    {"name": "Arun E Satheesh", "role": "Tester", "image": "arun.png"},
    {"name": "Devarjun", "role": "Tester", "image": "devarjun.png"}
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
st.markdown("<center>✨ THE POWER HOUSE CREW ✨</center>", unsafe_allow_html=True)
