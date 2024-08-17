import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
        print(f"Generated Password: {password}")

        another = input("Generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
