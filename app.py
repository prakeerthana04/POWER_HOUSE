import streamlit as st
from PIL import Image
import os
import json
from datetime import datetime

# ----------------- CONFIG -----------------
st.set_page_config(page_title="POWER HOUSE | Official Team Website", layout="wide")

# ----------------- PATHS -----------------
LOGO_PATH = "logo.png"
IMAGES_DIR = "images"
MOMENTS_DIR = "moments"
DATA_FILE = "moments.json"

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(MOMENTS_DIR, exist_ok=True)

# ----------------- HEADER -----------------
col1, col2 = st.columns([1, 5])

with col1:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=120)

with col2:
    st.markdown("# ⚡ POWER HOUSE ⚡")
    st.caption("Official Team Website | Mechanical Engineering")

st.markdown("---")

# ----------------- SIDEBAR -----------------
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Team Members", "Team Moments"])

# ----------------- TEAM DATA -----------------
team_details = {
    "Team Name": "POWER HOUSE",
    "Department": "MECHANICAL ENGINEERING",
    "Institution": "VIDYA ACADEMY OF SCIENCE AND TECHNOLOGY",
    "Instagram": "https://www.instagram.com/_power_house08"
}

team_members = [
    {"name": "Godwin C Baiju", "role": "Captain of House", "image": "images/godwin.png", "desc": "A passionate mechanical engineering student with strong leadership skills and a drive for innovation."},
    {"name": "Vishnudev M S", "role": "Vice Captain", "image": "images/vishnu.png", "desc": "A dedicated mechanical engineering student focused on teamwork, discipline, and continuous improvement."},
    {"name": "Vinayak", "role": "Designer", "image": "images/vinayak.png", "desc": "A creative mechanical engineering student with a strong interest in design, visualization, and innovation."},
    {"name": "Goutham K V", "role": "Tester", "image": "images/goutham.png", "desc": "A detail-oriented mechanical engineering student skilled in analysis, testing, and quality assurance."},
    {"name": "Rohith K R", "role": "Tester", "image": "images/rohith.png", "desc": "A motivated mechanical engineering student with a passion for problem-solving and technical excellence."},
    {"name": "Athul T Santhosh", "role": "Tester", "image": "images/athul.png", "desc": "An enthusiastic mechanical engineering student committed to learning, teamwork, and innovation."},
    {"name": "Arun E Satheesh", "role": "Tester", "image": "images/arun.png", "desc": "A focused mechanical engineering student with strong analytical skills and a hands-on approach."},
    {"name": "Devarjun", "role": "Tester", "image": "images/devarjun.png", "desc": "A hardworking mechanical engineering student passionate about engineering concepts and practical applications."}
]

# Sort team members to maintain consistent order everywhere
team_members = sorted(team_members, key=lambda x: x['name'])

    {"name": "Godwin C Baiju", "role": "Captain of House", "image": "images/godwin.png"},
    {"name": "Vishnudev M S", "role": "Vice Captain", "image": "images/vishnu.png"},
    {"name": "Vinayak", "role": "Designer", "image": "images/vinayak.png"},
    {"name": "Goutham K V", "role": "Tester", "image": "images/goutham.png"},
    {"name": "Rohith K R", "role": "Tester", "image": "images/rohith.png"},
    {"name": "Athul T Santhosh", "role": "Tester", "image": "images/athul.png"},
    {"name": "Arun E Satheesh", "role": "Tester", "image": "images/arun.png"},
    {"name": "Devarjun", "role": "Tester", "image": "images/devarjun.png"}
]

# ----------------- MOMENT DATA HANDLING -----------------
def load_moments():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_moments(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

moments_data = load_moments()

# ----------------- HOME PAGE -----------------
if page == "Home":
    st.subheader("📌 Team Overview")
    cols = st.columns(2)

    for i, (k, v) in enumerate(team_details.items()):
        if k == "Instagram":
            cols[i % 2].markdown(f"**{k}:** [Visit Profile]({v})")
        else:
            cols[i % 2].markdown(f"**{k}:** {v}")

    st.markdown("---")
    st.subheader("👥 Team Members")

    grid = st.columns(4)
    for i, member in enumerate(team_members):
        with grid[i % 4]:
            if os.path.exists(member['image']):
                st.image(member['image'], width=130)
            st.markdown(f"**{member['name']}**")
            st.caption(member['role'])
            st.write(member['desc'])

# ----------------- TEAM MEMBERS PAGE -----------------
elif page == "Team Members":
    st.subheader("🧑‍🤝‍🧑 Team Profiles")

    for member in team_members:
        c1, c2 = st.columns([1, 4])

        with c1:
            if os.path.exists(member['image']):
                st.image(member['image'], width=140)
            else:
                st.warning("Image not found")

        with c2:
            st.markdown(f"### {member['name']}")
            st.markdown(f"**Role:** {member['role']}**")
            st.write(member['desc'])

        st.markdown("---")

# ----------------- TEAM MOMENTS PAGE -----------------
elif page == "Team Moments":
    st.subheader("📸 Team Moments Gallery")

    with st.expander("➕ Add New Moment"):
        photo = st.file_uploader("Upload Photo", type=["png", "jpg", "jpeg"])
        desc = st.text_area("Moment Description")

        if st.button("Save Moment") and photo is not None:
            filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
            filepath = os.path.join(MOMENTS_DIR, filename)

            with open(filepath, "wb") as f:
                f.write(photo.getbuffer())

            entry = {
                "image": filepath,
                "description": desc,
                "time": datetime.now().strftime("%d %b %Y, %I:%M %p")
            }

            moments_data.append(entry)
            save_moments(moments_data)
            st.success("Moment saved successfully!")

    st.markdown("---")

    if moments_data:
        cols = st.columns(3)
        for i, m in enumerate(reversed(moments_data)):
            with cols[i % 3]:
                if os.path.exists(m['image']):
                    st.image(m['image'], use_container_width=True)
                st.caption(m['time'])
                st.write(m['description'])

# ----------------- FOOTER -----------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center>⚡ POWER HOUSE CREW | Built with Streamlit ⚡</center>", unsafe_allow_html=True)
