
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

weight_kg = float(input("Hello friend! What is your weight please (kg)?: "))
height_m = float(input("Hello friend! What is your height (m)?: "))

bmi = calculate_bmi(weight_kg, height_m)

# print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("Your weight is normal.")
elif 25 <= bmi < 30:
    print("You are overweight.")
elif 30 <= bmi < 35:
    print("You are obese.")
else:
    print("You are in a higher category of obesity and at risk! Please consult a doctor, as soon as possible.")