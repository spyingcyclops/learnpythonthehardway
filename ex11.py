age = input("How old are you? ")
height = float(input("How tall are you, in centimeters? "))
weight = float(input("How much do you weigh, in kilograms? "))

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
imp_height = height * 0.393701
imp_weight = weight * 2.20462
print(f"Your weight in pounds is {imp_weight}lbs, and your height in inches is {imp_height}.")

print("3 variables")
print(age)
print(height)
print(weight)
