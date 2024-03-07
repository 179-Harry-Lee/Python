def find_min_number():
    n = int(input("Nhập số phần tử của list: "))
    num_list = []
    
    for i in range(n):
        num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
        num_list.append(num)
    
    min_num = min(num_list)
    print("Số nhỏ nhất trong list là:", min_num)

find_min_number()