# Câu a
Nhietdo = [28.5,30.0,32.5,29.0,31.5,27.0,33.0]
tong = 0
for nhiet in Nhietdo:
    tong += nhiet
NDTB = tong / len(Nhietdo)
print(f"Nhiệt độ trung bình trong tuần là: {NDTB} độ C")
# Câu b
Nhietdocaonhattrongdanhsach = Nhietdo[0]
for nhiet in Nhietdo:
    if nhiet > Nhietdocaonhattrongdanhsach:
        Nhietdocaonhattrongdanhsach = nhiet
print(f"Nhiệt độ cao nhất trong tuần là: {Nhietdocaonhattrongdanhsach} độ C")
# Câu c
Hon30do = 0
for nhiet in Nhietdo:
    if nhiet >= 30:
        Hon30do += 1
    print(f"Số ngày có nhiệt độ trên 30 độ C là: {Hon30do} ngày")
# Câu d 
for i in range(len(Nhietdo)):
    for j in range (i+1,len(Nhietdo)):
        if Nhietdo[i] > Nhietdo[j]:
            temp = Nhietdo[i]
            Nhietdo[i] = Nhietdo[j]
            Nhietdo[j] = temp
    print("Danh sách nhiệt độ sau khi sắp xếp là:", Nhietdo)
