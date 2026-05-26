

print("=" * 60)
print("    KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI  ")
print("=" * 60)

is_validate = True
is_validate_performance = True
while is_validate:
    print("[Nhập thông tin nhân viên]")

    emp_id = ""
    while emp_id == "": 
            emp_id = input("Enter employee ID: ")
            if not emp_id.strip() :
                    print("Lỗi: Mã nhân viên không được trống hoặc sai cú pháp. Vui lòng nhập lại.")
                    emp_id = ""
    emp_name = ""
    while emp_name == "":
            emp_name = input("Enter FULLNAME employee : ")
            if not emp_name.strip() :
                print("Lỗi: Tên không được trống hoặc sai cú pháp. Vui lòng nhập lại.")
                emp_name = ""
         

    salary = 0
    while salary <= 0:
            salary = float(input("Enter salary:  "))
            if salary <= 0:
                print("[LỖI]: Lương không thể là số âm hoặc bằng 0. vui lòng nhập lại")

    performance = 0
    while performance < 1 or performance > 5:
            performance = float(input("Enter performance score(1.0 to 5.0): "))
            if performance < 1 or performance > 5:
                print("Lỗi Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")
            
        
    year_experience = -1
    while year_experience < 0:
            year_experience = int(input("Enter year of experience: "))
            if year_experience <= 0: 
                print("Lỗi kinh nghiệm phải từ 0 năm trở lên. Vui lòng nhập lại.")
        

    print("=" * 60)
    print("      E-PROFILE CẬP NHẬT     ")
    print("=" * 60)
    print("ID: ",emp_id)
    print("Name: ", emp_name)
    print("Salary: ", salary)
    print("KPI Score: ", performance)
    print("Experience:" , year_experience)

    print("=" * 60)
    print("    IT SYSTEM LOG   ")
    print("=" * 60)
    print("employee_id             |" , type(emp_id))
    print("employee_name           |" , type(emp_name))
    print("employee_salary         |" , type(salary))
    print("employee_score          |" , type(performance))
    print("employee_years          |" , type(year_experience))

    print("-" * 60)

    continue_system = input("Do you want to enter another employee? (y/n) :")
    if continue_system == "n":
        is_validate = False
        print("Đang tắt kiosk ... tạm biệt")
    


