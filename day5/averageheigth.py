n=int(input("Number of students"))
lst_height=[]
for i in range(0,n):
    student_height=float(input("Enter height"))
    lst_height.append(student_height)
heigth_total=0
for i in range(0,n):
    heigth_total+=lst_height[i]
print(round(heigth_total/n,2))
