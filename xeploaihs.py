import math 
def diem_tong_ket():
    Toan = int(input(f"Điểm toán là:"))
    Van = int(input(f"Điểm văn là:"))
    Anh = int(input(f"Điểm anh là:"))
    DTK = (Toan*2 + Van + Anh) / 4
    if DTK >= 9:
        print(f"Điểm tổng kết là: {DTK} - Học lực: Xuất sắc")
    elif DTK >= 7:
        print(f"Điểm tổng kết là: {DTK} - Học lực: Giỏi")
    elif DTK >= 5:
        print(f"Điểm tổng kết là: {DTK} - Học lực: Khá")
    else:
        print(f"Điểm tổng kết là: {DTK} - Học lực: Trung bình")
    if Toan <= 4 or Van <= 4 or Anh <= 4:
        print("Học sinh bị rớt vì có điểm liệt 4")
diem_tong_ket()