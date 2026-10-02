# EXERCISES
# Day 3

#1. Declare your age as integer variable
age = 100

#2. Declare your height as a float variable
height = 1.95

#3. Declare a variable that stores a complex number
complex_number = 4 +2j

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter base of triangle: '))
height = float(input('Enter height of triangle: '))
area_triangle = 0.5 * base * height
print('Area of triangle:', area_triangle)

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input('Enter side a of triangle: '))
side_b = float(input('Enter side b of triangle: '))
side_c = float(input('Enter side c of triangle: '))
perimeter_triangle = side_a + side_b + side_c
print('Perimeter of triangle:', perimeter_triangle)

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input('Enter length of rectangle: '))
width = float(input('Enter width of rectangle: '))
area_rectangle = length * width
perimeter_rectangle = 2*(length + width)
print('Area of rectangle:', area_rectangle)
print('Perimeter of rectangle:', perimeter_rectangle)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope = 2
y_intercept = -2
x_intercept = -y_intercept / Slope

print('Slope: ', Slope)
print('x-intercept: ', x_intercept)
print('y-intercept: ', y_intercept)

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
Slope_v2 = (y2-y1)/(x2-x1)
Euclidian_distance = (x2-x1)**2 + (y2-y1)**2
print('Slope between points (2,2) and (6,10): ', Slope_v2)
print('Euclidean distance between points (2,2) and (6,10): ', Euclidian_distance)


#10. Compare the slopes in tasks 8 and 9.
Slope_comparison = Slope - Slope_v2
print('Difference in slopes: ', Slope_comparison)

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = float(input('Enter x value: '))
y = x**2 + 6*x + 9
print('Value of y: ', y)

for x in range(-10, 10):
    y = x ** 2 + 6 * x + 9

    print("x =", x, "y =", y)

    if y == 0:
        print("y is 0 when x =", x)

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
python_has_on = 'on' in 'python'
dragon_has_on = 'on' in 'dragon'
both_have_on = python_has_on and dragon_has_on
print('Does "python" and "dragon" both contain "on"?', both_have_on)

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
jargon = 'jargon'  in 'I hope this course is not full of jargon.'
print('Is "jargon" in the sentence?', jargon)

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = float(input('Enter a number: '))
leftover = number % 2
if leftover == 0:
    print('The number is even.')
else:
    print('The number is not even.')

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_value = int(2.7)
if floor_division - int_value == 0:
    print('The floor division of 7 by 3 is equal to the int converted value of 2.7.')
else:
    print('The floor division of 7 by 3 is not equal to the int converted value of 2.7.')

#23. Write a Python script that displays the following table
for number in range(1, 6):
    print(number, number**0, number ** 2, number ** 3, number ** 4)