# Get user input for two numbers separated by space
choice_numbers = input("Enter any two numbers: ")
# num1, num2 = map(int, choice_numbers.split())
num1, num2 = map(int, choice_numbers.split())
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
modulus_result = num1 % num2
print(f'SUM = {sum_result}')
print(f'DIFFERENCE = {difference_result}')
print(f'PRODUCT = {product_result}')
print(f'QUOTIENT = {quotient_result}')
print(f'MODULUS = {modulus_result}')