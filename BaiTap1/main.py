#nguyên nhân lỗi là do khi nhập vào nhịp tim lớn hơn 100 thì điều kiện hear_rate > 100 đúng thì nó sẽ dừng và không xét bên dưới nữa

print("---- EMERGENCY TRIAGE SYSTEM ----")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại ưu tiên (ĐÃ SỬA)
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")