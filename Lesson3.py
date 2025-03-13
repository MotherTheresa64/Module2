# ====================
# Engage & Apply: Create a Dictionary 
# ====================

# Creating a dictionary to represent a book
book = {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'genre': 'Dystopian'
}

# Add a new key for publisher
book['publisher'] = 'Secker & Warburg'

# Modify the value for the year
book['year'] = 1950

# Display the updated dictionary
print(book)


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Create a dictionary to represent a movie
movie = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010,
    'genre': 'Sci-Fi'
}

# Add a new key for duration (in minutes)
movie['duration'] = 148

# Modify the genre of the movie
movie['genre'] = 'Thriller'

# Display the updated movie dictionary
print(movie)


# ====================
# Final Challenge: Student Grade Program 
# ====================

# Dictionary of students and their grades
students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

# Checking whether each student passed or failed
for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")


# ====================
# My Version of the Final Challenge
# ====================

# Dictionary of employees and their performance scores
employees = {
    'John': 88,
    'Emma': 74,
    'Michael': 59,
    'Sophia': 91
}

# Checking whether each employee's performance is satisfactory
for employee, score in employees.items():
    if score >= 70:
        print(f"{employee} has satisfactory performance.")
    else:
        print(f"{employee} needs improvement.")
