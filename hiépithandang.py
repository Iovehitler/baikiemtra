import random
def Tro_choi_hiep_si():
    Tongdiem = 0
    for i in range(1, 11):
        if random.random() >= 0.7:
            diemtrung = random.randint(50, 100)
            Tongdiem += diemtrung
    else:
        diemtru = 20
        Tongdiem -= diemtru
    if Tongdiem  > 400:
        print("Chúc mừng bạn đã trở thành hiệp sĩ thần đằng với tổng điểm là:", Tongdiem)
        return
    print("Rất tiếc bạn đã thất bại với tổng điểm là:", Tongdiem)
Tro_choi_hiep_si()