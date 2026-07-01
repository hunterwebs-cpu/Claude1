#!/usr/bin/env python3
"""
send_topic_briefing.py
Reads content/substack/topic-pipeline.md and emails the weekly topic
briefing via Gmail SMTP.

Environment variables required (set in Routine's cloud environment config):
    GMAIL_APP_PASSWORD   — Gmail App Password for nmateservices@gmail.com
                           Generate at: myaccount.google.com →
                           Security → 2-Step Verification → App Passwords

Usage:
    python3 scripts/send_topic_briefing.py
"""

import os
import smtplib
import sys
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


GMAIL_USER = "nmateservices@gmail.com"
RECIPIENT  = "khan.erik@protonmail.com"
PIPELINE_FILE = Path("content/substack/topic-pipeline.md")


def load_pipeline():
    if not PIPELINE_FILE.exists():
        print(f"ERROR: {PIPELINE_FILE} not found.", file=sys.stderr)
        sys.exit(1)
    return PIPELINE_FILE.read_text()


def extract_results_section(content):
    """Pull everything from THIS WEEK'S RESEARCH RESULTS onward."""
    marker = "## THIS WEEK'S RESEARCH RESULTS"
    idx = content.find(marker)
    if idx == -1:
        return content  # fallback: send the whole file
    return content[idx:]


def build_plain(results_section):
    today = date.today().strftime("%B %d, %Y")
    return f"""SUBSTACK TOPIC BRIEFING — {today}
Surviving the Feds: Dispatches from the Inside
================================================

{results_section}

------------------------------------------------
To write an article:
1. Pick a topic number from the list above
2. Open a new Claude Code session
3. Type: /substack
4. Tell Claude which topic number you want

Claude will run deep research, interview you, write the article,
and generate the Word doc for Doug — all in one session.
------------------------------------------------
"""


def build_html(results_section):
    today = date.today().strftime("%B %d, %Y")
    # Convert basic markdown to readable HTML
    lines = results_section.split('\n')
    html_lines = []
    for line in lines:
        if line.startswith('## '):
            html_lines.append(f'<h2 style="color:#1a3a6b;border-bottom:2px solid #1a3a6b;padding-bottom:6px">{line[3:]}</h2>')
        elif line.startswith('### ') or line.startswith('#### '):
            html_lines.append(f'<h3 style="color:#333">{line.lstrip("#").strip()}</h3>')
        elif line.startswith('**') and line.endswith('**'):
            html_lines.append(f'<p><strong>{line[2:-2]}</strong></p>')
        elif line.strip() == '---':
            html_lines.append('<hr style="border:none;border-top:1px solid #ccc;margin:16px 0">')
        elif line.strip() == '':
            html_lines.append('<br>')
        else:
            # Bold inline **text**
            import re
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            html_lines.append(f'<p style="margin:4px 0;line-height:1.6">{line}</p>')

    body_html = '\n'.join(html_lines)

    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="font-family:Georgia,serif;max-width:680px;margin:0 auto;padding:24px;color:#1a1a1a">

<div style="background:#1a3a6b;color:#fff;padding:16px 24px;border-radius:4px;margin-bottom:24px">
  <div style="font-size:11px;text-transform:uppercase;letter-spacing:1px;opacity:0.8">Weekly Briefing</div>
  <div style="font-size:20px;font-weight:bold;margin-top:4px">Surviving the Feds: Dispatches from the Inside</div>
  <div style="font-size:13px;opacity:0.8;margin-top:4px">{today}</div>
</div>

{body_html}

<div style="background:#f0f4ff;border-left:4px solid #1a3a6b;padding:16px 20px;margin-top:32px;border-radius:0 4px 4px 0">
  <strong>To write an article this week:</strong><br>
  1. Pick a topic number from the list above<br>
  2. Open a new Claude Code session<br>
  3. Type <code>/substack</code><br>
  4. Tell Claude which topic number you want<br><br>
  Claude will run deep research, interview you, write the article,
  and generate the Word doc for Doug — all in one session.
</div>

</body>
</html>"""


def send(plain_body, html_body, subject):
    app_password = os.environ.get("GMAIL_APP_PASSWORD")
    if not app_password:
        print("ERROR: GMAIL_APP_PASSWORD environment variable not set.", file=sys.stderr)
        sys.exit(1)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = GMAIL_USER
    msg["To"]      = RECIPIENT

    msg.attach(MIMEText(plain_body, "plain"))
    msg.attach(MIMEText(html_body,  "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(GMAIL_USER, app_password)
        server.sendmail(GMAIL_USER, RECIPIENT, msg.as_string())

    print(f"Sent to {RECIPIENT}")


def main():
    content         = load_pipeline()
    results_section = extract_results_section(content)
    today_str       = date.today().strftime("%B %d, %Y")
    subject         = f"Substack Topic Briefing — {today_str}"
    plain           = build_plain(results_section)
    html            = build_html(results_section)
    send(plain, html, subject)


if __name__ == "__main__":
    main()
