stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
mantissa = stdform[:stdform.find("x")]
exponent = stdform[stdform.find("^") + 1::]

print(f"This number in E notation is {mantissa}E{exponent}.")
