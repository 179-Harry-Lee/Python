def sort_list_ascending():
    n = int(input("Nhập số phần tử của list: "))
    num_list = []
    
    for i in range(n):
        num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
        num_list.append(num)
    
    for i in range(n):
        for j in range(i+1, n):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    
    print("Các phần tử trong list sau khi được sắp xếp là:", num_list)

sort_list_ascending()