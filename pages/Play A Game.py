import streamlit as st
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sort It Right",
    page_icon="🎮",
    layout="wide"
)

# ============================================================
# WASTEVISION THEME
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

/* METRIC CARDS */

div[data-testid="stMetric"] {
    background-color: #0c1b13;
    border: 1px solid #1e422d;
    border-radius: 18px;
    padding: 18px;
}

/* BUTTONS */

.stButton > button {
    background-color: #10271c;
    color: #71e58b;
    border: 1px solid #347149;
    border-radius: 13px;
    min-height: 48px;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #71e58b;
    color: white;
}

/* INFO / SUCCESS / WARNING / ERROR */

div[data-testid="stAlert"] {
    border-radius: 16px;
}

/* PROGRESS */

div[data-testid="stProgressBar"] {
    padding-top: 5px;
}

/* SELECTED GAME AREA */

.game-item {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(113,229,139,0.08),
            transparent 50%
        ),
        #0c1b13;
    border: 1px solid #28563a;
    border-radius: 24px;
    padding: 35px;
    text-align: center;
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# WASTE DATABASE
# ============================================================

WASTE_ITEMS = [
    {
        "name": "Plastic Bottle",
        "emoji": "🥤",
        "category": "Recyclable",
        "explanation": "Plastic bottles are commonly recyclable when they are emptied and properly prepared.",
        "tip": "Empty and rinse the bottle before recycling."
    },
    {
        "name": "Banana Peel",
        "emoji": "🍌",
        "category": "Organic",
        "explanation": "Banana peels are biodegradable organic waste.",
        "tip": "Place it in an appropriate compost or organic-waste collection."
    },
    {
        "name": "Newspaper",
        "emoji": "📰",
        "category": "Recyclable",
        "explanation": "Clean and dry newspaper is generally suitable for paper recycling.",
        "tip": "Keep paper dry and free from food contamination."
    },
    {
        "name": "AA Battery",
        "emoji": "🔋",
        "category": "Hazardous",
        "explanation": "Batteries require special handling and should not normally be placed with ordinary household waste.",
        "tip": "Use an approved battery collection point."
    },
    {
        "name": "Glass Jar",
        "emoji": "🫙",
        "category": "Recyclable",
        "explanation": "Many glass jars can be recycled after being emptied and cleaned.",
        "tip": "Rinse the jar and follow your local glass-recycling rules."
    },
    {
        "name": "Apple Core",
        "emoji": "🍎",
        "category": "Organic",
        "explanation": "An apple core is biodegradable organic material.",
        "tip": "Place it in compost or an organic-waste stream where available."
    },
    {
        "name": "Aluminium Can",
        "emoji": "🥫",
        "category": "Recyclable",
        "explanation": "Aluminium cans are widely recyclable.",
        "tip": "Empty the can before recycling."
    },
    {
        "name": "Cardboard Box",
        "emoji": "📦",
        "category": "Recyclable",
        "explanation": "Clean and dry cardboard is commonly accepted for recycling.",
        "tip": "Flatten the box and remove excessive contamination."
    },
    {
        "name": "Food Scraps",
        "emoji": "🍽️",
        "category": "Organic",
        "explanation": "Food scraps are biodegradable and can often be composted or processed as organic waste.",
        "tip": "Keep food waste separate from packaging."
    },
    {
        "name": "Broken Ceramic Cup",
        "emoji": "☕",
        "category": "General",
        "explanation": "Ceramics are not generally processed with ordinary glass recycling.",
        "tip": "Follow local guidance for ceramic and broken household items."
    },
    {
        "name": "Old Paint Can",
        "emoji": "🪣",
        "category": "Hazardous",
        "explanation": "Paint and paint containers may require special disposal depending on their contents.",
        "tip": "Follow local hazardous-waste collection guidance."
    },
    {
        "name": "Plastic Food Wrapper",
        "emoji": "🍫",
        "category": "General",
        "explanation": "Many flexible food wrappers are not accepted in standard recycling systems.",
        "tip": "Check local recycling rules before disposal."
    }
]

CATEGORIES = [
    "♻️ Recyclable",
    "🌱 Organic",
    "🗑️ General",
    "⚠️ Hazardous"
]

CATEGORY_MAP = {
    "♻️ Recyclable": "Recyclable",
    "🌱 Organic": "Organic",
    "🗑️ General": "General",
    "⚠️ Hazardous": "Hazardous"
}


# ============================================================
# SESSION STATE
# ============================================================

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "game_items" not in st.session_state:
    st.session_state.game_items = []

if "game_index" not in st.session_state:
    st.session_state.game_index = 0

if "game_score" not in st.session_state:
    st.session_state.game_score = 0

if "game_answered" not in st.session_state:
    st.session_state.game_answered = False

if "game_last_answer" not in st.session_state:
    st.session_state.game_last_answer = ""

if "game_correct" not in st.session_state:
    st.session_state.game_correct = 0

if "game_wrong" not in st.session_state:
    st.session_state.game_wrong = 0


# ============================================================
# FUNCTIONS
# ============================================================

def start_game():

    st.session_state.game_items = random.sample(
        WASTE_ITEMS,
        10
    )

    st.session_state.game_index = 0
    st.session_state.game_score = 0
    st.session_state.game_correct = 0
    st.session_state.game_wrong = 0
    st.session_state.game_answered = False
    st.session_state.game_last_answer = ""
    st.session_state.game_started = True


def restart_game():
    start_game()


def submit_answer(answer):

    if st.session_state.game_answered:
        return

    current_item = st.session_state.game_items[
        st.session_state.game_index
    ]

    correct_answer = current_item["category"]

    st.session_state.game_last_answer = answer
    st.session_state.game_answered = True

    if answer == correct_answer:

        st.session_state.game_score += 10
        st.session_state.game_correct += 1

    else:

        st.session_state.game_wrong += 1


def next_question():

    st.session_state.game_index += 1
    st.session_state.game_answered = False
    st.session_state.game_last_answer = ""


# ============================================================
# TITLE
# ============================================================

st.caption("🎮 WASTEVISION • CHALLENGE")

st.title("Sort It Right!")

st.write(
    "Test your waste-sorting skills. Look at each item, "
    "choose the correct category and learn why your answer matters."
)

st.divider()


# ============================================================
# START SCREEN
# ============================================================

if not st.session_state.game_started:

    st.header("🌱 Ready to play?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Questions", "10")

    with col2:
        st.metric("Points", "100")

    with col3:
        st.metric("Categories", "4")

    st.divider()

    st.info(
        """
        **How to play**

        1. Look at the waste item.
        2. Choose the correct category.
        3. Get 10 points for a correct answer.
        4. Learn why the answer is correct.
        5. Complete all 10 rounds.
        """
    )

    if st.button(
        "🚀 START GAME",
        use_container_width=True
    ):

        start_game()
        st.rerun()

    st.stop()


# ============================================================
# GAME COMPLETE
# ============================================================

if st.session_state.game_index >= 10:

    score = st.session_state.game_score
    correct = st.session_state.game_correct

    st.success("🎉 GAME COMPLETE!")

    st.header("🏆 Your Result")

    st.metric(
        "Final Score",
        f"{score} / 100"
    )

    st.write(
        f"You correctly sorted **{correct} out of 10 items**."
    )

    st.progress(
        correct / 10,
        text=f"{correct}/10 correct"
    )

    if correct == 10:

        st.balloons()

        st.success(
            "🌟 PERFECT SCORE! You're a Waste Sorting Champion!"
        )

    elif correct >= 8:

        st.success(
            "🌱 Excellent work! You have strong waste-sorting knowledge."
        )

    elif correct >= 5:

        st.info(
            "♻️ Good effort! A little more practice will improve your score."
        )

    else:

        st.warning(
            "🌍 Keep learning! The Sorting Guide can help you improve."
        )

    st.divider()

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        st.metric(
            "✅ Correct",
            correct
        )

    with result_col2:

        st.metric(
            "❌ Incorrect",
            st.session_state.game_wrong
        )

    st.divider()

    st.subheader("🎯 Want another challenge?")

    if st.button(
        "🔄 PLAY AGAIN",
        use_container_width=True
    ):

        restart_game()
        st.rerun()

    st.stop()


# ============================================================
# CURRENT QUESTION
# ============================================================

current_item = st.session_state.game_items[
    st.session_state.game_index
]

question_number = st.session_state.game_index + 1


# ============================================================
# GAME HEADER
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "🏆 Score",
        st.session_state.game_score
    )

with col2:

    st.metric(
        "🎯 Question",
        f"{question_number}/10"
    )

with col3:

    st.metric(
        "✅ Correct",
        st.session_state.game_correct
    )


st.progress(
    question_number / 10,
    text=f"Round {question_number} of 10"
)

st.divider()


# ============================================================
# WASTE ITEM
# ============================================================

st.markdown(
    "<div class='game-item'>",
    unsafe_allow_html=True
)

st.markdown(
    f"# {current_item['emoji']}"
)

st.markdown(
    f"## {current_item['name']}"
)

st.markdown(
    "### Where does this item belong?"
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ============================================================
# ANSWER BUTTONS
# ============================================================

answer_cols = st.columns(4)

for i, display_category in enumerate(CATEGORIES):

    with answer_cols[i]:

        disabled = st.session_state.game_answered

        if st.button(
            display_category,
            use_container_width=True,
            disabled=disabled
        ):

            answer = CATEGORY_MAP[display_category]

            submit_answer(answer)

            st.rerun()


# ============================================================
# FEEDBACK
# ============================================================

if st.session_state.game_answered:

    correct_answer = current_item["category"]
    user_answer = st.session_state.game_last_answer

    st.divider()

    if user_answer == correct_answer:

        st.success(
            f"🎉 Correct! **{current_item['name']}** belongs "
            f"to the **{correct_answer}** category."
        )

    else:

        st.error(
            f"❌ Not quite! The correct category is "
            f"**{correct_answer}**."
        )

    st.info(
        f"💡 **Why?** {current_item['explanation']}"
    )

    st.warning(
        f"🌱 **Tip:** {current_item['tip']}"
    )

    if st.button(
        "➡️ NEXT ITEM",
        use_container_width=True
    ):

        next_question()
        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "♻️ WasteVision • Sort responsibly • Build sustainable communities"
)