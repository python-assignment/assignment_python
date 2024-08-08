word1=input("enter the str1 :")
u=0
l=0
for i in word1:
    if i.isupper():
        u+=1
    else:
        l+=1
print("Uppercase",u,end=" ")
print("Lowercase",l)                    
