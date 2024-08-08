sen1=input("enter any string :")
sen2=list(sen1)
l=0
d=0
for i in sen2:
    if i.isalpha():
        l+=1
    if i.isdigit():
        d+=1
    else:
        pass    
print("letters",l,end=" ")
print("digit",d)        
           