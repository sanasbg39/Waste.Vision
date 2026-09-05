import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Waste Detector",
    page_icon="🤖",
    layout="wide"
)

# ==================================================
# WASTEVISION WASTE DETECTOR
# ==================================================

st.title("🤖 WasteVision")

# --------------------------------------------------
# INTERNAL NAVIGATION
# --------------------------------------------------

section = st.radio(
    "Choose a section",
    [
        "🔍 Waste Detector",
        "🌍 SDG 11 Impact"
    ],
    horizontal=True
)

st.divider()


# ==================================================
# WASTE DETECTOR
# ==================================================

if section == "🔍 Waste Detector":

    st.title("♻️ AI Waste Detector")

    st.markdown(
        """
        Upload an image of waste and use WasteVision
        to identify the appropriate waste category.

        Detection runs live in your browser (TensorFlow.js + COCO-SSD) —
        no server call, no upload to any backend.
        """
    )

    # --------------------------------------------------
    # LOAD WASTE HTML
    # --------------------------------------------------
    # Save the detector file I generated as "detector.html" in the same
    # folder as your old "waste.html" (i.e. BASE_DIR below). If you'd
    # rather keep the old filename, just rename the new file to
    # "waste.html" and change WASTE_HTML_FILENAME back to that — no other
    # code changes needed either way.

    WASTE_HTML_FILENAME = "detector.html"

    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    WASTE_HTML = os.path.join(
        BASE_DIR,
        WASTE_HTML_FILENAME
    )

    with open(WASTE_HTML, "r", encoding="utf-8") as f:
        html_content = f.read()

    components.html(
        html_content,
        height=950,   # new layout is a bit taller than the old demo card
        scrolling=True
    )

    # --------------------------------------------------
    # RECORD DETECTION
    # --------------------------------------------------

    st.divider()

    st.subheader("📊 Record Detection")

    st.caption(
        "The detector above shows live results per object — pick the "
        "stream it sorted your item into and log it here."
    )

    detected_waste = st.selectbox(
        "Select the detected waste category",
        [
            "Recyclable ♻️",
            "Organic 🍃",
            "Hazardous ☣️",
            "General 🗑️"
        ]
    )

    if st.button(
        "➕ Add to Waste History",
        use_container_width=True
    ):

        if "history" not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append(
            detected_waste
        )

        st.success(
            f"✅ {detected_waste} added to your waste history!"
        )


# ==================================================
# SDG 11 IMPACT
# ==================================================

else:

    st.title("🌍 SDG 11 Impact")

    st.markdown(
        """
        ## Sustainable Cities & Communities

        **WasteVision connects artificial intelligence,
        responsible waste segregation and environmental
        awareness to the goals of sustainable communities.**
        """
    )

    st.divider()

    # --------------------------------------------------
    # SDG INTRODUCTION
    # --------------------------------------------------

    st.subheader("🎯 What is SDG 11?")

    st.write(
        """
        Sustainable Development Goal 11 aims to make cities
        and human settlements inclusive, safe, resilient and
        sustainable.

        Waste management is an important part of creating
        cleaner and more sustainable communities.
        """
    )

    # --------------------------------------------------
    # CONNECTION TO WASTEVISION
    # --------------------------------------------------

    st.subheader("♻️ How does WasteVision contribute?")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### 🤖 AI-Powered Identification

            WasteVision uses an AI-based waste detection
            system to help users identify waste materials.

            This can make waste segregation easier and
            more accessible.
            """
        )

    with col2:

        st.markdown(
            """
            ### ♻️ Better Waste Segregation

            Correctly identifying waste can help users
            understand which materials belong in different
            disposal categories.
            """
        )

    col3, col4 = st.columns(2)

    with col3:

        st.markdown(
            """
            ### 🧠 Environmental Awareness

            The application provides information about
            recyclable, organic, hazardous and general waste.

            This encourages users to make more informed
            disposal decisions.
            """
        )

    with col4:

        st.markdown(
            """
            ### 🏙️ Sustainable Communities

            When responsible waste practices become
            everyday habits, individuals can contribute
            to cleaner and more sustainable surroundings.
            """
        )

    # --------------------------------------------------
    # PROJECT CONNECTION
    # --------------------------------------------------

    st.divider()

    st.subheader("🌱 The WasteVision Approach")

    st.markdown(
        """
        **Identify → Understand → Sort → Track → Improve**

        WasteVision combines AI detection, educational
        resources and waste tracking to encourage
        responsible waste-management habits.

        The objective is not simply to identify waste,
        but to help users understand what to do with it.
        """
    )

    # --------------------------------------------------
    # SDG CHALLENGE
    # --------------------------------------------------

    st.divider()

    st.subheader("🏆 SDG 11 Challenge")

    st.write(
        """
        Can you correctly identify and segregate
        10 waste items?
        """
    )

    history = st.session_state.get("history", [])

    progress = min(len(history) / 10, 1.0)

    st.progress(
        progress,
        text=f"{min(len(history), 10)} / 10 items"
    )

    if len(history) >= 10:

        st.success(
            "🎉 Challenge complete! "
            "You've made 10 waste-sorting decisions."
        )

    else:

        remaining = 10 - len(history)

        st.info(
            f"🌱 {remaining} more decisions to complete "
            "the SDG 11 challenge."
        )
