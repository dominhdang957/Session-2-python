print("=" * 55)
print("HỆ THỐNG TỰ ĐỘNG HÓA NHẬP LIỆU")
print("=" * 55)

is_check_validate = True
for i in range(1,4):
    emp_id = input("Nhập mã nhân viên: ")
    emp_name = input("Nhập vào họ tên nhân viên: ")
    department = input("Nhập vào phòng ban công tác: ")

    if not emp_id.strip() or not emp_name.strip() :
        print("Cảnh báo dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên.")
    else:
        print("=" * 55)
        print("Hồ sơ nhân viên")
        print("=" * 55)
        print("Mã nhân viên:  ", emp_id)
        print("Tên         :"  , emp_name)
        print("Phòng ban    : ", department)
        print("=" * 55)