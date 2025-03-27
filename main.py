import os
import subprocess
import sys
from datetime import datetime, timedelta

import pyfiglet

WEEKS_PER_YEAR = 52
DAYS_PER_WEEK = 7
DENSITY = 10

message = sys.argv[1]

rendered = pyfiglet.Figlet(font="banner").renderText(message)

lines = rendered.split("\n")[:7]
# height = len(lines)
# assert height == DAYS_PER_WEEK, "wrong height"
assert all(len(line) == len(lines[0]) for line in lines), "uneven lines"
width = len(lines[0])
assert width <= WEEKS_PER_YEAR, "too long"

if width < WEEKS_PER_YEAR:
    pad = WEEKS_PER_YEAR - width
    rpad = pad // 2
    lpad = WEEKS_PER_YEAR - width - rpad
    lines = [(lpad * " ") + line + (rpad * " ") for line in lines]

for line in lines:
    print(line, ".")


today = datetime.now()
# 52 weeks before last sunday
start_date = today - timedelta(days=today.weekday() + 1) - timedelta(days=52 * 7)
print(start_date)

# print(start_date.strftime("%Y-%m-%d"))

# subprocess.run(["git", "branch", "-D", "main"])
# subprocess.run(["git", "switch", "--orphan", "main"])
subprocess.run(["git", "checkout", "gh-pages"])
subprocess.run(["git", "reset", "--hard", "initial"])
subprocess.run(["git", "checkout", "main", "--", "README.md"])


for day, row in enumerate(lines):
    for week, char in enumerate(row):
        if char != "#":
            continue
        date = start_date + timedelta(day + (7 * week))
        date_str = date.strftime("%Y-%m-%d")

        for i in range(DENSITY):

            subprocess.run(
                ["git", "commit", "-m", f"fake commit {i} on {date_str}", "--allow-empty"],
                env={
                    **os.environ,
                    "GIT_AUTHOR_DATE": f"{date_str} 12:00:00",
                    "GIT_COMMITTER_DATE": f"{date_str} 12:00:00",
                },
                capture_output=True,
                text=True,
            )

subprocess.run(["git", "checkout", "main"])
