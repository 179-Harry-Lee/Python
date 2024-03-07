mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu", "Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi", "Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi", "Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu", "Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "42000","Published_Year": "2013"}, 
{"Title": "App Inventor", "Author": "Man Nhi", "Publisher": "LD", "Price": "30000","Published_Year": "2015"}, ]


search_choose = input("Chon tuy chon tim kiem: 1.Title, 2.Author, 3. Publisher: ")

search_item = input("Chon ky tu muon tim kiem:")


def kqsearch(search_choose,search_item):
    ketqua = []
    if search_choose == "1" :
            for sach in mybooks:
                    if search_item in sach["title"]:
                            ketqua.append(sach)
    elif search_choose == "2" :
            for sach in mybooks:
                    if search_item in sach["Author"]:
                            ketqua.append(sach)

    elif search_choose == "3" :
            for sach in mybooks:
                    if search_item in sach["Publisher"]:
                            ketqua.append(sach)

    return ketqua


ketqua = kqsearch(search_choose, search_item)

if ketqua:
            print("Kết quả",search_item,":")
            for kq in ketqua:
                print(kq)
else:
            print("Khong tim thay ket qua")


