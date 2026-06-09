import re
import string
import secrets

common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "welcome",
    "letmein"
]

password = input("Enter Password: ")
score = 0
reasons = []

# Length Check
if len(password) >= 8:
    score += 1
else:
    reasons.append("Password should be at least 8 characters long.")
if len(password) >= 12:
    score += 1

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1
else:
    reasons.append("Add at least one uppercase letter (A-Z).")

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1
else:
    reasons.append("Add at least one lowercase letter (a-z).")

# Digit Check
if re.search(r"\d", password):
    score += 1
else:
    reasons.append("Add at least one number (0-9).")

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    reasons.append("Add at least one special character (!,@,#,$,etc.).")

# Common Password Check
if password.lower() in common_passwords:
    reasons.append("This is a common password and can be easily guessed.")

# Strength Evaluation
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
elif score == 5:
    strength = "Strong"
else:
    strength = "Very Strong"
print("\nPassword Strength:", strength)

# Show reasons and suggestions if not strong
if strength in ["Weak", "Medium"]:
    print("\nSuggestions:")
    for reason in reasons:
        print("-", reason)
    # Generate random strong password
    characters = (string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    suggested_password = ''.join(secrets.choice(characters) for _ in range(12))
    print("\nSuggested Strong Password:")
    print(suggested_password)
