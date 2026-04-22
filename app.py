import random

import streamlit as st
from questions import ALL_CATEGORIES, QUESTIONS

# ─────────────────────────────────────────────────────────────────────────────
# Page config (must be first Streamlit call)
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Tufin QA Interview Prep",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# Custom CSS — Tufin-inspired dark blue theme
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Google Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* ── Root palette ── */
    :root {
        --tufin-dark:    #0a1628;
        --tufin-navy:    #0d2045;
        --tufin-blue:    #1a4b8c;
        --tufin-accent:  #2e7df7;
        --tufin-bright:  #5aa3ff;
        --tufin-teal:    #00c2cb;
        --tufin-text:    #e8edf5;
        --tufin-muted:   #8fa3c0;
        --tufin-success: #22c55e;
        --tufin-error:   #ef4444;
        --tufin-warning: #f59e0b;
        --card-bg:       #111f38;
        --card-border:   #1e3a6e;
    }

    /* ── Global ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        color: var(--tufin-text) !important;
    }
    .stApp {
        background: linear-gradient(135deg, var(--tufin-dark) 0%, var(--tufin-navy) 100%) !important;
        min-height: 100vh;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1a30 0%, #0d2045 100%) !important;
        border-right: 1px solid var(--card-border) !important;
    }
    [data-testid="stSidebar"] * {
        color: var(--tufin-text) !important;
    }
    [data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {
        background-color: var(--tufin-blue) !important;
    }

    /* ── Headings ── */
    h1 {
        color: var(--tufin-bright) !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }
    h2 {
        color: var(--tufin-teal) !important;
        font-weight: 600 !important;
    }
    h3 {
        color: var(--tufin-bright) !important;
        font-weight: 600 !important;
    }

    /* ── Cards ── */
    .quiz-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 14px;
        padding: 28px 32px;
        margin: 12px 0;
        box-shadow: 0 4px 24px rgba(0,0,0,0.4);
    }
    .question-text {
        font-size: 1.15rem;
        font-weight: 500;
        color: var(--tufin-text);
        line-height: 1.6;
        margin-bottom: 6px;
    }
    .category-badge {
        display: inline-block;
        background: rgba(46,125,247,0.18);
        border: 1px solid rgba(46,125,247,0.4);
        color: var(--tufin-bright);
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 20px;
        margin-bottom: 16px;
    }

    /* ── Feedback boxes ── */
    .feedback-correct {
        background: rgba(34,197,94,0.12);
        border: 1px solid rgba(34,197,94,0.45);
        border-radius: 10px;
        padding: 16px 20px;
        margin-top: 16px;
    }
    .feedback-incorrect {
        background: rgba(239,68,68,0.12);
        border: 1px solid rgba(239,68,68,0.45);
        border-radius: 10px;
        padding: 16px 20px;
        margin-top: 16px;
    }
    .feedback-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .feedback-explanation {
        font-size: 0.9rem;
        color: #b8cce4;
        line-height: 1.55;
        margin-top: 8px;
    }
    .correct-answer-label {
        font-size: 0.85rem;
        color: var(--tufin-success);
        font-weight: 600;
        margin-top: 8px;
    }

    /* ── Score card ── */
    .score-card {
        background: linear-gradient(135deg, #0d2045 0%, #112240 100%);
        border: 1px solid var(--tufin-blue);
        border-radius: 18px;
        padding: 36px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    }
    .score-number {
        font-size: 4rem;
        font-weight: 800;
        color: var(--tufin-bright);
        line-height: 1;
    }
    .score-label {
        font-size: 1rem;
        color: var(--tufin-muted);
        margin-top: 4px;
    }
    .score-pct {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 10px;
    }

    /* ── Progress bar override ── */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--tufin-accent) 0%, var(--tufin-teal) 100%) !important;
        border-radius: 4px;
    }
    .stProgress > div > div {
        background-color: #1a2e50 !important;
        border-radius: 4px;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, var(--tufin-accent) 0%, #1a6aef 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 10px 24px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 12px rgba(46,125,247,0.35) !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 20px rgba(46,125,247,0.55) !important;
        opacity: 0.95 !important;
    }
    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ── Radio buttons ── */
    .stRadio > div {
        gap: 8px !important;
    }
    .stRadio > div > label {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 8px !important;
        padding: 10px 16px !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
        color: var(--tufin-text) !important;
    }
    .stRadio > div > label:hover {
        background: rgba(46,125,247,0.12) !important;
        border-color: var(--tufin-accent) !important;
    }

    /* ── Selectbox / multiselect ── */
    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        background: #0d1f3c !important;
        border: 1px solid var(--card-border) !important;
        color: var(--tufin-text) !important;
    }

    /* ── Table ── */
    .stDataFrame, table {
        background: var(--card-bg) !important;
    }

    /* ── Dividers ── */
    hr {
        border-color: var(--card-border) !important;
        margin: 24px 0 !important;
    }

    /* ── Metrics ── */
    [data-testid="stMetricValue"] {
        color: var(--tufin-bright) !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: var(--tufin-muted) !important;
    }

    /* ── Expander ── */
    .streamlit-expanderHeader {
        background: var(--card-bg) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 8px !important;
        color: var(--tufin-bright) !important;
        font-weight: 600 !important;
    }
    .streamlit-expanderContent {
        background: rgba(13,32,69,0.6) !important;
        border: 1px solid var(--card-border) !important;
        border-top: none !important;
    }

    /* ── Welcome banner ── */
    .welcome-banner {
        background: linear-gradient(135deg, #0d2045 0%, #0b3060 50%, #0d2045 100%);
        border: 1px solid rgba(46,125,247,0.3);
        border-radius: 16px;
        padding: 32px 36px;
        text-align: center;
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }
    .welcome-banner::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 50%, rgba(46,125,247,0.08) 0%, transparent 60%);
        pointer-events: none;
    }
    .welcome-subtitle {
        color: var(--tufin-muted);
        font-size: 0.95rem;
        margin-top: 8px;
        line-height: 1.5;
    }

    /* ── Instruction list ── */
    .instruction-box {
        background: rgba(255,255,255,0.03);
        border: 1px solid var(--card-border);
        border-radius: 12px;
        padding: 20px 24px;
        margin: 16px 0;
    }
    .instruction-box li {
        color: var(--tufin-muted);
        margin-bottom: 8px;
        font-size: 0.92rem;
        line-height: 1.5;
    }
    .instruction-box li span {
        color: var(--tufin-text);
    }

    /* ── Review item ── */
    .review-item {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 16px;
    }
    .review-correct {
        border-left: 4px solid var(--tufin-success) !important;
    }
    .review-incorrect {
        border-left: 4px solid var(--tufin-error) !important;
    }
    .review-q-num {
        font-size: 0.75rem;
        color: var(--tufin-muted);
        font-weight: 600;
        letter-spacing: 0.6px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .review-q-text {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 10px;
        line-height: 1.5;
    }
    .review-answer-row {
        font-size: 0.875rem;
        margin: 3px 0;
    }
    .option-correct {
        color: var(--tufin-success);
        font-weight: 600;
    }
    .option-wrong {
        color: var(--tufin-error);
        font-weight: 600;
    }
    .option-neutral {
        color: var(--tufin-muted);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# Session state initialisation
# ─────────────────────────────────────────────────────────────────────────────
DEFAULTS = {
    "page": "home",  # home | quiz | results | review
    "questions": [],  # active question list for this session
    "current_idx": 0,  # index into active list
    "answers": {},  # {idx: selected_option_text}
    "submitted": {},  # {idx: True}  — whether this Q was submitted
    "score": 0,
    "selected_categories": list(ALL_CATEGORIES),
    "question_count": "20",
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
def start_quiz():
    cats = st.session_state.selected_categories
    pool = [q for q in QUESTIONS if q["category"] in cats]
    random.shuffle(pool)
    count_raw = st.session_state.question_count
    if count_raw == "All":
        count = len(pool)
    else:
        count = min(int(count_raw), len(pool))
    st.session_state.questions = pool[:count]
    st.session_state.current_idx = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.score = 0
    st.session_state.page = "quiz"


def go_home():
    st.session_state.page = "home"


def go_review():
    st.session_state.page = "review"


def go_results():
    st.session_state.page = "results"


def letter_for(idx: int) -> str:
    return ["A", "B", "C", "D"][idx] if idx < 4 else "?"


def compute_score():
    total = 0
    for i, q in enumerate(st.session_state.questions):
        if i in st.session_state.answers:
            if st.session_state.answers[i] == q["answer"]:
                total += 1
    return total


def category_breakdown():
    results = {}
    for i, q in enumerate(st.session_state.questions):
        cat = q["category"]
        if cat not in results:
            results[cat] = {"correct": 0, "total": 0}
        results[cat]["total"] += 1
        if i in st.session_state.answers and st.session_state.answers[i] == q["answer"]:
            results[cat]["correct"] += 1
    return results


# ─────────────────────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style='text-align:center; padding: 8px 0 20px;'>
            <div style='font-size:2.4rem;'>🛡️</div>
            <div style='font-size:1.05rem; font-weight:700; color:#5aa3ff; letter-spacing:0.5px;'>
                Tufin QA Prep
            </div>
            <div style='font-size:0.78rem; color:#8fa3c0; margin-top:2px;'>
                Interview Practice Quiz
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    st.markdown(
        "<p style='font-size:0.8rem; font-weight:600; color:#5aa3ff; "
        "letter-spacing:0.8px; text-transform:uppercase; margin-bottom:6px;'>"
        "📚 Categories</p>",
        unsafe_allow_html=True,
    )
    selected_cats = st.multiselect(
        "Select categories",
        options=ALL_CATEGORIES,
        default=st.session_state.selected_categories,
        label_visibility="collapsed",
    )
    if selected_cats:
        st.session_state.selected_categories = selected_cats

    st.markdown(
        "<p style='font-size:0.8rem; font-weight:600; color:#5aa3ff; "
        "letter-spacing:0.8px; text-transform:uppercase; margin-top:16px; margin-bottom:6px;'>"
        "🔢 Question Count</p>",
        unsafe_allow_html=True,
    )
    q_count = st.selectbox(
        "Question count",
        options=["10", "15", "20", "All"],
        index=["10", "15", "20", "All"].index(st.session_state.question_count),
        label_visibility="collapsed",
    )
    st.session_state.question_count = q_count

    # pool size info
    pool_size = len(
        [q for q in QUESTIONS if q["category"] in st.session_state.selected_categories]
    )
    st.markdown(
        f"<p style='font-size:0.78rem; color:#8fa3c0; margin-top:6px;'>"
        f"📊 {pool_size} questions available in selected categories</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    if st.session_state.page != "home":
        if st.button("🏠 Home", use_container_width=True):
            go_home()
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    if st.session_state.page in ("results", "review"):
        if st.button("🔄 New Quiz", use_container_width=True):
            start_quiz()
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    st.markdown(
        "<div style='margin-top:32px; font-size:0.72rem; color:#4a6080; text-align:center; line-height:1.6;'>"
        "Built for Tufin QA<br>Automation Engineer prep<br>"
        "<span style='color:#2e7df7;'>150+ questions · 6 categories</span>"
        "</div>",
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: HOME
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "home":
    st.markdown(
        """
        <div class='welcome-banner'>
            <div style='font-size:2.8rem; margin-bottom:8px;'>🛡️</div>
            <h1 style='margin:0; font-size:1.9rem;'>Tufin QA Interview Prep</h1>
            <p class='welcome-subtitle'>
                Master QA fundamentals, networking, Java debugging, APIs, SQL, Check Point,
                and behavioral strategy — all in one interactive quiz.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Stats row
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total Questions", len(QUESTIONS))
    with c2:
        st.metric("Categories", len(ALL_CATEGORIES))
    with c3:
        st.metric("Topics Covered", "6")

    st.markdown("---")

    st.markdown("### 📋 How It Works")
    st.markdown(
        """
        <div class='instruction-box'>
        <ul style='list-style:none; padding:0; margin:0;'>
            <li>🎯 <span>Select which <b>categories</b> to include from the sidebar</span></li>
            <li>🔢 <span>Choose your <b>question count</b> (10 / 15 / 20 / All)</span></li>
            <li>📝 <span>Answer each question using the <b>radio buttons</b> — one at a time</span></li>
            <li>✅ <span>Submit each answer to see <b>immediate feedback</b> + explanation</span></li>
            <li>📊 <span>Review your <b>score breakdown</b> by category at the end</span></li>
            <li>🔄 <span>Questions are <b>randomly shuffled</b> every new quiz</span></li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📚 Categories Covered")
    cat_icons = {
        "QA Fundamentals": "🧪",
        "Tufin & Networking": "🌐",
        "Java & Debugging": "☕",
        "API, SQL & Linux": "🔌",
        "Check Point Networking": "🔒",
        "Behavioral & Strategy": "🎯",
    }
    cols = st.columns(2)
    for i, cat in enumerate(ALL_CATEGORIES):
        icon = cat_icons.get(cat, "📌")
        count = len([q for q in QUESTIONS if q["category"] == cat])
        cols[i % 2].markdown(
            f"<div style='background:rgba(255,255,255,0.03); border:1px solid #1e3a6e; "
            f"border-radius:8px; padding:10px 14px; margin-bottom:8px;'>"
            f"<span style='font-size:1.1rem;'>{icon}</span> "
            f"<span style='font-weight:600; color:#e8edf5;'>{cat}</span> "
            f"<span style='color:#8fa3c0; font-size:0.83rem;'>({count} questions)</span>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Validate selection
    pool_size = len(
        [q for q in QUESTIONS if q["category"] in st.session_state.selected_categories]
    )
    if not st.session_state.selected_categories:
        st.warning(
            "⚠️ Please select at least one category in the sidebar before starting."
        )
    elif pool_size == 0:
        st.warning("⚠️ No questions found for the selected categories.")
    else:
        count_label = st.session_state.question_count
        if count_label == "All":
            quiz_size = pool_size
        else:
            quiz_size = min(int(count_label), pool_size)
        st.markdown(
            f"<div style='text-align:center; color:#8fa3c0; font-size:0.9rem; margin-bottom:16px;'>"
            f"Ready to quiz on <b style='color:#5aa3ff;'>{quiz_size}</b> questions "
            f"from <b style='color:#5aa3ff;'>{len(st.session_state.selected_categories)}</b> categories"
            f"</div>",
            unsafe_allow_html=True,
        )
        col_btn = st.columns([1, 2, 1])
        with col_btn[1]:
            if st.button("🚀 Start Quiz", use_container_width=True):
                start_quiz()
                st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: QUIZ
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "quiz":
    questions = st.session_state.questions
    idx = st.session_state.current_idx
    total = len(questions)

    if total == 0:
        st.error("No questions loaded. Please go home and start again.")
        st.button("🏠 Home", on_click=go_home)
        st.stop()

    q = questions[idx]
    already_submitted = idx in st.session_state.submitted

    # ── Progress ──────────────────────────────────────────────────────────────
    progress_val = (idx + (1 if already_submitted else 0)) / total
    st.markdown(
        f"<div style='display:flex; justify-content:space-between; "
        f"align-items:center; margin-bottom:4px;'>"
        f"<span style='font-size:0.82rem; color:#8fa3c0;'>Question {idx + 1} of {total}</span>"
        f"<span style='font-size:0.82rem; color:#8fa3c0;'>"
        f"{idx}/{total} completed</span>"
        f"</div>",
        unsafe_allow_html=True,
    )
    st.progress(progress_val)
    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

    # ── Question card ─────────────────────────────────────────────────────────
    st.markdown(
        f"<div class='quiz-card'>"
        f"<div class='category-badge'>{q['category']}</div>"
        f"<div class='question-text'>{q['question']}</div>"
        f"</div>",
        unsafe_allow_html=True,
    )

    # ── Answer choices ────────────────────────────────────────────────────────
    options_display = [f"{letter_for(i)}.  {opt}" for i, opt in enumerate(q["options"])]
    # Map displayed label → raw option text
    label_to_option = {
        f"{letter_for(i)}.  {opt}": opt for i, opt in enumerate(q["options"])
    }

    current_selection_label = None
    if idx in st.session_state.answers:
        raw = st.session_state.answers[idx]
        for lbl, opt in label_to_option.items():
            if opt == raw:
                current_selection_label = lbl
                break

    selected_label = st.radio(
        "Choose your answer:",
        options=options_display,
        index=options_display.index(current_selection_label)
        if current_selection_label
        else None,
        key=f"radio_{idx}",
        disabled=already_submitted,
        label_visibility="collapsed",
    )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # ── Submit / Next ─────────────────────────────────────────────────────────
    col_l, col_r = st.columns([1, 1])

    if not already_submitted:
        with col_l:
            if st.button(
                "✅ Submit Answer", use_container_width=True, key=f"submit_{idx}"
            ):
                if selected_label is None:
                    st.warning("⚠️ Please select an answer before submitting.")
                else:
                    raw_answer = label_to_option[selected_label]
                    st.session_state.answers[idx] = raw_answer
                    st.session_state.submitted[idx] = True
                    st.rerun()
    else:
        # Show feedback
        user_raw = st.session_state.answers.get(idx, "")
        is_correct = user_raw == q["answer"]

        if is_correct:
            st.markdown(
                f"<div class='feedback-correct'>"
                f"<div class='feedback-title' style='color:#22c55e;'>✅ Correct!</div>"
                f"<div class='feedback-explanation'>{q['explanation']}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='feedback-incorrect'>"
                f"<div class='feedback-title' style='color:#ef4444;'>❌ Incorrect</div>"
                f"<div class='correct-answer-label'>✔ Correct answer: {q['answer']}</div>"
                f"<div class='feedback-explanation'>{q['explanation']}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        with col_l:
            if idx < total - 1:
                if st.button(
                    "➡️ Next Question", use_container_width=True, key=f"next_{idx}"
                ):
                    st.session_state.current_idx += 1
                    st.rerun()
            else:
                if st.button("🏁 See Results", use_container_width=True, key="finish"):
                    st.session_state.score = compute_score()
                    st.session_state.page = "results"
                    st.rerun()

        with col_r:
            if st.button(
                "🏠 Quit to Home", use_container_width=True, key=f"quit_{idx}"
            ):
                go_home()
                st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: RESULTS
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "results":
    questions = st.session_state.questions
    total = len(questions)
    score = compute_score()
    pct = round((score / total) * 100) if total else 0

    # Emoji + message
    if pct >= 80:
        emoji = "😎"
        grade_label = "Excellent!"
        grade_color = "#22c55e"
        grade_msg = "You're ready for that Tufin interview. Outstanding performance!"
    elif pct >= 60:
        emoji = "🙂"
        grade_label = "Good Job"
        grade_color = "#f59e0b"
        grade_msg = "Solid foundation! Review the missed questions and you'll nail it."
    else:
        emoji = "😬"
        grade_label = "Keep Studying"
        grade_color = "#ef4444"
        grade_msg = "Don't worry — practice makes perfect. Review and try again!"

    # Confetti JS for >80%
    if pct >= 80:
        st.markdown(
            """
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
            <script>
            setTimeout(function(){
                confetti({
                    particleCount: 180,
                    spread: 90,
                    origin: { y: 0.4 },
                    colors: ['#2e7df7','#5aa3ff','#00c2cb','#22c55e','#ffffff']
                });
            }, 300);
            </script>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class='score-card'>
            <div style='font-size:3.5rem; margin-bottom:4px;'>{emoji}</div>
            <div style='font-size:1.2rem; color:#8fa3c0; margin-bottom:4px;'>Quiz Complete!</div>
            <div class='score-number'>{score}<span style='font-size:1.8rem; color:#8fa3c0;'>/{total}</span></div>
            <div class='score-label'>questions correct</div>
            <div class='score-pct' style='color:{grade_color};'>{pct}%</div>
            <div style='font-size:1.1rem; font-weight:600; color:{grade_color}; margin-top:4px;'>{grade_label}</div>
            <div style='font-size:0.9rem; color:#8fa3c0; margin-top:8px;'>{grade_msg}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Category Breakdown ────────────────────────────────────────────────────
    st.markdown("### 📊 Category Breakdown")
    breakdown = category_breakdown()

    for cat, data in breakdown.items():
        c_pct = round((data["correct"] / data["total"]) * 100) if data["total"] else 0
        bar_color = (
            "#22c55e" if c_pct >= 80 else "#f59e0b" if c_pct >= 60 else "#ef4444"
        )
        icon = cat_icons.get(cat, "📌") if "cat_icons" in dir() else "📌"
        st.markdown(
            f"""
            <div style='background:#111f38; border:1px solid #1e3a6e; border-radius:10px;
                        padding:14px 18px; margin-bottom:10px;'>
                <div style='display:flex; justify-content:space-between; align-items:center;
                            margin-bottom:6px;'>
                    <span style='font-weight:600; font-size:0.92rem;'>{cat}</span>
                    <span style='font-size:0.88rem; color:{bar_color}; font-weight:700;'>
                        {data["correct"]}/{data["total"]} ({c_pct}%)
                    </span>
                </div>
                <div style='background:#1a2e50; border-radius:4px; height:6px;'>
                    <div style='background:{bar_color}; width:{c_pct}%; height:6px;
                                border-radius:4px; transition:width 0.5s;'></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Action buttons ────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔍 Review Answers", use_container_width=True):
            go_review()
            st.rerun()
    with col2:
        if st.button("🔄 New Quiz", use_container_width=True):
            start_quiz()
            st.rerun()
    with col3:
        if st.button("🏠 Home", use_container_width=True):
            go_home()
            st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: REVIEW
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "review":
    questions = st.session_state.questions
    total = len(questions)
    score = compute_score()
    pct = round((score / total) * 100) if total else 0

    st.markdown(
        f"<h2 style='margin-bottom:4px;'>🔍 Answer Review</h2>"
        f"<p style='color:#8fa3c0; font-size:0.9rem; margin-bottom:20px;'>"
        f"Score: <b style='color:#5aa3ff;'>{score}/{total}</b> ({pct}%) — "
        f"scroll through all questions below</p>",
        unsafe_allow_html=True,
    )

    # Filter toggle
    filter_choice = st.radio(
        "Show:",
        ["All Questions", "Incorrect Only", "Correct Only"],
        horizontal=True,
        label_visibility="visible",
    )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    for i, q in enumerate(questions):
        user_ans = st.session_state.answers.get(i, None)
        is_correct = user_ans == q["answer"] if user_ans else False
        was_answered = user_ans is not None

        # Apply filter
        if filter_choice == "Incorrect Only" and is_correct:
            continue
        if filter_choice == "Correct Only" and not is_correct:
            continue

        border_class = "review-correct" if is_correct else "review-incorrect"
        status_icon = "✅" if is_correct else "❌"
        status_color = "#22c55e" if is_correct else "#ef4444"

        with st.expander(
            f"{status_icon}  Q{i + 1}: {q['question'][:90]}{'...' if len(q['question']) > 90 else ''}",
            expanded=False,
        ):
            st.markdown(
                f"<div class='category-badge'>{q['category']}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div style='font-size:1rem; font-weight:500; margin-bottom:12px; line-height:1.5;'>"
                f"{q['question']}"
                f"</div>",
                unsafe_allow_html=True,
            )

            # Options with colour coding
            for j, opt in enumerate(q["options"]):
                letter = letter_for(j)
                is_correct_opt = opt == q["answer"]
                is_user_opt = opt == user_ans

                if is_correct_opt and is_user_opt:
                    icon_opt = "✅"
                    color = "#22c55e"
                    weight = "700"
                elif is_correct_opt:
                    icon_opt = "✔"
                    color = "#22c55e"
                    weight = "600"
                elif is_user_opt:
                    icon_opt = "✗"
                    color = "#ef4444"
                    weight = "600"
                else:
                    icon_opt = "○"
                    color = "#4a6080"
                    weight = "400"

                st.markdown(
                    f"<div style='font-size:0.875rem; color:{color}; font-weight:{weight}; "
                    f"padding:4px 0;'>{icon_opt} {letter}. {opt}</div>",
                    unsafe_allow_html=True,
                )

            st.markdown(
                f"<div style='background:rgba(46,125,247,0.08); border-left:3px solid #2e7df7; "
                f"padding:10px 14px; border-radius:0 6px 6px 0; margin-top:12px; "
                f"font-size:0.875rem; color:#b8cce4; line-height:1.55;'>"
                f"<b style='color:#5aa3ff;'>💡 Explanation:</b> {q['explanation']}"
                f"</div>",
                unsafe_allow_html=True,
            )

            if not was_answered:
                st.markdown(
                    "<div style='color:#f59e0b; font-size:0.83rem; margin-top:8px;'>"
                    "⚠️ This question was not answered.</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Back to Results", use_container_width=True):
            go_results()
            st.rerun()
    with col2:
        if st.button("🔄 New Quiz", use_container_width=True):
            start_quiz()
            st.rerun()
