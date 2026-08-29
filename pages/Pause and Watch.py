import streamlit as st
import streamlit.components.v1 as components
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from turtle_design import flower_svg


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Pause & Watch",
    page_icon="🌸",
    layout="wide"
)


# ============================================================
# DARK GREEN THEME
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

.pause-label {
    color: #71e58b;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2.5px;
    margin-bottom: 10px;
}

.pause-title {
    color: white;
    font-size: 48px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 12px;
}

.pause-subtitle {
    color: #aebfb4;
    font-size: 17px;
    line-height: 1.7;
    max-width: 800px;
}

/* SECTION */

.pause-section {
    color: white;
    font-size: 28px;
    font-weight: 750;
    margin-top: 25px;
    margin-bottom: 20px;
}

/* INFO CARDS */

.pause-card {
    background: linear-gradient(145deg, #10271c, #0a1711);
    border: 1px solid #28563a;
    border-radius: 22px;
    padding: 28px;
}

.pause-card-title {
    color: #71e58b;
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 12px;
}

.pause-card-text {
    color: #aebfb4;
    line-height: 1.7;
    font-size: 15px;
}

/* BUTTON */

.stButton > button {
    background-color: #71e58b;
    color: #07110d;
    border: none;
    border-radius: 12px;
    font-weight: 700;
}

.stButton > button:hover {
    background-color: #8af09d;
    color: #07110d;
}

/* DIVIDERS */

hr {
    border-color: #1b3927 !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="pause-label">
    🌿 WASTEVISION • SLOW DOWN
</div>

<div class="pause-title">
    Pause & <span style="color:#71e58b;">Watch.</span>
</div>

<div class="pause-subtitle">
    Take a moment. Watch a mathematical flower form itself,
    one curve at a time, using Python, mathematics and
    procedural generation.
</div>
""", unsafe_allow_html=True)

st.divider()


# ============================================================
# GENERATIVE FLOWER
# ============================================================

st.markdown(
    '<div class="pause-section">🌸 Generative Flower</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    petals = st.slider(
        "Number of petals",
        min_value=12,
        max_value=72,
        value=36,
        step=6
    )

with col2:
    radius = st.slider(
        "Flower size",
        min_value=150,
        max_value=260,
        value=230,
        step=10
    )

with col3:
    variation = st.slider(
        "Pattern variation",
        min_value=0,
        max_value=20,
        value=5,
        step=1
    )


# ============================================================
# GENERATE FLOWER
# ============================================================

if st.button(
    "🌸 Grow a New Flower",
    use_container_width=True
):

    svg = flower_svg(
        petals=petals,
        radius=radius,
        variation=variation
    )

    # IMPORTANT:
    # Keep the SVG directly inside components.html.
    # Do NOT place it inside st.markdown HTML.

    components.html(
        svg,
        height=630,
        scrolling=False
    )

else:

    st.info(
        "Choose your settings and click "
        "**Grow a New Flower** to begin."
    )


# ============================================================
# EXPLANATION
# ============================================================

st.divider()

st.subheader("🧠 What's happening behind the scenes?")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🐍 Python creates the pattern")

    st.write(
        """
        The flower is generated using:

        • **math** — trigonometric calculations  
        • **random** — controlled pattern variation  
        • **functions** — reusable drawing logic  
        • **loops** — generating multiple petals  
        • **polar coordinates** — positioning curves  
        • **SVG** — displaying the generated artwork
        """
    )


with col2:

    st.markdown("### ✨ Every flower is generated")

    st.write(
        """
        The flower is **not a stored image**.

        Every time you change the settings and generate
        a flower, Python calculates the curves again.

        The browser then animates those curves so you
        can watch the pattern grow.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("""
<div style="
    text-align:center;
    padding:25px;
    color:#81968a;
    font-size:14px;
">
    🌿 Sometimes sustainability is also about
    <span style="color:#71e58b;">slowing down, observing and learning.</span>
</div>
""", unsafe_allow_html=True)