# ====================
# Engage & Apply: Tuple Exploration
# ====================

# Creating a tuple containing at least 4 different data types: an integer, string, float, and boolean
my_tuple = (42, "hello", 3.14, True)

# Accessing and printing the first and last elements of the tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Attempting to modify one element of the tuple to observe the error (will raise an error)
# Uncomment the next line to see the error
# my_tuple[1] = "world"  # This should raise an error


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Creating a tuple containing different data types: an integer, a string, a boolean, and a float
my_tuple = (25, "Python", 4.5, False)

# Accessing and printing the first and last elements of the tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Attempting to modify the tuple (will raise an error)
# Uncomment the next line to see the error
# my_tuple[2] = 5.0  # This should raise an error


# ====================
# Final Challenge: Tuple Mastery
# ====================

# Creating a tuple with at least 6 elements (mixing integers, strings, and floats)
my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")

# Accessing and printing the third and fifth elements
print("Third element:", my_tuple[2])
print("Fifth element:", my_tuple[4])

# Slicing the tuple to extract elements from the second to the fifth position
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)

# Using the count() method to find how many times 'Code' appears in the tuple
count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code)

# Unpacking the tuple into individual variables and printing them
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)

# Concatenating the tuple with another tuple and printing the new tuple
new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)


# ====================
# My Version of the Final Challenge
# ====================

# Creating a tuple with at least 6 elements
my_tuple = (12, "Learning", 7.8, "Programming", 42, "Fun")

# Accessing and printing the third and fifth elements
print("Third element:", my_tuple[2])
print("Fifth element:", my_tuple[4])

# Slicing the tuple to extract elements from the second to the fifth position
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)

# Using the count() method to find how many times 'Learning' appears in the tuple
count_learning = my_tuple.count("Learning")
print("Count of 'Learning':", count_learning)

# Unpacking the tuple into individual variables and printing them
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)

# Concatenating the tuple with another tuple and printing the new tuple
new_tuple = my_tuple + ("New", "Challenge")
print("Concatenated tuple:", new_tuple)
