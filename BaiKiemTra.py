

print("===== CÂU 1: TÍNH TIỀN THANH TOÁN =====")

don_gia = float(input("Nhập đơn giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))

tong_tien = don_gia * so_luong

if tong_tien >= 1000000:
    giam_gia = tong_tien * 0.1
    thanh_toan = tong_tien - giam_gia
    print("Khách hàng được giảm giá 10%")
else:
    giam_gia = 0
    thanh_toan = tong_tien
    print("Không được giảm giá")

print("Tổng tiền ban đầu:", tong_tien)
print("Số tiền giảm:", giam_gia)
print("Số tiền phải thanh toán:", thanh_toan)



print("\n===== CÂU 2: HỆ THỐNG ĐĂNG NHẬP =====")

mat_khau_dung = "123456"
so_lan_sai = 0

while so_lan_sai < 3:
    mat_khau = input("Nhập mật khẩu: ")

    if mat_khau == mat_khau_dung:
        print("Đăng nhập thành công!")
        break
    else:
        so_lan_sai += 1
        print("Mật khẩu sai, vui lòng nhập lại!")
        print("Số lần nhập sai còn lại:", 3 - so_lan_sai)

if so_lan_sai == 3:
    print("Tài khoản đã bị khóa!")



print("\n===== CÂU 3: THỐNG KÊ LÔ HÀNG =====")

tong_san_pham = 0
so_thung_hop_le = 0

while True:
    so_luong = int(input("Nhập số lượng sản phẩm của thùng: "))

    if so_luong < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")

    elif so_luong == 0:
        print("Kết thúc kiểm đếm!")
        break

    else:
        tong_san_pham += so_luong
        so_thung_hop_le += 1
        print("Đã thêm", so_luong, "sản phẩm vào hệ thống")

print("\n===== KẾT QUẢ THỐNG KÊ =====")
print("Tổng số thùng hàng hợp lệ đã đếm:", so_thung_hop_le)
print("Tổng số lượng sản phẩm thu được:", tong_san_pham)
