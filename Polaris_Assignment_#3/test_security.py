import re
import pytest
from password_security import check_password_strength

# --- THE TEST CASES ---

def test_strong_password():
    # 1. Test a Perfect Password
    # Should return an empty list [] because there are no issues
    assert check_password_strength("Strong1!") == []

def test_missing_uppercase():
    # 2. Test Missing Uppercase
    issues = check_password_strength("weak1!")
    assert "Missing uppercase letter (A-Z)" in issues

def test_missing_special():
    # 3. Test Missing Special Char
    issues = check_password_strength("NoSpecial1")
    assert "Missing special character (!@#...)" in issues

def test_weak_password():
    # 4. Test Missing Everything (Total failure)
    issues = check_password_strength("weak")
    # Should fail on Uppercase, Number, AND Special char (3 errors)
    assert len(issues) == 3


# --- THE "NO-FLASH" FIX ---
if __name__ == "__main__":
    # This block allows you to double-click the file to run tests
    print("Running Security Tests... 🧪")
    print("__________\n")
    
    # This runs pytest on this specific file
    pytest.main(["-v", __file__])
    
    print("\n__________")
    input("Tests completed. Press Enter to close...")
