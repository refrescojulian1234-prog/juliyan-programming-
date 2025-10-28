# Name: Julian Mendis
# Student Number: 10685665

import json
import os

# Function definitions
def input_something(prompt):
    """
    Repeatedly prompts user for input until they enter a non-empty value.
    
    Parameters:
        prompt (str): The message to display when asking for input
    
    Returns:
        str: The user's input with whitespace stripped
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:  # If not empty after stripping whitespace
            return user_input


def input_int(prompt, max_value):
    """
    Repeatedly prompts user for an integer between 1 and max_value.
    
    Parameters:
        prompt (str): The message to display when asking for input
        max_value (int): The maximum acceptable value
    
    Returns:
        int: A valid integer between 1 and max_value (inclusive)
    """
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between 1 and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def save_data(data):
    """
    Saves the data list to data.txt in JSON format.
    
    Parameters:
        data (list): The list of category dictionaries to save
    
    Returns:
        None
    """
    with open('data.txt', 'w') as file:
        json.dump(data, file, indent=4)


# Main program
# Load data from file
try:
    with open('data.txt', 'r') as file:
        data = json.load(file)
except:
    data = []

# Display welcome message
print("\n" + "="*50)
print("WELCOME TO ONE MUST GO - ADMIN PROGRAM")
print("Created by Julian Mendis")
print("="*50)

# Main menu loop
while True:
    print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input("Enter your choice: ").lower().strip()
    
    if choice == 'a':
        # Add a new category
        print("\n--- ADD NEW CATEGORY ---")
        
        # Get category name
        category_name = input_something("Enter category name: ")
        
        # Check for duplicate category names
        existing_names = [cat['name'].lower() for cat in data]
        if category_name.lower() in existing_names:
            print("Error: A category with this name already exists.")
            continue
        
        # Get options (2 to 5)
        options = []
        while len(options) < 5:
            if len(options) < 2:
                option_name = input_something(f"Enter option {len(options) + 1}: ")
            else:
                option_input = input(f"Enter option {len(options) + 1} (or press Enter if done): ").strip()
                if not option_input and len(options) >= 2:
                    break
                if not option_input:
                    print("You must enter at least 2 options.")
                    continue
                option_name = option_input
            
            # Check for duplicate options
            existing_options = [opt.lower() for opt in options]
            if option_name.lower() in existing_options:
                print("Error: This option already exists in this category.")
                continue
            
            options.append(option_name)
            
            if len(options) == 5:
                print("Maximum of 5 options reached.")
                break
        
        # Create category dictionary
        new_category = {
            "name": category_name,
            "options": [{"name": opt, "votes": 0} for opt in options]
        }
        
        # Add to data and save
        data.append(new_category)
        save_data(data)
        print(f"\nCategory '{category_name}' added successfully!")
    
    elif choice == 'l':
        # List all categories
        print("\n--- ALL CATEGORIES ---")
        
        if not data:
            print("No categories saved.")
        else:
            for index, category in enumerate(data):
                option_count = len(category['options'])
                print(f"{index + 1}. {category['name']} ({option_count} options)")
    
    elif choice == 's':
        # Search categories
        print("\n--- SEARCH CATEGORIES ---")
        
        if not data:
            print("No categories saved.")
        else:
            search_term = input_something("Enter search term: ").lower()
            
            results_found = False
            for index, category in enumerate(data):
                if search_term in category['name'].lower():
                    option_count = len(category['options'])
                    print(f"{index + 1}. {category['name']} ({option_count} options)")
                    results_found = True
            
            if not results_found:
                print("No results found.")
    
    elif choice == 'v':
        # View category details
        print("\n--- VIEW CATEGORY ---")
        
        if not data:
            print("No categories saved.")
        else:
            index_num = input_int("Enter category number: ", len(data))
            category = data[index_num - 1]
            
            print(f"\nCategory: {category['name']}")
            print(f"Options ({len(category['options'])}):")
            for option in category['options']:
                print(f"  - {option['name']}: {option['votes']} votes")
    
    elif choice == 'd':
        # Delete category
        print("\n--- DELETE CATEGORY ---")
        
        if not data:
            print("No categories saved.")
        else:
            index_num = input_int("Enter category number to delete: ", len(data))
            category_name = data[index_num - 1]['name']
            
            confirm = input(f"Are you sure you want to delete '{category_name}'? (y/n): ").lower()
            if confirm == 'y':
                del data[index_num - 1]
                save_data(data)
                print("Category deleted.")
            else:
                print("Deletion cancelled.")
    
    elif choice == 'q':
        # Quit program
        print("\nThank you for using the One Must Go Admin Program by Julian Mendis!")
        print("Goodbye!\n")
        break
    
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")