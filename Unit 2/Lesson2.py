#Creating a professional email for a university

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username = f"{first[0]}{last}"
print(f"your email is: {username.lower()}@university.com")