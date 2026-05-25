

print("=" * 55)
print("   HỆ THỐNG TIẾP NHẬN VÀ PHÂN LUỒNG BỆNH NHÂN")
print("=" * 55)


full_name = input("Nhập họ và tên bệnh nhân : ")
age   = int(input("Nhập tuổi bệnh nhân      : "))




if len(full_name) == 0:
    print("LỖI: Tên không hợp lệ!")

elif age < 0 or age > 150:
    print("LỖI: Tuổi nằm ngoài phạm vi con người (0-150)!")
else:
    if age < 6:
        result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif age >= 80:
        result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    # ── BƯỚC 4: IN PHIẾU KHÁM BỆNH ──────────────────────────
    print("\n" + "=" * 55)
    print("         PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print("=" * 55)
    print(f"  Họ và tên : {full_name}")
    print(f"  Tuổi      : {age}")
    print("-" * 55)
    print(f"  Phân luồng: {result}")
    print("=" * 55)