import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
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

.analytics-label {
    color: #71e58b;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2.5px;
    margin-bottom: 10px;
}

.analytics-title {
    color: white;
    font-size: 48px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 12px;
}

.analytics-subtitle {
    color: #aebfb4;
    font-size: 17px;
    line-height: 1.7;
    max-width: 800px;
}

/* SECTION HEADINGS */

.section-heading {
    color: white;
    font-size: 27px;
    font-weight: 750;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* DIVIDERS */

hr {
    border-color: #1b3927 !important;
}

/* BUTTON */

.stDownloadButton > button {
    background-color: #71e58b;
    color: #07110d;
    border: none;
    border-radius: 12px;
    font-weight: 700;
}

.stDownloadButton > button:hover {
    background-color: #8af09d;
    color: #07110d;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="analytics-label">
    📊 WASTEVISION • DATA & INSIGHTS
</div>

<div class="analytics-title">
    Waste <span style="color:#71e58b;">Analytics.</span>
</div>

<div class="analytics-subtitle">
    Turn your recorded waste into meaningful statistics,
    patterns and environmental insights.
</div>
""", unsafe_allow_html=True)

st.divider()


# ============================================================
# GET DATA
# ============================================================

if "waste_entries" not in st.session_state:
    st.session_state.waste_entries = []

entries = st.session_state.waste_entries

if not entries:

    st.info(
        "No waste data available yet. "
        "Add some entries in Waste Tracker to begin analysing your data."
    )

    st.stop()

df = pd.DataFrame(entries)


# ============================================================
# DATA PREPARATION
# ============================================================

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Weight (kg)"] = pd.to_numeric(
    df["Weight (kg)"],
    errors="coerce"
)

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df = df.dropna(
    subset=["Weight (kg)", "Category"]
)


# ============================================================
# RECYCLING RATE
# ============================================================

recyclable_categories = [
    "Plastic",
    "Paper",
    "Glass",
    "Metal"
]

recyclable_weight = df[
    df["Category"].isin(recyclable_categories)
]["Weight (kg)"].sum()

total_weight = df["Weight (kg)"].sum()

recycling_rate = (
    recyclable_weight / total_weight * 100
    if total_weight > 0
    else 0
)


# ============================================================
# SUMMARY STATISTICS
# ============================================================

st.markdown(
    '<div class="section-heading">📊 Summary Statistics</div>',
    unsafe_allow_html=True
)

total_entries = len(df)

average_weight = df["Weight (kg)"].mean()

highest_entry = df["Weight (kg)"].max()

most_common = df["Category"].value_counts().idxmax()

median_weight = df["Weight (kg)"].median()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📝 Total Entries",
        total_entries
    )

with col2:
    st.metric(
        "⚖️ Total Weight",
        f"{total_weight:.2f} kg"
    )

with col3:
    st.metric(
        "📊 Average Entry",
        f"{average_weight:.2f} kg"
    )

with col4:
    st.metric(
        "🏆 Most Common",
        most_common
    )


# ============================================================
# EXTRA STATISTICS
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">🔬 Statistical Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📌 Median Weight",
        f"{median_weight:.2f} kg"
    )

with col2:
    st.metric(
        "⬆️ Largest Entry",
        f"{highest_entry:.2f} kg"
    )

with col3:

    total_quantity = df["Quantity"].sum()

    st.metric(
        "📦 Total Items",
        int(total_quantity)
    )


# ============================================================
# CATEGORY ANALYSIS
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">♻️ Waste by Category</div>',
    unsafe_allow_html=True
)

category_counts = df["Category"].value_counts()

fig, ax = plt.subplots()

ax.bar(
    category_counts.index,
    category_counts.values
)

ax.set_xlabel("Waste Category")
ax.set_ylabel("Number of Entries")
ax.set_title("Number of Waste Entries by Category")

plt.xticks(rotation=30)

st.pyplot(fig)


# ============================================================
# WEIGHT BY CATEGORY
# ============================================================

st.markdown(
    '<div class="section-heading">⚖️ Weight by Category</div>',
    unsafe_allow_html=True
)

weight_by_category = (
    df.groupby("Category")["Weight (kg)"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots()

ax.bar(
    weight_by_category.index,
    weight_by_category.values
)

ax.set_xlabel("Waste Category")
ax.set_ylabel("Weight (kg)")
ax.set_title("Total Waste Weight by Category")

plt.xticks(rotation=30)

st.pyplot(fig)


# ============================================================
# PERCENTAGE DISTRIBUTION
# ============================================================

st.markdown(
    '<div class="section-heading">🥧 Waste Composition</div>',
    unsafe_allow_html=True
)

percentage = (
    weight_by_category /
    weight_by_category.sum()
    * 100
)

fig, ax = plt.subplots()

ax.pie(
    percentage.values,
    labels=percentage.index,
    autopct="%1.1f%%"
)

ax.set_title(
    "Waste Composition by Weight"
)

st.pyplot(fig)


# ============================================================
# AUTOMATIC INSIGHTS
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">🧠 Automatic Insights</div>',
    unsafe_allow_html=True
)

highest_category = weight_by_category.idxmax()

highest_category_weight = weight_by_category.max()

st.info(
    f"📌 **{highest_category}** represents the largest amount "
    f"of recorded waste by weight: **{highest_category_weight:.2f} kg**."
)

st.info(
    f"🔎 The most frequently recorded category is "
    f"**{most_common}**."
)


# Recycling insight

if recycling_rate >= 50:

    st.success(
        f"🌱 More than half of your recorded waste "
        f"({recycling_rate:.1f}%) falls into potentially recyclable categories."
    )

elif recycling_rate >= 25:

    st.warning(
        f"♻️ About {recycling_rate:.1f}% of recorded waste "
        f"is potentially recyclable."
    )

else:

    st.warning(
        f"🌍 Only {recycling_rate:.1f}% of recorded waste "
        f"is currently classified as potentially recyclable."
    )


# ============================================================
# DAILY TREND
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">📅 Waste Trend Over Time</div>',
    unsafe_allow_html=True
)

daily_weight = (
    df.groupby(
        df["Date"].dt.date
    )["Weight (kg)"]
    .sum()
)

if len(daily_weight) >= 2:

    fig, ax = plt.subplots()

    ax.plot(
        daily_weight.index,
        daily_weight.values,
        marker="o"
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Waste Weight (kg)")
    ax.set_title("Waste Weight Over Time")

    plt.xticks(rotation=30)

    st.pyplot(fig)

else:

    st.info(
        "Add waste entries on different dates to see a time trend."
    )


# ============================================================
# CATEGORY FILTER
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">🔎 Explore Your Data</div>',
    unsafe_allow_html=True
)

categories = [
    "All"
] + sorted(
    df["Category"].unique().tolist()
)

selected_category = st.selectbox(
    "Filter by category",
    categories
)

if selected_category == "All":

    filtered_df = df

else:

    filtered_df = df[
        df["Category"] == selected_category
    ]

st.write(
    f"Showing **{len(filtered_df)}** entries."
)

st.dataframe(
    filtered_df,
    use_container_width=True
)


# ============================================================
# DOWNLOAD DATA
# ============================================================

st.divider()

st.markdown(
    '<div class="section-heading">📥 Export Data</div>',
    unsafe_allow_html=True
)

csv = df.to_csv(
    index=False
)

st.download_button(
    label="⬇️ Download Waste Data as CSV",
    data=csv,
    file_name="waste_analytics.csv",
    mime="text/csv",
    use_container_width=True
)


# ============================================================
# FINAL
# ============================================================

st.divider()

st.success(
    "📈 Analytics transforms your recorded waste data "
    "into statistics, patterns and environmental insights."
)