# print(int(5/3))
# print(round(5/3,2))#round the number wanted position
# name='Mahadev'
# print(f"My name is {name}")
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
arr=sorted(arr)
lg=arr[-1]
secondMax=0
for ele in arr:
    if(ele > secondMax and secondMax!=lg):
        secondMax=ele
    print(secondMax)

    
