import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Waste Tracker",
    page_icon="📝",
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

.tracker-label {
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
    margin-top: 32px;
    margin-bottom: 18px;
}

.tracker-box {
    background: linear-gradient(145deg, #10271c, #0a1711);
    border: 1px solid #1e422d;
    border-radius: 22px;
    padding: 28px;
    margin-top: 25px;
}

.history-box {
    background: #0c1b13;
    border: 1px solid #1b3927;
    border-radius: 18px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="tracker-label">♻️ WASTEVISION</div>',
    unsafe_allow_html=True
)

st.title("Waste Tracker")

st.write(
    "Record the waste you dispose of and build a clearer "
    "picture of your everyday waste habits."
)


# ============================================================
# CREATE HISTORY
# ============================================================

if "waste_entries" not in st.session_state:
    st.session_state.waste_entries = []


# ============================================================
# QUICK OVERVIEW
# ============================================================

total_entries = len(st.session_state.waste_entries)

total_weight = sum(
    entry["Weight (kg)"]
    for entry in st.session_state.waste_entries
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📋 Total Entries",
        total_entries
    )

with col2:
    st.metric(
        "♻️ Total Waste",
        f"{total_weight:.2f} kg"
    )


# ============================================================
# LOG WASTE
# ============================================================

st.markdown(
    '<div class="section-title">➕ Log New Waste</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tracker-box">',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")


with col1:

    category = st.selectbox(
        "Waste Category",
        [
            "Plastic",
            "Paper",
            "Glass",
            "Metal",
            "Organic",
            "General",
            "Hazardous"
        ]
    )

    item_name = st.text_input(
        "Item Name",
        placeholder="Example: Plastic bottle"
    )


with col2:

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.0,
        step=0.1
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        step=1
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ADD ENTRY
# ============================================================

if st.button(
    "➕ Add Waste Entry",
    use_container_width=True
):

    if item_name.strip() == "":
        st.warning(
            "Please enter the item name."
        )

    elif weight <= 0:
        st.warning(
            "Please enter a weight greater than 0."
        )

    else:

        entry = {
            "Date": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

            "Category": category,

            "Item": item_name,

            "Weight (kg)": weight,

            "Quantity": quantity
        }

        st.session_state.waste_entries.append(
            entry
        )

        st.success(
            "✅ Waste entry added successfully!"
        )

        st.rerun()


# ============================================================
# WASTE HISTORY
# ============================================================

st.markdown(
    '<div class="section-title">📋 Waste History</div>',
    unsafe_allow_html=True
)

if st.session_state.waste_entries:

    st.markdown(
        '<div class="history-box">',
        unsafe_allow_html=True
    )

    st.dataframe(
        st.session_state.waste_entries,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

else:

    st.info(
        "No waste entries recorded yet. "
        "Add your first entry above to start tracking."
    )


# ============================================================
# ECO MESSAGE
# ============================================================

if total_entries > 0:

    st.markdown(
        '<div class="section-title">🌱 Keep Going</div>',
        unsafe_allow_html=True
    )

    st.success(
        f"You have recorded {total_entries} waste "
        f"entries totaling {total_weight:.2f} kg. "
        "Keep tracking to understand your waste habits better!"
    )