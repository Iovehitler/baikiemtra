def lasohoanhao(n):
    tong_uoc = 0
    
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    
    if tong_uoc == n:
        return True
    else:
        return False


n = int(input("Nhập một số nguyên dương: "))

if lasohoanhao(n):
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")