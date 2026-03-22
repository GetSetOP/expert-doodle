import string
print("\nPassword Strength Checker")
print("NOTE: We neither save nor share your password.")
while True:
    password = input("\nEnter password: ")

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0

    if length >= 8:
        score += 1
    if has_symbol:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1

    if score <= 3:
        print("Weak ❌")
    elif score == 4:
        print("Medium ⚠️")
    else:
        print("Strong ✅")
        break
input("Feedback: ")
