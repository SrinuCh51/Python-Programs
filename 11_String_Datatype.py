#Collection of charecters enclosed with ('')or("")or('''''')or("""""")
#Space also consider one charecter
#Supports positive and negative indexes
#Multiline content also supports
str1='S reenu'
str2="Chinnu"
str3='''Junnu'''
str4="""Sreenu
        Chinnu
        Junnu"""
print(str1,str2,str3)
print()
print("Indexing")
print(str1[1])
print(str2[0])
print(str3[-1])
print()
print("Multiline Content")
print(str4)