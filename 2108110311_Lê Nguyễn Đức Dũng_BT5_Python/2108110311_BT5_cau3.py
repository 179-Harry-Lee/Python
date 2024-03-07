

students = [
    {
        "MSSV": "2108110311",
        "name": "Lê Nguyễn Đức Dũng",
        "year": "2003",
        "major": "Kỹ Thuật lập trình"
    },

    {
        "MSSV": "2108110336",
        "name": "Trần Minh Quân",
        "year": "2003",
        "major": "An ninh mạng"
    },

    {
        "MSSV": "2108110233",
        "name": "Bùi Thuân Tình",
        "year": "2003",
        "major": "Đa cấp"
    }
]


def add():
    new_student = {
        "MSSV": input("Nhập mã số sinh viên: "),
        "name": input("Nhập tên: "),
        "year": input("Nhập năm sinh: "),
        "major": input("Nhập chuyên ngành: ")
    }
    students.append(new_student)
    print("Thêm thành công!")


def delete():
    student_id = input("Nhập mã số sinh viên: ")
    for i in range(len(students)):
        if students[i]["MSSV"] == student_id:
            del students[i]
            print("Xóa thành công!")
            break
    else:
        print("Không tìm thấy số sinh viên này!")


def edit():
    student_id = input("Nhập mã số sinh viên: ")
    for i in range(len(students)):
        if students[i]["MSSV"] == student_id:
            students[i]["name"] = input("Nhập tên: ")
            students[i]["year"] = input("Nhập năm sinh: ")
            students[i]["major"] = input("Nhập chuyên ngành: ")
            print("Sửa thành công!")
            break
    else:
        print("Không tìm thấy số sinh viên này!")


def view_student():
    for student in students:
        print(f"{student['MSSV']}. {student['name']}, {student['year']}, {student['major']}")



def trangchu():
    while True:
        print(" Chức năng quản lý sinh viên")
        print(" 1.Chức năng Thêm sinh viên")
        print(" 2.Chức năng Xóa sinh viên")
        print(" 3.Chức năng Sửa sinh viên")
        print(" 4.Chức năng Xuất danh sách sinh viên")
        print(" 5.Thoát")


        choose = input("Chọn một chức năng sinh viên: ")
        if choose == "1":
            add()
        elif choose == "2":
            delete()
        elif choose == "3":
            edit()
        elif choose == "4":
            view_student()
        elif choose == "5":
            break
        else: 
            print("Chức năng ko tồn tại")

if __name__ =="__main__":
    trangchu()