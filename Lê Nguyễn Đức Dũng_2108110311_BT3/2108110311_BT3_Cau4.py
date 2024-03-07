def filter_odd_numbers():
    n = int(input("Nhập vào phần tử của list: "))
    num_list = []
    
    for i in range(n):
        num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
        num_list.append(num)
    
    odd_numbers = [num for num in num_list if num % 2 != 0]
    
    print("Các số lẻ có trong list vừa nhập là:", odd_numbers)

filter_odd_numbers()