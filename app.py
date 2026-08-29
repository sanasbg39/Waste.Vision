import streamlit as st

st.set_page_config(
    page_title="WasteVision",
    page_icon="♻️",
    layout="wide"
)
# ============================================================
# WASTEVISION SIDEBAR
# ============================================================

st.markdown("""
<style>

/* =========================
   SIDEBAR
   ========================= */

[data-testid="stSidebar"] {
    background: #08140e;
    border-right: 1px solid #193524;
}

/* Sidebar content */
[data-testid="stSidebarContent"] {
    padding: 1.5rem 0.8rem;
}

/* =========================
   WASTEVISION BRAND
   ========================= */

.wv-brand {
    padding: 8px 12px 25px 12px;
    border-bottom: 1px solid #193524;
    margin-bottom: 18px;
}

.wv-logo {
    font-size: 30px;
    margin-bottom: 5px;
}

.wv-name {
    color: #ffffff;
    font-size: 21px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.wv-name span {
    color: #71e58b;
}

.wv-tagline {
    color: #718579;
    font-size: 11px;
    margin-top: 4px;
    letter-spacing: 0.8px;
}

/* =========================
   NAVIGATION
   ========================= */

/* Section headings */
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #718579;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

/* Navigation buttons */
[data-testid="stSidebar"] button {
    border-radius: 12px !important;
    margin: 3px 0 !important;
    transition: all 0.2s ease !important;
}

/* Hover */
[data-testid="stSidebar"] button:hover {
    background-color: #10271c !important;
}

/* Active page */
[data-testid="stSidebar"] button[aria-current="page"] {
    background: linear-gradient(
        90deg,
        #173522,
        #10271c
    ) !important;

    border-left: 3px solid #71e58b !important;
}

/* Active text */
[data-testid="stSidebar"] button[aria-current="page"] p {
    color: #71e58b !important;
    font-weight: 700 !important;
}

/* Navigation icons */
[data-testid="stSidebar"] button span {
    color: #9fb3a6;
}

/* Active icon */
[data-testid="stSidebar"] button[aria-current="page"] span {
    color: #71e58b !important;
}

/* =========================
   SIDEBAR FOOTER
   ========================= */

.wv-sidebar-footer {
    margin-top: 30px;
    padding: 15px 12px;
    border-top: 1px solid #193524;
    color: #62776a;
    font-size: 11px;
    line-height: 1.5;
}

.wv-sidebar-footer strong {
    color: #71e58b;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

pages = {
    "MAIN": [
    st.Page("pages/Home.py", title="Home", icon=":material/home:"),
    st.Page("pages/Dashboard.py", title="Dashboard", icon=":material/dashboard:"),
    st.Page("pages/Waste_Detector.py", title="Waste Detector", icon=":material/robot_2:"),
    st.Page("pages/Analytics.py", title="Analytics", icon=":material/analytics:"),
    ],

    "MANAGE": [
        st.Page("pages/Waste_Tracker.py", title="Waste Tracker", icon=":material/recycling:"),
        st.Page("pages/Sorting_Guide.py", title="Sorting Guide", icon=":material/menu_book:"),
    ],

    "EXPLORE": [
        st.Page("pages/Eco Knowledge.py", title="Eco Knowledge", icon=":material/eco:"),
        st.Page("pages/Play A Game.py", title="Play A Game", icon=":material/sports_esports:"),
        st.Page("pages/Pause and Watch.py", title="Pause & Watch", icon=":material/pause_circle:"),
    ],

    "SYSTEM": [
        st.Page("pages/Settings.py", title="Settings", icon=":material/settings:"),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=True)

pg.run()