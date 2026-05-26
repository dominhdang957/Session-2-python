print("---- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

for i in range(1,4):
    print("----- Đang xử lý nhân viên số: ", i, "-----")
    working_days = int(input("Nhập số ngày công trong tháng: "))
    
    if working_days <= 0:
        print("Cảnh báo: Nhân viên nghỉ cả tháng không xét duyệt thưởng.")
    else:
        bonus_amount = working_days * 200000
        print("=" * 55)
        print("Đã gửi email: Chúc mừng nhận được ", bonus_amount , "VND tiền thưởng")
        print("=" * 55)

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!!")