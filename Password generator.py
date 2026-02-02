import random
import string

print("===== Password Generator =====")

length = int(input("Enter desired password length: "))

print("\nSelect Password Complexity:")
print("1. Only Letters")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols (Strong Password)")

choice = input("Enter your choice (1/2/3): ")

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

if choice == '1':
    characters = letters
elif choice == '2':
    characters = letters + digits
elif choice == '3':
    characters = letters + digits + symbols
else:
    print("Invalid choice! Using Strong Password by default.")
    characters = letters + digits + symbols

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)
