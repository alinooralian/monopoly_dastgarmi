import tkinter as tk
from landing import signin, login 

def signin_action():
    signin()
def login_action():
    login(1)
window = tk.Tk()
window.title("Monopoly")
window.geometry("300x250")  
window.configure(bg="#FFC0CB")
tk.Label(window, text="Monopoly Login", bg="#FFC0CB", font=("Arial", 14)).pack(pady=10)
tk.Button(window, text="Signup", command=signin_action, bg="#E05D9F", fg="black").pack(pady=5)
tk.Button(window, text="Login", command=login_action, bg="#E05D9F", fg="black").pack(pady=5)
tk.Button(window, text="Exit", command=window.destroy, bg="#E05D9F", fg="black").pack(pady=5)

window.mainloop()
