# Get user input for two numbers separated by space
choice_numbers = input("Enter any two numbers: ")
num1, num2 = map(int, choice_numbers.split())
sum_result = num1 + num2
print(f'Sum of {num1} and {num2} = {sum_result}')