import utils
from tkinter import messagebox

def login(username, password, on_success_callback):
    data = utils.read_data()
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            on_success_callback(user)
            return
    messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu!")

def get_balance(user):
    return f"Số dư: {user['balance']} VND"

def deposit(user, amount):
    user["balance"] += amount
    utils.write_data({"users": [user]})
    messagebox.showinfo("Thành công", f"Nạp thành công! Số dư mới: {user['balance']} VND")

def play_game(user, time_play):
    cost = time_play * 500
    if user["balance"] >= cost:
        user["balance"] -= cost
        utils.write_data({"users": [user]})
        messagebox.showinfo("Thành công", f"Đã trừ {cost} VND. Số dư còn lại: {user['balance']} VND.")
    else:
        messagebox.showerror("Lỗi", "Số dư không đủ!")
