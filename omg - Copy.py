# Name: Julian Mendis
# Student Number: 10685665

import tkinter as tk
import tkinter.messagebox as messagebox
import json

class ProgramGUI:
    def __init__(self):
        # Load data from file
        try:
            with open('data.txt', 'r') as file:
                self.data = json.load(file)
        except:
            messagebox.showerror("Error", "Missing/Invalid file: data.txt not found or corrupted.\nPlease run admin.py first.")
            return
        
        # Check if data is empty
        if not self.data:
            messagebox.showerror("Error", "No categories found in data.txt.\nPlease add categories using admin.py first.")
            return
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("One Must Go")
        self.root.geometry("600x500")
        self.root.configure(bg='#2c3e50')
        
        # Initialize index to track current category
        self.index = 0
        
        # Create GUI widgets
        # Header frame
        header_frame = tk.Frame(self.root, bg='#34495e', height=100)
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="ONE MUST GO",
            font=("Arial", 24, "bold"),
            fg='white',
            bg='#34495e'
        )
        title_label.pack(expand=True)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Which one would you be most willing to live without?",
            font=("Arial", 11),
            fg='#ecf0f1',
            bg='#34495e'
        )
        subtitle_label.pack()
        
        # Category name label
        self.category_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 18, "bold"),
            fg='#3498db',
            bg='#2c3e50',
            wraplength=550
        )
        self.category_label.pack(pady=20)
        
        # Options frame (where buttons will be created)
        self.options_frame = tk.Frame(self.root, bg='#2c3e50')
        self.options_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=10)
        
        # Footer frame
        footer_frame = tk.Frame(self.root, bg='#34495e', height=50)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Click on your choice",
            font=("Arial", 10),
            fg='#bdc3c7',
            bg='#34495e'
        )
        footer_label.pack(expand=True)
        
        # Display first category
        self.show_category()
        
        # Start main loop
        self.root.mainloop()
    
    def show_category(self):
        """Display the current category name and create buttons for its options."""
        # Get current category
        current_category = self.data[self.index]
        
        # Update category name label
        self.category_label.config(text=current_category['name'])
        
        # Clear previous option buttons
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Create button for each option
        for option in current_category['options']:
            option_name = option['name']
            
            # Create button with lambda to pass option name
            btn = tk.Button(
                self.options_frame,
                text=option_name,
                font=("Arial", 13),
                bg='#34495e',
                fg='white',
                activebackground='#3498db',
                activeforeground='white',
                relief='flat',
                padx=20,
                pady=15,
                cursor='hand2',
                command=lambda name=option_name: self.record_vote(name)
            )
            btn.pack(fill=tk.X, pady=5)
            
            # Add hover effects
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg='#3498db'))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg='#34495e'))
    
    def record_vote(self, name):
        """Record a vote for the specified option and proceed to next category."""
        # Find the option and increment its vote count
        current_category = self.data[self.index]
        for option in current_category['options']:
            if option['name'] == name:
                option['votes'] += 1
                break
        
        # Save data to file
        with open('data.txt', 'w') as file:
            json.dump(self.data, file, indent=4)
        
        # Show confirmation message
        messagebox.showinfo("Vote Recorded", f"Your vote for '{name}' has been recorded!")
        
        # Check if this was the last category
        if self.index == len(self.data) - 1:
            # Last category - show completion message and end program
            messagebox.showinfo(
                "Complete",
                f"Thank you for completing all {len(self.data)} categories!\n\nYour votes have been saved."
            )
            self.root.destroy()
        else:
            # Move to next category
            self.index += 1
            self.show_category()


if __name__ == "__main__":
    ProgramGUI()