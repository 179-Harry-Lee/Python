#Su dung ham lamda
lst = [10,7,6,9,12,4,5,2,15]





#Su dung ham thong thuong
def lst_de1():
    lst = [10,7,6,9,12,4,5,2,15]
    lst_1 = []
    for i in lst:
        if i%2 != 0:
            lst_1.append(i)
        print("List số lẽ trong list: ",lst_1)
lst_de1()


def lst_de2():
    lst_1 = [lst_1]
    lst_2 = []

    for i in lst_1:
        j = i*2
        lst_2.append(j)
    print("List các số lẻ nhân đôi của list: ",lst_2)

lst_de2()
        

    
