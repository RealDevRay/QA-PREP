# data.py — Behavioral Q&A and Scenario Drills
# Raymond's personalized Tufin QA interview preparation data

BEHAVIORAL_QA = [
    {
        "id": "tell_me",
        "question": "Tell me about yourself.",
        "framework": "Past → Present → Future",
        "answer": (
            "My background is in software engineering — full-stack and AI platforms. "
            "I built Luminae, an AI platform with five concurrent agents processing academic papers. "
            "When those agents returned broken data and crashed the frontend, I stopped adding features "
            "and started preventing failures. I added Pydantic validation at the API layer to enforce "
            "a strict data contract, and built a Redis circuit breaker for cost control. "
            "That defensive engineering mindset led me to QA. I want to bring it to Tufin — "
            "a product where a bug is not a visual glitch but a real security hole."
        ),
        "points": [
            "Open: full-stack + AI engineering background",
            "Name Luminae and the 5-agent architecture",
            "Pivot moment: from 'building features' → 'preventing failures'",
            "Name your solutions: Pydantic + Redis circuit breaker",
            "Close specifically on Tufin: security infrastructure, not glitches",
        ],
        "tip": "60–90 seconds max. Always end on WHY Tufin specifically — never let the answer trail off.",
        "avoid": "Don't list every past job. Save Luminae technical depth for the complex-project question.",
    },
    {
        "id": "why_qa",
        "question": "Why do you want to work in QA and not stay as a developer?",
        "framework": "Reframe + Evidence",
        "answer": (
            "QA isn't a fallback — it's a different discipline. Developers are trained to focus "
            "on the happy path. I naturally look for what breaks. On Luminae I built more defensive "
            "systems than features — validation layers, circuit breakers, retry logic. "
            "I found that more satisfying than building the features themselves. "
            "I want to make investigating and preventing failures my full-time job."
        ),
        "points": [
            "Open with the reframe: 'QA is not a fallback — it is a specialisation'",
            "Developers = happy path. You = edge cases and failure modes",
            "Evidence from Luminae: defensive systems outnumbered features",
            "Close: 'make this my full-time job' — conviction, not desperation",
        ],
        "tip": "The word 'naturally' is key — it signals instinct, not a career pivot out of necessity.",
        "avoid": "Never say 'I want to move away from coding' or imply QA is a step down.",
    },
    {
        "id": "why_tufin",
        "question": "Why Tufin specifically?",
        "framework": "Problem → Stakes → Your Role",
        "answer": (
            "Tufin solves the policy-at-scale problem. Managing thousands of firewall rules manually "
            "across hybrid clouds creates security gaps — one wrong rule is a potential breach. "
            "Tufin removes human error by centralising and automating policy management. "
            "I want to test infrastructure where a bug is not a visual glitch but a real security hole."
        ),
        "points": [
            "Name the actual problem Tufin solves: policy-at-scale across hybrid clouds",
            "Quantify the stakes: one wrong rule = potential breach",
            "What Tufin does: centralise + automate policy management",
            "Your motivation: test something with real security consequences",
        ],
        "tip": "Mention SecureTrack or SecureChange by name if you can — it signals product research.",
        "avoid": "Don't say 'I heard it's a great company'. Don't focus on perks or location.",
    },
    {
        "id": "complex_project",
        "question": "Tell me about the most complex technical project you have worked on.",
        "framework": "Context → Problem → Action → Result",
        "answer": (
            "Luminae — an AI platform with five concurrent agents processing academic papers. "
            "The core problem: AI returns unpredictable JSON that standard tests couldn't catch, "
            "causing silent frontend crashes. My solution had two parts. First, I added Pydantic models "
            "to enforce a strict data contract at the API layer — any malformed payload was rejected "
            "before reaching the UI. Second, I built a Redis circuit breaker that killed the process "
            "if API costs exceeded the budget threshold. "
            "Result: zero structural defects reaching the UI and zero budget overruns."
        ),
        "points": [
            "Context: Luminae, 5 concurrent agents, academic papers",
            "Problem: unpredictable JSON → silent crashes (standard tests missed it)",
            "Action 1: Pydantic models → strict data contract at API boundary",
            "Action 2: Redis circuit breaker → real-time cost control",
            "Result: zero structural defects to UI, zero budget overruns",
        ],
        "tip": "Slow down on the result — pause after 'zero structural defects' and let it land.",
        "avoid": "Don't just describe the architecture. The story must end with a measurable outcome.",
    },
    {
        "id": "critical_bug",
        "question": "Describe a time you found a critical bug.",
        "framework": "STAR (Situation → Task → Action → Result)",
        "answer": (
            "On Luminae, users reported frontend crashes but the logs showed nothing — a classic silent failure. "
            "My task: trace the root cause with no error trail. I added staged logging at each API boundary. "
            "I found that malformed AI payloads were passing through the API layer without validation. "
            "I added Pydantic schemas so anything outside the expected shape was rejected at the gateway "
            "before it could reach the frontend. The crashes stopped immediately after deployment."
        ),
        "points": [
            "Situation: frontend crashes with no logs — a silent failure",
            "Task: trace root cause with no error trail",
            "Action: staged logging → found unvalidated AI payloads → added Pydantic schemas",
            "Result: crashes stopped immediately after deployment",
        ],
        "tip": "'Silent failure with no logs' shows advanced debugging skill. Emphasise that detail — it's the hook.",
        "avoid": "Don't describe a trivial or UI-only bug. This must sound production-level and serious.",
    },
    {
        "id": "new_tech",
        "question": "Tell me about a time you had to learn a new technology quickly.",
        "framework": "Goal → Method → Principle",
        "answer": (
            "I needed Redis for Luminae's circuit breaker but had never used it. "
            "My approach: 30% reading the official docs, 70% building. "
            "I gave myself a one-weekend deadline — a working cost monitor. "
            "I shipped it, it worked, and I refined it from there. "
            "My principle: when I need to learn fast, I build something real as early as possible. "
            "Theory without practice doesn't stick."
        ),
        "points": [
            "Technology: Redis (needed for circuit breaker — never used before)",
            "Method: 30% docs / 70% building",
            "Constraint: one-weekend deadline",
            "Outcome: shipped, worked, refined iteratively",
            "Principle: 'build something real as early as possible'",
        ],
        "tip": "The 30/70 split is memorable and shows a mature engineering approach to learning.",
        "avoid": "Don't say 'I just Googled it'. Show a deliberate method and a principle.",
    },
    {
        "id": "conflict_dev",
        "question": "Describe a conflict with a developer. How did you resolve it?",
        "framework": "Disagree → Evidence → Collaborate",
        "answer": (
            "I raised a concern about missing validation on Luminae's data pipeline. "
            "The developer felt it was unnecessary overhead. Instead of arguing, I built a proof of "
            "concept that reproduced the crash and showed it running live. "
            "The developer saw the failure with their own eyes. The fix went in the same day. "
            "My rule: show the problem — don't just describe it."
        ),
        "points": [
            "Conflict: I wanted validation, developer called it unnecessary overhead",
            "Action: built a PoC that reproduced the exact crash — live demo",
            "Result: developer saw it, fix was merged the same day",
            "Principle: 'show the problem — do not just describe it'",
        ],
        "tip": "End with the principle — it shows you extracted a lesson, not just scored a win.",
        "avoid": "Don't frame it as 'I was right, they were wrong'. Frame it as collaborative problem-solving.",
    },
    {
        "id": "ambiguous_reqs",
        "question": "How do you handle ambiguous requirements?",
        "framework": "First Bug → 3-Question Framework → Document",
        "answer": (
            "I treat ambiguity as the first bug to resolve. I document the gap and ask three questions: "
            "what does success look like, what is the worst-case failure, and who decides? "
            "If I can't get clarity in time, I test both interpretations and document my assumption. "
            "I never silently guess — that leads to testing the wrong thing entirely."
        ),
        "points": [
            "Frame it: 'ambiguity is the first bug to resolve'",
            "Three specific questions: success criteria / worst-case failure / decision-maker",
            "Fallback: test both interpretations, document assumptions explicitly",
            "Principle: never silently guess",
        ],
        "tip": "Memorise those three questions exactly — they show structured thinking under pressure.",
        "avoid": "Don't say 'I just ask my manager'. Show your own structured reasoning process.",
    },
    {
        "id": "bug_priority",
        "question": "How do you prioritise which bugs to fix first?",
        "framework": "Severity-Impact Matrix",
        "answer": (
            "I use a severity-impact matrix. High severity and high impact — fix it now. "
            "High severity and low impact — this sprint. Low severity and high impact — next sprint. "
            "Low severity and low impact — backlog. "
            "Security bugs are always P1 regardless of apparent impact — one exploit is one too many."
        ),
        "points": [
            "Tool: 2×2 severity-impact matrix",
            "High/High → fix now | High/Low → this sprint",
            "Low/High → next sprint | Low/Low → backlog",
            "Security exception: always P1 — 'one exploit is one too many'",
        ],
        "tip": "Sketch the matrix in the air on video — it makes the answer visual and memorable.",
        "avoid": "Don't just say 'I prioritise by severity'. The matrix shows a system, not just instinct.",
    },
    {
        "id": "weakness",
        "question": "What is your greatest weakness?",
        "framework": "Real Weakness + Active Fix + Outcome",
        "answer": (
            "I tend to over-engineer. I reach for the most complete solution even when a simpler one would work. "
            "I've learned to time-box design decisions to 20 minutes — if I'm still designing after that, "
            "I build the simpler version first and iterate. "
            "It's made me faster without sacrificing quality."
        ),
        "points": [
            "Real weakness: over-engineering — not a cliché",
            "Show self-awareness: you recognise when it's happening",
            "Active fix: the 20-minute time-box rule",
            "Outcome: faster without sacrificing quality",
        ],
        "tip": "Over-engineering reads as 'I care deeply about quality'. It's a credible, engineer-friendly weakness.",
        "avoid": "Never say 'I work too hard' or 'I'm a perfectionist'. Be specific and show the fix.",
    },
    {
        "id": "three_years",
        "question": "Where do you see yourself in three years?",
        "framework": "Depth → Ownership → Impact",
        "answer": (
            "Deeply expert in network security testing. Knowing the Tufin platform well enough to catch "
            "edge cases others would miss. Owning end-to-end test suites for critical features and "
            "helping build the automation frameworks the team depends on. "
            "I want to have shipped things, broken things on purpose, and made the product measurably more reliable."
        ),
        "points": [
            "Depth: become the expert in network security testing",
            "Platform mastery: catch edge cases others would miss",
            "Ownership: own test suites, build automation frameworks",
            "Memorable close: 'broken things on purpose' — shows QA identity",
        ],
        "tip": "Don't mention management or switching roles. Show you want to go deeper, not sideways.",
        "avoid": "Don't say 'I hope to be a Senior QA'. Talk about impact and mastery, not job titles.",
    },
]


SCENARIO_QA = [
    {
        "id": "permissions_manager",
        "title": "Permissions Manager Screen",
        "scenario": "You are shown Tufin's Permissions Manager screen. How would you test it?",
        "clarify_first": [
            "What roles exist in the system?",
            "Does a permission change apply immediately or on next login?",
            "What endpoints does the Permissions UI call under the hood?",
        ],
        "layers": [
            {
                "name": "Layer 1 — UI Tests",
                "color_key": "blue",
                "points": [
                    "Check a permission → verify the user gains that action immediately",
                    "Uncheck it → verify the user loses the action",
                    "Navigate directly to a restricted URL as a Viewer — must be blocked",
                ],
            },
            {
                "name": "Layer 2 — API Test ★ CRITICAL",
                "color_key": "red",
                "points": [
                    "Extract the Viewer's session token",
                    "Send PUT /restricted-endpoint with that token",
                    "Server MUST return 403 Forbidden",
                    "200 OK = backend RBAC vulnerability — the UI was just decoration",
                ],
            },
            {
                "name": "Layer 3 — Live Session Test",
                "color_key": "purple",
                "points": [
                    "Remove a permission from a currently logged-in user",
                    "Confirm it applies immediately — no re-login required",
                ],
            },
        ],
        "key_insight": "Hiding a button is a UI control, not a security control. The backend must enforce permissions independently of what the frontend renders.",
        "diagram_hint": "See '3-Layer RBAC Test' in Visual Reference → Networking tab.",
    },
    {
        "id": "firewall_event_log",
        "title": "Firewall Event Log",
        "scenario": "You are shown a Firewall Event Log screen. Walk me through your test plan.",
        "clarify_first": [
            "Which events should appear in the log?",
            "Is the log append-only, or can entries be edited/deleted?",
            "What filters are available — time range, source IP, action, interface?",
        ],
        "layers": [
            {
                "name": "Injection Tests",
                "color_key": "red",
                "points": [
                    "Inject known blocked traffic — verify the event appears",
                    "Check timestamp accuracy: log time vs actual event time",
                    "Verify the correct rule name is logged for each event",
                ],
            },
            {
                "name": "Filter Tests",
                "color_key": "blue",
                "points": [
                    "Time range filter: events outside the range must not appear",
                    "Source IP filter: exact IP and CIDR notation",
                    "Action filter: allow vs block — must show only matching rows",
                    "Interface filter",
                ],
            },
            {
                "name": "Integrity Tests",
                "color_key": "green",
                "points": [
                    "Log is READ-ONLY — no user should be able to edit or delete entries",
                    "CSV export is complete and matches what is displayed",
                    "Performance: 10,000+ events must not break the UI or filters",
                ],
            },
        ],
        "key_insight": "The most important test is immutability. A security log that can be modified is worse than no log — it creates false confidence.",
        "diagram_hint": "See the 'Firewall Event Log' strategy diagram in Visual Reference → Networking tab.",
    },
    {
        "id": "detection_dashboard",
        "title": "Detection & Response Dashboard",
        "scenario": "You are shown a detection dashboard with summary counts and live alerts. How would you test it?",
        "clarify_first": [
            "What is the data source for the counts — live query or cached?",
            "How often does the dashboard refresh?",
            "Does filtering by date affect all three widgets simultaneously?",
        ],
        "layers": [
            {
                "name": "Data Integrity — Test This FIRST",
                "color_key": "red",
                "points": [
                    "Open + Acknowledged + Closed MUST equal Total",
                    "If those numbers don't add up, everything else is irrelevant — the data is wrong",
                    "Verify counts update correctly when an alert changes state",
                ],
            },
            {
                "name": "Widget Synchronisation",
                "color_key": "blue",
                "points": [
                    "Change the date range filter — all three widgets must update together",
                    "No widget should show stale data while another updates",
                    "Empty state: zero alerts must show a message, not a broken layout",
                ],
            },
            {
                "name": "Edge Cases",
                "color_key": "purple",
                "points": [
                    "Date range spanning midnight and timezone boundaries",
                    "Simultaneously open and close an alert — does the count go negative?",
                    "Very large alert volumes — does the UI degrade gracefully?",
                ],
            },
        ],
        "key_insight": "Start with the maths. Open + Acknowledged + Closed must equal Total. If that equation breaks, every other test on this dashboard is built on corrupted data.",
        "diagram_hint": "See 'Detection Dashboard' diagram in Visual Reference → Networking tab.",
    },
    {
        "id": "change_management",
        "title": "Change Management Workflow",
        "scenario": "You are shown a Change Management workflow screen. Walk me through your full test plan.",
        "clarify_first": [
            "Who can initiate a change request, and who can approve it?",
            "What happens when a request is rejected?",
            "Can an admin approve their own change request?",
        ],
        "layers": [
            {
                "name": "Happy Path",
                "color_key": "green",
                "points": [
                    "Submit → Approve → Implement → verify every step is logged with timestamp + user ID",
                    "Rejection path: requester is notified, change is NOT applied",
                    "Completed change appears in the audit trail",
                ],
            },
            {
                "name": "Authorisation Tests ★ CRITICAL",
                "color_key": "red",
                "points": [
                    "Viewer submitting a change must be blocked at UI AND API level",
                    "Non-approver token + PUT /approve → must return 403",
                    "Admin cannot approve their own request — test this explicitly",
                ],
            },
            {
                "name": "Edge Cases",
                "color_key": "purple",
                "points": [
                    "Approver's role is revoked while a request is pending",
                    "Concurrent approvals: two approvers submit simultaneously",
                    "Timeout: what happens to a request pending for 30 days?",
                ],
            },
        ],
        "key_insight": "No admin may approve their own change request. This is a segregation-of-duties control required by PCI-DSS, SOX, and similar compliance frameworks. Test it explicitly.",
        "diagram_hint": "See 'Change Management Workflow' diagram in Visual Reference → Networking tab.",
    },
]
