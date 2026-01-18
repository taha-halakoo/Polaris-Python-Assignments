import pytest
from password_security import check_password_strength

# 1. Test a Perfect Password
def test_strong_password():
    # Should return an empty list [] because there are no issues
    assert check_password_strength("Strong1!") == []

# 2. Test Missing Uppercase
def test_missing_uppercase():
    # We check if the specific error message is inside the returned list
    issues = check_password_strength("weak1!")
    assert "Missing uppercase letter (A-Z)" in issues

# 3. Test Missing Special Char
def test_missing_special():
    issues = check_password_strength("NoSpecial1")
    assert "Missing special character (!@#...)" in issues

# 4. Test Missing Everything (Total failure)
def test_weak_password():
    issues = check_password_strength("weak")
    # Should fail on Uppercase, Number, AND Special char (3 errors)
    assert len(issues) == 3
