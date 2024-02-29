import matplotlib.pyplot as plt

# Read values from the C program output
with open('output.txt', 'r') as file:
    values = [int(line.strip()) for line in file]

# Generate x values (1 to 50)
x_values = list(range(1, 51))

# Create a stem plot
plt.stem(x_values, values, basefmt='r-', linefmt='b-', markerfmt='bo')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Stem Plot of the Generated Function')
plt.show()

