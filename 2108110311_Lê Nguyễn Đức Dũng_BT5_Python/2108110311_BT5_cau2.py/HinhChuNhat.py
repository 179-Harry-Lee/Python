import Xulydulieu

dai = float(input("Nhập vào chiều dài của hcn: "))
rong = float(input("Nhập vào chiều rộng của hcn: "))
             

chuvihcn = Xulydulieu.chuvi(dai,rong)

dientichhcn = Xulydulieu.dientich(dai,rong)


print("Chu vi hình chữ nhật là: ", chuvihcn)
print("Dien tich Hình chữ nhật là: ",dientichhcn)