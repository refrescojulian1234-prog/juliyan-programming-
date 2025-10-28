# Name: Julian Mendis
# Student Number: 10685665

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import json
import os

class AdminGUI:
    def __init__(self):
        self.data = []
        self.load_data()
        self.root = tk.Tk()
        self.root.title("One Must Go - Admin Panel")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        self.center_window()
        self.create_ui()
        self.refresh_categories()
        self.root.mainloop()
    
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - 800) // 2
        y = (self.root.winfo_screenheight() - 600) // 2
        self.root.geometry(f'800x600+{x}+{y}')
    
    def create_ui(self):
        # Header
        header = tk.Frame(self.root, bg='#34495e', height=80)
        header.pack(fill=tk.X, padx=20, pady=20)
        header.pack_propagate(False)
        tk.Label(header, text="🎮 ONE MUST GO - ADMIN PANEL", font=("Arial", 20, "bold"), fg='white', bg='#34495e').pack(expand=True)
        
        # Main content with background color
        main = tk.Frame(self.root, bg='#2c3e50')
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # panel Controls in left side 
        left = tk.Frame(main, bg='#34495e', width=250)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left.pack_propagate(False)
        
        btn_style = {'font': ('Arial', 11, 'bold'), 'bg': '#3498db', 'fg': 'white', 'relief': 'flat', 'padx': 20, 'pady': 12, 'width': 20}
        tk.Label(left, text="ACTIONS", font=("Arial", 12, "bold"), fg='white', bg='#34495e').pack(pady=(20, 10))
        tk.Button(left, text="➕ ADD CATEGORY", command=self.add_category, **btn_style).pack(pady=8)
        tk.Button(left, text="📋 LIST ALL", command=self.list_categories, **btn_style).pack(pady=8)
        tk.Button(left, text="🔍 SEARCH", command=self.search_categories, **btn_style).pack(pady=8)
        tk.Button(left, text="👁️ VIEW DETAILS", command=self.view_category, **btn_style).pack(pady=8)
        tk.Button(left, text="🗑️ DELETE", command=self.delete_category, **btn_style).pack(pady=8)
        
        stats = tk.Frame(left, bg='#2c3e50', relief='raised', bd=1)
        stats.pack(fill=tk.X, padx=10, pady=20)
        tk.Label(stats, text="📊 STATISTICS", font=("Arial", 11, "bold"), fg='white', bg='#2c3e50').pack(pady=10)
        self.stats_label = tk.Label(stats, text="Categories: 0\nTotal Votes: 0", font=("Arial", 10), fg='#bdc3c7', bg='#2c3e50')
        self.stats_label.pack(pady=(0, 10))
        
        # panel Display right side view tab
        right = tk.Frame(main, bg='#ecf0f1')
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        display_header = tk.Frame(right, bg='#34495e', height=40)
        display_header.pack(fill=tk.X)
        display_header.pack_propagate(False)
        tk.Label(display_header, text="CATEGORIES LIST", font=("Arial", 12, "bold"), fg='white', bg='#34495e').pack(expand=True)
        
        self.tree = ttk.Treeview(right, columns=('#1', '#2', '#3'), show='headings', height=15)
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Category Name')
        self.tree.heading('#3', text='Options/Votes')
        self.tree.column('#1', width=50, anchor='center')
        self.tree.column('#2', width=200, anchor='w')
        self.tree.column('#3', width=150, anchor='center')
        
        scrollbar = ttk.Scrollbar(right, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
        
        self.details_text = scrolledtext.ScrolledText(right, height=8, font=("Arial", 10), bg='#f8f9fa', fg='#2c3e50')
        self.details_text.pack(fill=tk.X, padx=10, pady=10)
    
    def load_data(self):
        try:
            if os.path.exists('data.txt'):
                with open('data.txt', 'r') as file:
                    self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []
    
    def save_data(self):
        try:
            with open('data.txt', 'w') as file:
                json.dump(self.data, file, indent=4)
            return True
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save data: {e}")
            return False
    
    def refresh_categories(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, cat in enumerate(self.data, 1):
            votes = sum(opt['votes'] for opt in cat['options'])
            self.tree.insert('', 'end', values=(i, cat['name'], f"{len(cat['options'])} opts, {votes} votes"))
        total_votes = sum(sum(opt['votes'] for opt in cat['options']) for cat in self.data)
        self.stats_label.config(text=f"Categories: {len(self.data)}\nTotal Votes: {total_votes}")
    
    def add_category(self):
        dialog = AddCategoryDialog(self.root, self)
        self.root.wait_window(dialog.dialog)
        if dialog.result:
            self.data.append(dialog.result)
            if self.save_data():
                self.refresh_categories()
                messagebox.showinfo("Success", "Category added successfully!")
    
    def list_categories(self):
        self.refresh_categories()
        self.details_text.delete(1.0, tk.END)
        if not self.data:
            self.details_text.insert(tk.END, "No categories available.\nUse 'Add Category' to create one.")
        else:
            self.details_text.insert(tk.END, "📋 ALL CATEGORIES:\n\n")
            for i, cat in enumerate(self.data, 1):
                self.details_text.insert(tk.END, f"{i}. {cat['name']}\n")
    #search chatogory 
    def search_categories(self):
        term = simpledialog.askstring("Search", "Enter first letter to search:")
        if term:
            self.details_text.delete(1.0, tk.END)
            letter = term.lower().strip()[0]
            results = []
            for i, cat in enumerate(self.data):
                if cat['name'].lower().startswith(letter):
                    results.append((i, cat, "category"))
                else:
                    matches = [opt['name'] for opt in cat['options'] if opt['name'].lower().startswith(letter)]
                    if matches:
                        results.append((i, cat, "option", matches))
            if results:
                self.details_text.insert(tk.END, f"🔍 SEARCH RESULTS for '{letter.upper()}':\n\nFound {len(results)} result(s)\n{'='*50}\n\n")
                for r in results:
                    self.details_text.insert(tk.END, f"{r[0]+1}. {r[1]['name']}\n")
                    if r[2] == "option" and len(r) > 3:
                        self.details_text.insert(tk.END, f"   Matching options: {', '.join(r[3])}\n")
                    self.details_text.insert(tk.END, f"   Total votes: {sum(opt['votes'] for opt in r[1]['options'])}\n\n")
            else:
                self.details_text.insert(tk.END, f"❌ No results found for '{letter.upper()}'\n\n💡 Try different letters")
    #view category instructions 
    def view_category(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Selection Required", "Please select a category from the list.")
            return
        idx = self.tree.item(sel[0])['values'][0] - 1
        if 0 <= idx < len(self.data):
            cat = self.data[idx]
            self.details_text.delete(1.0, tk.END)
            self.details_text.insert(tk.END, f"👁️ VIEWING: {cat['name']}\n\nOPTIONS & VOTES:\n{'-'*40}\n")
            total = sum(opt['votes'] for opt in cat['options'])
            for opt in sorted(cat['options'], key=lambda x: x['votes'], reverse=True):
                pct = (opt['votes'] / total * 100) if total > 0 else 0
                self.details_text.insert(tk.END, f"• {opt['name']}: {opt['votes']} votes ({pct:.1f}%)\n")
            if total == 0:
                self.details_text.insert(tk.END, "\n📭 No votes recorded yet.")
    # this is the delete category
    def delete_category(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Selection Required", "Please select a category to delete.")
            return
        item = self.tree.item(sel[0])
        name = item['values'][1]
        idx = item['values'][0] - 1
        if messagebox.askyesno("Confirm Delete", f"Delete category '{name}'?"):
            self.data.pop(idx)
            if self.save_data():
                self.refresh_categories()
                messagebox.showinfo("Success", f"Category '{name}' deleted!")
# this is the add category part
class AddCategoryDialog:
    def __init__(self, parent, admin):
        self.admin = admin
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add New Category")
        self.dialog.geometry("500x400")
        self.dialog.configure(bg='#ecf0f1')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        x = parent.winfo_x() + (parent.winfo_width() - 500) // 2
        y = parent.winfo_y() + (parent.winfo_height() - 400) // 2
        self.dialog.geometry(f"500x400+{x}+{y}")
        self.create_ui()
    #this is the pop up add catergory display  
    def create_ui(self):
        tk.Label(self.dialog, text="➕ ADD NEW CATEGORY", font=("Arial", 16, "bold"), fg='#2c3e50', bg='#ecf0f1').pack(pady=20)
        name_frame = tk.Frame(self.dialog, bg='#ecf0f1')
        name_frame.pack(fill=tk.X, padx=50, pady=10)
        tk.Label(name_frame, text="Category Name:", font=("Arial", 11, "bold"), fg='#2c3e50', bg='#ecf0f1').pack(anchor='w')
        self.name_entry = tk.Entry(name_frame, font=("Arial", 12), width=30)
        self.name_entry.pack(fill=tk.X, pady=5)
        
        opts = tk.Frame(self.dialog, bg='#ecf0f1')
        opts.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
        tk.Label(opts, text="Options (2-5 required):", font=("Arial", 11, "bold"), fg='#2c3e50', bg='#ecf0f1').pack(anchor='w')
        self.options_list = tk.Listbox(opts, font=("Arial", 11), height=6)
        self.options_list.pack(fill=tk.BOTH, expand=True, pady=5)
        
        add_frame = tk.Frame(opts, bg='#ecf0f1')
        add_frame.pack(fill=tk.X, pady=5)
        self.opt_entry = tk.Entry(add_frame, font=("Arial", 11))
        self.opt_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.opt_entry.bind('<Return>', lambda e: self.add_opt())
        tk.Button(add_frame, text="Add Option", command=self.add_opt, bg='#27ae60', fg='white', font=("Arial", 10, "bold"), relief='flat').pack(side=tk.RIGHT)
        
        btns = tk.Frame(self.dialog, bg='#ecf0f1')
        btns.pack(fill=tk.X, padx=50, pady=20)
        tk.Button(btns, text="🗑️ Remove", command=self.remove_opt, bg='#e74c3c', fg='white', font=("Arial", 10, "bold"), relief='flat').pack(side=tk.LEFT)
        tk.Button(btns, text="✅ Save", command=self.save, bg='#27ae60', fg='white', font=("Arial", 11, "bold"), relief='flat', padx=20).pack(side=tk.RIGHT)
        tk.Button(btns, text="❌ Cancel", command=self.dialog.destroy, bg='#95a5a6', fg='white', font=("Arial", 10, "bold"), relief='flat').pack(side=tk.RIGHT, padx=(0, 10))
    
    def add_opt(self):
        opt = self.opt_entry.get().strip()
        if opt:
            existing = [self.options_list.get(i).lower() for i in range(self.options_list.size())]
            if opt.lower() in existing:
                messagebox.showwarning("Duplicate", "This option already exists!")
                return
            self.options_list.insert(tk.END, opt)
            self.opt_entry.delete(0, tk.END)
            if self.options_list.size() >= 5:
                self.opt_entry.config(state='disabled')
                messagebox.showinfo("Maximum", "Maximum 5 options reached!")
    # remove option
    def remove_opt(self):
        sel = self.options_list.curselection()
        if sel:
            self.options_list.delete(sel[0])
            self.opt_entry.config(state='normal')
    #this saves the data
    def save(self):
        name = self.name_entry.get().strip()
        count = self.options_list.size()
        if not name:
            messagebox.showerror("Error", "Please enter a category name.")
            return
        if count < 2:
            messagebox.showerror("Error", "Please add at least 2 options.")
            return
        existing = [c['name'].lower() for c in self.admin.data]
        if name.lower() in existing:
            messagebox.showerror("Error", "A category with this name already exists.")
            return
        self.result = {"name": name, "options": [{"name": self.options_list.get(i), "votes": 0} for i in range(count)]}
        self.dialog.destroy()

if __name__ == "__main__":
    AdminGUI()