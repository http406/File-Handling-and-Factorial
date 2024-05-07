# Create a file named 'factorial.py' and write the following code in it
with open('factorial.py', 'w') as file:
    file.write("def factorial(n):\n")
    file.write("    if n == 0:\n")
    file.write("        return 1\n")
    file.write("    else:\n")
    file.write("        return n * factorial(n - 1)\n")

# Import the newly created module and use the factorial function
import factorial

# Calculate the factorial of a number
number = 5
result = factorial.factorial(number)
print("Factorial of", number, "is:", result)
