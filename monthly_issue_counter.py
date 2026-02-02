def monthly_issue(events):
    # 1️⃣ Validate input type considered serious error
    if not isinstance(events, list):
        raise TypeError(
            "monthly_issue() expects a list of event strings "
            "in the format '[TAG] YYYY-MM-DD description'"
        )

    count = {}

    for issue in events:
        # 2️⃣ Skip invalid entries safely
        if not isinstance(issue, str):
            continue

        if not issue.startswith("["):
            continue

        parts = issue.split()
        if len(parts) < 2:
            continue

        date = parts[1]
        if len(date) < 7 or date[4] != "-" or date[7] != "-":
            continue

        month = date[:7]

        try:
            tag = issue[1:issue.index("]")]
        except ValueError:
            continue

        if month not in count:
            count[month] = {}

        count[month][tag] = count[month].get(tag, 0) + 1

    return count


if __name__ == "__main__":
    events = [
        "[BUG] 2024-01-10 Login crash",
        "[FEATURE] 2024-01-12 Dark mode",
        "Broken entry",
        123,
        "[BUG] 2024-02-18 Profile crash"
    ]

    print(monthly_issue(events))
