import secrets
import string


def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    pools = []
    required_chars = []

    if use_upper:
        pools.append(string.ascii_uppercase)
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        pools.append(string.ascii_lowercase)
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        pools.append(string.digits)
        required_chars.append(secrets.choice(string.digits))
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.?/|")
        required_chars.append(secrets.choice("!@#$%^&*()-_=+[]{};:,.?/|"))

    if not pools:
        raise ValueError("At least one character type must be selected.")
    if length < len(required_chars):
        raise ValueError(
            f"Length must be at least {len(required_chars)} for selected character types."
        )

    all_chars = "".join(pools)
    password_chars = required_chars[:]

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y or n.")


def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("Enter password length (minimum 4): ").strip())
            if length < 4:
                print("Length must be 4 or more.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    print("\nChoose character types:")
    use_upper = ask_yes_no("Include uppercase letters? (y/n): ")
    use_lower = ask_yes_no("Include lowercase letters? (y/n): ")
    use_digits = ask_yes_no("Include digits? (y/n): ")
    use_symbols = ask_yes_no("Include symbols? (y/n): ")

    try:
        password = generate_password(
            length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols,
        )
        print(f"\nGenerated password: {password}")
    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
