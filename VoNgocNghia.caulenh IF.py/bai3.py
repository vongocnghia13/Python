thang = int(input("Thang :"))
nam = int(input("Nam :"))

if(thang == 1):
    print("so ngay :",31)
elif(thang == 2):
    if(nam%4==0):
        print("so ngay :",28)
    else:
        print("so ngay :",29)
elif(thang == 3):
    print("so ngay :",31)
elif(thang == 4):
    print("so ngay :",30)
elif(thang == 5):
    print("so ngay :",31)
elif(thang == 6):
    print("so ngay :",30)
elif(thang == 7):
    print("so ngay :",31)
elif(thang == 8):
    print("so ngay :",31)
elif(thang == 9):
    print("so ngay :",30)
elif(thang == 10):
    print("so ngay :",31)
elif(thang == 11):
    print("so ngay :",30)
elif(thang == 12):
    print("so ngay :",31)
else:
    print("Khong ton tai ")