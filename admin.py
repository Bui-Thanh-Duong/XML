import utils
from tkinter import messagebox

def login(username, password, on_success_callback):
    data = utils.read_data()
    if data["admin"]["username"] == username and data["admin"]["password"] == password:
        on_success_callback()  # Chạy giao diện admin
    else:
        messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu!")

def get_employees():
    data = utils.read_data()
    return [f"Tên: {emp['fullName']} - SĐT: {emp['phone']}" for emp in data["employees"]]

def get_revenue():
    data = utils.read_data()
    total_revenue = sum(user["balance"] for user in data["users"])
    return f"Tổng doanh thu: {total_revenue} VND"
