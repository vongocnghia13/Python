tuoi = int(input("Nhap vao tuoi :"))
if tuoi>0 and tuoi<=2:
    print("trẻ sơ sinh")
elif tuoi>2 and tuoi<=10:
    print("nhi đồng")
elif tuoi>=10 and tuoi<=17:
    print("vị thành niên")
elif tuoi<17 and tuoi<=39:
    print("thanh niên")
elif tuoi>39 and tuoi<=50:
    print("trung niên")
else :
    print("cao niên")