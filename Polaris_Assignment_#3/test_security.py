import re

def check_password(password):
    issues = []

    if not re.search(r"[A-Z]", password):
        issues.append("uppercase")

    if not re.search(r"\d", password):
        issues.append("number")

    if not re.search(r"[^A-Za-z0-9]", password):
        issues.append("special")

    return issues


def test_valid_password():
    assert check_password("Strong1!") == []

def test_missing_uppercase():
    assert "uppercase" in check_password("strong1!")

def test_missing_everything():
    issues = check_password("password")
    assert len(issues) == 3
