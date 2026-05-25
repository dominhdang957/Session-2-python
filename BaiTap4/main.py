print("=" * 55)
print("     HỆ THỐNG DUYỆT ĐIỀU KIỆN PHẪU THUẬT")
print("=" * 55)


age        = int(input("Nhập tuổi bệnh nhân (Age)              : "))
blood_pressure    = int(input("Nhập huyết áp tâm thu (mmHg)           : "))
blood_sugar = int(input("Nhập đường huyết (mg/dL)               : "))

print("-" * 55)

if age < 75:
    if 90 <= blood_pressure <= 140:
        if blood_sugar < 150:
            print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        else:
            print("TỪ CHỐI: Đường huyết vượt ngưỡng.")
    else:
        print("TỪ CHỐI: Huyết áp ngoài giới hạn an toàn.")
else:
    print("TỪ CHỐI: Tuổi vượt giới hạn phẫu thuật.")