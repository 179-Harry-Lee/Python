Ten = input("Bạn vui lòng cho biết họ tên: ")
NamSinh = int(input("Bạn sinh năm nào? "))
NamHienTai = 2024
Tuoi = NamHienTai - NamSinh
Tuoitrong3namtoi = Tuoi + 3
sinhvien = int(input("Bạn là sinh viên năm mấy? "))
namhocconlai = 4 - sinhvien

message = f"Chào bạn {Ten}, năm nay bạn {Tuoi} tuổi, {Tuoitrong3namtoi} tuổi sau 3 năm. Bạn là sinh viên năm {sinhvien}. Vậy là còn {namhocconlai} năm nữa là bạn sẽ tốt nghiệp"
print(message)