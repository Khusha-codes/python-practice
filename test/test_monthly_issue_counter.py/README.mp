import pytest
from monthly_issue_counter import monthly_issue


# Test 1: Valid input
def test_valid_input():
    events = [
        "[BUG] 2024-01-10 Login crash",
        "[FEATURE] 2024-01-12 Dark mode",
        "[BUG] 2024-01-15 Logout crash",
        "[DOC] 2024-01-20 Update README",
        "[BUG] 2024-02-02 Payment failure",
        "[FEATURE] 2024-02-10 Improve UI",
        "[BUG] 2024-02-18 Profile crash"
    ]

    result = monthly_issue(events)

    assert isinstance(result, dict)
    assert result["2024-01"]["BUG"] == 2
    assert result["2024-01"]["FEATURE"] == 1
    assert result["2024-02"]["BUG"] == 2


# Test 2: Non-list input should raise TypeError
def test_non_list_input():
    events = (
        "[BUG] 2024-01-10 Login crash",
        "[FEATURE] 2024-01-12 Dark mode"
    )

    with pytest.raises(TypeError):
        monthly_issue(events)


# Test 3: Mixed valid + invalid entries
def test_mixed_valid_invalid_entries():
    events = [
        "[BUG] 2024-01-10 Login crash",
        "Random text without format",
        123,
        "[FEATURE] 2024-01-12 Dark mode"
    ]

    result = monthly_issue(events)

    assert result["2024-01"]["BUG"] == 1
    assert result["2024-01"]["FEATURE"] == 1


# Test 4: Stable output
def test_stable_output():
    events = [
        "[BUG] 2024-02-18 Profile crash",
        "[FEATURE] 2024-02-10 Improve UI"
    ]

    result1 = monthly_issue(events)
    result2 = monthly_issue(events)

    assert result1 == result2
