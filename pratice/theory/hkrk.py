lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
lst=sorted(lst)
for i in range(n):
    if(slg>lst[i] and slg!=max(lst)):
        slg=lst[i]
print(slg)
