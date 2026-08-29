import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="WasteVision Dashboard",
    page_icon="📊",
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

/* ============================================================
   TITLES
   ============================================================ */

.dashboard-label {
    color: #71e58b;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 5px;
}

.section-title {
    color: white;
    font-size: 25px;
    font-weight: 750;
    margin-top: 35px;
    margin-bottom: 18px;
}

/* ============================================================
   STAT CARDS
   ============================================================ */

.stat-card {
    background: linear-gradient(145deg, #10271c, #0a1711);
    border: 1px solid #1e422d;
    border-radius: 18px;
    padding: 22px;
    min-height: 120px;
}

.stat-icon {
    font-size: 23px;
    margin-bottom: 8px;
}

.stat-label {
    color: #81968a;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.8px;
}

.stat-value {
    color: white;
    font-size: 26px;
    font-weight: 750;
    margin-top: 5px;
}

/* ============================================================
   ECO SCORE
   ============================================================ */

.score-box {
    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(113,229,139,0.12),
            transparent 35%
        ),
        linear-gradient(135deg, #173522, #0c1d14);

    border: 1px solid #347149;
    border-radius: 24px;
    padding: 28px;
}

.score-label {
    color: #71e58b;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.score-number {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin-top: 5px;
}

.score-description {
    color: #a9bdb0;
    font-size: 14px;
    line-height: 1.6;
    margin-top: 5px;
}

/* ============================================================
   INFO BOXES
   ============================================================ */

.info-box {
    background: #0c1b13;
    border: 1px solid #1b3927;
    border-radius: 18px;
    padding: 25px;
}

.info-title {
    color: white;
    font-size: 18px;
    font-weight: 700;
}

.info-text {
    color: #9fb3a6;
    font-size: 14px;
    line-height: 1.6;
    margin-top: 7px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-label">♻️ WASTEVISION</div>',
    unsafe_allow_html=True
)

st.title("Your Waste Dashboard")

st.write(
    "Monitor your waste habits, recycling progress and "
    "environmental impact."
)


# ============================================================
# DATA
# ============================================================

if "waste_entries" not in st.session_state:
    st.session_state.waste_entries = []

entries = st.session_state.waste_entries


# ============================================================
# NO DATA STATE
# ============================================================

if not entries:

    st.info(
        "No waste has been recorded yet. "
        "Go to Waste Tracker and add your first entry."
    )

    st.markdown(
        '<div class="section-title">🌱 Welcome to WasteVision</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">♻️</div>
            <div class="stat-label">TOTAL WASTE</div>
            <div class="stat-value">0 kg</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">📋</div>
            <div class="stat-label">TOTAL ENTRIES</div>
            <div class="stat-value">0</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">🌱</div>
            <div class="stat-label">RECYCLING RATE</div>
            <div class="stat-value">0%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">💡 Getting Started</div>',
        unsafe_allow_html=True
    )

    st.success(
        "Start recording your waste in Waste Tracker. "
        "Your Eco Score and environmental statistics will "
        "appear here automatically."
    )

    st.stop()


# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(entries)

total_entries = len(df)

total_weight = df["Weight (kg)"].sum()

recyclable_categories = [
    "Plastic",
    "Paper",
    "Glass",
    "Metal"
]

recyclable_weight = df[
    df["Category"].isin(recyclable_categories)
]["Weight (kg)"].sum()

recycling_rate = (
    recyclable_weight / total_weight * 100
    if total_weight > 0
    else 0
)


# ============================================================
# ECO SCORE
# ============================================================

category_counts = df["Category"].value_counts()

recyclable_count = sum(
    category_counts.get(category, 0)
    for category in recyclable_categories
)

organic_count = category_counts.get("Organic", 0)

general_count = category_counts.get("General", 0)

if total_entries > 0:

    recycling_points = (
        recyclable_count / total_entries
    ) * 50

    organic_points = (
        organic_count / total_entries
    ) * 20

    responsible_points = (
        (total_entries - general_count)
        / total_entries
    ) * 20

    awareness_points = min(
        total_entries * 2,
        10
    )

    eco_score = round(
        recycling_points
        + organic_points
        + responsible_points
        + awareness_points
    )

else:
    eco_score = 0

eco_score = min(eco_score, 100)


# ============================================================
# ECO SCORE
# ============================================================

st.markdown(
    '<div class="section-title">🌱 Your Eco Score</div>',
    unsafe_allow_html=True
)

score_col1, score_col2 = st.columns([1, 2], gap="medium")

with score_col1:

    st.markdown(f"""
    <div class="score-box">

        <div class="score-label">
            CURRENT SCORE
        </div>

        <div class="score-number">
            {eco_score}/100
        </div>

        <div class="score-description">
            Your score reflects your recycling,
            segregation and waste-recording habits.
        </div>

    </div>
    """, unsafe_allow_html=True)


with score_col2:

    st.write("")

    st.progress(
        eco_score / 100
    )

    if eco_score >= 80:

        st.success(
            "🌿 Excellent! Your waste-management habits "
            "are making a positive contribution."
        )

    elif eco_score >= 50:

        st.info(
            "🌱 Good progress! Keep improving your "
            "waste segregation habits."
        )

    else:

        st.warning(
            "♻️ Keep going! Better segregation can "
            "improve your Eco Score."
        )


# ============================================================
# OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-title">📊 Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4, gap="medium")


with col1:

    st.markdown(f"""
    <div class="stat-card">

        <div class="stat-icon">♻️</div>

        <div class="stat-label">
            TOTAL WASTE
        </div>

        <div class="stat-value">
            {total_weight:.2f} kg
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div class="stat-card">

        <div class="stat-icon">📋</div>

        <div class="stat-label">
            TOTAL ENTRIES
        </div>

        <div class="stat-value">
            {total_entries}
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""
    <div class="stat-card">

        <div class="stat-icon">🌱</div>

        <div class="stat-label">
            RECYCLING RATE
        </div>

        <div class="stat-value">
            {recycling_rate:.1f}%
        </div>

    </div>
    """, unsafe_allow_html=True)


with col4:

    most_common = df["Category"].value_counts().idxmax()

    st.markdown(f"""
    <div class="stat-card">

        <div class="stat-icon">📦</div>

        <div class="stat-label">
            MOST COMMON
        </div>

        <div class="stat-value">
            {most_common}
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# WASTE DISTRIBUTION
# ============================================================

st.markdown(
    '<div class="section-title">📈 Waste Distribution</div>',
    unsafe_allow_html=True
)

category_data = (
    df.groupby("Category")["Weight (kg)"]
    .sum()
)

fig, ax = plt.subplots(figsize=(9, 4))

ax.bar(
    category_data.index,
    category_data.values
)

ax.set_xlabel("Waste Category")
ax.set_ylabel("Weight (kg)")
ax.set_title("Waste Distribution by Weight")

plt.xticks(rotation=30)

plt.tight_layout()

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)


# ============================================================
# ENVIRONMENTAL IMPACT
# ============================================================

st.markdown(
    '<div class="section-title">🌍 Environmental Impact</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="medium")

with col1:

    st.markdown(f"""
    <div class="info-box">

        <div class="info-title">
            ♻️ Recyclable Waste
        </div>

        <div class="info-text">
            You have recorded
            <strong>{recyclable_weight:.2f} kg</strong>
            of recyclable materials.
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div class="info-box">

        <div class="info-title">
            🌱 Recycling Rate
        </div>

        <div class="info-text">
            <strong>{recycling_rate:.1f}%</strong>
            of your recorded waste belongs to
            recyclable categories.
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# ECO TIP
# ============================================================

st.markdown(
    '<div class="section-title">💡 Eco Tip</div>',
    unsafe_allow_html=True
)

st.info(
    "Separating recyclable materials from general waste "
    "helps reduce contamination and improves recycling."
)


# ============================================================
# RECENT ENTRIES
# ============================================================

st.markdown(
    '<div class="section-title">📋 Recent Waste Entries</div>',
    unsafe_allow_html=True
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)