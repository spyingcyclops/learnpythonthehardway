name = 'Zed A. Shaw'
age = 35 #not a lie
imperial_height = 74 #inches
metric_height = imperial_height * 2.54
imperial_weight = 180 #lbs
metric_weight = imperial_weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {imperial_height} inches tall.")
print(f"That's {metric_height} in centimeters.")
print(f"He's {imperial_weight} pounds heavy.")
print(f"That's {metric_weight} in kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth}, depending on the coffee.")
# this line is tricky, so try to get it exactly right
total = age + imperial_height + imperial_weight
print(f"If I add {age}, {imperial_height}, and {imperial_weight} I get {total}.")
