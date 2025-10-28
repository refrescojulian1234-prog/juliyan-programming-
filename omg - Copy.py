# Name: Julian Mendis
# Student Number: 10685665

import tkinter as tk
import tkinter.messagebox as messagebox
import json
import random
from tkinter import ttk

class ProgramGUI:
    def __init__(self):
        if not self.load_data():
            return
        random.shuffle(self.data)
        self.index = 0
        self.main_window = tk.Tk()
        self.main_window.title("One Must Go - Decision Game")
        self.main_window.geometry("700x600")
        self.main_window.configure(bg='#1a1a1a')
        self.center_window()
        self.create_ui()
        self.show_category()
        self.main_window.mainloop()
    
    def center_window(self):
        self.main_window.update_idletasks()
        x = (self.main_window.winfo_screenwidth() - 700) // 2
        y = (self.main_window.winfo_screenheight() - 600) // 2
        self.main_window.geometry(f'700x600+{x}+{y}')
    
    def load_data(self):
        try:
            with open('data.txt', 'r') as file:
                self.data = json.load(file)
            if not self.data:
                messagebox.showerror("No Categories", "🎮 No categories found!\n\nPlease run the Admin Program first.")
                return False
        except FileNotFoundError:
            messagebox.showerror("File Missing", "📁 Data file not found!\n\nPlease run the Admin Program first.")
            return False
        except json.JSONDecodeError:
            messagebox.showerror("Invalid Data", "❌ Corrupted data file!\n\nPlease run the Admin Program to fix this.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"⚠️ An error occurred:\n{str(e)}")
            return False
        return True
    
    def create_ui(self):
        main = tk.Frame(self.main_window, bg='#1a1a1a')
        main.pack(fill=tk.BOTH, expand=True)
        
        header = tk.Frame(main, bg='#2c3e50', height=120)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text="🎮 ONE MUST GO", font=("Arial", 28, "bold"), fg='white', bg='#2c3e50').pack(expand=True)
        tk.Label(header, text="Which one would you be most willing to live without?", font=("Arial", 12), fg='#ecf0f1', bg='#2c3e50').pack(pady=(0, 20))
        
        self.progress_frame = tk.Frame(main, bg='#1a1a1a')
        self.progress_frame.pack(fill=tk.X, pady=20, padx=30)
        self.progress_info = tk.Label(self.progress_frame, text="", font=("Arial", 11, "bold"), fg='#ecf0f1', bg='#1a1a1a')
        self.progress_info.pack()
        
        prog_container = tk.Frame(self.progress_frame, bg='#34495e', height=20, relief='sunken', bd=1)
        prog_container.pack(fill=tk.X, pady=10)
        prog_container.pack_propagate(False)
        self.progress_fill = tk.Frame(prog_container, bg='#3498db', height=18)
        self.progress_fill.place(relx=0, rely=0, relwidth=0, relheight=1)
        
        self.cat_frame = tk.Frame(main, bg='#1a1a1a')
        self.cat_frame.pack(fill=tk.X, pady=10, padx=30)
        self.cat_label = tk.Label(self.cat_frame, text="", font=("Arial", 20, "bold"), fg='#3498db', bg='#1a1a1a', wraplength=600)
        self.cat_label.pack()
        
        opts_container = tk.Frame(main, bg='#1a1a1a')
        opts_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        self.canvas = tk.Canvas(opts_container, bg='#1a1a1a', highlightthickness=0)
        scrollbar = ttk.Scrollbar(opts_container, orient="vertical", command=self.canvas.yview)
        self.scrollable = tk.Frame(self.canvas, bg='#1a1a1a')
        self.scrollable.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        footer = tk.Frame(main, bg='#2c3e50', height=50)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        footer.pack_propagate(False)
        tk.Label(footer, text="💡 Click on your choice - Which one could you live without?", font=("Arial", 10), fg='#bdc3c7', bg='#2c3e50').pack(expand=True)
    
    def show_category(self):
        total = len(self.data)
        progress = ((self.index + 1) / total) * 100
        self.progress_fill.place(relx=0, rely=0, relwidth=progress/100, relheight=1)
        self.progress_info.config(text=f"Category {self.index + 1} of {total} • {progress:.0f}% Complete")
        
        cat = self.data[self.index]
        self.cat_label.config(text=f"🎯 {cat['name']}")
        
        for w in self.scrollable.winfo_children():
            w.destroy()
        
        opts = cat['options'].copy()
        random.shuffle(opts)
        for opt in opts:
            self.create_button(opt)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def create_button(self, opt):
        frame = tk.Frame(self.scrollable, bg='#1a1a1a')
        frame.pack(fill=tk.X, pady=6, padx=10)
        btn = tk.Button(frame, text=f"   {opt['name']}", font=("Arial", 14, "bold"), fg='white', bg='#34495e', activebackground='#3498db', activeforeground='white', relief='flat', bd=0, padx=30, pady=15, anchor='w', cursor='hand2', command=lambda: self.vote(opt['name']))
        btn.pack(fill=tk.X)
        btn.bind("<Enter>", lambda e: btn.configure(bg='#3498db'))
        btn.bind("<Leave>", lambda e: btn.configure(bg='#34495e'))
        if opt['votes'] > 0:
            badge = tk.Label(frame, text=f"{opt['votes']} votes", font=("Arial", 9, "bold"), fg='white', bg='#e74c3c', padx=8, pady=2)
            badge.place(relx=0.85, rely=0.5, anchor='center')
    
    def vote(self, name):
        cat = self.data[self.index]
        voted = None
        for opt in cat['options']:
            if opt['name'] == name:
                opt['votes'] += 1
                voted = opt
                break
        try:
            with open('data.txt', 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save your vote: {e}")
            return
        self.show_feedback(cat, voted)
    
    def show_feedback(self, cat, voted):
        fb = tk.Toplevel(self.main_window)
        fb.title("Vote Recorded ✅")
        fb.geometry("450x350")
        fb.configure(bg='#2c3e50')
        fb.resizable(False, False)
        fb.transient(self.main_window)
        fb.grab_set()
        x = (self.main_window.winfo_x() + self.main_window.winfo_width() // 2) - 225
        y = (self.main_window.winfo_y() + self.main_window.winfo_height() // 2) - 175
        fb.geometry(f"450x350+{x}+{y}")
        
        tk.Label(fb, text="✅ VOTE RECORDED", font=("Arial", 18, "bold"), fg='#27ae60', bg='#2c3e50').pack(pady=(30, 10))
        
        total = sum(o['votes'] for o in cat['options'])
        if total == 1:
            msg = f"🎉 You're the FIRST to vote on:\n\"{cat['name']}\"!\n\nYour choice: \"{voted['name']}\""
        else:
            popular = max(cat['options'], key=lambda x: x['votes'])
            if voted['votes'] == popular['votes'] and popular['name'] == voted['name']:
                msg = f"🔥 TRENDING CHOICE!\n\"{voted['name']}\" is now the MOST popular!"
            else:
                msg = f"✓ You chose: \"{voted['name']}\"\n\n🏆 Most popular: \"{popular['name']}\" ({popular['votes']} votes)"
            msg += f"\n\n📊 Total votes: {total}"
        
        tk.Label(fb, text=msg, font=("Arial", 12), fg='white', bg='#2c3e50', wraplength=400, justify=tk.CENTER).pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        cont_text = "➡️ Continue" if self.index < len(self.data) - 1 else "🎉 Finish"
        tk.Button(fb, text=cont_text, font=("Arial", 12, "bold"), fg='white', bg='#27ae60', activebackground='#219a52', relief='flat', padx=30, pady=12, command=fb.destroy).pack(pady=20)
        
        self.main_window.wait_window(fb)
        if self.index == len(self.data) - 1:
            self.show_complete()
        else:
            self.index += 1
            self.show_category()
    
    def show_complete(self):
        comp = tk.Toplevel(self.main_window)
        comp.title("Game Complete! 🎉")
        comp.geometry("500x450")
        comp.configure(bg='#27ae60')
        comp.resizable(False, False)
        x = (self.main_window.winfo_x() + self.main_window.winfo_width() // 2) - 250
        y = (self.main_window.winfo_y() + self.main_window.winfo_height() // 2) - 225
        comp.geometry(f"500x450+{x}+{y}")
        
        tk.Label(comp, text="🎉 GAME COMPLETE! 🎉", font=("Arial", 24, "bold"), fg='white', bg='#27ae60').pack(pady=(50, 20))
        total_votes = sum(sum(o['votes'] for o in c['options']) for c in self.data)
        stats = f"\n📊 YOUR GAMING SESSION\n\n• Categories completed: {len(self.data)}\n• Total votes cast: {total_votes}\n• Thank you for playing!\n\n🎮 What's Next?\n\nRun the Admin Program to:\n• View detailed voting results\n• Add more categories\n• See which options are most popular\n• Manage your game database\n\nWant to play again with different categories?\nThe Admin Panel lets you customize everything!"
        tk.Label(comp, text=stats, font=("Arial", 12), fg='white', bg='#27ae60', justify=tk.LEFT).pack(pady=20, padx=30)
        tk.Button(comp, text="🚪 Close Game", font=("Arial", 12, "bold"), fg='#27ae60', bg='white', activebackground='#ecf0f1', relief='flat', command=lambda: [comp.destroy(), self.main_window.destroy()], padx=30, pady=12).pack(pady=20)

if __name__ == "__main__":
    ProgramGUI()