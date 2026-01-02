import tkinter as tk
from landing import signin, login

def signin_action():
    signin()
def login_action():
    login(1)

window = tk.Tk()
window.title("Monopoly")
window.geometry("300x250")
window.configure(bg="#FFDDEE")

tk.Label(
    window, 
    text="Monopoly Login", 
    bg="#FFDDEE", 
    fg="#FF69B4", 
    font=("Comic Sans MS", 16, "bold")
).pack(pady=15)

button_style = {
    "width": 15,
    "height": 2,
    "bg": "#FF99CC",
    "fg": "white",
    "font": ("Comic Sans MS", 12, "bold"),
    "relief": "raised",
    "bd": 3
}

tk.Button(window, text="Signup", command=signin_action, **button_style).pack(pady=5)
tk.Button(window, text="Login", command=login_action, **button_style).pack(pady=5)
tk.Button(window, text="Exit", command=window.destroy, **button_style).pack(pady=5)

window.mainloop()
