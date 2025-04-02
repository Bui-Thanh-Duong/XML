import json

def read_data():
    # Đọc dữ liệu từ file data.json
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)

def write_data(data):
    # Đọc dữ liệu hiện tại từ file
    current_data = read_data()

    # Cập nhật các phần dữ liệu cần thiết (ở đây là chỉ cập nhật users)
    if "users" in data:
        current_data["users"] = data["users"]
    if "rooms" in data:
        current_data["rooms"] = data["rooms"]
    if "employees" in data:
        current_data["employees"] = data["employees"]
    if "admin" in data:
        current_data["admin"] = data["admin"]

    # Ghi lại toàn bộ dữ liệu vào file
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(current_data, file, ensure_ascii=False, indent=4)
