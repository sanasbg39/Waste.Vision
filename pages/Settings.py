import streamlit as st
import pandas as pd
import json

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #07110d;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* HEADER */

.settings-label {
    color: #71e58b;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2.5px;
    margin-bottom: 10px;
}

.settings-title {
    color: white;
    font-size: 48px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 12px;
}

.settings-subtitle {
    color: #aebfb4;
    font-size: 17px;
    line-height: 1.7;
    max-width: 800px;
}

/* SECTION TITLES */

.section-heading {
    color: white;
    font-size: 27px;
    font-weight: 750;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* CARDS */

.settings-card {
    background: linear-gradient(145deg, #10271c, #0a1711);
    border: 1px solid #28563a;
    border-radius: 22px;
    padding: 28px;
    margin-bottom: 20px;
}

.card-heading {
    color: #71e58b;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* BUTTONS */

.stButton > button,
.stDownloadButton > button {
    border-radius: 12px;
    font-weight: 700;
}

.stDownloadButton > button {
    background-color: #71e58b;
    color: #07110d;
    border: none;
}

.stDownloadButton > button:hover {
    background-color: #8af09d;
    color: #07110d;
}

/* DIVIDERS */

hr {
    border-color: #1b3927 !important;
}

/* VERSION */

.version-text {
    color: #81968a;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA
# ============================================================

if "waste_entries" not in st.session_state:
    st.session_state.waste_entries = []

entries = st.session_state.waste_entries


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="settings-label">
    ⚙️ WASTEVISION • SYSTEM
</div>

<div class="settings-title">
    Settings
</div>

<div class="settings-subtitle">
    Manage your waste data, export your records and
    control your WasteVision session.
</div>
""", unsafe_allow_html=True)

st.divider()


# ============================================================
# EXPORT DATA
# ============================================================

st.markdown(
    '<div class="section-heading">📤 Export Data</div>',
    unsafe_allow_html=True
)

if entries:

    df = pd.DataFrame(entries)

    csv_data = df.to_csv(index=False)

    json_data = json.dumps(
        entries,
        indent=4
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="⬇️ Export as CSV",
            data=csv_data,
            file_name="waste_data.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:

        st.download_button(
            label="⬇️ Export as JSON",
            data=json_data,
            file_name="waste_data.json",
            mime="application/json",
            use_container_width=True
        )

else:

    st.info(
        "There is no waste data to export yet. "
        "Add some entries through Waste Tracker first."
    )


# ============================================================
# RESET DATA
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">🗑️ Reset Data</div>',
    unsafe_allow_html=True
)

st.warning(
    "Resetting your data will remove all waste entries "
    "from the current session."
)

if st.button(
    "🗑️ Reset All Data",
    use_container_width=True
):

    st.session_state.waste_entries = []

    st.success(
        "✅ All waste data has been reset."
    )


# ============================================================
# ABOUT
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">ℹ️ About WasteVision</div>',
    unsafe_allow_html=True
)

st.write(
    """
    **Smart Waste Management System**

    WasteVision uses technology and artificial intelligence
    to encourage responsible waste management and support
    **Sustainable Development Goal 11 — Sustainable Cities
    and Communities.**
    """
)

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        "**Version**  \n"
        "1.0"
    )

with col2:

    st.markdown(
        "**Developed for**  \n"
        "SDG 11 — Sustainable Cities & Communities"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "♻️ Smart waste management for cleaner and more sustainable communities."
)