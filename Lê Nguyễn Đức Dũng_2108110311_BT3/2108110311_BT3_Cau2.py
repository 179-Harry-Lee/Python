def find_sum_number():
    n = int(input("Nhập số phần tử của list: "))
    num_list = []
    
    for i in range(n):
        num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
        num_list.append(num)
    
    sum_num = sum(num_list)
    print("Tổng các giá trị trong list là:", sum_num)

find_sum_number()