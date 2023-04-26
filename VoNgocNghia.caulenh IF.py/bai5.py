a = int(input("Nhập vào a:"))
b = int(input("Nhập vào b:"))
if a == 0 and b == 0 :
    print("phương trình vô số nghiệm")
if a==0 and b != 0:
    print("phương trình vô nghiệm")
if a != 0 : 
    print("nghiệm của phương trình là :", -b/a)