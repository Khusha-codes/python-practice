# Counts monthly issues by tag from event logs
events = [
    "[BUG] 2024-01-10 Login crash",
    "[FEATURE] 2024-01-12 Dark mode",
    "[BUG] 2024-01-15 Logout crash",
    "[DOC] 2024-01-20 Update README",
    "[BUG] 2024-02-02 Payment failure",
    "[FEATURE] 2024-02-10 Improve UI",
    "Random text without format",
    "[BUG] 2024-02-18 Profile crash"
]

count = {}

for issue in events :
    if not issue.startswith("["):
        continue
    else:
        parts = issue.split()
        date = parts[1]
        month = date[:7]
        tag = issue[1:issue.index("]")]
        if month not in count:
            count[month] = {}
        count[month][tag] = count[month].get(tag, 0) + 1

for month, tags in count.items():
    print(f"{month}")
    for tag, total in tags.items():
        print("     "f"{tag}:{total}")
