#Bài 1
list=[2,4,6,8,10,321,21,165]
def tong_le(lst):
    return sum(filter(lambda x: x % 2 != 0, lst))
#Bài 2
def tong_chan(lst):
    return sum(lst[::2])
#Bài 3
def xoa_so_am(lst):
    return list(filter(lambda x: x >= 0, lst))
#Bài 4
def vi_tri_max(lst):
    return lst.index(max(lst))
#Bài 5
def thay_the_so_am(lst):
    return [0 if i < 0 else i for i in lst]