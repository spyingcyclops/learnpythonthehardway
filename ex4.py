# define cars variable
cars = 100
# define space_in_a_car variable
space_in_a_car = 4.0
# define drivers variable
drivers = 30
# define passengers variable
passengers = 90
# define cars_not_driven
cars_not_driven = cars - drivers
# define cars_driven variable
cars_driven = drivers
# define carpool_capacity variable
carpool_capacity = cars_driven * space_in_a_car
# define average_passengers_per_car variable
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
