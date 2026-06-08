from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
DESKTOP = Path.home() / "Desktop"
OUT_DESKTOP = DESKTOP / "Ricardo_Del_Castillo_Remote_AI_Automation_CV.pdf"
OUT_PORTFOLIO = ROOT / "output" / "Ricardo_Del_Castillo_Remote_AI_Automation_CV.pdf"

PAGE_W, PAGE_H = landscape(LETTER)

INK = colors.HexColor("#101820")
MUTED = colors.HexColor("#62716F")
LIGHT = colors.HexColor("#EEF4F1")
LINE = colors.HexColor("#DCE7E2")
ACCENT = colors.HexColor("#0F615A")
ACCENT_DARK = colors.HexColor("#0A4B45")
SOFT = colors.HexColor("#F7FAF9")


def wrap_text(c, text, max_width, font="Helvetica", size=9):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if c.stringWidth(test, font, size) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_text_block(c, x, y, text, width, size=9, leading=12, color=INK, font="Helvetica", max_lines=None):
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap_text(c, text, width, font, size)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def label(c, x, y, text):
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(ACCENT)
    c.drawString(x, y, text.upper())


def chip(c, x, y, text):
    w = c.stringWidth(text, "Helvetica-Bold", 7.2) + 14
    c.setFillColor(SOFT)
    c.setStrokeColor(LINE)
    c.roundRect(x, y - 4, w, 15, 7, stroke=1, fill=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(x + 7, y, text)
    return x + w + 6


def project_card(c, x, y, w, title, meta, text, stack):
    c.setFillColor(colors.white)
    c.setStrokeColor(LINE)
    c.roundRect(x, y - 78, w, 78, 7, stroke=1, fill=1)
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 6.8)
    c.drawString(x + 10, y - 15, meta.upper())
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 10, y - 29, title)
    draw_text_block(c, x + 10, y - 43, text, w - 20, size=7.2, leading=9, color=MUTED, max_lines=1)
    cx = x + 10
    for item in stack[:4]:
        cx = chip(c, cx, y - 68, item)


def build_pdf(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(path), pagesize=landscape(LETTER))
    c.setTitle("Ricardo Del Castillo - Remote AI Automation Profile")
    c.setAuthor("Ricardo Del Castillo Velasco")

    margin = 0.42 * inch
    left_w = 2.48 * inch
    gutter = 0.25 * inch
    mid_w = 3.45 * inch
    right_w = PAGE_W - margin * 2 - left_w - mid_w - gutter * 2

    # Background rails
    c.setFillColor(colors.white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(SOFT)
    c.roundRect(margin, margin, left_w, PAGE_H - margin * 2, 8, stroke=0, fill=1)
    c.setStrokeColor(LINE)
    c.line(margin + left_w + gutter / 2, margin, margin + left_w + gutter / 2, PAGE_H - margin)

    # Left identity rail
    x = margin + 0.22 * inch
    y = PAGE_H - margin - 0.34 * inch
    c.setFillColor(ACCENT_DARK)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(x, y, "Ricardo")
    y -= 24
    c.drawString(x, y, "Del Castillo")
    y -= 24
    c.drawString(x, y, "Velasco")

    y -= 26
    c.setStrokeColor(ACCENT)
    c.setLineWidth(2.2)
    c.line(x, y, x + 1.45 * inch, y)
    y -= 24
    draw_text_block(
        c,
        x,
        y,
        "Business operations background, practical software builder and AI automation specialist.",
        left_w - 0.44 * inch,
        size=9.2,
        leading=12,
        color=INK,
        font="Helvetica-Bold",
    )

    y -= 48
    label(c, x, y, "Remote focus")
    y -= 16
    draw_text_block(
        c,
        x,
        y,
        "Remote U.S.-focused roles in AI automation, internal tools, full-stack products and business systems.",
        left_w - 0.44 * inch,
        size=8.1,
        leading=10.5,
        color=MUTED,
    )

    y -= 58
    label(c, x, y, "Target roles")
    y -= 16
    role_lines = [
        "AI Automation Specialist",
        "Internal Tools Developer",
        "Full Stack Developer",
        "Business Systems Analyst",
        "Operations Automation Specialist",
        "AI Workflow Builder",
    ]
    for role in role_lines:
        c.setFillColor(colors.white)
        c.setStrokeColor(LINE)
        c.roundRect(x, y - 4, left_w - 0.44 * inch, 17, 6, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 7.7)
        c.drawString(x + 8, y + 1, role)
        y -= 21

    y -= 8
    label(c, x, y, "Contact")
    y -= 16
    draw_text_block(
        c,
        x,
        y,
        "Puebla, Mexico | LinkedIn profile included in portfolio",
        left_w - 0.44 * inch,
        size=7.7,
        leading=10,
        color=MUTED,
    )

    # Middle column
    mx = margin + left_w + gutter
    y = PAGE_H - margin - 0.2 * inch
    label(c, mx, y, "Profile")
    y -= 20
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(mx, y, "I turn business")
    y -= 22
    c.drawString(mx, y, "operations into")
    y -= 22
    c.drawString(mx, y, "usable systems.")
    y -= 24
    draw_text_block(
        c,
        mx,
        y,
        "I build practical software that turns fragmented operations into structured workflows, dashboards, automations and internal tools. My edge is combining international business, day-to-day operations and hands-on product building inside real businesses.",
        mid_w,
        size=9,
        leading=12,
        color=MUTED,
    )

    y -= 74
    label(c, mx, y, "Capabilities")
    y -= 18
    caps = [
        ("AI Workflows", "Automation design, LLM-ready processes, prompt design"),
        ("Full-Stack Products", "React, TypeScript, JavaScript, Vite, APIs"),
        ("Business Systems", "POS, inventory, payroll, finance, CRM, dashboards"),
        ("Serverless Tools", "Netlify Functions, Netlify Blobs, lightweight data stores"),
        ("Operations Analysis", "Workflow mapping, reports, exceptions, follow-up"),
        ("Product Thinking", "Real business needs translated into usable tools"),
    ]
    card_w = (mid_w - 10) / 2
    for i, (head, body) in enumerate(caps):
        cx = mx + (i % 2) * (card_w + 10)
        cy = y - (i // 2) * 54
        c.setFillColor(colors.white)
        c.setStrokeColor(LINE)
        c.roundRect(cx, cy - 42, card_w, 42, 6, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(cx + 8, cy - 13, head)
        draw_text_block(c, cx + 8, cy - 25, body, card_w - 16, size=6.9, leading=8.3, color=MUTED, max_lines=2)

    y -= 182
    label(c, mx, y, "Education")
    y -= 17
    edu = [
        ("Seattle University", "Business Management", "2016 - 2018"),
        ("UPAEP", "International Business", "2013 - 2018"),
        ("Vysoka skola financni a spravni - Praha", "Project Management", "2017"),
    ]
    for school, degree, years in edu:
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 7.9)
        c.drawString(mx, y, school)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 7.7)
        c.drawString(mx, y - 10, f"{degree} | {years}")
        y -= 26

    # Right column projects
    rx = mx + mid_w + gutter
    y = PAGE_H - margin - 0.2 * inch
    label(c, rx, y, "Selected systems")
    y -= 20
    projects = [
        (
            "Better Mood Operations OS",
            "Cafe operations platform",
            "Tasks, POS, stock, HR, finance and planning.",
            ["React", "TypeScript", "Netlify", "POS"],
        ),
        (
            "Richi Personal Growth",
            "Private full-stack dashboard",
            "Health, habits, goals, charts and auth.",
            ["React", "TS", "Blobs", "Charts"],
        ),
        (
            "Shippin' Now",
            "Logistics and trade software",
            "Freight, import/export, portals and tracking.",
            ["Node", "Netlify", "Turf.js", "RBAC"],
        ),
        (
            "Panera Signature Systems",
            "Commerce and marketing tools",
            "SEO site, WhatsApp, B2B catalog and sales tools.",
            ["HTML", "JS", "Netlify", "CRM"],
        ),
        (
            "AirDesk / Cursor Dedos",
            "Native macOS remote-control app",
            "Swift app for private local device control.",
            ["Swift", "Vision", "LAN", "macOS"],
        ),
    ]
    for title, meta, text, stack in projects:
        project_card(c, rx, y, right_w, title, meta, text, stack)
        y -= 87

    # Footer statement
    c.setStrokeColor(LINE)
    c.line(mx, margin + 0.28 * inch, PAGE_W - margin, margin + 0.28 * inch)
    c.setFillColor(ACCENT_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(mx, margin + 0.11 * inch, "Portfolio theme:")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.2)
    c.drawString(mx + 0.92 * inch, margin + 0.11 * inch, "international business + operations + AI automation + practical software building")

    c.showPage()
    c.save()


def main():
    build_pdf(OUT_DESKTOP)
    build_pdf(OUT_PORTFOLIO)
    print(OUT_DESKTOP)
    print(OUT_PORTFOLIO)


if __name__ == "__main__":
    main()
