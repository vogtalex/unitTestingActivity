def add(a, b):
	return (a + b)


print('\nWelcome to the Unit Testing Activity!')


a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))

sum = add(a, b)
difference = subtract(a, b)
product = multiply(a, b)
quotient = divide(a, b)

print("sum: ", sum)
print("difference: ", difference)
print("product: ", product)
print("quotient: ", quotient)
