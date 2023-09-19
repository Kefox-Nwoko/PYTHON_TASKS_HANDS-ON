

# define function is_even() to check if a number is even by using the modulo operator (%)
def is_even(num):
    return num % 2 == 0

# Get the user input
number_input = input("What number do you want to check?: ")
# Check if the user input is a valid integer
try:
  number_input = int(number_input)
except ValueError:
  print("Invalid input. Please enter an integer.")
else:
  # Check if the number is even
  if is_even(number_input):
    print("Yeah! This is an even number")
  else:
    print("Yeah! This is an odd number")