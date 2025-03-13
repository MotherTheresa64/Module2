# ====================
# Lesson 5: File Handling
# ====================

# 📌 Brief Overview:
# In this lesson, you'll learn the fundamentals of Python file handling—how to open, read, write, and append to files.
# You will also explore how to manage structured data, such as lists, dictionaries, and custom data formats, using files.
# By the end of this lesson, you'll be able to build a simple program that interacts with files to store and retrieve data interactively.

# ====================
# Engage & Apply: Mid-Lesson Exercise
# ====================

# Task: Create a simple Python program that:
# - Allows the user to add favorite foods to a list.
# - Stores the data in a file.
# - Lets the user view or remove items from the list.

# Example solution for managing a list of favorite foods
def write_foods(foods):
    """Writes the list of favorite foods to a file."""
    with open('foods.txt', 'w') as file:
        for food in foods:
            file.write(food + '\n')

def read_foods():
    """Reads the list of favorite foods from a file."""
    foods_list = []
    try:
        with open('foods.txt', 'r') as file:
            for line in file:
                foods_list.append(line.strip())
    except FileNotFoundError:
        return []
    return foods_list

def main():
    """Main function to allow interaction with favorite foods."""
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == '1':
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == '2':
            print("Your favorite foods:")
            for idx, food in enumerate(foods, 1):
                print(f"{idx}. {food}")
        elif action == '3':
            idx = int(input("Which food to remove? "))
            if 0 < idx <= len(foods):
                foods.pop(idx - 1)
                write_foods(foods)
                print("Food removed successfully.")
            else:
                print("Invalid index.")
        elif action == '4':
            break

main()


# ====================
# Final Challenge: Edit Platform or Genre
# ====================

# Scenario: Modify the TV show manager program to allow the user to edit the platform or genre of an existing TV show.

import re

# Function to write TV shows to a file
def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

# Function to add a show to the list and write it to the file
def add_show(shows):
    title = input("What is the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("What is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)

# Function to read TV shows from a file
def read_shows():
    shows_list = []
    try:
        with open('shows_list.txt', 'r') as file:
            for line in file:
                data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
                shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    except FileNotFoundError:
        return []
    return shows_list

# Function to view the list of TV shows
def view(shows):
    print("Shows List")
    print('-----------------------')
    for idx, show in enumerate(shows, 1):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

# Function to remove a TV show from the list and write the updated list to the file
def remove_show(shows):
    view(shows)
    option = int(input("\nChoose a number for the show you'd like to remove: "))
    if 0 < option <= len(shows):
        show = shows.pop(option - 1)  # index - 1
        print(f"\n{show['Title']} was successfully removed!")
        write_show(shows)
    else:
        print("Invalid option.")

# Function to edit a TV show's platform or genre
def edit_show(shows):
    view(shows)
    option = int(input("\nChoose a number for the show you'd like to edit: "))
    if 0 < option <= len(shows):
        show = shows[option - 1]
        print(f"Editing {show['Title']}")
        choice = input("Would you like to edit the platform (p) or genre (g)? ")
        
        if choice.lower() == 'p':
            new_platform = input("Enter the new platform: ")
            show['Platform'] = new_platform
        elif choice.lower() == 'g':
            new_genre = input("Enter the new genre: ")
            show['Genre'] = new_genre
        
        write_show(shows)
        print(f"{show['Title']} has been updated!")
    else:
        print("Invalid option.")

def main_tv_show_manager():
    """Main function to manage TV shows."""
    while True:
        shows_list = read_shows()  # Read the current list of shows from the file
        action = input('''
Options
-----------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Edit Platform/Genre of a TV Show
5 - Quit
''')
        if action == '1':
            add_show(shows_list)  # Add a new show
        elif action == '2':
            remove_show(shows_list)  # Remove a show
        elif action == '3':
            view(shows_list)  # View the list of shows
        elif action == '4':
            edit_show(shows_list)  # Edit the platform/genre of a show
        elif action == '5':
            print("Thanks for using this app!")
            break

main_tv_show_manager()
