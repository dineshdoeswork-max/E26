
import tkinter as tk

def on_click(button_text):
    current = entry.get()

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END) 
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif button_text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("The Dinesh Calculator")
root.geometry("300x250")

entry = tk.Entry(root, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
row_val = 1
col_val = 0

for btn in buttons:
    action = lambda x=btn: on_click(x)

    tk.Button(root,text=btn,width=5,height=2,command=action).grid(row=row_val, column=col_val)

    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
