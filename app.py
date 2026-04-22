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
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# Custom CSS — Tufin dark theme with full visibility fix
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap');

    :root {
        --t-dark:    #0a1628;
        --t-navy:    #0d2045;
        --t-blue:    #1a4b8c;
        --t-accent:  #2e7df7;
        --t-bright:  #5aa3ff;
        --t-teal:    #00c2cb;
        --t-text:    #e8edf5;
        --t-muted:   #8fa3c0;
        --t-success: #22c55e;
        --t-error:   #ef4444;
        --t-warn:    #f59e0b;
        --card-bg:   #111f38;
        --card-bdr:  #1e3a6e;
    }

    html, body, [class*="css"], .stMarkdown, .stMarkdown p,
    .stMarkdown span, p, span, label, div {
        font-family: 'Inter', sans-serif !important;
        color: var(--t-text) !important;
    }
    .stApp {
        background: linear-gradient(135deg, var(--t-dark) 0%, var(--t-navy) 100%) !important;
        min-height: 100vh;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1a30 0%, #0d2045 100%) !important;
        border-right: 1px solid var(--card-bdr) !important;
    }
    [data-testid="stSidebar"] * { color: var(--t-text) !important; }

    /* ── Headings ── */
    h1 { color: var(--t-bright) !important; font-weight: 700 !important; }
    h2 { color: var(--t-teal)  !important; font-weight: 600 !important; }
    h3 { color: var(--t-bright) !important; font-weight: 600 !important; }

    /* ── Progress bar ── */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--t-accent) 0%, var(--t-teal) 100%) !important;
        border-radius: 4px;
    }
    .stProgress > div > div {
        background-color: #1a2e50 !important;
        border-radius: 4px;
    }

    /* ── All buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, var(--t-accent) 0%, #1a6aef 100%) !important;
        color: #ffffff !important;
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
        opacity: 0.92 !important;
    }
    .stButton > button p { color: #ffffff !important; }

    /* ── Option card buttons — unselected ── */
    .opt-btn-wrap .stButton > button {
        background: #111f38 !important;
        border: 1.5px solid #1e3a6e !important;
        border-radius: 10px !important;
        color: #e8edf5 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        text-align: left !important;
        padding: 14px 18px !important;
        box-shadow: none !important;
        width: 100% !important;
        justify-content: flex-start !important;
    }
    .opt-btn-wrap .stButton > button:hover {
        background: rgba(46,125,247,0.14) !important;
        border-color: var(--t-accent) !important;
        transform: none !important;
        box-shadow: 0 0 0 1px rgba(46,125,247,0.4) !important;
    }
    .opt-btn-wrap .stButton > button p { color: #e8edf5 !important; }

    /* ── Option card buttons — selected (before submit) ── */
    .opt-btn-selected .stButton > button {
        background: rgba(46,125,247,0.22) !important;
        border: 2px solid #2e7df7 !important;
        color: #ffffff !important;
        box-shadow: 0 0 0 2px rgba(46,125,247,0.25) !important;
    }
    .opt-btn-selected .stButton > button p { color: #ffffff !important; }

    /* ── Option card buttons — correct (after submit) ── */
    .opt-btn-correct .stButton > button {
        background: rgba(34,197,94,0.18) !important;
        border: 2px solid #22c55e !important;
        color: #ffffff !important;
        cursor: default !important;
    }
    .opt-btn-correct .stButton > button p { color: #ffffff !important; }

    /* ── Option card buttons — wrong answer chosen ── */
    .opt-btn-wrong .stButton > button {
        background: rgba(239,68,68,0.18) !important;
        border: 2px solid #ef4444 !important;
        color: #ffffff !important;
        cursor: default !important;
    }
    .opt-btn-wrong .stButton > button p { color: #ffffff !important; }

    /* ── Option card buttons — neutral (other options after submit) ── */
    .opt-btn-neutral .stButton > button {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid #1a2e50 !important;
        color: #4a6080 !important;
        cursor: default !important;
        opacity: 0.6 !important;
    }
    .opt-btn-neutral .stButton > button p { color: #4a6080 !important; }

    /* ── Quiz card ── */
    .quiz-card {
        background: var(--card-bg);
        border: 1px solid var(--card-bdr);
        border-radius: 14px;
        padding: 26px 30px;
        margin: 10px 0 18px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.4);
    }
    .question-text {
        font-size: 1.12rem !important;
        font-weight: 500 !important;
        color: #e8edf5 !important;
        line-height: 1.65 !important;
        margin: 0 !important;
    }
    .category-badge {
        display: inline-block;
        background: rgba(46,125,247,0.15);
        border: 1px solid rgba(46,125,247,0.4);
        color: var(--t-bright) !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 20px;
        margin-bottom: 14px;
    }
    .options-label {
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        color: var(--t-muted) !important;
        letter-spacing: 0.6px;
        text-transform: uppercase;
        margin: 0 0 8px !important;
    }

    /* ── Feedback boxes ── */
    .feedback-correct {
        background: rgba(34,197,94,0.10);
        border: 1px solid rgba(34,197,94,0.4);
        border-left: 4px solid #22c55e;
        border-radius: 10px;
        padding: 16px 20px;
        margin-top: 14px;
    }
    .feedback-incorrect {
        background: rgba(239,68,68,0.10);
        border: 1px solid rgba(239,68,68,0.4);
        border-left: 4px solid #ef4444;
        border-radius: 10px;
        padding: 16px 20px;
        margin-top: 14px;
    }
    .feedback-title {
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        margin-bottom: 6px !important;
    }
    .feedback-explanation {
        font-size: 0.9rem !important;
        color: #b8cce4 !important;
        line-height: 1.6 !important;
        margin-top: 8px !important;
    }
    .correct-answer-label {
        font-size: 0.88rem !important;
        color: #22c55e !important;
        font-weight: 600 !important;
        margin-top: 6px !important;
    }

    /* ── Score card ── */
    .score-card {
        background: linear-gradient(135deg, #0d2045 0%, #112240 100%);
        border: 1px solid var(--t-blue);
        border-radius: 18px;
        padding: 36px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    }
    .score-number {
        font-size: 4rem !important;
        font-weight: 800 !important;
        color: var(--t-bright) !important;
        line-height: 1 !important;
    }
    .score-label {
        font-size: 1rem !important;
        color: var(--t-muted) !important;
        margin-top: 4px !important;
    }

    /* ── Selectbox / multiselect ── */
    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        background: #0d1f3c !important;
        border: 1px solid var(--card-bdr) !important;
        color: var(--t-text) !important;
    }

    /* ── Metrics ── */
    [data-testid="stMetricValue"] { color: var(--t-bright) !important; font-weight: 700 !important; }
    [data-testid="stMetricLabel"] { color: var(--t-muted) !important; }

    /* ── Expander ── */
    .streamlit-expanderHeader {
        background: var(--card-bg) !important;
        border: 1px solid var(--card-bdr) !important;
        border-radius: 8px !important;
        color: var(--t-bright) !important;
        font-weight: 600 !important;
    }
    .streamlit-expanderContent {
        background: rgba(13,32,69,0.6) !important;
        border: 1px solid var(--card-bdr) !important;
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
    }
    .welcome-subtitle {
        color: var(--t-muted) !important;
        font-size: 0.95rem !important;
        margin-top: 8px !important;
        line-height: 1.5 !important;
    }

    /* ── Instruction box ── */
    .instruction-box {
        background: rgba(255,255,255,0.03);
        border: 1px solid var(--card-bdr);
        border-radius: 12px;
        padding: 20px 24px;
        margin: 16px 0;
    }
    .instruction-box li {
        color: var(--t-muted) !important;
        margin-bottom: 8px;
        font-size: 0.92rem;
        line-height: 1.5;
    }
    .instruction-box li span { color: var(--t-text) !important; }

    /* ── Review ── */
    .review-item {
        background: var(--card-bg);
        border: 1px solid var(--card-bdr);
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 14px;
    }
    .review-correct { border-left: 4px solid var(--t-success) !important; }
    .review-incorrect { border-left: 4px solid var(--t-error) !important; }
    .review-q-num {
        font-size: 0.72rem !important; color: var(--t-muted) !important;
        font-weight: 600 !important; letter-spacing: 0.6px;
        text-transform: uppercase; margin-bottom: 6px !important;
    }
    .review-q-text {
        font-size: 1rem !important; font-weight: 500 !important;
        margin-bottom: 10px !important; line-height: 1.5 !important;
    }
    .option-correct { color: var(--t-success) !important; font-weight: 600 !important; }
    .option-wrong   { color: var(--t-error)   !important; font-weight: 600 !important; }
    .option-neutral { color: var(--t-muted)   !important; }

    hr { border-color: var(--card-bdr) !important; margin: 24px 0 !important; }

    /* ── Material Symbols — ensures sidebar arrow icon renders as icon, not text ── */
    /* Without this, mobile browsers that fail to load the font show the literal  */
    /* ligature text e.g. "keyboard_double_arrow_right" instead of the >> glyph.  */
    .material-symbols-rounded {
        font-family: 'Material Symbols Rounded', 'Material Icons', sans-serif !important;
        font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24 !important;
        font-size: 24px !important;
        line-height: 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        display: inline-block !important;
        white-space: nowrap !important;
        -webkit-font-smoothing: antialiased !important;
    }

    /* ── Mobile responsive ── */
    @media (max-width: 768px) {
        /* Tighter page padding */
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1.5rem !important;
            max-width: 100% !important;
        }

        /* Headings scale down */
        h1 { font-size: 1.45rem !important; }
        h2 { font-size: 1.2rem  !important; }
        h3 { font-size: 1.05rem !important; }

        /* Welcome banner */
        .welcome-banner {
            padding: 20px 16px !important;
            border-radius: 12px !important;
        }

        /* Quiz card */
        .quiz-card {
            padding: 16px !important;
            border-radius: 10px !important;
        }
        .question-text { font-size: 1rem !important; }

        /* Score card */
        .score-card { padding: 22px 16px !important; }
        .score-number { font-size: 2.8rem !important; }

        /* Instruction box */
        .instruction-box { padding: 14px !important; }

        /* Feedback boxes */
        .feedback-correct,
        .feedback-incorrect { padding: 12px 14px !important; }

        /* Review item */
        .review-item { padding: 14px !important; }

        /* Stack ALL Streamlit columns into a single vertical flow on mobile.   */
        /* This handles: 3-metric row, 2-col category grid, 3-button results   */
        /* row, Submit+Quit pair, Next+Quit pair, and Review button pair.       */
        [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
            gap: 0 !important;
        }
        [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
            min-width: 100% !important;
            flex: 1 1 100% !important;
        }

        /* Option card buttons — slightly smaller text on small screens */
        .opt-btn-wrap .stButton > button,
        .opt-btn-selected .stButton > button,
        .opt-btn-correct .stButton > button,
        .opt-btn-wrong .stButton > button,
        .opt-btn-neutral .stButton > button {
            font-size: 0.9rem !important;
            padding: 12px 14px !important;
        }

        /* General buttons */
        .stButton > button {
            font-size: 0.9rem !important;
            padding: 10px 16px !important;
        }

        /* Sidebar toggle button — make it larger for easier tapping */
        [data-testid="collapsedControl"] {
            top: 0.5rem !important;
        }
        [data-testid="collapsedControl"] button {
            width: 2.4rem !important;
            height: 2.4rem !important;
        }
    }

    /* ── Very small screens (≤ 480px) ── */
    @media (max-width: 480px) {
        h1 { font-size: 1.25rem !important; }
        .welcome-banner { padding: 16px 12px !important; }
        .score-number   { font-size: 2.4rem !important; }
        .quiz-card      { padding: 12px !important; }
        .block-container {
            padding-left: 0.75rem !important;
            padding-right: 0.75rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# Session state initialisation
# ─────────────────────────────────────────────────────────────────────────────
DEFAULTS = {
    "page": "home",
    "questions": [],
    "current_idx": 0,
    "answers": {},
    "submitted": {},
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
    raw = st.session_state.question_count
    count = len(pool) if raw == "All" else min(int(raw), len(pool))
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


def letter_for(i: int) -> str:
    return ["A", "B", "C", "D"][i] if i < 4 else "?"


def compute_score() -> int:
    return sum(
        1
        for i, q in enumerate(st.session_state.questions)
        if st.session_state.answers.get(i) == q["answer"]
    )


def category_breakdown() -> dict:
    out = {}
    for i, q in enumerate(st.session_state.questions):
        cat = q["category"]
        out.setdefault(cat, {"correct": 0, "total": 0})
        out[cat]["total"] += 1
        if st.session_state.answers.get(i) == q["answer"]:
            out[cat]["correct"] += 1
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style='text-align:center;padding:8px 0 20px;'>
            <div style='font-size:2.4rem;'>🛡️</div>
            <div style='font-size:1.05rem;font-weight:700;color:#5aa3ff;letter-spacing:0.5px;'>
                Tufin QA Prep
            </div>
            <div style='font-size:0.78rem;color:#8fa3c0;margin-top:2px;'>
                Interview Practice Quiz
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    st.markdown(
        "<p style='font-size:0.8rem;font-weight:600;color:#5aa3ff;"
        "letter-spacing:0.8px;text-transform:uppercase;margin-bottom:6px;'>"
        "📚 Categories</p>",
        unsafe_allow_html=True,
    )
    selected_cats = st.multiselect(
        "categories",
        options=ALL_CATEGORIES,
        default=st.session_state.selected_categories,
        label_visibility="collapsed",
    )
    if selected_cats:
        st.session_state.selected_categories = selected_cats

    st.markdown(
        "<p style='font-size:0.8rem;font-weight:600;color:#5aa3ff;"
        "letter-spacing:0.8px;text-transform:uppercase;margin-top:16px;margin-bottom:6px;'>"
        "🔢 Question Count</p>",
        unsafe_allow_html=True,
    )
    q_count = st.selectbox(
        "count",
        options=["10", "15", "20", "All"],
        index=["10", "15", "20", "All"].index(st.session_state.question_count),
        label_visibility="collapsed",
    )
    st.session_state.question_count = q_count

    pool_size = len(
        [q for q in QUESTIONS if q["category"] in st.session_state.selected_categories]
    )
    st.markdown(
        f"<p style='font-size:0.78rem;color:#8fa3c0;margin-top:6px;'>"
        f"📊 {pool_size} questions in selected categories</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    if st.session_state.page != "home":
        if st.button("🏠 Home", use_container_width=True):
            go_home()
            st.rerun()
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    if st.session_state.page in ("results", "review"):
        if st.button("🔄 New Quiz", use_container_width=True):
            start_quiz()
            st.rerun()
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    st.markdown(
        "<div style='margin-top:32px;font-size:0.72rem;color:#4a6080;"
        "text-align:center;line-height:1.6;'>"
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
            <div style='font-size:2.8rem;margin-bottom:8px;'>🛡️</div>
            <h1 style='margin:0;font-size:1.9rem;'>Tufin QA Interview Prep</h1>
            <p class='welcome-subtitle'>
                Master QA fundamentals, networking, Java debugging, APIs, SQL,
                Check Point, and behavioral strategy — all in one interactive quiz.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
        <ul style='list-style:none;padding:0;margin:0;'>
            <li>🎯 <span>Select <b>categories</b> in the sidebar</span></li>
            <li>🔢 <span>Choose your <b>question count</b> (10 / 15 / 20 / All)</span></li>
            <li>📝 <span>Click an answer card, then hit <b>Submit</b></span></li>
            <li>✅ <span>See <b>instant feedback</b> and explanation after each answer</span></li>
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
        cnt = len([q for q in QUESTIONS if q["category"] == cat])
        cols[i % 2].markdown(
            f"<div style='background:rgba(255,255,255,0.03);border:1px solid #1e3a6e;"
            f"border-radius:8px;padding:10px 14px;margin-bottom:8px;'>"
            f"<span style='font-size:1.1rem;'>{icon}</span> "
            f"<span style='font-weight:600;color:#e8edf5;'>{cat}</span> "
            f"<span style='color:#8fa3c0;font-size:0.83rem;'>({cnt} questions)</span>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    pool_size = len(
        [q for q in QUESTIONS if q["category"] in st.session_state.selected_categories]
    )
    if not st.session_state.selected_categories:
        st.warning("⚠️ Please select at least one category in the sidebar.")
    elif pool_size == 0:
        st.warning("⚠️ No questions found for selected categories.")
    else:
        raw = st.session_state.question_count
        quiz_size = pool_size if raw == "All" else min(int(raw), pool_size)
        st.markdown(
            f"<div style='text-align:center;color:#8fa3c0;font-size:0.9rem;margin-bottom:16px;'>"
            f"Ready to quiz on <b style='color:#5aa3ff;'>{quiz_size}</b> questions "
            f"from <b style='color:#5aa3ff;'>{len(st.session_state.selected_categories)}</b> categories"
            f"</div>",
            unsafe_allow_html=True,
        )
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
        st.error("No questions loaded. Go home and start again.")
        st.button("🏠 Home", on_click=go_home)
        st.stop()

    q = questions[idx]
    already_submitted = idx in st.session_state.submitted

    # ── Session-state key tracking which option is highlighted ────────────────
    sel_key = f"pending_sel_{idx}"
    if sel_key not in st.session_state:
        # Restore previous selection if navigating back
        st.session_state[sel_key] = st.session_state.answers.get(idx)

    # ── Progress bar ──────────────────────────────────────────────────────────
    done = len(st.session_state.submitted)
    st.markdown(
        f"<div style='display:flex;justify-content:space-between;"
        f"align-items:center;margin-bottom:4px;'>"
        f"<span style='font-size:0.82rem;color:#8fa3c0;'>Question {idx + 1} of {total}</span>"
        f"<span style='font-size:0.82rem;color:#8fa3c0;'>{done}/{total} completed</span>"
        f"</div>",
        unsafe_allow_html=True,
    )
    st.progress((idx + (1 if already_submitted else 0)) / total)
    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

    # ── Question card ─────────────────────────────────────────────────────────
    st.markdown(
        f"<div class='quiz-card'>"
        f"<div class='category-badge'>{q['category']}</div>"
        f"<p class='question-text'>{q['question']}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

    # ── Answer option cards ───────────────────────────────────────────────────
    # Each option is rendered as a styled full-width button.
    # We track which option the user has clicked via session_state[sel_key].
    # After submission the buttons are replaced by read-only styled divs.

    st.markdown(
        "<p class='options-label'>Choose your answer</p>",
        unsafe_allow_html=True,
    )

    correct_ans = q["answer"]
    user_ans = st.session_state.answers.get(idx)
    pending = st.session_state[sel_key]

    for i, opt in enumerate(q["options"]):
        letter = letter_for(i)

        if already_submitted:
            # ── Read-only result display ──────────────────────────────────────
            if opt == correct_ans:
                bg = "rgba(34,197,94,0.15)"
                border = "2px solid #22c55e"
                letter_color = "#22c55e"
                icon = "✅"
                text_color = "#e8edf5"
            elif opt == user_ans:
                bg = "rgba(239,68,68,0.15)"
                border = "2px solid #ef4444"
                letter_color = "#ef4444"
                icon = "❌"
                text_color = "#e8edf5"
            else:
                bg = "rgba(255,255,255,0.02)"
                border = "1px solid #1a2e50"
                letter_color = "#2e4060"
                icon = ""
                text_color = "#4a6080"

            st.markdown(
                f"<div style='"
                f"background:{bg};"
                f"border:{border};"
                f"border-radius:10px;"
                f"padding:14px 18px;"
                f"margin:6px 0;"
                f"display:flex;"
                f"align-items:center;"
                f"gap:14px;"
                f"'>"
                f"<span style='font-weight:700;font-size:1rem;color:{letter_color};"
                f"min-width:22px;'>{letter}</span>"
                f"<span style='font-size:0.98rem;color:{text_color};"
                f"font-weight:500;line-height:1.45;flex:1;'>{opt}</span>"
                f"<span style='font-size:1.1rem;'>{icon}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )
        else:
            # ── Clickable option button ───────────────────────────────────────
            is_selected = pending == opt

            if is_selected:
                bg = "rgba(46,125,247,0.20)"
                border = "2px solid #2e7df7"
                letter_color = "#2e7df7"
                text_color = "#ffffff"
                shadow = "0 0 0 3px rgba(46,125,247,0.20)"
            else:
                bg = "#111f38"
                border = "1.5px solid #1e3a6e"
                letter_color = "#5aa3ff"
                text_color = "#e8edf5"
                shadow = "none"

            # Render a styled div for visual, then a transparent Streamlit
            # button layered on top via negative margin so the whole row is
            # clickable. We use a creative trick: render the div, then
            # immediately render a full-width button BELOW and use CSS to
            # make it merge visually. Instead we just render the button
            # directly with the letter prefix — cleaner and reliable.
            label_text = f"{letter}.   {opt}"

            # We render the styled card using st.markdown, then place a
            # near-invisible click-trigger button absolutely beneath it.
            # Simpler: render the full option as a styled markdown card,
            # and track click via a regular full-width button.

            st.markdown(
                f"<div style='"
                f"background:{bg};"
                f"border:{border};"
                f"border-radius:10px;"
                f"padding:14px 18px;"
                f"margin:6px 0 0 0;"
                f"display:flex;"
                f"align-items:center;"
                f"gap:14px;"
                f"box-shadow:{shadow};"
                f"cursor:pointer;"
                f"transition:all 0.15s ease;"
                f"'>"
                f"<span style='font-weight:700;font-size:1rem;color:{letter_color};"
                f"min-width:22px;'>{letter}</span>"
                f"<span style='font-size:0.98rem;color:{text_color};"
                f"font-weight:500;line-height:1.45;flex:1;'>{opt}</span>"
                f"{'<span style="font-size:1rem;">🔵</span>' if is_selected else ''}"
                f"</div>",
                unsafe_allow_html=True,
            )

            # Thin "Select" button directly below the card, same width,
            # minimal height — the user clicks it to register the selection.
            st.markdown(
                f"<style>"
                f"div[data-testid='stButton']:has(button[kind='secondary']#sel_{idx}_{i}) > button {{"
                f"  margin-top:-4px !important;"
                f"}}"
                f"</style>",
                unsafe_allow_html=True,
            )

            # Use a compact, muted "select" button to register the click
            select_css_wrap = "opt-btn-selected" if is_selected else "opt-btn-wrap"
            st.markdown(
                f"<div class='{select_css_wrap}' style='margin-top:-2px;'>",
                unsafe_allow_html=True,
            )
            if st.button(
                f"{'✔  Selected' if is_selected else f'Select  {letter}'}",
                key=f"sel_{idx}_{i}",
                use_container_width=True,
            ):
                st.session_state[sel_key] = opt
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='height:2px'></div>", unsafe_allow_html=True)

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ── Feedback ──────────────────────────────────────────────────────────────
    if already_submitted:
        is_correct = user_ans == correct_ans
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
                f"<div class='correct-answer-label'>✔ Correct answer: {correct_ans}</div>"
                f"<div class='feedback-explanation'>{q['explanation']}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
        col_l, col_r = st.columns(2)
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

    else:
        # ── Submit button ─────────────────────────────────────────────────────
        col_l, col_r = st.columns(2)
        with col_l:
            submit_disabled = pending is None
            if st.button(
                "✅ Submit Answer",
                use_container_width=True,
                key=f"submit_{idx}",
                disabled=submit_disabled,
            ):
                st.session_state.answers[idx] = pending
                st.session_state.submitted[idx] = True
                st.rerun()
        with col_r:
            if st.button(
                "🏠 Quit to Home", use_container_width=True, key=f"quit_pre_{idx}"
            ):
                go_home()
                st.rerun()

        if pending is None:
            st.markdown(
                "<p style='font-size:0.82rem;color:#8fa3c0;margin-top:6px;'>"
                "👆 Click an answer card above, then submit.</p>",
                unsafe_allow_html=True,
            )


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: RESULTS
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "results":
    questions = st.session_state.questions
    total = len(questions)
    score = compute_score()
    pct = round((score / total) * 100) if total else 0

    if pct >= 80:
        emoji, grade_label, grade_color = "😎", "Excellent!", "#22c55e"
        grade_msg = "You're ready for that Tufin interview. Outstanding performance!"
    elif pct >= 60:
        emoji, grade_label, grade_color = "🙂", "Good Job", "#f59e0b"
        grade_msg = "Solid foundation! Review the missed questions and you'll nail it."
    else:
        emoji, grade_label, grade_color = "😬", "Keep Studying", "#ef4444"
        grade_msg = "Don't worry — practice makes perfect. Review and try again!"

    if pct >= 80:
        st.markdown(
            """
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
            <script>
            setTimeout(function(){
                confetti({particleCount:180,spread:90,origin:{y:0.4},
                    colors:['#2e7df7','#5aa3ff','#00c2cb','#22c55e','#ffffff']});
            }, 300);
            </script>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class='score-card'>
            <div style='font-size:3.5rem;margin-bottom:4px;'>{emoji}</div>
            <div style='font-size:1.1rem;color:#8fa3c0;margin-bottom:4px;'>Quiz Complete!</div>
            <div class='score-number'>{score}<span style='font-size:1.8rem;color:#8fa3c0;'>/{total}</span></div>
            <div class='score-label'>questions correct</div>
            <div style='font-size:1.8rem;font-weight:700;color:{grade_color};margin-top:10px;'>{pct}%</div>
            <div style='font-size:1.05rem;font-weight:600;color:{grade_color};margin-top:2px;'>{grade_label}</div>
            <div style='font-size:0.88rem;color:#8fa3c0;margin-top:8px;'>{grade_msg}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📊 Category Breakdown")
    breakdown = category_breakdown()
    for cat, data in sorted(breakdown.items()):
        c_score = data["correct"]
        c_total = data["total"]
        c_pct = round((c_score / c_total) * 100) if c_total else 0
        bar_color = (
            "#22c55e" if c_pct >= 70 else "#f59e0b" if c_pct >= 50 else "#ef4444"
        )
        st.markdown(
            f"<div style='background:var(--card-bg);border:1px solid var(--card-bdr);"
            f"border-radius:10px;padding:14px 18px;margin-bottom:10px;'>"
            f"<div style='display:flex;justify-content:space-between;align-items:center;"
            f"margin-bottom:8px;'>"
            f"<span style='font-weight:600;color:#e8edf5;font-size:0.92rem;'>{cat}</span>"
            f"<span style='font-weight:700;color:{bar_color};font-size:0.92rem;'>"
            f"{c_score}/{c_total} &nbsp;({c_pct}%)</span>"
            f"</div>"
            f"<div style='background:#1a2e50;border-radius:4px;height:6px;'>"
            f"<div style='background:{bar_color};width:{c_pct}%;height:6px;"
            f"border-radius:4px;transition:width 0.4s ease;'></div>"
            f"</div>"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("🔍 Review Answers", use_container_width=True):
            go_review()
            st.rerun()
    with col_b:
        if st.button("🔄 New Quiz", use_container_width=True):
            start_quiz()
            st.rerun()
    with col_c:
        if st.button("🏠 Home", use_container_width=True):
            go_home()
            st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: REVIEW
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "review":
    questions = st.session_state.questions
    score = compute_score()
    total = len(questions)

    st.markdown("## 🔍 Review Your Answers")
    st.markdown(
        f"<p style='color:#8fa3c0;margin-bottom:20px;'>"
        f"You scored <b style='color:#5aa3ff;'>{score}/{total}</b>. "
        f"Expand any question to see the full explanation.</p>",
        unsafe_allow_html=True,
    )

    filter_options = ["All", "✅ Correct Only", "❌ Incorrect Only"]
    review_filter = st.selectbox("Filter", filter_options, label_visibility="collapsed")

    for i, q in enumerate(questions):
        user_ans = st.session_state.answers.get(i, "—")
        correct_ans = q["answer"]
        is_correct = user_ans == correct_ans

        if review_filter == "✅ Correct Only" and not is_correct:
            continue
        if review_filter == "❌ Incorrect Only" and is_correct:
            continue

        result_icon = "✅" if is_correct else "❌"
        border_class = "review-correct" if is_correct else "review-incorrect"

        with st.expander(
            f"{result_icon}  Q{i + 1}: {q['question'][:80]}{'…' if len(q['question']) > 80 else ''}"
        ):
            st.markdown(
                f"<div class='review-item {border_class}'>"
                f"<div class='review-q-num'>{q['category']} — Question {i + 1}</div>"
                f"<div class='review-q-text'>{q['question']}</div>",
                unsafe_allow_html=True,
            )
            for j, opt in enumerate(q["options"]):
                if opt == correct_ans:
                    cls = "option-correct"
                    pfx = "✅"
                elif opt == user_ans and not is_correct:
                    cls = "option-wrong"
                    pfx = "❌"
                else:
                    cls = "option-neutral"
                    pfx = "○"
                st.markdown(
                    f"<div class='review-answer-row'>"
                    f"<span class='{cls}'>{pfx}  {letter_for(j)}.  {opt}</span>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
            st.markdown(
                f"<div style='margin-top:12px;padding-top:10px;"
                f"border-top:1px solid #1e3a6e;'>"
                f"<span style='font-size:0.8rem;font-weight:600;color:#5aa3ff;"
                f"text-transform:uppercase;letter-spacing:0.6px;'>Explanation</span><br>"
                f"<span style='font-size:0.9rem;color:#b8cce4;line-height:1.6;'>"
                f"{q['explanation']}</span>"
                f"</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("📊 Back to Results", use_container_width=True):
            go_results()
            st.rerun()
    with col_b:
        if st.button("🔄 New Quiz", use_container_width=True):
            start_quiz()
            st.rerun()
