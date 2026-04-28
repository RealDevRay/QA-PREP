"""charts.py — Matplotlib diagram generators for the Tufin QA Interview Prep app."""

import io

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
BG = "#F7F9FC"


# ─────────────────────────────────────────────────────────────────────────────
# Shared drawing helpers
# ─────────────────────────────────────────────────────────────────────────────
def _rounded_box(
    ax, x, y, w, h, text, fc, ec="white", lw=2, tc="white", fs=9, fw="bold"
):
    rect = mpatches.FancyBboxPatch(
        (x - w / 2, y - h / 2),
        w,
        h,
        boxstyle="round,pad=0.12",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
    )
    ax.add_patch(rect)
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        fontweight=fw,
        color=tc,
        multialignment="center",
    )


def _arrow(ax, x1, y1, x2, y2, lc="#7F8C8D", lw=2, ls="-"):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color=lc, lw=lw, linestyle=ls),
    )


# ═════════════════════════════════════════════════════════════════════════════
#   NETWORKING DIAGRAMS
# ═════════════════════════════════════════════════════════════════════════════


def rule_order_diagram():
    fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.set_title(
        "Firewall Rule Evaluation: Top-Down, First Match Wins",
        fontsize=12,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )

    cols = ["#", "Source", "Destination", "Port", "Action"]
    xs = [0.5, 1.9, 4.0, 6.3, 7.9]
    ws = [1.2, 1.9, 2.0, 1.3, 2.4]
    y = 6.8
    for hdr, cx, cw in zip(cols, xs, ws):
        ax.add_patch(
            mpatches.Rectangle(
                (cx, y - 0.3), cw - 0.1, 0.6, facecolor="#2E74B5", edgecolor="white"
            )
        )
        ax.text(
            cx + (cw - 0.1) / 2,
            y,
            hdr,
            ha="center",
            va="center",
            fontsize=9.5,
            fontweight="bold",
            color="white",
        )

    rules = [
        (
            "1",
            "Any",
            "Any",
            "Any",
            "DENY ALL",
            "#C0392B",
            "#FDECEA",
            "← Matches FIRST — every packet blocked",
        ),
        (
            "2",
            "192.168.1.0/24",
            "10.0.0.5",
            "443",
            "ALLOW",
            "#BDC3C7",
            "#F5F5F5",
            "← Dead code — never reached",
        ),
        (
            "3",
            "Any",
            "10.0.0.5",
            "80",
            "ALLOW",
            "#BDC3C7",
            "#F5F5F5",
            "← Dead code — never reached",
        ),
    ]
    for ri, (num, src, dst, port, action, ac, bg, note) in enumerate(rules):
        ry = y - 0.95 * (ri + 1)
        ax.add_patch(
            mpatches.Rectangle(
                (0.5, ry - 0.3), 9.3, 0.6, facecolor=bg, edgecolor="#D5D8DC"
            )
        )
        for val, cx, cw in zip([num, src, dst, port, action], xs, ws):
            fc = ac if val == action else "#2C3E50"
            ax.text(
                cx + (cw - 0.1) / 2,
                ry,
                val,
                ha="center",
                va="center",
                fontsize=8.5,
                color=fc,
                fontweight="bold" if val == action else "normal",
            )
        ax.text(
            10.1,
            ry,
            note,
            ha="left",
            va="center",
            fontsize=7.5,
            color="#7F8C8D",
            style="italic",
        )

    _arrow(ax, 0.2, 6.55, 0.2, 5.05, lc="#3498DB")
    ax.text(
        0.2,
        4.85,
        "eval\norder",
        ha="center",
        fontsize=7,
        color="#3498DB",
        fontweight="bold",
    )

    ax.text(
        5.5,
        1.4,
        "FIX: Move specific ALLOW rules ABOVE the DENY-ALL",
        ha="center",
        fontsize=10.5,
        color="#27AE60",
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="#EAFAF1", edgecolor="#27AE60", pad=0.4),
    )
    fig.tight_layout()
    return fig


def publish_install_diagram():
    fig, ax = plt.subplots(figsize=(9.5, 4), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.5)
    ax.set_title(
        "Publish vs Install Policy — Two Completely Separate Operations",
        fontsize=12,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )

    _rounded_box(ax, 1.6, 3.8, 2.6, 1.0, "Admin edits\nrule", "#3498DB")
    _rounded_box(
        ax,
        5.3,
        3.8,
        2.8,
        1.0,
        "Mgmt Server DB\nupdated\n(visible to admins)",
        "#8E44AD",
    )
    _rounded_box(ax, 9.3, 3.8, 2.8, 1.0, "Gateway enforces\nnew rules ✓", "#27AE60")

    _arrow(ax, 2.9, 3.8, 3.9, 3.8, lc="#8E44AD")
    ax.text(
        3.4,
        4.35,
        "PUBLISH",
        fontsize=8.5,
        color="#8E44AD",
        fontweight="bold",
        ha="center",
    )
    _arrow(ax, 6.7, 3.8, 7.9, 3.8, lc="#E74C3C")
    ax.text(
        7.3,
        4.35,
        "INSTALL POLICY",
        fontsize=8.5,
        color="#E74C3C",
        fontweight="bold",
        ha="center",
    )

    _rounded_box(
        ax,
        5.3,
        1.8,
        4.0,
        1.0,
        "⚠  Only PUBLISH done\nGateway still enforces OLD rules!",
        "#C0392B",
    )
    ax.annotate(
        "",
        xy=(5.3, 2.3),
        xytext=(5.3, 3.3),
        arrowprops=dict(arrowstyle="->", color="#C0392B", lw=2, linestyle="dashed"),
    )
    fig.tight_layout()
    return fig


def multi_domain_diagram():
    fig, ax = plt.subplots(figsize=(9.5, 5.5), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(
        "Multi-Domain: Each Domain Is Completely Isolated",
        fontsize=12,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )

    _rounded_box(
        ax,
        5.0,
        6.2,
        4.8,
        0.9,
        "Multi-Domain Server (MDS)  |  Admin context: Domain A only",
        "#2E74B5",
    )

    for bx, by, bw, bh, label, fc, items in [
        (
            2.3,
            3.7,
            4.2,
            2.5,
            "Domain A",
            "#27AE60",
            ["✓  Policy changed", "✓  Install Policy run"],
        ),
        (
            7.7,
            3.7,
            4.2,
            2.5,
            "Domain B",
            "#C0392B",
            ["✗  NOT touched", "    (old policy still active)"],
        ),
    ]:
        ax.add_patch(
            mpatches.FancyBboxPatch(
                (bx - bw / 2, by - bh / 2),
                bw,
                bh,
                boxstyle="round,pad=0.2",
                facecolor=fc,
                edgecolor="white",
                linewidth=2,
            )
        )
        ax.text(
            bx,
            by + 0.85,
            label,
            ha="center",
            fontsize=11,
            fontweight="bold",
            color="white",
        )
        for i, item in enumerate(items):
            ax.text(
                bx,
                by + 0.15 - i * 0.6,
                item,
                ha="center",
                fontsize=8.5,
                color="white",
                multialignment="center",
            )

    _arrow(ax, 3.5, 5.75, 2.3, 4.95, lc="#27AE60")
    ax.annotate(
        "",
        xy=(7.7, 4.95),
        xytext=(6.5, 5.75),
        arrowprops=dict(arrowstyle="->", color="#C0392B", lw=2, linestyle="dashed"),
    )

    for gx, gc, gl in [
        (1.5, "#27AE60", "GW-A1"),
        (3.1, "#27AE60", "GW-A2"),
        (6.5, "#C0392B", "GW-B1"),
        (8.1, "#C0392B", "GW-B2"),
    ]:
        _rounded_box(ax, gx, 1.5, 1.2, 0.65, gl, gc, fs=8.5)
        _arrow(ax, gx, 2.45, gx, 1.85, lc=gc)

    ax.text(
        5.0,
        0.4,
        "Fix: switch to Domain B context → make change → Publish → Install Policy on Domain B gateways",
        ha="center",
        fontsize=8,
        color="#7F8C8D",
        style="italic",
    )
    fig.tight_layout()
    return fig


def time_rule_diagram():
    fig, ax = plt.subplots(figsize=(9.5, 3.8), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 4)

    ax.axvspan(0, 9, alpha=0.18, color="#E74C3C")
    ax.axvspan(9, 17, alpha=0.20, color="#27AE60")
    ax.axvspan(17, 24, alpha=0.18, color="#E74C3C")
    ax.axvline(x=9, color="#27AE60", linewidth=2.5, linestyle="--")
    ax.axvline(x=17, color="#27AE60", linewidth=2.5, linestyle="--")

    ax.text(
        4.5,
        2.8,
        "BLOCKED",
        ha="center",
        fontsize=14,
        color="#E74C3C",
        fontweight="bold",
        alpha=0.75,
    )
    ax.text(
        13.0,
        2.8,
        "ALLOWED",
        ha="center",
        fontsize=14,
        color="#27AE60",
        fontweight="bold",
    )
    ax.text(
        20.5,
        2.8,
        "BLOCKED",
        ha="center",
        fontsize=14,
        color="#E74C3C",
        fontweight="bold",
        alpha=0.75,
    )

    for t, lbl, c in [
        (8.983, "8:59:59\nBLOCKED", "#C0392B"),
        (9.0, "9:00:00\nALLOWED", "#27AE60"),
        (16.983, "4:59:59\nALLOWED", "#27AE60"),
        (17.0, "5:00:01\nBLOCKED", "#C0392B"),
    ]:
        ax.axvline(x=t, color=c, linewidth=1.5, linestyle=":")
        ax.text(
            t,
            0.35,
            lbl,
            ha="center",
            fontsize=7.5,
            color=c,
            fontweight="bold",
            multialignment="center",
        )

    ax.set_xticks(range(0, 25, 3))
    ax.set_xticklabels([f"{h:02d}:00" for h in range(0, 25, 3)], fontsize=9)
    ax.set_yticks([])
    ax.set_xlabel("Time of Day", fontsize=10)
    ax.set_title(
        "Time-Based Rule: 09:00–17:00 ALLOW  |  Boundary tests at exact seconds  |  Verify timezone handling",
        fontsize=10,
        fontweight="bold",
        color="#2C3E50",
        pad=8,
    )
    for sp in ["top", "left", "right"]:
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    return fig


def securetrack_securechange_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), facecolor=BG)
    fig.suptitle(
        "SecureTrack vs SecureChange", fontsize=14, fontweight="bold", color="#2C3E50"
    )

    for ax, title, fc, items in [
        (
            ax1,
            "SecureTrack\n(Visibility & Compliance)",
            "#2E74B5",
            [
                "• View all firewall rules across all devices",
                "• Track every policy change over time",
                "• Flag rule conflicts & shadow rules",
                "• Compliance reports (PCI, SOX, HIPAA…)",
                "• Network topology path analysis",
                "",
                '➜ "What do the rules look like RIGHT NOW?"',
            ],
        ),
        (
            ax2,
            "SecureChange\n(Workflow Automation)",
            "#27AE60",
            [
                "• Manage change requests end-to-end",
                "• Route tickets to correct approvers",
                "• Risk analysis before rule is approved",
                "• Auto-deploy approved changes to gateways",
                "• Full audit trail per change request",
                "",
                '➜ "How do I change a rule SAFELY?"',
            ],
        ),
    ]:
        ax.set_facecolor(fc)
        ax.axis("off")
        ax.text(
            0.5,
            0.96,
            title,
            ha="center",
            va="top",
            transform=ax.transAxes,
            fontsize=11,
            fontweight="bold",
            color="white",
            multialignment="center",
        )
        for i, item in enumerate(items):
            bold = item.startswith("➜")
            ax.text(
                0.06,
                0.82 - i * 0.1,
                item,
                ha="left",
                va="top",
                transform=ax.transAxes,
                fontsize=8.5,
                color="white",
                fontweight="bold" if bold else "normal",
                style="italic" if bold else "normal",
            )

    fig.tight_layout(rect=[0, 0, 1, 0.93])
    return fig


def rbac_layers_diagram():
    fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(
        "3-Layer RBAC Test: Viewer Cannot Modify Firewall Rules",
        fontsize=12,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )

    layers = [
        (
            4.5,
            5.6,
            9.0,
            1.3,
            "Layer 1 — UI Test",
            "• Log in as Viewer  |  Edit/Save buttons must be hidden or disabled\n"
            "• Type the edit URL directly — must be blocked",
            "#3498DB",
        ),
        (
            4.5,
            3.7,
            9.0,
            1.3,
            "Layer 2 — API Test  ★ MOST CRITICAL",
            "• Extract Viewer session token\n"
            "• PUT /rules/{id}  →  expect 403 Forbidden\n"
            "• 200 OK = backend RBAC vulnerability!",
            "#C0392B",
        ),
        (
            4.5,
            1.8,
            9.0,
            1.3,
            "Layer 3 — Live Session Test",
            "• Demote an Admin to Viewer mid-session\n"
            "• Next save attempt must be rejected immediately",
            "#8E44AD",
        ),
    ]
    for lx, ly, lw, lh, title, desc, fc in layers:
        _rounded_box(ax, lx, ly, lw, lh, "", fc, lw=2)
        ax.text(
            lx,
            ly + 0.42,
            title,
            ha="center",
            va="center",
            fontsize=9.5,
            fontweight="bold",
            color="white",
        )
        ax.text(
            lx,
            ly - 0.15,
            desc,
            ha="center",
            va="center",
            fontsize=8.5,
            color="#ECF0F1",
            multialignment="center",
        )
    fig.tight_layout()
    return fig


# ═════════════════════════════════════════════════════════════════════════════
#   QA FRAMEWORK DIAGRAMS
# ═════════════════════════════════════════════════════════════════════════════


def severity_matrix_diagram():
    fig, ax = plt.subplots(figsize=(7, 5.5), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title(
        "Bug Prioritisation: Severity-Impact Matrix",
        fontsize=12,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )

    # Quadrants
    for qx, qy, label, sub, fc in [
        (7, 6, "FIX NOW", "High Severity / High Impact", "#C0392B"),
        (3, 6, "THIS SPRINT", "High Severity / Low Impact", "#E67E22"),
        (7, 3, "NEXT SPRINT", "Low Severity / High Impact", "#F39C12"),
        (3, 3, "BACKLOG", "Low Severity / Low Impact", "#27AE60"),
    ]:
        _rounded_box(ax, qx, qy, 3.5, 2.2, f"{label}\n{sub}", fc, fs=9)

    # Axis labels
    ax.text(
        5.0,
        1.2,
        "← Low Impact          High Impact →",
        ha="center",
        fontsize=9,
        color="#7F8C8D",
    )
    ax.text(
        0.5,
        4.5,
        "High\nSeverity",
        ha="center",
        fontsize=8.5,
        color="#7F8C8D",
        rotation=90,
    )
    ax.text(
        0.5,
        2.5,
        "Low\nSeverity",
        ha="center",
        fontsize=8.5,
        color="#7F8C8D",
        rotation=90,
    )

    # Security annotation
    ax.text(
        5.0,
        0.45,
        "★  Security bugs → always P1 regardless of quadrant — one exploit is one too many",
        ha="center",
        fontsize=9,
        color="#C0392B",
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="#FDECEA", edgecolor="#C0392B", pad=0.35),
    )
    fig.tight_layout()
    return fig


def test_pyramid_diagram():
    fig, ax = plt.subplots(figsize=(7, 5.5), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title(
        "The Test Pyramid", fontsize=12, fontweight="bold", color="#2C3E50", pad=10
    )

    levels = [
        (
            5.0,
            1.5,
            8.0,
            1.8,
            "Unit Tests",
            "Many  ·  Fast  ·  Cheap  ·  Isolated",
            "#27AE60",
        ),
        (
            5.0,
            3.8,
            5.5,
            1.8,
            "Integration Tests",
            "Fewer  ·  Slower  ·  Test interfaces",
            "#F39C12",
        ),
        (5.0, 6.0, 3.0, 1.8, "E2E Tests", "Few  ·  Slow  ·  Expensive", "#C0392B"),
    ]
    for lx, ly, lw, lh, title, sub, fc in levels:
        _rounded_box(ax, lx, ly, lw, lh, f"{title}\n{sub}", fc, fs=8.5)

    ax.annotate(
        "",
        xy=(1.5, 0.6),
        xytext=(1.5, 7.0),
        arrowprops=dict(arrowstyle="<->", color="#7F8C8D", lw=1.5),
    )
    ax.text(
        1.0,
        3.8,
        "More\ntests",
        ha="center",
        fontsize=8,
        color="#27AE60",
        rotation=90,
        fontweight="bold",
    )
    ax.annotate(
        "",
        xy=(8.8, 0.6),
        xytext=(8.8, 7.0),
        arrowprops=dict(arrowstyle="<->", color="#7F8C8D", lw=1.5),
    )
    ax.text(
        9.4,
        3.8,
        "Slower &\ncostlier",
        ha="center",
        fontsize=8,
        color="#C0392B",
        rotation=90,
        fontweight="bold",
    )
    fig.tight_layout()
    return fig


# ═════════════════════════════════════════════════════════════════════════════
#   JAVA CODING DIAGRAMS
# ═════════════════════════════════════════════════════════════════════════════


def hashset_diagram():
    fig, ax = plt.subplots(figsize=(9, 3.8), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.set_title(
        "HashSet Duplicate Detection  |  add() returns FALSE on duplicate → return true immediately",
        fontsize=10,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )

    steps = [
        ("add(3)", True, "{3}", "true ✓"),
        ("add(7)", True, "{3, 7}", "true ✓"),
        ("add(2)", True, "{3, 7, 2}", "true ✓"),
        ("add(3)", False, "{3, 7, 2}", "FALSE → DUPLICATE!"),
    ]
    for i, (op, ok, state, ret) in enumerate(steps):
        x = i * 2.35 + 1.0
        fc = "#27AE60" if ok else "#C0392B"
        _rounded_box(ax, x, 3.5, 1.9, 0.85, op, fc, fs=9)
        ax.text(
            x,
            2.7,
            f"returns: {ret}",
            ha="center",
            fontsize=7.5,
            color=fc,
            fontweight="bold",
        )
        ax.text(x, 2.0, f"Set: {state}", ha="center", fontsize=7.5, color="#7F8C8D")
        if i < len(steps) - 1:
            _arrow(ax, x + 0.95, 3.5, x + 1.4, 3.5, lc="#BDC3C7")

    ax.text(
        5.0,
        0.9,
        "O(n) time  ·  O(n) space  ·  Exit immediately on false return",
        ha="center",
        fontsize=9,
        color="#7F8C8D",
    )
    fig.tight_layout()
    return fig


def two_pointer_diagram():
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.5), facecolor=BG)
    fig.suptitle(
        "Two-Pointer Pattern: Reverse String  &  Palindrome Check",
        fontsize=11,
        fontweight="bold",
        color="#2C3E50",
    )

    # Left: reverse "hello"
    stages_rev = [
        (list("hello"), 0, 4, "Swap h ↔ o"),
        (list("oellh"), 1, 3, "Swap e ↔ l"),
        (list("olleh"), 2, 2, 'L=R → done: "olleh"'),
    ]
    ax = axes[0]
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(-0.5, 14.5)
    ax.set_ylim(-1.2, 3.5)
    ax.set_title(
        'Reverse: "hello" → "olleh"', fontsize=9.5, fontweight="bold", color="#2C3E50"
    )
    for si, (arr, L, R, title) in enumerate(stages_rev):
        ox = si * 5
        ax.text(
            ox + 2.0,
            3.1,
            title,
            ha="center",
            fontsize=8,
            color="#2C3E50",
            fontweight="bold",
        )
        for i, ch in enumerate(arr):
            fc = (
                "#E74C3C"
                if (i == L or i == R) and L != R
                else "#F39C12"
                if i == L == R
                else "#3498DB"
            )
            rect = mpatches.FancyBboxPatch(
                (ox + i * 0.85 + 0.1, 0.35),
                0.75,
                0.75,
                boxstyle="round,pad=0.05",
                facecolor=fc,
                edgecolor="white",
                linewidth=2,
            )
            ax.add_patch(rect)
            ax.text(
                ox + i * 0.85 + 0.47,
                0.72,
                ch,
                ha="center",
                va="center",
                fontsize=11,
                fontweight="bold",
                color="white",
            )
        if L != R:
            ax.text(
                ox + L * 0.85 + 0.47,
                -0.2,
                "↑L",
                ha="center",
                fontsize=8,
                color="#E74C3C",
                fontweight="bold",
            )
            ax.text(
                ox + R * 0.85 + 0.47,
                -0.2,
                "R↑",
                ha="center",
                fontsize=8,
                color="#E74C3C",
                fontweight="bold",
            )
        else:
            ax.text(
                ox + L * 0.85 + 0.47,
                -0.2,
                "L=R",
                ha="center",
                fontsize=8,
                color="#F39C12",
                fontweight="bold",
            )
        if si < 2:
            ax.text(
                ox + 4.5,
                0.72,
                "→",
                ha="center",
                fontsize=14,
                color="#BDC3C7",
                fontweight="bold",
            )

    # Right: palindrome "racecar"
    stages_pal = [
        (list("racecar"), 0, 6, "r == r ✓"),
        (list("racecar"), 1, 5, "a == a ✓"),
        (list("racecar"), 3, 3, "L=R → true"),
    ]
    ax2 = axes[1]
    ax2.set_facecolor(BG)
    ax2.axis("off")
    ax2.set_xlim(-0.5, 20)
    ax2.set_ylim(-1.2, 3.5)
    ax2.set_title(
        'Palindrome: "racecar" → true', fontsize=9.5, fontweight="bold", color="#2C3E50"
    )
    for si, (arr, L, R, title) in enumerate(stages_pal):
        ox = si * 7
        ax2.text(
            ox + 3.0,
            3.1,
            title,
            ha="center",
            fontsize=8,
            color="#2C3E50",
            fontweight="bold",
        )
        for i, ch in enumerate(arr):
            if i == L == R:
                fc = "#F39C12"
            elif i == L or i == R:
                fc = "#E74C3C"
            elif i < L or i > R:
                fc = "#BDC3C7"
            else:
                fc = "#3498DB"
            rect = mpatches.FancyBboxPatch(
                (ox + i * 0.85 + 0.1, 0.35),
                0.75,
                0.75,
                boxstyle="round,pad=0.05",
                facecolor=fc,
                edgecolor="white",
                linewidth=2,
            )
            ax2.add_patch(rect)
            ax2.text(
                ox + i * 0.85 + 0.47,
                0.72,
                ch,
                ha="center",
                va="center",
                fontsize=11,
                fontweight="bold",
                color="white",
            )
        if L != R:
            ax2.text(
                ox + L * 0.85 + 0.47,
                -0.2,
                "↑L",
                ha="center",
                fontsize=8,
                color="#E74C3C",
                fontweight="bold",
            )
            ax2.text(
                ox + R * 0.85 + 0.47,
                -0.2,
                "R↑",
                ha="center",
                fontsize=8,
                color="#E74C3C",
                fontweight="bold",
            )
        else:
            ax2.text(
                ox + L * 0.85 + 0.47,
                -0.2,
                "L=R",
                ha="center",
                fontsize=8,
                color="#F39C12",
                fontweight="bold",
            )
        if si < 2:
            ax2.text(
                ox + 6.5,
                0.72,
                "→",
                ha="center",
                fontsize=14,
                color="#BDC3C7",
                fontweight="bold",
            )

    fig.tight_layout()
    return fig


def fizzbuzz_tree_diagram():
    fig, ax = plt.subplots(figsize=(7.5, 6), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title(
        "FizzBuzz + Tufin Decision Tree  |  Most-Specific Condition FIRST",
        fontsize=10,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )

    _rounded_box(ax, 5, 9.3, 4.5, 0.75, "i  from 1 to 20", "#2E74B5")
    _arrow(ax, 5, 8.92, 5, 8.22)
    _rounded_box(ax, 5, 7.82, 5.5, 0.75, "i%3==0  AND  i%5==0  AND  i%7==0?", "#8E44AD")
    ax.text(1.55, 8.08, "YES", fontsize=8.5, color="#27AE60", fontweight="bold")
    ax.annotate(
        "",
        xy=(1.5, 7.35),
        xytext=(2.25, 7.82),
        arrowprops=dict(arrowstyle="->", color="#27AE60", lw=1.8),
    )
    _rounded_box(ax, 1.5, 7.0, 2.2, 0.6, "FizzBuzzTufin", "#27AE60", fs=8.5)

    _arrow(ax, 5, 7.44, 5, 6.72)
    _rounded_box(
        ax, 5, 6.32, 5.5, 0.75, "Two-factor combo?\n(3&5) | (3&7) | (5&7)", "#16A085"
    )
    ax.text(1.55, 6.58, "YES", fontsize=8.5, color="#27AE60", fontweight="bold")
    ax.annotate(
        "",
        xy=(1.5, 5.9),
        xytext=(2.25, 6.32),
        arrowprops=dict(arrowstyle="->", color="#27AE60", lw=1.8),
    )
    _rounded_box(
        ax, 1.5, 5.5, 2.5, 0.7, "FizzBuzz\nFizzTufin\nBuzzTufin", "#27AE60", fs=8
    )

    _arrow(ax, 5, 5.94, 5, 5.22)
    _rounded_box(ax, 5, 4.82, 4.5, 0.75, "Single divisor?\ni%3 | i%5 | i%7", "#E67E22")
    ax.text(1.55, 5.08, "YES", fontsize=8.5, color="#27AE60", fontweight="bold")
    ax.annotate(
        "",
        xy=(1.5, 4.38),
        xytext=(2.75, 4.82),
        arrowprops=dict(arrowstyle="->", color="#27AE60", lw=1.8),
    )
    _rounded_box(ax, 1.5, 4.0, 2.2, 0.6, "Fizz / Buzz / Tufin", "#E67E22", fs=8.5)

    _arrow(ax, 5, 4.44, 5, 3.72)
    _rounded_box(ax, 5, 3.35, 3.0, 0.65, "print(i)", "#C0392B")

    ax.text(
        5,
        1.9,
        "Output 1–20:  1  2  Fizz  4  Buzz  Fizz  Tufin  8  Fizz  Buzz\n"
        "11  Fizz  13  Tufin  FizzBuzz  16  17  Fizz  19  Buzz",
        ha="center",
        fontsize=8.5,
        color="#2C3E50",
        bbox=dict(boxstyle="round", facecolor="#EBF5FB", edgecolor="#2E74B5", pad=0.4),
    )
    fig.tight_layout()
    return fig


def word_freq_diagram():
    fig, ax = plt.subplots(figsize=(7, 3.5), facecolor=BG)
    ax.set_facecolor(BG)
    words = ["apple", "banana", "orange"]
    counts = [2, 1, 1]
    colors = ["#3498DB", "#9B59B6", "#E67E22"]
    bars = ax.barh(words, counts, color=colors, edgecolor="white", height=0.45)
    for bar, cnt in zip(bars, counts):
        ax.text(
            bar.get_width() + 0.05,
            bar.get_y() + bar.get_height() / 2,
            str(cnt),
            va="center",
            fontsize=12,
            fontweight="bold",
            color="#2C3E50",
        )
    ax.set_xlim(0, 3.3)
    ax.set_xlabel("Frequency", fontsize=10)
    ax.set_title(
        "HashMap Word Frequency  |  getOrDefault(word, 0) + 1  prevents NullPointerException",
        fontsize=10,
        fontweight="bold",
        color="#2C3E50",
        pad=10,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# Registry
# ─────────────────────────────────────────────────────────────────────────────
DIAGRAM_REGISTRY = {
    "🌐 Networking": [
        ("Rule Order Evaluation", rule_order_diagram),
        ("Publish vs Install Policy", publish_install_diagram),
        ("Multi-Domain Isolation", multi_domain_diagram),
        ("Time-Based Firewall Rule", time_rule_diagram),
        ("SecureTrack vs SecureChange", securetrack_securechange_diagram),
        ("3-Layer RBAC Test", rbac_layers_diagram),
    ],
    "🧪 QA Frameworks": [
        ("Severity-Impact Matrix", severity_matrix_diagram),
        ("Test Pyramid", test_pyramid_diagram),
    ],
    "☕ Java Coding": [
        ("HashSet Duplicate Detection", hashset_diagram),
        ("Two-Pointer Pattern", two_pointer_diagram),
        ("FizzBuzz Decision Tree", fizzbuzz_tree_diagram),
        ("HashMap Word Frequency", word_freq_diagram),
    ],
}
