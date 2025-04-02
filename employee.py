import utils
from tkinter import messagebox

def login(username, password, on_success_callback):
    data = utils.read_data()
    for emp in data["employees"]:
        if emp["username"] == username and emp["password"] == password:
            on_success_callback()
            return
    messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu!")

def get_computer_list():
    data = utils.read_data()
    computers = []
    for room in data["rooms"]:
        for comp in room["computers"]:
            computers.append(f"Phòng {room['roomID']} - Máy {comp['computerID']} - {comp['status']}")
    return computers

def report_issue(room_id, comp_id):
    data = utils.read_data()
    for room in data["rooms"]:
        if room["roomID"] == room_id:
            for comp in room["computers"]:
                if comp["computerID"] == comp_id:
                    comp["status"] = "Bị lỗi"
                    utils.write_data(data)
                    messagebox.showinfo("Thành công", "Báo cáo lỗi thành công!")
                    return
    messagebox.showerror("Lỗi", "Không tìm thấy máy!")
