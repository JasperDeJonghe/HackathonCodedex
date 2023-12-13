import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Christmas Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=20, font=('Helvetica', 14))
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 14),
                       bg='#c71e1e', fg='white',  
                       command=lambda value=text: click_button(value) if value != "=" else calculate())
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

clear_button = tk.Button(root, text="C", padx=20, pady=20, font=('Helvetica', 14),
                         bg='#38761d', fg='white',  # Green background with white text
                         command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=3, sticky='nsew', pady=5)


root.configure(bg="#ffe4e1")

root.mainloop()
