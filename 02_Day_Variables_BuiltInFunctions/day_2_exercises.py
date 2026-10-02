# EXERCISES
# Level 1
# 2.Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of Python Programming

#3. Declare a first name variable and assign a value to it
first_name = 'Daniel'

#4. Declare a last name variable and assign a value to it
last_name = 'van Dijk'

#5. Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name
print(full_name)

#6. Declare a country variable and assign a value to it
country = 'Netherlands'
print(country)

#7. Declare a city variable and assign a value to it
city = 'Oudewater'
print(city)

#8. Declare an age variable and assign a value to it
age = 100
print(age)

#9. Declare a year variable and assign a value to it
year = 2024

#10. Declare a variable is_married and assign a value to it
is_married = False
print(is_married)

#11. Declare a variable is_true and assign a value to it
is_true = True
print(is_true)

#12. Declare a variable is_light_on and assign a value to it
is_light_on = False
print(is_light_on)

#13. Declare multiple varibles on one line
colour, shape, height = 'blue', 'square', 100
print(colour, shape, height)
print(colour)
print(shape)
print(height)



# Level 2
#1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(colour))
print(type(shape))
print(type(height))

#2. Using the len() built-in function, find the length of your first name
print(len(first_name))

#3. Compare the length of your first name and your last name
print(len(first_name) - len(last_name))

#4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#5 Add num_one and num_two and assign the value to a variable total
num_total = num_one + num_two
print(num_total)

#6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)

#7. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

#8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

#9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

#10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two
print(exp)

#11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

#12i. The radius of a circle is 30 meters - Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
r = 30
area_of_circle = math.pi * r**2
print(area_of_circle)

#12ii. The radius of a circle is 30 meters - Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*math.pi*r
print(circum_of_circle)

#12iii. Take radius as user input and calculate the area.
input_radius = int(input("Enter the radius of a circle: "))
circum_of_circle_v2 = math.pi*input_radius**2
print(circum_of_circle_v2)

#13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
input_first_name = str(input('Enter your first name: '))
input_last_name = str(input('Enter your last name: '))
input_country = str(input('Enter your country: '))
input_age = int(input('Enter your age: '))


#14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')