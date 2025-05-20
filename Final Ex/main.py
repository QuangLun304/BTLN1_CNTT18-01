import json
data_patch = "Final EX\data.json"




def kiem_tra_tinh_trang_file():
    file_status = {}
    try:
        with open(data_patch, 'r', encoding='utf-8') as f:
            file_status = json.load(f)
    except ValueError as e:
        print("Lỗi định dạng dữ liệu:", e)
    else:
        print("File đã nhận")




def doc_du_lieu():
    sinh_vien = {}
    try:
        with open(data_patch, 'r', encoding='utf-8') as f:
            sinh_vien = json.load(f)
    except ValueError as e:
        print("Lỗi định dạng dữ liệu:", e)
    else:
        print(sinh_vien)
    return sinh_vien


def them_lop():
    try:
        with open(data_patch, 'r', encoding='utf-8') as f:
            sinh_vien = json.load(f)
        ma_buoi_hoc = input("Nhập mã buổi học: ").strip()
    except ValueError:
        print("Giá trị không hợp lệ.")
        return
    buoi_hoc_moi = {
        ma_buoi_hoc: {

        }
    }
    sinh_vien.update(buoi_hoc_moi)
    with open(data_patch, 'w', encoding='utf-8') as f:
        json.dump(sinh_vien, f, ensure_ascii=False, indent=4)
    print("Thêm lớp thành công")



def them_sinh_vien():
    try:
        with open(data_patch, 'r', encoding='utf-8') as f:
            sinh_vien = json.load(f)
        ma_buoi_hoc = input("Nhập mã buổi học: ").strip()
        if ma_buoi_hoc not in sinh_vien:
            print("Mã buổi học không tồn tại.")
            return
        ma_sv = input("Nhập mã sinh viên: ").strip()
        ho_ten = input("Nhập họ tên sinh viên: ").strip()
        gioi_tinh = input("Nhập giới tính (Nam/Nữ): ").strip()
        ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ").strip()
        dia_chi = input("Nhập địa chỉ: ").strip()
        khoa = input("Nhập khoa: ").strip()
        tinh_trang = input("Nhập tình trạng điểm danh (Vắng/Có mặt/None): ").strip()
        so_tiet_nghi = int(input("Nhập số tiết nghỉ: ").strip())
    except ValueError:
        print("Giá trị không hợp lệ.")
        return
    sinh_vien_moi = {
        ma_sv: {
            "ho_ten": ho_ten,
            "ngay_sinh": ngay_sinh,
            "gioi_tinh": gioi_tinh,
            "dia_chi": dia_chi,
            "khoa": khoa,
            "tinh_trang": tinh_trang,
            "so_tiet_nghi": so_tiet_nghi
        }
    }
    sinh_vien[ma_buoi_hoc].update(sinh_vien_moi)
    with open(data_patch, 'w', encoding='utf-8') as f:
        json.dump(sinh_vien, f, ensure_ascii=False, indent=4)
    print("Thêm sinh viên thành công")




def sua_thong_tin_sinh_vien():
    try:
        with open(data_patch, 'r', encoding='utf-8') as f:
            sinh_vien = json.load(f)
        ma_sv = input("Nhập mã sinh viên cần sửa: ").strip()
        if ma_sv not in sinh_vien:
            print("Mã sinh viên không tồn tại.")
            return
        ho_ten = input("Nhập họ tên mới: ").strip()
        gioi_tinh = input("Nhập giới tính mới (Nam/Nữ): ").strip()
        ngay_sinh = input("Nhập ngày sinh mới (dd/mm/yyyy): ").strip()
        dia_chi = input("Nhập địa chỉ mới: ").strip()
        khoa = input("Nhập khoa mới: ").strip()
    except ValueError:
        print("Giá trị không hợp lệ.")
        return
    sinh_vien[ma_sv].update({
        "ho_ten": ho_ten,
        "ngay_sinh": ngay_sinh,
        "gioi_tinh": gioi_tinh,
        "dia_chi": dia_chi,
        "khoa": khoa,
    })
    with open(data_patch, 'w', encoding='utf-8') as f:
        json.dump(sinh_vien, f, ensure_ascii=False, indent=4)
    print("Sửa thông tin sinh viên thành công")



def cap_nhat_thong_tin_diem_danh():
    try:
        with open(data_patch, 'r', encoding='utf-8') as f:
            sinh_vien = json.load(f)
        ma_sv = input("Nhập mã sinh viên cần cập nhật: ").strip()
        if ma_sv not in sinh_vien:
            print("Mã sinh viên không tồn tại.")
            return
        tinh_trang = input("Nhập tình trạng điểm danh mới (Vắng/Có mặt): ").strip()
        so_tiet_nghi = int(input("Nhập số tiết nghỉ mới: ").strip())
    except ValueError:
        print("Giá trị không hợp lệ.")
        return
    sinh_vien[ma_sv].update({
        "tinh_trang": tinh_trang,
        "so_tiet_nghi": so_tiet_nghi
    })
    with open(data_patch, 'w', encoding='utf-8') as f:
        json.dump(sinh_vien, f, ensure_ascii=False, indent=4)
    print("Cập nhật thông tin điểm danh thành công")




def xoa_sinh_vien():
    try:
        with open(data_patch, 'r', encoding='utf-8') as f:
            sinh_vien = json.load(f)
        ma_sv = input("Nhập mã sinh viên cần xóa: ").strip()
        if ma_sv not in sinh_vien:
            print("Mã sinh viên không tồn tại.")
            return
    except ValueError:
        print("Giá trị không hợp lệ.")
        return
    del sinh_vien[ma_sv]
    with open(data_patch, 'w', encoding='utf-8') as f:
        json.dump(sinh_vien, f, ensure_ascii=False, indent=4)
    print("Xóa sinh viên thành công")




def hien_thi_danh_sach_sinh_vien():
    with open(data_patch, 'r', encoding='utf-8') as f:
        sinh_vien = json.load(f)
    print(f"|=========================================================   Danh sách sinh viên   =========================================================|")
    print(f"|{'Mã Học':<10}|{'Mã SV':<10}|{'Họ tên':<30}|{'Ngày sinh':<12}|{'Giới tính':<10}|{'Địa chỉ':<20}|{'Khoa':<15}|{'Tình trạng':<12}|{'Số tiết nghỉ':<12}|")
    print('-' * 141)
    for ma_buoi_hoc, danh_sach in sinh_vien.items():
        for ma_sv, info in danh_sach.items():
            print(f"|{ma_buoi_hoc:<10}|{ma_sv:<10}|{info['ho_ten']:<30}|{info['ngay_sinh']:<12}|{info['gioi_tinh']:<10}|{info['dia_chi']:<20}|{info['khoa']:<15}|{info['tinh_trang']:<12}|{info['so_tiet_nghi']:<12}|")




def hien_thi_danh_sach_sinh_vien_theo_lop():
    with open(data_patch, 'r', encoding='utf-8') as f:
        sinh_vien = json.load(f)
    khoa = input("Nhập tên lớp cần hiển thị: ").strip()
    print(f"=====================================================   Danh sách sinh viên   =====================================================")
    print(f"{'Mã SV':<10} {'Họ tên':<30} {'Ngày sinh':<12} {'Giới tính':<10} {'Địa chỉ':<20} {'Khoa':<15} {'Tình trạng':<12} {'Số tiết nghỉ':<5}")
    print('-' * 130)
    for ma_sv, info in sinh_vien.items():
        if info['khoa'] == khoa:
            print(f"{ma_sv:<10} {info['ho_ten']:<30} {info['ngay_sinh']:<12} {info['gioi_tinh']:<10} {info['dia_chi']:<20} {info['khoa']:<15} {info['tinh_trang']:<12} {info['so_tiet_nghi']:<5}")



def hien_thi_danh_sach_sinh_vien_theo_ma_buoi_hoc():
    with open(data_patch, 'r', encoding='utf-8') as f:
        sinh_vien = json.load(f)
    ma_buoi_hoc = input("Nhập mã buổi học: ").strip()
    print(f"|=========================================================   Danh sách sinh viên   =========================================================|")
    print(f"|{'Mã Học':<10}|{'Mã SV':<10}|{'Họ tên':<30}|{'Ngày sinh':<12}|{'Giới tính':<10}|{'Địa chỉ':<20}|{'Khoa':<15}|{'Tình trạng':<12}|{'Số tiết nghỉ':<12}|")
    print('-' * 141)
    for ma_sv, info in sinh_vien[ma_buoi_hoc].items():
        if ma_buoi_hoc in sinh_vien:
                print(f"|{ma_buoi_hoc:<10}|{ma_sv:<10}|{info['ho_ten']:<30}|{info['ngay_sinh']:<12}|{info['gioi_tinh']:<10}|{info['dia_chi']:<20}|{info['khoa']:<15}|{info['tinh_trang']:<12}|{info['so_tiet_nghi']:<12}|")




def hien_thi_danh_sach_sinh_vien_theo_tinh_trang():
    with open(data_patch, 'r', encoding='utf-8') as f:
        sinh_vien = json.load(f)
    tinh_trang = input("Nhập tình trạng điểm danh: ").strip()
    print(f"===================================================   Danh sách sinh viên lớp   ===================================================")
    print(f"{'Mã SV':<10} {'Họ tên':<30} {'Ngày sinh':<12} {'Giới tính':<10} {'Địa chỉ':<20} {'Khoa':<15} {'Tình trạng':<12} {'Số tiết nghỉ':<5}")
    print('-' * 130) 
    for ma_sv, info in sinh_vien.items():
        if info['tinh_trang'] == tinh_trang:
            print(f"{ma_sv:<10} {info['ho_ten']:<30} {info['ngay_sinh']:<12} {info['gioi_tinh']:<10} {info['dia_chi']:<20} {info['khoa']:<15} {info['tinh_trang']:<12} {info['so_tiet_nghi']:<5}")



def tim_Kiem_sinh_vien_theo_ma_sinh_vien():
    print()



if __name__ == "__main__":
    sinh_vien = {}
    while True:
        print("""
            ======================== QUẢN LÝ ĐIỂM DANH SINH VIÊN ========================
            1. Kiểm tra tình trạng file data
            2. Đọc dữ liệu từ file
            3. Thêm lớp
            4. Thêm sinh viên
            5. Sửa thông tin sinh viên
            6. Cập nhập thông tin điểm danh
            7. Xóa sinh viên
            8. Hiển thị danh sách sinh viên
            9. Hiển thị danh sách sinh viên theo lớp
            10. Hiển thị danh sách sinh viên theo mã buổi học
            11. Hiển thị danh sách sinh viên theo tình trạng điểm danh
            12. Tìm kiếm sinh viên theo mã sinh viên
            13. Tìm kiếm sinh viên theo tên
            14. Hiển thị danh sách sinh viên đang trong tình trạng cấm thi
            15. Hiển thị danh sách sinh viên theo số tiết nghỉ
            16. 
            =============================================================================
            """)
        choice = input("Nhập lựa chọn của bạn: ").strip()
        if choice == '1':
            file_status = kiem_tra_tinh_trang_file()
        elif choice == '2':
            sinh_vien = doc_du_lieu()
        elif choice == '3':
            sinh_vien = them_lop()
        elif choice == '4':
            sinh_vien = them_sinh_vien()
        elif choice == '5':
            sinh_vien = sua_thong_tin_sinh_vien()
        elif choice == '6':
            sinh_vien = cap_nhat_thong_tin_diem_danh()
        elif choice == '7':
            sinh_vien = xoa_sinh_vien()
        elif choice == '8':
            sinh_vien = hien_thi_danh_sach_sinh_vien()
        elif choice == '9':
            sinh_vien = hien_thi_danh_sach_sinh_vien_theo_lop()
        elif choice == '10':
            sinh_vien = hien_thi_danh_sach_sinh_vien_theo_ma_buoi_hoc()
        elif choice == '11':
            sinh_vien = hien_thi_danh_sach_sinh_vien_theo_tinh_trang()
        elif choice == '12':
            sinh_vien = tim_Kiem_sinh_vien_theo_ma_sinh_vien()