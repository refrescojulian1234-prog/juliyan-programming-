# Name: Julian Mendis
# Student Number: 10685665
"""
Pseudocode for admin.py
Name: Julian Mendis
Student Number: 10685665

================================================================================
MAIN PROGRAM
================================================================================

Try to open data.txt in read mode
    Load JSON data from file into data variable
    Close file
If any exceptions occur
    Set data to empty list

Display line of equals signs
Display "WELCOME TO ONE MUST GO - ADMIN PROGRAM"
Display "Created by Julian Mendis"
Display line of equals signs

Loop endlessly
    Display blank line
    Display menu prompt: "Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit."
    Prompt user to enter their choice
    Convert choice to lowercase and strip whitespace
    
    If choice is a
        Display "ADD NEW CATEGORY" heading
        
        Call input_something function with "Enter category name: " prompt
        Store result in category_name variable
        
        Create list of existing category names in lowercase from data list
        If category_name in lowercase exists in existing names list
            Display error message about duplicate category name
            Continue to next iteration of main loop
        
        Create empty options list
        
        Loop while length of options list is less than 5
            If length of options list is less than 2
                Call input_something function with prompt showing option number
                Store result in option_name variable
            Otherwise
                Prompt user for option name or Enter to finish
                Strip whitespace from input
                If input is empty and options list has at least 2 items
                    Break out of options loop
                If input is empty and options list has fewer than 2 items
                    Display error about needing at least 2 options
                    Continue to next iteration of options loop
                Set option_name to the input value
            
            Create list of existing option names in lowercase from options list
            If option_name in lowercase exists in existing options list
                Display error message about duplicate option
                Continue to next iteration of options loop
            
            Append option_name to options list
            
            If length of options list equals 5
                Display "Maximum of 5 options reached" message
                Break out of options loop
        
        Create new_category dictionary with two keys
        Set name key to category_name value
        Set options key to list comprehension creating dictionaries for each option
        Each option dictionary has name key set to option and votes key set to 0
        
        Append new_category dictionary to data list
        Call save_data function passing data as parameter
        Display success message with category name
    
    Otherwise if choice is l
        Display "ALL CATEGORIES" heading
        
        If data list is empty
            Display "No categories saved" message
        Otherwise
            Loop through data list using enumerate to get index and category
                Get length of category options list and store in option_count
                Display index plus 1, category name, and option count in parentheses
    
    Otherwise if choice is s
        Display "SEARCH CATEGORIES" heading
        
        If data list is empty
            Display "No categories saved" message
        Otherwise
            Call input_something function with "Enter search term: " prompt
            Convert result to lowercase and store in search_term
            
            Set results_found flag to False
            
            Loop through data list using enumerate to get index and category
                If search_term is contained in category name converted to lowercase
                    Get length of category options list and store in option_count
                    Display index plus 1, category name, and option count in parentheses
                    Set results_found flag to True
            
            If results_found flag is False
                Display "No results found" message
    
    Otherwise if choice is v
        Display "VIEW CATEGORY" heading
        
        If data list is empty
            Display "No categories saved" message
        Otherwise
            Call input_int function with prompt and data list length as max value
            Store result in index_num variable
            Get category from data list at index of index_num minus 1
            
            Display blank line
            Display "Category: " followed by category name
            Display "Options" with count in parentheses
            Loop through each option in category options list
                Display option name and vote count with proper formatting
    
    Otherwise if choice is d
        Display "DELETE CATEGORY" heading
        
        If data list is empty
            Display "No categories saved" message
        Otherwise
            Call input_int function with delete prompt and data list length as max value
            Store result in index_num variable
            Get category name from data list at index of index_num minus 1
            
            Prompt user to confirm deletion with y/n
            Convert confirmation to lowercase
            If confirmation equals y
                Delete item from data list at index of index_num minus 1
                Call save_data function passing data as parameter
                Display "Category deleted" message
            Otherwise
                Display "Deletion cancelled" message
    
    Otherwise if choice is q
        Display blank line
        Display thank you message including program name and author name
        Display "Goodbye!" message with blank line
        Break out of main loop to end program
    
    Otherwise
        Display "Invalid choice. Please try again." message

Program ends

================================================================================
FUNCTION DEFINITIONS
================================================================================

Function: input_something
Parameters: prompt (the message to display when asking for input)
Returns: String containing validated user input with whitespace removed

    Loop endlessly
        Prompt user for input using prompt parameter
        Strip whitespace from beginning and end of input
        Store result in user_input variable
        
        If user_input is not empty
            Return user_input string
            
End function

--------------------------------------------------------------------------------

Function: input_int
Parameters: prompt (the message to display), max_value (maximum acceptable value)
Returns: Integer between 1 and max_value inclusive

    Loop endlessly
        Try to execute the following
            Prompt user for input using prompt parameter
            Convert input to integer and store in value variable
            
            If value is between 1 and max_value inclusive
                Return value as integer
            Otherwise
                Display message asking for number between 1 and max_value
                
        If ValueError exception occurs
            Display "Invalid input. Please enter a valid number." message
            
End function

--------------------------------------------------------------------------------

Function: save_data
Parameters: data (the list of category dictionaries to save to file)
Returns: Nothing

    Open data.txt file in write mode
    Write data to file in JSON format with 4-space indentation
    Close file
    
End function
```

---

## Pseudocode for omg.py (NOT REQUIRED - For Reference Only)
```
Pseudocode for omg.py (GUI Program)
Name: Julian Mendis
Student Number: 10685665

Note: Pseudocode is not required for GUI programs according to assignment brief.
This is provided for reference only and should NOT be submitted.

================================================================================
CLASS: ProgramGUI
================================================================================

Constructor Method: __init__
Parameters: self
Returns: Nothing

    Try to execute the following
        Open data.txt file in read mode
        Load JSON data from file into self.data attribute
        Close file
    If any exceptions occur
        Display error messagebox with title "Error"
        Display message about missing or invalid file
        Return from constructor to end program
    
    If self.data list is empty
        Display error messagebox with title "Error"
        Display message about no categories found
        Return from constructor to end program
    
    Create main window and store in self.root attribute
    Set window title to "One Must Go"
    Set window geometry to 600x500 pixels
    Set window background color to dark blue
    
    Set self.index attribute to 0
    
    Create header_frame with dark background and fixed height
    Pack header_frame at top with padding
    Disable frame propagation
    
    Create title_label in header_frame
    Set text to "ONE MUST GO" in large bold white font
    Pack title_label to expand in frame
    
    Create subtitle_label in header_frame
    Set text to question about living without options
    Pack subtitle_label below title
    
    Create self.category_label for displaying category names
    Set font to large bold blue text
    Set text wrapping width
    Pack label with vertical padding
    
    Create self.options_frame for holding option buttons
    Set background to dark color
    Pack frame to fill and expand with padding
    
    Create footer_frame with dark background and fixed height
    Pack footer_frame at bottom
    Disable frame propagation
    
    Create footer_label in footer_frame
    Set text to "Click on your choice"
    Pack label to expand in frame
    
    Call show_category method
    
    Call mainloop method on self.root to start GUI
    
End constructor

--------------------------------------------------------------------------------

Method: show_category
Parameters: self
Returns: Nothing

    Get current category from self.data at index self.index
    Store in current_category variable
    
    Update self.category_label text to show current category name
    
    Loop through all widgets in self.options_frame
        Destroy each widget to clear previous buttons
    
    Loop through each option in current category options list
        Get option name from option dictionary
        
        Create button in self.options_frame
        Set button text to option name
        Set font to medium size
        Set colors for normal and active states
        Set padding and cursor style
        Set command to call record_vote method with option name using lambda
        Pack button to fill horizontally with vertical padding
        
        Bind mouse enter event to change button background color
        Bind mouse leave event to restore button background color
        
End method

--------------------------------------------------------------------------------

Method: record_vote
Parameters: self, name (the name of the selected option)
Returns: Nothing

    Get current category from self.data at index self.index
    
    Loop through each option in current category options list
        If option name matches name parameter
            Add 1 to option votes value
            Break out of loop
    
    Open data.txt file in write mode
    Write self.data to file in JSON format with indentation
    Close file
    
    Display info messagebox with title "Vote Recorded"
    Display message confirming vote for option name
    
    If self.index equals length of self.data minus 1
        Display info messagebox with title "Complete"
        Display thank you message with category count
        Destroy self.root window to end program
    Otherwise
        Add 1 to self.index
        Call show_category method to display next category
        
End method

================================================================================
MAIN EXECUTION
================================================================================

If this file is run directly
    Create instance of ProgramGUI class

"""
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