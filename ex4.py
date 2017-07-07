# Exercise 4: Variables and Names

# Assign integer 100 to a variable called car
cars = 100

# Assign float value 4.0 to a variable space_in_a_car
space_in_a_car = 4

# Assign int 30 to a vriable drivers
drivers = 30

# Assign int 90 to a viralbe passengers
passengers = 90

# Assign calculated value of 100 - 30 to a variable cars_not_driven
cars_not_driven = cars - drivers

# Assgin a value from a variable drivers to a variable cars_driven
cars_driven = drivers

# Assign a calculated value of 30 * 4.0 to a variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# Assign a calculated value of 90 / 30 to a variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

print("There are ", cars, "cars available.")
print("There are only ", drivers, "available.")
print("There will be ", cars_not_driven, "emtpy cars today.")
print("We can transport ", carpool_capacity, "people today.")
print("We have ", passengers, "to carpool today.")
print("We need to put about ", average_passengers_per_car, "people in each car")
