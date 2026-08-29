import streamlit as st

st.set_page_config(
    page_title="Sorting Guide",
    page_icon="📚",
    layout="wide"
)

# ============================================================
# GREEN WASTEVISION THEME
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

/* Main headings */

h1, h2, h3 {
    color: white !important;
}

/* Normal text */

p, li {
    color: #b7c9bd !important;
}

/* Selectbox */

div[data-baseweb="select"] > div {
    background-color: #10271c;
    border-color: #347149;
}

/* Divider */

hr {
    border-color: #28563a;
}

/* Success */

div[data-testid="stAlert"] {
    border-radius: 16px;
}

/* Buttons */

.stButton > button {
    background-color: #173522;
    color: #71e58b;
    border: 1px solid #347149;
    border-radius: 12px;
}

.stButton > button:hover {
    border-color: #71e58b;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.caption("♻️ WASTEVISION • LEARN")

st.title("Waste Sorting Guide")

st.write(
    "Learn how to identify, separate and dispose of common "
    "types of waste correctly."
)

st.divider()


# ============================================================
# CATEGORY SELECTOR
# ============================================================

st.subheader("🔎 Choose a Waste Category")

category = st.selectbox(
    "Select a waste category",
    [
        "Plastic",
        "Paper",
        "Glass",
        "Metal",
        "Organic"
    ]
)


# ============================================================
# GUIDE DATA
# ============================================================

guides = {
    "Plastic": {
        "accepted": [
            "Clean plastic bottles",
            "Plastic containers",
            "Food packaging where accepted"
        ],
        "not_accepted": [
            "Heavily contaminated plastic",
            "Certain plastic bags",
            "Mixed-material packaging"
        ],
        "tip": (
            "Rinse plastic containers and remove leftover "
            "food before recycling."
        )
    },

    "Paper": {
        "accepted": [
            "Newspapers",
            "Cardboard",
            "Office paper",
            "Paper bags"
        ],
        "not_accepted": [
            "Wet paper",
            "Greasy paper",
            "Tissues and used paper towels"
        ],
        "tip": (
            "Keep paper clean and dry so it can be recycled "
            "properly."
        )
    },

    "Glass": {
        "accepted": [
            "Glass bottles",
            "Glass jars",
            "Clear glass containers"
        ],
        "not_accepted": [
            "Broken ceramics",
            "Mirrors",
            "Window glass"
        ],
        "tip": (
            "Empty and rinse glass containers before placing "
            "them in the appropriate recycling collection."
        )
    },

    "Metal": {
        "accepted": [
            "Aluminium cans",
            "Steel cans",
            "Clean metal containers"
        ],
        "not_accepted": [
            "Paint cans with residue",
            "Sharp hazardous metal items",
            "Electronic components"
        ],
        "tip": (
            "Empty and rinse metal containers before recycling."
        )
    },

    "Organic": {
        "accepted": [
            "Fruit and vegetable scraps",
            "Food leftovers",
            "Coffee grounds",
            "Garden waste"
        ],
        "not_accepted": [
            "Plastic packaging",
            "Glass",
            "Metal"
        ],
        "tip": (
            "Keep organic waste free from plastic and other "
            "non-biodegradable materials."
        )
    }
}

guide = guides[category]


# ============================================================
# SELECTED CATEGORY
# ============================================================

st.subheader(f"♻️ {category} Waste")

col1, col2 = st.columns(2)


# ============================================================
# ACCEPTED
# ============================================================

with col1:

    st.success("✅ ACCEPTED")

    for item in guide["accepted"]:
        st.write(f"✓ {item}")


# ============================================================
# NOT ACCEPTED
# ============================================================

with col2:

    st.error("❌ NOT ACCEPTED")

    for item in guide["not_accepted"]:
        st.write(f"✕ {item}")


# ============================================================
# SORTING TIP
# ============================================================

st.divider()

st.subheader("💡 Sorting Tip")

st.info(guide["tip"])


# ============================================================
# FINAL MESSAGE
# ============================================================

st.divider()

st.success(
    "🌍 Correct waste segregation helps reduce contamination "
    "and supports more effective recycling."
)