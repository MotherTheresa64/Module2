# ====================
# Engage & Apply: Create a program that creates a set from a list of favorite hobbies and removes duplicates.
# ====================

# Creating a list of favorite hobbies, making sure to repeat a few of them
hobbies = ['reading', 'gaming', 'hiking', 'gaming', 'swimming', 'hiking']

# Converting the list into a set to automatically remove duplicates
hobbies_set = set(hobbies)

# Printing both the original list and the set to compare
print("Original List:", hobbies)
print("Set with Duplicates Removed:", hobbies_set)


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Creating a list of favorite fruits, making sure to repeat a few of them
fruits = ['apple', 'banana', 'orange', 'banana', 'grape', 'apple']

# Converting the list into a set to automatically remove duplicates
fruits_set = set(fruits)

# Printing both the original list and the set to compare
print("Original List:", fruits)
print("Set with Duplicates Removed:", fruits_set)


# ====================
# Final Challenge: Build a program that takes a list of email addresses and removes duplicates.
# ====================

# A list of email addresses (some duplicates)
emails = ['a@example.com', 'b@example.com', 'a@example.com', 'c@example.com', 'b@example.com']

# Converting the list into a set to automatically remove duplicates
unique_emails = set(emails)

# Printing out the unique emails
print("Unique Emails:", unique_emails)


# ====================
# My Version of the Final Challenge
# ====================

# A list of phone numbers (some duplicates)
phone_numbers = ['123-456-7890', '987-654-3210', '123-456-7890', '555-555-5555']

# Converting the list into a set to automatically remove duplicates
unique_phone_numbers = set(phone_numbers)

# Printing out the unique phone numbers
print("Unique Phone Numbers:", unique_phone_numbers)
