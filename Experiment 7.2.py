import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    game TEXT NOT NULL
)
""")
conn.commit()

def submit_data():
    name = name_entry.get()
    branch = branch_entry.get()
    game = game_entry.get()

    if name == "" or branch == "" or game == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    cursor.execute("INSERT INTO students (name, branch, game) VALUES (?, ?, ?)",
                   (name, branch, game))
    conn.commit()

    messagebox.showinfo("Success", "Record Saved Successfully!")

    name_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    game_entry.delete(0, tk.END)

def view_records():
    view_window = tk.Toplevel(root)
    view_window.title("Saved Student Records")
    view_window.geometry("500x300")

    tree = ttk.Treeview(view_window, columns=("Name", "Branch", "Game"), show="headings")

    tree.heading("Name", text="Name")
    tree.heading("Branch", text="Branch")
    tree.heading("Game", text="Favorite Game")

    tree.pack(fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(view_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    cursor.execute("SELECT name, branch, game FROM students")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


root = tk.Tk()
root.title("Spandan Student Registration Form")
root.geometry("400x300")

name_label = tk.Label(root, text="Student Name")
name_label.pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

branch_label = tk.Label(root, text="Branch")
branch_label.pack(pady=5)

branch_entry = tk.Entry(root)
branch_entry.pack(pady=5)


game_label = tk.Label(root, text="Favorite Game")
game_label.pack(pady=5)


game_entry = tk.Entry(root)
game_entry.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.pack(pady=10)

view_btn = tk.Button(root, text="View Records", command=view_records)
view_btn.pack(pady=10)

root.mainloop()

conn.close()