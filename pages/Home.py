import streamlit as st

st.set_page_config(
    page_title="WasteVision",
    page_icon="♻️",
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
    padding-bottom: 2rem;
    max-width: 1250px;
}

/* ============================================================
   HERO
   ============================================================ */

.hero {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(
            circle at 85% 20%,
            rgba(113,229,139,0.12),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #10271c 0%,
            #07110d 75%
        );

    border: 1px solid #28563a;
    border-radius: 28px;
    padding: 65px 60px;
    margin-bottom: 45px;
}

.hero::after {
    content: "♻";
    position: absolute;
    right: 55px;
    bottom: -45px;
    font-size: 210px;
    color: rgba(113,229,139,0.035);
    font-weight: bold;
}

.hero-small {
    color: #71e58b;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2.5px;
    margin-bottom: 12px;
}

.hero-title {
    color: white;
    font-size: 64px;
    line-height: 1.05;
    font-weight: 800;
    letter-spacing: -2px;
    margin-bottom: 20px;
}

.hero-title span {
    color: #71e58b;
}

.hero-text {
    color: #b7c9bd;
    font-size: 19px;
    line-height: 1.7;
    max-width: 760px;
}

/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: white;
    font-size: 30px;
    font-weight: 750;
    margin-top: 45px;
    margin-bottom: 22px;
}

/* ============================================================
   FEATURE CARDS
   ============================================================ */

.card {
    background: linear-gradient(
        145deg,
        #0e2117,
        #0a1711
    );

    border: 1px solid #1e422d;
    border-radius: 22px;
    padding: 30px;
    min-height: 210px;
    transition: all 0.2s ease;
}

.card:hover {
    border-color: #347149;
    transform: translateY(-3px);
}

.card-icon {
    font-size: 34px;
    margin-bottom: 14px;
}

.card-title {
    color: white;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 9px;
}

.card-text {
    color: #9fb3a6;
    line-height: 1.65;
    font-size: 15px;
}

/* ============================================================
   HOW IT WORKS
   ============================================================ */

.step {
    background: #0c1b13;
    border: 1px solid #1b3927;
    border-radius: 18px;
    padding: 25px;
    min-height: 125px;
}

.step-number {
    color: #71e58b;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.step-title {
    color: white;
    font-size: 25px;
    font-weight: 650;
}

.step-line {
    height: 1px;
    background: #28563a;
    margin-top: 18px;
}

/* ============================================================
   SDG
   ============================================================ */

.sdg {
    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(113,229,139,0.08),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #173522,
            #0c1d14
        );

    border: 1px solid #347149;
    border-radius: 24px;
    padding: 34px;
    margin-bottom: 20px;
}

.sdg-label {
    color: #71e58b;
    font-size: 13px;
    font-weight: 750;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

.sdg-title {
    color: white;
    font-size: 29px;
    font-weight: 750;
    margin-bottom: 10px;
}

.sdg-text {
    color: #b4c7ba;
    line-height: 1.7;
    font-size: 16px;
    max-width: 1050px;
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    padding: 45px 20px 25px;
    margin-top: 55px;
    border-top: 1px solid #1b3525;
}

.footer-title {
    color: #71e58b;
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 8px;
}

.footer-text {
    color: #81968a;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.html("""
<div class="hero-small">
    ♻️ SMART WASTE MANAGEMENT PLATFORM
</div>

    <div class="hero-title">
        Meet <span>WasteVision.</span>
    </div>

    <div class="hero-text">
        Make smarter decisions about waste, understand your
        environmental impact, and turn everyday actions into
        measurable progress.
    </div>

</div>
""")


# ============================================================
# FEATURES
# ============================================================

st.html("""
<div class="section-title">
    🌱 Explore WasteVision
</div>
""")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.html("""
    <div class="card">

        <div class="card-icon">🤖</div>

        <div class="card-title">
            Smart Detection
        </div>

        <div class="card-text">
            Use artificial intelligence to identify different
            types of waste and understand what belongs where.
        </div>

    </div>
    """)

with col2:
    st.html("""
    <div class="card">

        <div class="card-icon">📊</div>

        <div class="card-title">
            Data & Analytics
        </div>

        <div class="card-text">
            Track waste, discover patterns and transform
            everyday data into meaningful environmental insights.
        </div>

    </div>
    """)

with col3:
    st.html("""
    <div class="card">

        <div class="card-icon">🌍</div>

        <div class="card-title">
            Learn & Act
        </div>

        <div class="card-text">
            Explore sustainability, sorting practices and
            environmental knowledge that can turn awareness
            into action.
        </div>

    </div>
    """)


# ============================================================
# HOW IT WORKS
# ============================================================

st.html("""
<div class="section-title">
    ⚡ How WasteVision Works
</div>
""")

col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
    st.html("""
    <div class="step">
        <div class="step-number">01</div>
        <div class="step-title">Detect</div>
        <div class="step-line"></div>
    </div>
    """)

with col2:
    st.html("""
    <div class="step">
        <div class="step-number">02</div>
        <div class="step-title">Understand</div>
        <div class="step-line"></div>
    </div>
    """)

with col3:
    st.html("""
    <div class="step">
        <div class="step-number">03</div>
        <div class="step-title">Track</div>
        <div class="step-line"></div>
    </div>
    """)

with col4:
    st.html("""
    <div class="step">
        <div class="step-number">04</div>
        <div class="step-title">Improve</div>
        <div class="step-line"></div>
    </div>
    """)


# ============================================================
# SDG
# ============================================================

st.html("""
<div class="section-title">
    🎯 Our Sustainable Development Goal
</div>
""")

st.html("""
<div class="sdg">

    <div class="sdg-label">
        UNITED NATIONS • SDG 11
    </div>

    <div class="sdg-title">
        Sustainable Cities & Communities
    </div>

    <div class="sdg-text">
        WasteVision encourages responsible waste management,
        environmental awareness and informed decision-making
        to contribute towards cleaner and more sustainable communities.
    </div>

</div>
""")


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    <div class="footer-title">
        🌿 See it. Sort it. Understand it. Change it.
    </div>

    <div class="footer-text">
        Small actions can contribute to bigger environmental change.
    </div>

</div>
""")
