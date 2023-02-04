b1=[1,2,3,4,5,6]
print(b1)
print()
obj=bytearray(b1)
print(obj)
print()
obj[0]=7                  #Mutable object
obj[1]=8
obj[2]=9
obj[3]=10
obj[4]=11
obj[5]=12
print()
print(*obj)