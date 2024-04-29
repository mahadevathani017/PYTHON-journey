lst1=lst2=[]
for i in range(21):
    if(i%2==0):
        lst1.append(i)
    else:
        lst2.append(i)
    
lst3=[lst1,lst2]
print(lst3[0][1])
