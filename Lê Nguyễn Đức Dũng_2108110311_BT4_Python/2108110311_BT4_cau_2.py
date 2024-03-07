
## Su dung lamda
lst = [10,7,6,9,12,4,5,2,15]

new_lst = list(filter(lambda a:(a%2==0) and (a%3==0),lst))
print("List số chia hết cho 2 và 3 là:",new_lst)




# Su dung ham thong thuong

# def lst_chia23():
#     lst = [10,7,6,9,12,4,5,2,15]
#     new_lst = []
#     for i in lst:
#         if i % 2 == 0 and i % 3 == 0:
#             new_lst.append(i)
#         print("List số chia hết cho 2 và 3 là:",new_lst)
# lst_chia23()



