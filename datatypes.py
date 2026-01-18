

# 1. Declaring variables of different data types
integer_var = 10
float_var = 12.5
string_var = "Python"
boolean_var = True

# 2. Printing values and their data types
print("Integer:", integer_var, type(integer_var))
print("Float:", float_var, type(float_var))
print("String:", string_var, type(string_var))
print("Boolean:", boolean_var, type(boolean_var))

print("-" * 40)

# 3. Arithmetic operations
sum_result = integer_var + float_var
product_result = integer_var * float_var

print("Sum:", sum_result)
print("Product:", product_result)

print("-" * 40)

# 4. Type conversion using user input
try:
    user_input = input("Enter a number: ")
    int_value = int(user_input)
    float_value = float(user_input)

    print("Integer Conversion:", int_value)
    print("Float Conversion:", float_value)

except ValueError:
    print("Invalid input! Please enter a valid number.")

print("-" * 40)

# 5. String and number concatenation
number = 25
result = "The value is " + str(number)
print(result)

print("-" * 40)

# 6. Dynamic typing demonstration
data = 100
print("Data:", data, type(data))

data = "Now I am a string"
print("Data:", data, type(data))
