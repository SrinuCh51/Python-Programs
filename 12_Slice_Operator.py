#To make the peices of the string
print("Positive Indexing")
str1="Sreenu"
print(str1[0:])       #Form1 (begin:)
print(str1[:6])       #Form2 (:end)
print(str1[0:6])      #Form3 (begin:end)
print(str1[0:6:2])    #form4 (begin:end:step)

#Form5
print(str1[0:])
print(str1[:])
print(str1[::])

print("Negative Indexing")
print(str1[-7:-1])
print(str1[-7:-1:-2])
