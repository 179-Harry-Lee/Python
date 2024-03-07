a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

if a > b:
    print("Không hợp lệ! a phải nhỏ hơn b.")
else:
    tong = 0
    for num in range(a, b + 1):
        tong += num

    print("Tổng các số nguyên từ", a, "đến", b, "là:", tong)