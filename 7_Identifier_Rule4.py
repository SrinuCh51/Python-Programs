#Case sensitive and Case insensitive
#Variable adresses are different--> Case sensitive
#Variable adresses are same--> Case insensitive
A=100
a=200
print("Case Sensitive")
print("A=",A,id(A))
print("a=",a,id(a))
print()
B=100
b=100
print("Case Insensitive")
print("B=",B,id(B))
print("b=",b,id(b))