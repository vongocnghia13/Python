n = int(input("Nhap vao n :"))
if (n%2!=0):
    print("Số lẻ")
elif (n%2==0 and n>= 100):
    print("Số chẵn và lớn hơn hoặc bằng 100")
else:
    print("Số chẵn và bé hơn 100")