

print("===== CÂU 1: TÍNH TIỀN THANH TOÁN =====")

price = float(input("Nhập đơn giá sản phẩm: "))
quantity = int(input("Nhập số lượng mua: "))

total = price * quantity

if total >= 1000000:
    sale_off = toltal * 0.1
    pay = total - sale_off
    print("Khách hàng được giảm giá 10%")
else:
    sale_off = 0
    pay = total
    print("Không được giảm giá")

print("Tổng tiền ban đầu:", total)
print("Số tiền giảm:", sale_off)
print("Số tiền phải thanh toán:", pay)



print("\n===== CÂU 2: HỆ THỐNG ĐĂNG NHẬP =====")

password = "123456"
wrongs = 0

while wrongs_time < 3:
    password = input("Nhập mật khẩu: ")

    if password == right_password:
        print("Đăng nhập thành công!")
        break
    else:
        wrongs_time += 1
        print("Mật khẩu sai, vui lòng nhập lại!")
        print("Số lần nhập sai còn lại:", 3 - so_lan_sai)

if wrongs_time == 3:
    print("Tài khoản đã bị khóa!")



print("\n===== CÂU 3: THỐNG KÊ LÔ HÀNG =====")

total = 0
valid_bin_number = 0

while True:
    quantity = int(input("Nhập số lượng sản phẩm của thùng: "))

    if quantity < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")

    elif quantity == 0:
        print("Kết thúc kiểm đếm!")
        break

    else:
        total += quantity
        valid_bin_number += 1
        print("Đã thêm", so_luong, "sản phẩm vào hệ thống")
        break

print("\n===== KẾT QUẢ THỐNG KÊ =====")
print("Tổng số thùng hàng hợp lệ đã đếm:", so_thung_hop_le)
print("Tổng số lượng sản phẩm thu được:", tong_san_pham)
