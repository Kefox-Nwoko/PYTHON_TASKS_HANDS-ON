

# Define the minimum salary amount
MINIMUM_SALARY = 2000

# Function to check if salary meets criteria
def check_salary(salary):
    if salary > MINIMUM_SALARY:
        print("Congratulations, you are eligible for a mortgage.")
        return True
    else:
        print("Sorry, you do not meet the criteria for a mortgage.")
        return False

# Function to calculate interest rate based on credit score
def calculate_interest_rate(credit_score):
    if credit_score >= 800:
        return 4
    elif credit_score >= 750:
        return 6
    else:
        return 8

# Get user input for salary and credit score
try:
    salary = float(input("What is your monthly salary? $"))
    if check_salary(salary):
        credit_score = int(input("What is your current credit score? : "))
        interest_rate = calculate_interest_rate(credit_score)
        print(f"Your interest rate is {interest_rate}%")
        disabilities = input("Hello, Please specify. Do you have any disabilities? Yes or No: ").lower()
        if disabilities == "yes":
            print("Congratulations you have been discounted, your new interest rate is now 4%")
        else:
            print(f"Your final interest rate remains unchanged at {interest_rate}%.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
