import tkinter as tk
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file is None:
        return
    text = entry.get("1.0", tk.END)  
    file.write(text)
    file.close()

def openfile():
    file = filedialog.askopenfile(mode="r", filetypes=[("Text Files", "*.txt")])
    if file is not None:
        cont = file.read()
        entry.delete("1.0", tk.END) 
        entry.insert("1.0", cont) 

root = tk.Tk()
root.title("NOTEPAD")
root.geometry("500x500")
root.config(bg="lightgray")

button1 = tk.Button(root, text="Save File", padx=50, pady=40, command=savefile)
button1.place(x=62, y=30)

button2 = tk.Button(root, text="Open File", padx=50, pady=40, command=openfile)
button2.place(x=280, y=30)

entry = tk.Text(root, height=20, width=60, wrap="word")
entry.place(x=10, y=150)

root.mainloop()