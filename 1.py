''''Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.Sample Output: 25 48'''
add_15 = lambda x: x + 15
multiply = lambda x, y: x * y
x = 10
y = 4
result1 = add_15(x)
result2 = multiply(x, y)
print(result1, result2)