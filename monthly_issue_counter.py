def monthly_issue(events):
    """
    Counts issues month-wise and tag-wise from a list of event strings.

    Expected input format:
        [TAG] YYYY-MM-DD description

    Parameters:
        events (list): A list of event strings.

    Returns:
        dict: A dictionary with month as key and tag counts as values.

    Raises:
        TypeError: If events is not a list.

    Notes:
        - Non-string entries are ignored safely.
        - Malformed strings are skipped.
    """
    # Validate input type considered serious error
    if not isinstance(events, list):
        raise TypeError(
            "monthly_issue() expects a list of event strings "
            "in the format '[TAG] YYYY-MM-DD description'"
        )

    count = {}

    for issue in events:
        # Skip invalid entries safely
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

    stable_count = {}

    for month in sorted(count):
        stable_count[month] = dict(sorted(count[month].items()))

    return stable_count



if __name__ == "__main__":
    events = [
        "[BUG] 2024-01-10 Login crash",
        "[FEATURE] 2024-01-12 Dark mode",
        "Broken entry",
        123,
        "[BUG] 2024-02-18 Profile crash"
    ]

    print(monthly_issue(events))
