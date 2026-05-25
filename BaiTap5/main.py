

print("=" * 60)
print("      CHÀO MỪNG ĐẾN VỚI KIOSK TIẾP NHẬN BỆNH NHÂN")
print("      Vui lòng điền đầy đủ thông tin theo hướng dẫn.")
print("=" * 60)



patient_name = input("Nhập Họ và tên bệnh nhân: ")

patient_age = int(input("Nhập  Tuổi bệnh nhân: "))

spo2_level = int(input("Nhập  Nồng độ oxy trong máu - SpO2 (%)"))

heart_rate = int(input("Nhập Nhịp tim (nhịp/phút): \n"))

has_insurance = input("Nhập Bạn có thẻ Bảo hiểm Y tế (BHYT) không?: ")

print("\n" + "=" * 60)


if spo2_level < 90 or heart_rate > 120:
    triage_result  = "BÁO ĐỘNG ĐỎ — Cấp cứu khẩn!"
    triage_note    = "Nhân viên y tế đang được điều phối đến ngay."

elif 90 <= spo2_level <= 95 or 100 <= heart_rate <= 120:
    triage_result  = " BÁO ĐỘNG VÀNG — Cần theo dõi sát."
    triage_note    = "Vui lòng ngồi khu vực ưu tiên, chờ điều dưỡng kiểm tra."

else:
    triage_result  = " XANH — Chỉ số an toàn, khám thường."
    triage_note    = "Vui lòng lấy số thứ tự và chờ tại sảnh."



BASE_FEE = 500000  

if patient_age < 6 or patient_age >= 80:
    hospital_fee  = 0
    fee_note      = "Miễn phí (Trẻ em dưới 6 tuổi hoặc người từ 80 tuổi trở lên)"

elif has_insurance == "yes":
    hospital_fee  = BASE_FEE // 2     
    fee_note      = "Giảm 50% (Có thẻ BHYT)"

else:
    hospital_fee  = BASE_FEE           
    fee_note      = "Thu 100% (Không thuộc diện miễn/giảm)"


print("               PHIẾU TIẾP NHẬN BỆNH NHÂN")
print("=" * 60)
print(f"  Họ và tên     : {patient_name}")
print(f"  Tuổi          : {patient_age} tuổi")
print(f"  SpO2          : {spo2_level}%")
print(f"  Nhịp tim      : {heart_rate} nhịp/phút")
print(f"  Thẻ BHYT      : {'Có' if has_insurance == 'yes' else 'Không'}")
print("-" * 60)
print(f"  Phân luồng    : {triage_result}")
print(f"  Hướng dẫn    : {triage_note}")
print("-" * 60)
print(f"  Tạm ứng phí  : {hospital_fee:,} VNĐ")
print(f"  Ghi chú       : {fee_note}")
print("=" * 60)
print("  Cảm ơn bạn đã sử dụng Kiosk. Chúc bạn sức khỏe!")
print("=" * 60)