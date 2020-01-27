#Ask for the name

name = input("What is your name?: ")

#Create output text

string = "Hello {}! Nice to meet you:)"
output = string.format(name)

#Print output to the screen
print(output)

# Ask user for age

age = input("How old are you?: ")

# Ask user for city

city = input("What city do you live in?: ")

# Ask user what they enjoy

hobbies = input("What do you love doing?: ")

# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, hobbies)

# Print output to screen
print(output)