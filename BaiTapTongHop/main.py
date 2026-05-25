

print("=" * 55)
print("     HỆ THỐNG ĐÁNH GIÁ NHANH TÌNH TRẠNG BỆNH NHÂN")
print("=" * 55)

patient_name    = input("Tên bệnh nhân          : ")
birth_year      = int(input("Năm sinh               : "))
sick_days       = int(input("Số ngày bị bệnh        : "))
body_temp       = float(input("Nhiệt độ cơ thể (°C)   : "))
exam_cost       = float(input("Chi phí khám (VNĐ)     : "))

from datetime import datetime

current_year = datetime.now().year

is_valid = True
error_message = ""

if len(patient_name) == 0:
    is_valid = False
    error_message = "Tên bệnh nhân không được để trống."
elif birth_year < 1900 or birth_year > current_year:
    is_valid = False
    error_message = f"Năm sinh phải nằm trong khoảng 1900 đến {current_year}."
elif sick_days < 0:
    is_valid = False
    error_message = "Số ngày bị bệnh phải lớn hơn hoặc bằng 0."
elif body_temp < 30 or body_temp > 45:
    is_valid = False
    error_message = "Nhiệt độ cơ thể phải nằm trong khoảng 30°C đến 45°C."
elif exam_cost <= 0:
    is_valid = False
    error_message = "Chi phí khám phải lớn hơn 0."

if not is_valid:
    print("\n" + "=" * 55)
    print(f"LỖI: {error_message}")
    print("Chương trình kết thúc.")
    print("=" * 55)
else:
    patient_age  = current_year - birth_year
    surcharge    = exam_cost * 0.1
    total_cost   = exam_cost + surcharge

    if body_temp > 38 and sick_days > 3:
        health_status = "Nguy hiểm"
    elif body_temp > 38:
        health_status = "Sốt cao"
    elif body_temp > 37.5:
        health_status = "Sốt nhẹ"
    else:
        health_status = "Bình thường"

    if health_status == "Nguy hiểm":
        if patient_age > 60:
            priority_level = "Cấp cứu"
        else:
            priority_level = "Ưu tiên cao"
    else:
        priority_level = "Bình thường"

    cost_level = "Cao" if total_cost > 500000 else "Thấp"

    print("\n" + "=" * 55)
    print("              KẾT QUẢ ĐÁNH GIÁ BỆNH NHÂN")
    print("=" * 55)
    print(f"  Họ và tên       : {patient_name.strip()}")
    print(f"  Năm sinh        : {birth_year}")
    print(f"  Tuổi            : {patient_age}")
    print(f"  Số ngày bệnh    : {sick_days} ngày")
    print(f"  Nhiệt độ        : {body_temp}°C")
    print("-" * 55)
    print(f"  Chi phí khám    : {exam_cost:,.0f} VNĐ")
    print(f"  Phụ phí (10%)   : {surcharge:,.0f} VNĐ")
    print(f"  Tổng chi phí    : {total_cost:,.0f} VNĐ")
    print(f"  Mức chi phí     : {cost_level}")
    print("-" * 55)
    print(f"  Tình trạng      : {health_status}")
    print(f"  Mức độ ưu tiên  : {priority_level}")
    print("=" * 55)