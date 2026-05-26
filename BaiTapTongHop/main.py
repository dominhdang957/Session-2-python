

print("=" * 55)
print("     HỆ THỐNG TUYỂN NHÂN VIÊN")
print("=" * 55)

is_running = True
choice = "y"
while is_running: 
    if (choice == "y") :
        emp_quantity = int(input("Nhập số lượng nhân viên: "))
        emp_name = input("Nhập tên nhân viên: ")
        day_amount = int(input("Nhập số ngày đi làm : "))

        print("=" * 60)
        print("THÔNG TIN NHÂN VIÊN")
        print("=" * 60)
        print("Tên: ",emp_name)
        print("Số ngày đi làm: ",day_amount)
        message = "Cần cải thiện chuyên cần" if day_amount < 20 else "Nhân viên chuyển cần tốt"
        print(message)
    elif (choice == "n") :
        is_running = False
        print("Chương trình kết thúc")
    choice = input("Tiếp tục chương trình? (y/n)")


