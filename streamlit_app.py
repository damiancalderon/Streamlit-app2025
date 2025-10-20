import streamlit as st

# -------------------------------
# APP CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="City Data Intelligence",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# STYLE (COLOR PALETTE)
# -------------------------------
st.markdown("""
<style>
    :root {
        --primary-color: #1E88E5;
        --secondary-color: #1565C0;
        --accent-color: #42A5F5;
        --background-color: #F5F7FA;
        --text-color: #1A1A1A;
    }
    body {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .stButton>button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: var(--secondary-color);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# USER ROLES
# -------------------------------
ROLES = [None, "Admin", "Decision Maker", "Citizen"]

if "role" not in st.session_state:
    st.session_state.role = None


# -------------------------------
# LOGIN & LOGOUT FUNCTIONS
# -------------------------------
def login():
    st.header("🔐 Log In")
    role = st.selectbox("Select your role", ROLES)
    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.header("🚪 Log Out")
    if st.button("Log out"):
        st.session_state.role = None
        st.rerun()


# -------------------------------
# DEFINE PAGES (Navigation)
# -------------------------------
role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

dashboard = st.Page(
    "Visualization/visualization.py",
    title="📊 Data Dashboard",
    icon=":material/dashboard:"
)
maps = st.Page(
    "Visualization/maps.py",
    title="🗺️ Interactive Maps",
    icon=":material/map:"
)
eda = st.Page(
    "EDA/eda.py",
    title="🔎 Exploratory Data Analysis",
    icon=":material/search:"
)
ml = st.Page(
    "ml/ml_analysis.py",
    title="🤖 Machine Learning Models",
    icon=":material/auto_awesome:"
)

# -------------------------------
# APP HEADER
# -------------------------------
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")
st.title("🌆 City Data Intelligence Platform")

# -------------------------------
# ROLE-BASED ACCESS
# -------------------------------
account_pages = [logout_page, settings]
visualization_pages = [dashboard, maps]
eda_pages = [eda]
ml_pages = [ml]

page_dict = {}

if role == "Admin":
    page_dict["Visualization"] = visualization_pages
    page_dict["EDA"] = eda_pages
    page_dict["Machine Learning"] = ml_pages

elif role == "Decision Maker":
    page_dict["Visualization"] = visualization_pages
    page_dict["Machine Learning"] = ml_pages

elif role == "Citizen":
    page_dict["Visualization"] = [maps]

# -------------------------------
# NAVIGATION
# -------------------------------
if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
