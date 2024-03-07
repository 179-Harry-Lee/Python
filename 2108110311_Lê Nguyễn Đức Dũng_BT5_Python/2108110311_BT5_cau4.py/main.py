# main.py
from student import *

menu = """
1. Thêm sinh viên
2. Xóa sinh viên
3. Sửa sinh viên
4. In danh sách sinh viên
5. Quay lại trang chủ
"""

while True:
    print(menu)
    choice = input("Chọn một chức năng: ")
    if choice == "1":
        name = input("Họ tên: ")
        id = input("Mã sinh viên: ")
        add_student(name, id)
    elif choice == "2":
        id = input("Mã sinh viên cần xóa: ")
        remove_student(id)
    elif choice == "3":
        id = input("Mã sinh viên cần sửa: ")
        name = input("Họ tên mới: ")
        edit_student(id, name)
    elif choice == "4":
        print_students()
    elif choice == "5":
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")