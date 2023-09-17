
numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

if numbers:
    print(f"Maximum number: {max(numbers)}, Minimum number: {min(numbers)}")
else:
    print("No numbers were entered.")
