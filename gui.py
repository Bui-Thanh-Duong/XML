import tkinter as tk
from tkinter import messagebox
import admin, employee, player

def run_app():
    root = tk.Tk()
    root.title("Hệ thống quản lý phòng net")
    root.geometry("800x600")

    main_frame = tk.Frame(root)
    main_frame.pack()
    
    def show_main_menu():
        main_frame.pack()
    
    def hide_main_menu():
        main_frame.pack_forget()
    
    def open_login(user_type):
        hide_main_menu()
        login_window = tk.Toplevel(root)
        login_window.title(f"Đăng nhập {user_type}")
        login_window.geometry("400x300")
        
        tk.Label(login_window, text="Tên đăng nhập:", font=("Arial", 12)).pack(pady=5)
        entry_username = tk.Entry(login_window, font=("Arial", 12), width=25)
        entry_username.pack(pady=5)
        
        tk.Label(login_window, text="Mật khẩu:", font=("Arial", 12)).pack(pady=5)
        entry_password = tk.Entry(login_window, show="*", font=("Arial", 12), width=25)
        entry_password.pack(pady=5)
        
        def on_login():
            username = entry_username.get()
            password = entry_password.get()
            if user_type == "Admin":
                admin.login(username, password, lambda: open_admin_menu(login_window))
            elif user_type == "Nhân viên":
                employee.login(username, password, lambda: open_employee_menu(login_window))
            elif user_type == "Người chơi":
                player.login(username, password, lambda user: open_player_menu(login_window, user))
        
        tk.Button(login_window, text="Đăng nhập", font=("Arial", 12), padx=20, pady=10, command=on_login).pack(pady=10)
    
    def open_admin_menu(parent):
        parent.destroy()
        admin_window = tk.Toplevel(root)
        admin_window.title("Quản trị viên")
        admin_window.geometry("600x400")
        
        tk.Label(admin_window, text="Menu quản trị viên", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(admin_window, text="Xem danh sách nhân viên", font=("Arial", 12), command=lambda: messagebox.showinfo("Nhân viên", "\n".join(admin.get_employees()))).pack(pady=5)
        tk.Button(admin_window, text="Xem doanh thu", font=("Arial", 12), command=lambda: messagebox.showinfo("Doanh thu", admin.get_revenue())).pack(pady=5)
        tk.Button(admin_window, text="Đăng xuất", font=("Arial", 12), command=lambda: [admin_window.destroy(), show_main_menu()]).pack(pady=20)
    
    def open_employee_menu(parent):
        parent.destroy()
        emp_window = tk.Toplevel(root)
        emp_window.title("Nhân viên")
        emp_window.geometry("600x400")
        
        tk.Label(emp_window, text="Menu nhân viên", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Thêm nút để xem danh sách máy
        tk.Button(emp_window, text="Xem danh sách máy", font=("Arial", 12), command=lambda: messagebox.showinfo("Danh sách máy", "\n".join(employee.get_computer_list()))).pack(pady=5)
        
        # Thêm phần báo cáo lỗi
        tk.Button(emp_window, text="Báo cáo lỗi", font=("Arial", 12), command=lambda: report_issue_window(emp_window)).pack(pady=5)
        
        # Đăng xuất
        tk.Button(emp_window, text="Đăng xuất", font=("Arial", 12), command=lambda: [emp_window.destroy(), show_main_menu()]).pack(pady=20)

    def report_issue_window(parent):
        # Tạo cửa sổ mới để báo cáo lỗi
        report_window = tk.Toplevel(parent)
        report_window.title("Báo cáo lỗi")
        report_window.geometry("400x300")
        
        tk.Label(report_window, text="Mã phòng:", font=("Arial", 12)).pack(pady=5)
        entry_room_code = tk.Entry(report_window, font=("Arial", 12), width=25)
        entry_room_code.pack(pady=5)

        tk.Label(report_window, text="Mã máy:", font=("Arial", 12)).pack(pady=5)
        entry_computer_code = tk.Entry(report_window, font=("Arial", 12), width=25)
        entry_computer_code.pack(pady=5)
        
        # Thêm nút để gửi báo cáo lỗi
        def submit_report():
            room_code = entry_room_code.get()
            computer_code = entry_computer_code.get()
            if not room_code or not computer_code:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ mã phòng và mã máy.")
            else:
                # Gọi hàm báo cáo lỗi với mã phòng và mã máy
                employee.report_issue(room_code, computer_code)
                messagebox.showinfo("Thông báo", "Báo cáo lỗi thành công!")
                report_window.destroy()
        
        tk.Button(report_window, text="Báo cáo lỗi", font=("Arial", 12), command=submit_report).pack(pady=10)

    def open_player_menu(parent, user):
        parent.destroy()
        player_window = tk.Toplevel(root)
        player_window.title("Người chơi")
        player_window.geometry("600x400")
        
        tk.Label(player_window, text="Menu người chơi", font=("Arial", 14, "bold")).pack(pady=10)

        # Xem số dư
        tk.Button(player_window, text="Xem số dư", font=("Arial", 12), command=lambda: messagebox.showinfo("Số dư", player.get_balance(user))).pack(pady=5)
        
        # Nạp tiền
        tk.Button(player_window, text="Nạp tiền", font=("Arial", 12), command=lambda: deposit_money_window(player_window, user)).pack(pady=5)

        # Chơi game
        tk.Button(player_window, text="Chơi game", font=("Arial", 12), command=lambda: play_game_window(player_window, user)).pack(pady=5)

        # Đăng xuất
        tk.Button(player_window, text="Đăng xuất", font=("Arial", 12), command=lambda: [player_window.destroy(), show_main_menu()]).pack(pady=20)

    def deposit_money_window(parent, user):
        # Cửa sổ nạp tiền
        deposit_window = tk.Toplevel(parent)
        deposit_window.title("Nạp tiền")
        deposit_window.geometry("400x300")
        
        tk.Label(deposit_window, text="Số tiền cần nạp (VND):", font=("Arial", 12)).pack(pady=5)
        entry_deposit = tk.Entry(deposit_window, font=("Arial", 12), width=25)
        entry_deposit.pack(pady=5)
        
        # Nút nạp tiền
        def submit_deposit():
            try:
                deposit_amount = int(entry_deposit.get())
                if deposit_amount <= 0:
                    messagebox.showerror("Lỗi", "Số tiền phải lớn hơn 0.")
                else:
                    player.deposit(user, deposit_amount)
                    messagebox.showinfo("Thông báo", f"Nạp tiền thành công {deposit_amount} VND.")
                    deposit_window.destroy()
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ.")
        
        tk.Button(deposit_window, text="Nạp tiền", font=("Arial", 12), command=submit_deposit).pack(pady=10)

    def play_game_window(parent, user):
        # Cửa sổ chơi game
        play_game_window = tk.Toplevel(parent)
        play_game_window.title("Chơi game")
        play_game_window.geometry("400x300")
        
        tk.Label(play_game_window, text="Số phút chơi:", font=("Arial", 12)).pack(pady=5)
        entry_play_time = tk.Entry(play_game_window, font=("Arial", 12), width=25)
        entry_play_time.pack(pady=5)

        # Nút chơi game
        def submit_play_game():
            try:
                play_minutes = int(entry_play_time.get())
                if play_minutes <= 0:
                    messagebox.showerror("Lỗi", "Số phút chơi phải lớn hơn 0.")
                else:
                    player.play_game(user, play_minutes)
                    messagebox.showinfo("Thông báo", f"Chơi game thành công trong {play_minutes} phút.")
                    play_game_window.destroy()
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ.")
        
        tk.Button(play_game_window, text="Chơi game", font=("Arial", 12), command=submit_play_game).pack(pady=10)
    
    tk.Label(main_frame, text="Hệ thống quản lý phòng net", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Button(main_frame, text="Đăng nhập người chơi", font=("Arial", 14), padx=20, pady=10, command=lambda: open_login("Người chơi")).pack(pady=5)
    tk.Button(main_frame, text="Đăng nhập nhân viên", font=("Arial", 14), padx=20, pady=10, command=lambda: open_login("Nhân viên")).pack(pady=5)
    tk.Button(main_frame, text="Đăng nhập quản trị viên", font=("Arial", 14), padx=20, pady=10, command=lambda: open_login("Admin")).pack(pady=5)
    tk.Button(main_frame, text="Thoát", font=("Arial", 14), padx=20, pady=10, command=root.quit).pack(pady=20)
    
    root.mainloop()
