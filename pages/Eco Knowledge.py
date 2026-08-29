import streamlit as st
import random

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Eco Knowledge",
    page_icon="🌍",
    layout="wide"
)

# ============================================================
# WASTEVISION GREEN THEME
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

/* HEADINGS */

h1, h2, h3 {
    color: white !important;
}

/* TEXT */

p, li {
    color: #b7c9bd !important;
}

/* DIVIDERS */

hr {
    border-color: #28563a;
}

/* SELECTBOX */

div[data-baseweb="select"] > div {
    background-color: #10271c;
    border-color: #347149;
}

/* SLIDERS */

div[data-testid="stSlider"] {
    padding-top: 8px;
}

/* BUTTONS */

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

/* METRICS */

div[data-testid="stMetric"] {
    background-color: #0c1b13;
    border: 1px solid #1e422d;
    padding: 18px;
    border-radius: 16px;
}

/* ALERTS */

div[data-testid="stAlert"] {
    border-radius: 16px;
}

/* DATA CARDS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #1e422d !important;
    border-radius: 18px !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA
# ============================================================

COUNTRIES = {
    "🇪🇪 Estonia": {
        "rank": 1,
        "score": 74.79,
        "fact": "Estonia ranked first overall in the 2026 Environmental Performance Index.",
        "focus": "Strong overall environmental performance."
    },
    "🇱🇺 Luxembourg": {
        "rank": 2,
        "score": 74.24,
        "fact": "Luxembourg ranked second overall in the 2026 Environmental Performance Index.",
        "focus": "Particularly strong environmental health performance."
    },
    "🇬🇧 United Kingdom": {
        "rank": 3,
        "score": 71.51,
        "fact": "The United Kingdom ranked third overall in the 2026 Environmental Performance Index.",
        "focus": "Strong performance across several environmental areas."
    },
    "🇫🇮 Finland": {
        "rank": 4,
        "score": 71.04,
        "fact": "Finland ranked fourth overall in the 2026 Environmental Performance Index.",
        "focus": "Strong environmental health and climate-related performance."
    },
    "🇩🇪 Germany": {
        "rank": 6,
        "score": 69.93,
        "fact": "Germany ranked sixth overall in the 2026 Environmental Performance Index.",
        "focus": "Strong performance in environmental health and climate indicators."
    },
    "🇩🇰 Denmark": {
        "rank": 11,
        "score": 66.57,
        "fact": "Denmark ranked 11th overall in the 2026 Environmental Performance Index.",
        "focus": "Known for strong environmental policies and climate action."
    }
}

SDGS = {
    "SDG 11": {
        "title": "Sustainable Cities & Communities",
        "icon": "🏙️",
        "description": "Make cities and human settlements inclusive, safe, resilient and sustainable.",
        "connection": "WasteVision contributes by encouraging better waste sorting and more responsible communities."
    },
    "SDG 12": {
        "title": "Responsible Consumption & Production",
        "icon": "♻️",
        "description": "Promote sustainable consumption and production patterns.",
        "connection": "This is the strongest connection to WasteVision because correct sorting helps responsible waste management."
    },
    "SDG 13": {
        "title": "Climate Action",
        "icon": "🌡️",
        "description": "Take urgent action to combat climate change and its impacts.",
        "connection": "Reducing waste and improving resource use can support broader environmental and climate goals."
    }
}

FACTS = [
    "♻️ Recycling and proper waste separation can help keep useful materials in circulation.",
    "🌱 Organic waste can be processed through composting or other biological treatment systems.",
    "🏙️ Sustainable cities need effective waste management, transportation, energy and water systems.",
    "💡 Sustainability is not only about the environment — it also includes economic and social well-being.",
    "🌍 The United Nations Sustainable Development Goals contain 17 interconnected global goals.",
    "♻️ Responsible consumption means thinking about what we buy, use and throw away.",
    "🌳 Protecting ecosystems is an important part of long-term sustainable development.",
    "💧 Water conservation is an important part of building resilient communities.",
    "☀️ Renewable energy can reduce dependence on fossil fuels.",
    "🚲 Sustainable transport can reduce pollution while providing efficient mobility."
]


# ============================================================
# SESSION STATE
# ============================================================

if "eco_fact" not in st.session_state:
    st.session_state.eco_fact = random.choice(FACTS)

if "city_score" not in st.session_state:
    st.session_state.city_score = 0

if "city_submitted" not in st.session_state:
    st.session_state.city_submitted = False


# ============================================================
# HEADER
# ============================================================

st.caption("🌍 WASTEVISION • EXPLORE")

st.title("Eco Knowledge")

st.write(
    "Learn about sustainability beyond your waste bin. "
    "Explore environmental leaders, the Sustainable Development "
    "Goals, the waste journey and sustainability in the UAE."
)

st.divider()


# ============================================================
# SECTION 1 — SUSTAINABILITY
# ============================================================

st.header("🌱 What is Sustainability?")

col1, col2 = st.columns([2, 1])

with col1:

    st.write(
        """
        Sustainable development means meeting the needs of people
        today without compromising the ability of future generations
        to meet their own needs.

        It involves finding a balance between **environmental
        protection, social well-being and economic development**.

        Sustainability is much bigger than simply recycling. It
        includes the way we produce energy, use water, design cities,
        manufacture products, travel and manage natural resources.
        """
    )

with col2:

    st.info(
        """
        🌍 **The big idea**

        A sustainable future asks:

        **Can we improve life today without damaging the ability
        of future generations to live well?**
        """
    )


# ============================================================
# SECTION 2 — ENVIRONMENTAL LEADERS
# ============================================================

st.divider()

st.header("🏆 Environmental Leaders")

st.write(
    "Explore countries that ranked highly in the 2026 "
    "Environmental Performance Index (EPI)."
)

country = st.selectbox(
    "Choose a country",
    list(COUNTRIES.keys())
)

data = COUNTRIES[country]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌍 EPI Rank",
        f"#{data['rank']}"
    )

with col2:
    st.metric(
        "📊 EPI Score",
        f"{data['score']}"
    )

with col3:
    st.metric(
        "🌱 Focus",
        "Environmental performance"
    )

st.success(data["fact"])

st.info(
    f"💡 **What to learn from it:** {data['focus']}"
)

st.caption(
    "Source: Yale Environmental Performance Index 2026."
)


# ============================================================
# SECTION 3 — SDGs
# ============================================================

st.divider()

st.header("🎯 The Sustainable Development Goals")

st.write(
    """
    The United Nations Sustainable Development Goals are 17
    interconnected goals created as part of the 2030 Agenda
    for Sustainable Development.

    They address environmental, social and economic challenges
    around the world.
    """
)

sdg = st.selectbox(
    "Explore an SDG connected to WasteVision",
    list(SDGS.keys())
)

sdg_data = SDGS[sdg]

st.subheader(
    f"{sdg_data['icon']} {sdg} — {sdg_data['title']}"
)

st.write(
    sdg_data["description"]
)

st.success(
    f"♻️ **WasteVision connection:** {sdg_data['connection']}"
)


# ============================================================
# SECTION 4 — WASTE JOURNEY
# ============================================================

st.divider()

st.header("♻️ What Happens to Waste?")

st.write(
    "Waste does not simply disappear after it leaves your hands."
)

steps = [
    (
        "01",
        "🗑️",
        "Dispose",
        "A person places an unwanted item into a waste stream."
    ),
    (
        "02",
        "🚛",
        "Collect",
        "Waste is collected and transported for processing."
    ),
    (
        "03",
        "🔍",
        "Sort",
        "Materials are separated according to their type."
    ),
    (
        "04",
        "♻️",
        "Process",
        "Recoverable materials may be recycled or treated."
    ),
    (
        "05",
        "🌱",
        "Reuse",
        "Materials can return to the economy as new resources."
    )
]

cols = st.columns(5)

for i, (number, icon, title, description) in enumerate(steps):

    with cols[i]:

        st.subheader(icon)

        st.caption(number)

        st.write(f"**{title}**")

        st.write(description)


# ============================================================
# SECTION 5 — UAE
# ============================================================

st.divider()

st.header("🇦🇪 Sustainability in the UAE")

st.write(
    """
    Sustainability is also a national priority in the UAE.

    The UAE's National Framework for Sustainable Development
    provides a comprehensive framework for environmental work
    and supports the achievement of the Sustainable Development Goals.
    """
)

uae_cols = st.columns(5)

uae_topics = [
    ("🌿", "Nature"),
    ("🫁", "Environmental Health"),
    ("🌡️", "Climate Change"),
    ("🦋", "Living Organisms"),
    ("🛡️", "Biosecurity")
]

for i, (icon, title) in enumerate(uae_topics):

    with uae_cols[i]:

        st.subheader(icon)

        st.write(f"**{title}**")


st.success(
    "🌍 WasteVision supports the wider idea of sustainable "
    "communities by encouraging responsible waste identification, "
    "sorting and learning."
)


# ============================================================
# SECTION 6 — DID YOU KNOW?
# ============================================================

st.divider()

st.header("💡 Did You Know?")

st.info(
    st.session_state.eco_fact
)

if st.button("🔄 Show Another Fact"):

    st.session_state.eco_fact = random.choice(FACTS)

    st.rerun()


# ============================================================
# SECTION 7 — BUILD A SUSTAINABLE CITY
# ============================================================

st.divider()

st.header("🏙️ Build Your Sustainable City")

st.write(
    """
    Imagine you are designing a city from scratch.

    You have a limited sustainability budget. Decide how strongly
    your city should invest in different environmental systems.
    """
)

col1, col2 = st.columns(2)

with col1:

    waste = st.slider(
        "♻️ Waste Management",
        0,
        20,
        10
    )

    energy = st.slider(
        "☀️ Renewable Energy",
        0,
        20,
        10
    )

    transport = st.slider(
        "🚇 Sustainable Transport",
        0,
        20,
        10
    )

with col2:

    water = st.slider(
        "💧 Water Conservation",
        0,
        20,
        10
    )

    green = st.slider(
        "🌳 Green Spaces",
        0,
        20,
        10
    )

    education = st.slider(
        "📚 Environmental Education",
        0,
        20,
        10
    )


# ============================================================
# CITY SCORE
# ============================================================

total = (
    waste +
    energy +
    transport +
    water +
    green +
    education
)

st.metric(
    "🌍 Sustainability Investment",
    f"{total} / 120"
)

if st.button(
    "🏙️ Evaluate My City",
    use_container_width=True
):

    st.session_state.city_score = total
    st.session_state.city_submitted = True


if st.session_state.city_submitted:

    score = st.session_state.city_score

    if score >= 100:

        st.success(
            f"🌟 Outstanding! Your city scored {score}/120. "
            "You are prioritising sustainability across multiple systems."
        )

    elif score >= 75:

        st.info(
            f"🌱 Strong design! Your city scored {score}/120. "
            "There is a good balance between different sustainability areas."
        )

    elif score >= 50:

        st.warning(
            f"🏙️ Decent start! Your city scored {score}/120. "
            "Consider increasing investment in some environmental systems."
        )

    else:

        st.error(
            f"🌍 Your city scored {score}/120. "
            "There is significant room for improvement."
        )


# ============================================================
# FINAL MESSAGE
# ============================================================

st.divider()

st.header("🌱 Small Actions. Bigger Goals.")

st.write(
    """
    WasteVision begins with something simple:

    **Identify the waste → Sort it correctly → Understand why it matters.**

    But sustainable development goes much further.

    The choices made by individuals, communities, businesses and
    governments all contribute to the future of our planet.
    """
)

st.caption(
    "Educational information based on the United Nations Sustainable "
    "Development Goals, the UAE Government's sustainability framework, "
    "and the Yale Environmental Performance Index."
)