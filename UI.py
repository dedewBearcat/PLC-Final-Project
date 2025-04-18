import tkinter as tk
from tkinter import filedialog, messagebox
import encrypt
import decrypt

def browseFile(): #handle file selection 
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        filePath.set(filepath)

def handleEncrypt(): #handles running encrypt module
    path = filePath.get()
    seed = seedEntry.get().strip() or None
    if not path:
        messagebox.showerror("No File", "Please select a text file to encrypt.")
        return
    result = encrypt.__encrypt(path, seed)
    openResultWindow(result)

def handleDecrypt(): #handles running decrypt module
    path = filePath.get()
    seed = seedEntry.get().strip() or None
    if not path:
        messagebox.showerror("No File", "Please select a text file to decrypt.")
        return
    result = decrypt.__decrypt(path, seed)
    openResultWindow(result)

def openResultWindow(result): #handles opening results window
    new_window = tk.Toplevel(root)
    new_window.title("Result")
    new_window.geometry("700x70")
    
    label = tk.Label(new_window, text=result)
    label.pack(pady=20)

root = tk.Tk() 
root.title("Andrew's Encryption/Decryption Program")
root.geometry("400x250")

filePath = tk.StringVar()

tk.Label(root, text="Select Text File:").pack(pady = (10, 0))
tk.Entry(root, textvariable = filePath, width = 50).pack(padx = 10)
tk.Button(root, text="Browse", command = browseFile).pack(pady = 5)

tk.Label(root, text="Optional Seeder:").pack(pady = 5)
seedEntry = tk.Entry(root, width = 20)
seedEntry.pack(pady = 5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady = 10)

tk.Button(root, text = "Encrypt File", command = handleEncrypt, bg = "pink").pack(pady = 5)
tk.Button(root, text = "Decrypt File", command = handleDecrypt, bg = "lightgreen").pack(pady = 5)

root.mainloop()