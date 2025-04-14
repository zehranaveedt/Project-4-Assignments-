import re
import random
import string

COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "admin", "welcome",
    "password123", "abc123", "letmein", "monkey", "1234567890"
]

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("❌ This is a commonly used password.")
        return 0, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one digit.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*).")

    if re.search(r"(abc|123|qwerty)", password.lower()):
        score -= 1
        feedback.append("❌ Avoid easy patterns like 'abc' or '123'.")

    score = max(0, score)
    return score, feedback


def generate_password(length=12, upper=True, lower=True, digits=True, special=True):
    chars = ""
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special:
        chars += "!@#$%^&*"

    if not chars:
        chars = string.ascii_letters + string.digits

    return ''.join(random.choice(chars) for _ in range(length))


# Main Program
while True:
    print("\n--- PASSWORD TOOL ---")
    print("1. Check Password Strength")
    print("2. Generate a Strong Password")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == '1':
        pwd = input("Enter your password: ")
        score, tips = check_password_strength(pwd)
        print(f"\nPassword Strength Score: {score}/5")
        if score >= 5:
            print("✅ Strong password!")
        elif score >= 3:
            print("⚠️ Moderate password.")
        else:
            print("❌ Weak password.")
        if tips:
            print("Suggestions:")
            for tip in tips:
                print("-", tip)

    elif choice == '2':
        length = int(input("Enter desired length (min 8): "))
        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include numbers? (y/n): ").lower() == 'y'
        special = input("Include special characters? (y/n): ").lower() == 'y'
        new_password = generate_password(length, upper, lower, digits, special)
        print("\nGenerated Password:", new_password)
        score, _ = check_password_strength(new_password)
        print(f"Strength Score: {score}/5")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
