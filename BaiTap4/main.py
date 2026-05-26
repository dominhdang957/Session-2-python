print("=" * 55)
print("     HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI    ")
print("=" * 55)

is_true = True
while is_true :
    quantity_emp = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))

    if quantity_emp <= 0 :
        print("LỖI: SỐ LƯỢNG KHÔNG HỢP LỆ! VUI LÒNG NHẬP MỘT CON SỐ LỚN HƠN 0.")
    else :
        print("[THÀNH CÔNG] ĐÃ GHI KẾT QUẢ YÊU CẦU CẤP PHÁT TÀI SẢN CHO ", quantity_emp ,"NHÂN SỰ")
        print("---- Chương trình kết thúc ----")
        is_true = False
    

