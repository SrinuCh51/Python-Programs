#Bytes datatype works non audio & video files (XML,JSON)
b1=[1,2,3,4,5,6]
print(b1)
print()
obj=bytes(b1)
print(obj,type(obj))
print()                                  #Bytes datatype is immutable
print(*obj,"------------------","256")   #Range must be from (0-256)