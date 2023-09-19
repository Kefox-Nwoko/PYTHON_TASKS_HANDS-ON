

print('Hello customer! Welcome to your cost calculator.')

# input number of planned stay days
stay_days = int(input("How many days will you stay?: "))
# input hotel cost per night
hotel_cost = int(input("How much does the hotel cost per night?: $"))
# input flight cost
flight_cost = int(input("How much does your flight cost?: $"))
# input choice for rented car amount if not enter zero
rented_car = int(input("If you need a rented car, enter the price else enter 0: $"))
# addition of variables
sum_result = stay_days + hotel_cost + flight_cost + rented_car
# total cost display
print(f'Your total cost is = ${sum_result:.2f}')