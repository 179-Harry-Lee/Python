user_dict = {
    "user1": "123456",
    "user2": "123456",
    "user3": "123456",
    "user4": "123456",
    "user5": "123456",
    "user6": "123456",
    "user7": "123456",
    "user8": "123456",
    "user9": "123456",
    "user10": "123456"
}

def login_system():
    username = input("Nhập vào username: ")
    password = input("Nhập vào password: ")
    
    if username not in user_dict:
        print("USER NAME KHÔNG TỒN TẠI")
    elif user_dict[username] != password:
        print("PASSWORD SAI")
    else:
        print("LOGIN THÀNH CÔNG")

login_system()