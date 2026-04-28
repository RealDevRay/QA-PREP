import random

import charts
import matplotlib.pyplot as plt
import streamlit as st
from data import BEHAVIORAL_QA, SCENARIO_QA
from questions import ALL_CATEGORIES, QUESTIONS

# ─────────────────────────────────────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Tufin QA Interview Prep",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# Inject Material Symbols font into <head> so Streamlit's expander arrow
# renders as an icon and not as raw ligature text (e.g. "keyboard_arrow_right")
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <script>
    (function () {
        var id = 'msymbols-font-link';
        if (document.getElementById(id)) return;
        var link = document.createElement('link');
        link.id   = id;
        link.rel  = 'stylesheet';
        link.href = 'https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded'
                  + ':opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=block';
        document.head.appendChild(link);
    })();
    </script>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS — dark Tufin theme
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

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
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1a30 0%, #0d2045 100%) !important;
    border-right: 1px solid var(--card-bdr) !important;
}
[data-testid="stSidebar"] * { color: var(--t-text) !important; }

h1 { color: var(--t-bright) !important; font-weight: 700 !important; }
h2 { color: var(--t-teal)   !important; font-weight: 600 !important; }
h3 { color: var(--t-bright) !important; font-weight: 600 !important; }

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--t-accent) 0%, var(--t-teal) 100%) !important;
    border-radius: 4px;
}
.stProgress > div > div {
    background-color: #1a2e50 !important;
    border-radius: 4px;
}

/* All buttons */
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

/* Option buttons */
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
}
.opt-btn-wrap .stButton > button p { color: #e8edf5 !important; }

.opt-btn-selected .stButton > button {
    background: rgba(46,125,247,0.22) !important;
    border: 2px solid #2e7df7 !important;
    color: #ffffff !important;
}
.opt-btn-correct .stButton > button {
    background: rgba(34,197,94,0.18) !important;
    border: 2px solid #22c55e !important;
    color: #ffffff !important;
    cursor: default !important;
}
.opt-btn-wrong .stButton > button {
    background: rgba(239,68,68,0.18) !important;
    border: 2px solid #ef4444 !important;
    color: #ffffff !important;
    cursor: default !important;
}
.opt-btn-neutral .stButton > button {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid #1a2e50 !important;
    color: #4a6080 !important;
    cursor: default !important;
    opacity: 0.55 !important;
}
.opt-btn-wrap .stButton > button p,
.opt-btn-selected .stButton > button p,
.opt-btn-correct .stButton > button p,
.opt-btn-wrong .stButton > button p   { color: inherit !important; }
.opt-btn-neutral .stButton > button p { color: #4a6080 !important; }

/* Cards */
.quiz-card {
    background: var(--card-bg);
    border: 1px solid var(--card-bdr);
    border-radius: 14px;
    padding: 26px 30px;
    margin: 10px 0 18px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
}
.answer-card {
    background: rgba(46,125,247,0.07);
    border: 1px solid rgba(46,125,247,0.3);
    border-left: 4px solid var(--t-accent);
    border-radius: 10px;
    padding: 18px 22px;
    margin: 10px 0;
    font-size: 1.02rem;
    line-height: 1.75;
}
.question-text {
    font-size: 1.12rem !important;
    font-weight: 500 !important;
    color: #e8edf5 !important;
    line-height: 1.65 !important;
    margin: 0 !important;
}
.badge {
    display: inline-block;
    background: rgba(46,125,247,0.18);
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
.cat-badge {
    display: inline-block;
    background: rgba(0,194,203,0.12);
    border: 1px solid rgba(0,194,203,0.35);
    color: var(--t-teal) !important;
    font-size: 0.7rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    padding: 2px 9px;
    border-radius: 20px;
    margin-bottom: 12px;
}

/* Feedback */
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

/* Score card */
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
.score-label { font-size: 1rem !important; color: var(--t-muted) !important; }

/* Insight / tip / avoid boxes */
.insight-box {
    background: rgba(245,158,11,0.1);
    border: 1px solid rgba(245,158,11,0.4);
    border-left: 4px solid #f59e0b;
    border-radius: 10px;
    padding: 14px 18px;
    margin: 8px 0;
    font-size: 0.95rem;
    line-height: 1.65;
}
.tip-box {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.35);
    border-left: 4px solid #22c55e;
    border-radius: 10px;
    padding: 12px 16px;
    margin: 6px 0;
    font-size: 0.9rem;
}
.avoid-box {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.3);
    border-left: 4px solid #ef4444;
    border-radius: 10px;
    padding: 12px 16px;
    margin: 6px 0;
    font-size: 0.9rem;
}

/* Welcome banner */
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
    margin-top: 6px !important;
}

/* Home mode card */
.mode-card {
    background: var(--card-bg);
    border: 1px solid var(--card-bdr);
    border-radius: 14px;
    padding: 22px 20px;
    text-align: center;
    margin-bottom: 10px;
    transition: border-color 0.2s;
    cursor: pointer;
}
.mode-card:hover { border-color: var(--t-accent); }
.mode-card .mode-icon { font-size: 2.2rem; margin-bottom: 8px; }
.mode-card .mode-title {
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    color: var(--t-bright) !important;
    margin-bottom: 5px !important;
}
.mode-card .mode-desc {
    font-size: 0.82rem !important;
    color: var(--t-muted) !important;
    line-height: 1.45 !important;
}

/* Tip of the day */
.tip-of-day {
    background: rgba(0,194,203,0.07);
    border: 1px solid rgba(0,194,203,0.25);
    border-radius: 10px;
    padding: 12px 18px;
    margin-top: 24px;
    font-size: 0.88rem;
}

/* Review */
.review-item {
    background: var(--card-bg);
    border: 1px solid var(--card-bdr);
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 12px;
}
.review-correct  { border-left: 4px solid var(--t-success) !important; }
.review-incorrect{ border-left: 4px solid var(--t-error)   !important; }

/* Selectbox */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: #0d1f3c !important;
    border: 1px solid var(--card-bdr) !important;
    color: var(--t-text) !important;
}
[data-testid="stMetricValue"] { color: var(--t-bright) !important; font-weight: 700 !important; }
[data-testid="stMetricLabel"] { color: var(--t-muted)  !important; }

/* Expander */
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

hr { border-color: var(--card-bdr) !important; margin: 20px 0 !important; }

/* Scenario layer colors */
.layer-blue   { border-left: 4px solid #3498db; background: rgba(52,152,219,0.08); border-radius: 8px; padding: 12px 16px; margin: 8px 0; }
.layer-red    { border-left: 4px solid #e74c3c; background: rgba(231,76,60,0.08);  border-radius: 8px; padding: 12px 16px; margin: 8px 0; }
.layer-green  { border-left: 4px solid #27ae60; background: rgba(39,174,96,0.08);  border-radius: 8px; padding: 12px 16px; margin: 8px 0; }
.layer-purple { border-left: 4px solid #8e44ad; background: rgba(142,68,173,0.08); border-radius: 8px; padding: 12px 16px; margin: 8px 0; }

/* ── Material Symbols — font-feature-settings:'liga' is REQUIRED for ligature
   glyphs to render. Without it the raw text appears in the expander label. ── */
.material-symbols-rounded {
    font-family: 'Material Symbols Rounded', sans-serif !important;
    font-weight: normal !important;
    font-style: normal !important;
    font-size: 24px !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    display: inline-block !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    -webkit-font-smoothing: antialiased !important;
    text-rendering: optimizeLegibility !important;
    font-feature-settings: 'liga' !important;
    -webkit-font-feature-settings: 'liga' !important;
}

/* Hard CSS fallback: if the font still hasn't loaded, hide the raw ligature
   text and draw a simple arrow via ::after so the expander stays usable. */
[data-testid="collapsedControl"] span[class*="material"],
[data-testid="collapsedControl"] span[class*="Material"] {
    font-size: 0 !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 1.5rem !important;
    height: 1.5rem !important;
}
[data-testid="collapsedControl"] span[class*="material"]::after,
[data-testid="collapsedControl"] span[class*="Material"]::after {
    font-family: system-ui, -apple-system, sans-serif !important;
    font-size: 1.2rem !important;
    content: '\276F' !important;
    color: #8fa3c0 !important;
    line-height: 1 !important;
}

/* Mobile */
@media (max-width: 768px) {
    .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
    h1 { font-size: 1.45rem !important; }
    h2 { font-size: 1.2rem !important; }
    .welcome-banner { padding: 20px 16px !important; }
    .quiz-card { padding: 16px !important; }
    .score-number { font-size: 2.8rem !important; }
    [data-testid="stHorizontalBlock"] { flex-wrap: wrap !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] { min-width: 100% !important; flex: 1 1 100% !important; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# Session state
# ─────────────────────────────────────────────────────────────────────────────
DAILY_TIPS = [
    "💡 Always ask 2–3 clarifying questions before writing a test plan. It signals structured thinking.",
    "💡 At the API level, a 200 OK with wrong data is still a bug. Always validate the response body.",
    "💡 Security bugs are always P1 — one exploit is one too many.",
    "💡 Publish saves to the database. Install Policy pushes to the gateway. They are two separate operations.",
    "💡 Firewall rules are first-match-wins, evaluated top-down. Specific rules always go above general ones.",
    "💡 Show the problem — don't just describe it. A proof of concept is worth a thousand words.",
    "💡 Over the API, a Viewer role must return 403 Forbidden — hidden UI buttons are not a security control.",
    "💡 Two-pointer pattern: reverse a string and check palindromes in O(n) with O(1) extra space.",
]

DEFAULTS: dict = {
    "page": "home",
    "beh_idx": 0,
    "beh_revealed": False,
    "beh_done": set(),
    "tip_idx": random.randrange(len(DAILY_TIPS)),
    "q_cats": list(ALL_CATEGORIES),
    "questions": [],
    "current_idx": 0,
    "answers": {},
    "submitted": {},
    "score": 0,
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# Navigation helper
# ─────────────────────────────────────────────────────────────────────────────
def go(page: str):
    st.session_state.page = page
    st.rerun()


def back_btn(dest: str = "home", label: str = "← Back"):
    if st.button(label, key=f"back_{dest}_{st.session_state.page}"):
        go(dest)


# ─────────────────────────────────────────────────────────────────────────────
# Quiz helpers
# ─────────────────────────────────────────────────────────────────────────────
def compute_score() -> int:
    return sum(
        1
        for i, q in enumerate(st.session_state.questions)
        if st.session_state.answers.get(i) == q["answer"]
    )


def category_breakdown() -> dict:
    out: dict = {}
    for i, q in enumerate(st.session_state.questions):
        cat = q["category"]
        out.setdefault(cat, {"correct": 0, "total": 0})
        out[cat]["total"] += 1
        if st.session_state.answers.get(i) == q["answer"]:
            out[cat]["correct"] += 1
    return out


def start_quiz():
    cats = st.session_state.q_cats
    pool = [q for q in QUESTIONS if q["category"] in cats]
    random.shuffle(pool)
    st.session_state.questions = pool
    st.session_state.current_idx = 0
    st.session_state.answers = {}
    st.session_state.submitted = {}
    st.session_state.score = 0
    st.session_state.page = "quiz"
    st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: HOME
# ─────────────────────────────────────────────────────────────────────────────
def render_home():
    st.markdown(
        """
    <div class="welcome-banner">
        <h1>🛡️ Tufin QA Interview Prep</h1>
        <p class="welcome-subtitle">Raymond's personalised preparation hub — all sections, one place</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 4 mode cards in 2×2 grid
    modes = [
        (
            "🎤",
            "Behavioral Practice",
            "11 personalised answers with frameworks, tips & what to avoid",
            "behavioral",
        ),
        (
            "🧠",
            "Knowledge Quiz",
            "MCQ across QA fundamentals, Check Point, Java, APIs & Tufin scenarios",
            "quiz_setup",
        ),
        (
            "📊",
            "Visual Reference",
            "Networking diagrams, coding patterns and QA frameworks",
            "diagrams",
        ),
        (
            "🎯",
            "Scenario Drills",
            "4 real Tufin QA scenarios with structured layered test plans",
            "scenarios",
        ),
    ]

    col_a, col_b = st.columns(2)
    for idx, (icon, title, desc, dest) in enumerate(modes):
        col = col_a if idx % 2 == 0 else col_b
        with col:
            st.markdown(
                f"""
            <div class="mode-card">
                <div class="mode-icon">{icon}</div>
                <div class="mode-title">{title}</div>
                <div class="mode-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button(f"Open {title}", key=f"home_{dest}", use_container_width=True):
                go(dest)

    # Tip of the day
    tip = DAILY_TIPS[st.session_state.tip_idx]
    st.markdown(
        f"""
    <div class="tip-of-day">
        <strong style="color:#00c2cb">Tip of the session</strong><br>
        {tip}
    </div>
    """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: BEHAVIORAL
# ─────────────────────────────────────────────────────────────────────────────
def render_behavioral():
    back_btn()
    st.markdown("## 🎤 Behavioral Practice")

    total = len(BEHAVIORAL_QA)
    idx = st.session_state.beh_idx
    card = BEHAVIORAL_QA[idx]
    done = st.session_state.beh_done

    # Progress
    st.progress((idx + 1) / total)
    st.caption(f"Card {idx + 1} of {total}  ·  {len(done)} reviewed")

    # Question card
    st.markdown(
        f"""
    <div class="quiz-card">
        <span class="badge">{card["framework"]}</span>
        <p class="question-text">{card["question"]}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Reveal / show answer
    if not st.session_state.beh_revealed:
        if st.button("🔍 Reveal Answer", use_container_width=True, key=f"reveal_{idx}"):
            st.session_state.beh_revealed = True
            st.rerun()
    else:
        st.markdown(
            f"""
        <div class="answer-card">
            {card["answer"]}
        </div>
        """,
            unsafe_allow_html=True,
        )

        with st.expander("📌 Key Talking Points"):
            for pt in card["points"]:
                st.markdown(f"• {pt}")

        with st.expander("✅ Delivery Tip"):
            st.markdown(
                f"""
            <div class="tip-box">{card["tip"]}</div>
            """,
                unsafe_allow_html=True,
            )

        with st.expander("⚠️ What to Avoid"):
            st.markdown(
                f"""
            <div class="avoid-box">{card["avoid"]}</div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")

    # Navigation row
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c1:
        if st.button(
            "← Previous",
            disabled=(idx == 0),
            key=f"beh_prev_{idx}",
            use_container_width=True,
        ):
            st.session_state.beh_idx = idx - 1
            st.session_state.beh_revealed = False
            st.rerun()
    with c2:
        already_done = card["id"] in done
        label = "✓ Reviewed" if already_done else "Mark Reviewed"
        if st.button(label, key=f"beh_mark_{idx}", use_container_width=True):
            if already_done:
                done.discard(card["id"])
            else:
                done.add(card["id"])
            st.session_state.beh_done = done
            st.rerun()
    with c3:
        if st.button(
            "Next →",
            disabled=(idx == total - 1),
            key=f"beh_next_{idx}",
            use_container_width=True,
        ):
            st.session_state.beh_idx = idx + 1
            st.session_state.beh_revealed = False
            st.rerun()

    # Progress tracker dots
    dot_parts = []
    for i in range(total):
        q_id = BEHAVIORAL_QA[i]["id"]
        q_title = BEHAVIORAL_QA[i]["question"][:40]
        if q_id in done:
            dot_parts.append(
                f'<span style="color:#22c55e;font-size:1.1rem" title="{q_title}">●</span> '
            )
        else:
            dot_parts.append('<span style="color:#1e3a6e;font-size:1.1rem">●</span> ')
    dots = "".join(dot_parts)
    st.markdown(
        f"<div style='margin-top:10px;text-align:center'>{dots}</div>",
        unsafe_allow_html=True,
    )

    # Completion banner
    if len(done) == total:
        st.markdown(
            """
        <div style="background:rgba(34,197,94,0.12);border:1px solid #22c55e;
                    border-radius:10px;padding:14px;text-align:center;margin-top:16px">
            🎉 <strong>All 11 behavioral answers reviewed!</strong>
            You know your story — now go deliver it.
        </div>
        """,
            unsafe_allow_html=True,
        )


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: QUIZ SETUP
# ─────────────────────────────────────────────────────────────────────────────
def render_quiz_setup():
    back_btn()
    st.markdown("## 🧠 Knowledge Quiz")
    st.markdown("Choose your topics, then hit Start.")

    # Quick filters
    st.markdown("**Quick filters:**")
    qf_cols = st.columns(4)
    quick = [
        ("All Topics", list(ALL_CATEGORIES)),
        ("Check Point", ["Check Point Networking"]),
        ("Java", ["Java & Debugging"]),
        ("Tufin", ["Tufin & Networking", "Tufin Scenario"]),
    ]
    for col, (label, cats) in zip(qf_cols, quick):
        with col:
            if st.button(label, key=f"qf_{label}", use_container_width=True):
                st.session_state.q_cats = cats
                st.rerun()

    # Full multiselect
    selected = st.multiselect(
        "Topics to include:",
        options=sorted(ALL_CATEGORIES),
        default=st.session_state.q_cats,
        key="cat_multiselect",
    )
    st.session_state.q_cats = selected if selected else list(ALL_CATEGORIES)

    count = len([q for q in QUESTIONS if q["category"] in st.session_state.q_cats])
    st.caption(f"{count} questions available in selected topics")

    st.markdown("")
    if st.button("🚀 Start Quiz →", use_container_width=True, disabled=(count == 0)):
        start_quiz()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: QUIZ (active)
# ─────────────────────────────────────────────────────────────────────────────
def render_quiz():
    questions = st.session_state.questions
    if not questions:
        go("quiz_setup")
        return

    idx = st.session_state.current_idx
    total = len(questions)
    q = questions[idx]
    submitted = st.session_state.submitted.get(idx, False)
    chosen = st.session_state.answers.get(idx)

    # Header row
    hc1, hc2 = st.columns([4, 1])
    with hc1:
        st.progress((idx + 1) / total)
        st.caption(f"Question {idx + 1} of {total}")
    with hc2:
        if st.button("🏠", key="quiz_home", help="Quit to Home"):
            go("home")

    # Question card
    st.markdown(
        f"""
    <div class="quiz-card">
        <span class="cat-badge">{q["category"]}</span>
        <p class="question-text">{q["question"]}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Options
    for opt in q["options"]:
        if submitted:
            if opt == q["answer"]:
                css = "opt-btn-correct"
            elif opt == chosen:
                css = "opt-btn-wrong"
            else:
                css = "opt-btn-neutral"
        else:
            css = "opt-btn-selected" if opt == chosen else "opt-btn-wrap"

        st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
        if st.button(
            opt, key=f"opt_{idx}_{opt}", use_container_width=True, disabled=submitted
        ):
            st.session_state.answers[idx] = opt
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Submit
    if not submitted and chosen:
        if st.button("Submit Answer ✓", use_container_width=True, key=f"submit_{idx}"):
            st.session_state.submitted[idx] = True
            if chosen == q["answer"]:
                st.session_state.score += 1
            st.rerun()

    # Feedback
    if submitted:
        correct = chosen == q["answer"]
        css = "feedback-correct" if correct else "feedback-incorrect"
        icon = "✅" if correct else "❌"
        label = "Correct!" if correct else "Not quite."
        st.markdown(
            f"""
        <div class="{css}">
            <div style="font-size:1.05rem;font-weight:700;margin-bottom:6px">
                {icon} {label}
            </div>
            <div style="font-size:0.9rem;color:#b8cce4;line-height:1.6">
                {q["explanation"]}
            </div>
            {"" if correct else f'<div style="font-size:0.88rem;color:#22c55e;font-weight:600;margin-top:6px">✓ Correct answer: {q["answer"]}</div>'}
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("")
        if idx < total - 1:
            if st.button(
                "Next Question →", use_container_width=True, key=f"next_{idx}"
            ):
                st.session_state.current_idx += 1
                st.rerun()
        else:
            if st.button("See Results 🏁", use_container_width=True, key="see_results"):
                st.session_state.score = compute_score()
                go("results")


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: RESULTS
# ─────────────────────────────────────────────────────────────────────────────
def render_results():
    score = st.session_state.score
    total = len(st.session_state.questions)
    pct = round(score / total * 100) if total else 0

    if pct >= 90:
        verdict = "🏆 Outstanding — interview ready!"
    elif pct >= 75:
        verdict = "✅ Strong — review any missed topics"
    elif pct >= 60:
        verdict = "📚 Getting there — keep drilling"
    else:
        verdict = "🔄 More practice needed — you've got this"

    st.markdown(
        f"""
    <div class="score-card">
        <div class="score-number">{score} / {total}</div>
        <div class="score-label">{pct}% correct</div>
        <div style="margin-top:14px;font-size:1.15rem;font-weight:600;color:#5aa3ff">
            {verdict}
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Category breakdown
    breakdown = category_breakdown()
    if breakdown:
        st.markdown("**Category Breakdown**")
        bc1, bc2, bc3 = st.columns(3)
        cols = [bc1, bc2, bc3]
        for i, (cat, data) in enumerate(breakdown.items()):
            with cols[i % 3]:
                cat_pct = round(data["correct"] / data["total"] * 100)
                st.metric(
                    label=cat[:28],
                    value=f"{data['correct']}/{data['total']}",
                    delta=f"{cat_pct}%",
                )

    st.markdown("---")
    rc1, rc2, rc3 = st.columns(3)
    with rc1:
        if st.button("🔁 Retake Quiz", use_container_width=True):
            start_quiz()
    with rc2:
        if st.button("🏠 Home", use_container_width=True):
            go("home")
    with rc3:
        show_review = st.button(
            "📖 Review Answers", use_container_width=True, key="show_review_toggle"
        )

    if show_review or st.session_state.get("_show_review"):
        st.session_state["_show_review"] = True
        st.markdown("---")
        st.markdown("### Answer Review")
        for i, q in enumerate(st.session_state.questions):
            user_ans = st.session_state.answers.get(i, "— not answered —")
            correct = user_ans == q["answer"]
            css = "review-correct" if correct else "review-incorrect"
            icon = "✅" if correct else "❌"
            st.markdown(
                f"""
            <div class="review-item {css}">
                <div style="font-size:0.7rem;color:#8fa3c0;font-weight:600;
                            letter-spacing:0.5px;text-transform:uppercase;margin-bottom:4px">
                    {icon}  Q{i + 1} · {q["category"]}
                </div>
                <div style="font-size:0.98rem;font-weight:500;margin-bottom:8px">
                    {q["question"]}
                </div>
                <div style="font-size:0.88rem;color:{"#22c55e" if correct else "#ef4444"};font-weight:600">
                    Your answer: {user_ans}
                </div>
                {'<div style="font-size:0.88rem;color:#22c55e;font-weight:600;margin-top:2px">Correct: ' + q["answer"] + "</div>" if not correct else ""}
                <div style="font-size:0.85rem;color:#8fa3c0;margin-top:6px;line-height:1.55">
                    {q["explanation"]}
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: DIAGRAMS
# ─────────────────────────────────────────────────────────────────────────────
def render_diagrams():
    back_btn()
    st.markdown("## 📊 Visual Reference")
    st.caption(
        "Diagrams generated from the podcast prep material — use these as study anchors."
    )

    tab_names = list(charts.DIAGRAM_REGISTRY.keys())
    tabs = st.tabs(tab_names)

    for tab, tab_name in zip(tabs, tab_names):
        with tab:
            for title, fn in charts.DIAGRAM_REGISTRY[tab_name]:
                st.subheader(title)
                fig = fn()
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)
                st.divider()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: SCENARIOS
# ─────────────────────────────────────────────────────────────────────────────
def render_scenarios():
    back_btn()
    st.markdown("## 🎯 Scenario Drills")
    st.markdown(
        """
    <div class="tip-box" style="margin-bottom:18px">
        <strong>Golden rule:</strong> Always ask your clarifying questions FIRST before giving any test plan.
        It signals structured thinking and prevents testing the wrong thing.
    </div>
    """,
        unsafe_allow_html=True,
    )

    LAYER_CSS = {
        "blue": "layer-blue",
        "red": "layer-red",
        "green": "layer-green",
        "purple": "layer-purple",
    }

    for sc in SCENARIO_QA:
        with st.expander(f"🗂️  {sc['title']}"):
            st.markdown(
                f"""
            <div class="quiz-card" style="margin-bottom:14px">
                <span class="badge">Scenario Question</span>
                <p class="question-text">{sc["scenario"]}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Clarify first
            st.markdown("#### ❓ Clarify First")
            for q in sc["clarify_first"]:
                st.markdown(
                    f'<div class="layer-blue" style="margin:4px 0;padding:8px 14px">→ {q}</div>',
                    unsafe_allow_html=True,
                )

            st.markdown("")

            # Test layers
            st.markdown("#### 📋 Test Layers")
            for layer in sc["layers"]:
                css = LAYER_CSS.get(layer["color_key"], "layer-blue")
                pts = "".join(f"<li>{p}</li>" for p in layer["points"])
                st.markdown(
                    f"""
                <div class="{css}">
                    <strong>{layer["name"]}</strong>
                    <ul style="margin:6px 0 0 0;padding-left:18px;font-size:0.9rem;line-height:1.7">
                        {pts}
                    </ul>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            st.markdown("")

            # Key insight
            st.markdown(
                f"""
            <div class="insight-box">
                <strong style="color:#f59e0b">💡 Key Insight</strong><br>
                {sc["key_insight"]}
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Diagram hint
            st.markdown(
                f"""
            <div style="font-size:0.82rem;color:#8fa3c0;margin-top:10px;font-style:italic">
                📊 {sc["diagram_hint"]}
            </div>
            """,
                unsafe_allow_html=True,
            )


# ─────────────────────────────────────────────────────────────────────────────
# Router
# ─────────────────────────────────────────────────────────────────────────────
PAGE = st.session_state.page

if PAGE == "home":
    render_home()
elif PAGE == "behavioral":
    render_behavioral()
elif PAGE == "quiz_setup":
    render_quiz_setup()
elif PAGE == "quiz":
    render_quiz()
elif PAGE == "results":
    render_results()
elif PAGE == "diagrams":
    render_diagrams()
elif PAGE == "scenarios":
    render_scenarios()
else:
    st.session_state.page = "home"
    st.rerun()
