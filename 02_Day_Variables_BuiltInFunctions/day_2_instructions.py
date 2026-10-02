# Variables and Built-in Functions
# Day 2 - 30DaysOfPython Challenge

print('Hello, World!')

print(len('Hello, World!'))

print(type('Hello, World!'))

print(str(10))

print(int('10'))

print(float(10))

name = ['Asabeneh', 'Python', 'Finland']
print(name)
print(name[0])

min(20, 30, 40, 50, 60)

max(20, 30, 40, 50, 60)

min([20, 30, 40, 50, 60])

max([20, 30, 40, 50, 60])

sum([20, 30, 40, 50, 60])


# Variables in Python
first_name = 'Daniel'
last_name = 'van Dijk'
country = 'Netherlands'
city = 'Oudewater'
skills = ['Corporate Finance', 'Equity Research', 'Public Equity Investing', 'Python']
person_info = {
   'firstname':'Daniel',
   'lastname':'van Dijk',
   'country':'Netherlands',
   'city':'Oudewater'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Skills: ', skills)
print('Person information: ', person_info)

print('First name:', person_info["firstname"])
print(person_info.keys())
print(person_info.values())

print(type((1,2)))

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_string = '10.6'
num_float = float(num_string)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(float(num_string)))      # 10
print('num_float', float(num_string))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']