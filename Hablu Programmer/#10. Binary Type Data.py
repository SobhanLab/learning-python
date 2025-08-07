mylist = [7, 6, 2, 4, 2, 6]
b = bytes(mylist)
print(b)
print(type(b))


mylist2 = [7, 6, 2, 4, 2, 6]
ba = bytearray(mylist2)
ba[2] = 65+25
print(ba[2])
print(ba)
print(type(ba))
