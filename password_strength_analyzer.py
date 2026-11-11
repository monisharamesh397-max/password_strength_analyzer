import string
import math
import secrets

def check_password(password):

    score = 0
    pool = 0

    # Check length
    length = len(password)

    if length >= 8:
        score += 20
    if length >= 12:
        score += 10

    # Check lowercase
    if any(c.islower() for c in password):
        score += 10
        pool += 26

    # Check uppercase
    if any(c.isupper() for c in password):
        score += 10
        pool += 26

    # Check digits
    if any(c.isdigit() for c in password):
        score += 10
        pool += 10

    # Check special characters
    if any(c in string.punctuation for c in password):
        score += 10
        pool += 32

    # Calculate entropy
    entropy = 0
    if pool > 0:
        entropy = length * math.log2(pool)

    if entropy >= 60:
        score += 30
    elif entropy >= 40:
        score += 20
    elif entropy >= 20:
        score += 10

    # Check uniqueness
    unique = len(set(password))

    if length > 0 and unique / length < 0.5:
        score -= 10

    # Check common passwords
    common = ["admin", "password",
              "123456", "qwerty"]

    if password.lower() in common:
        score = 0

    score = max(0, min(score, 100))

    # Display analysis
    print("\n--- PASSWORD ANALYSIS ---")
    print("Length:", length)
    print("Unique characters:", unique)
    print("Entropy:", round(entropy, 2))
    print("Score:", score, "/100")

    if score < 40:
        print("Strength: WEAK")
    elif score < 60:
        print("Strength: MODERATE")
    elif score < 80:
        print("Strength: STRONG")
    else:
        print("Strength: VERY STRONG")

    # Suggest stronger alternative
    if score < 80:
        print("\nSuggested stronger password:")

        chars = string.ascii_letters + string.digits + string.punctuation
        suggestion = ''.join(secrets.choice(chars) for i in range(16))

        print(suggestion)


print("PASSWORD STRENGTH ANALYZER")

password = input("Enter a sample password: ")

check_password(password)