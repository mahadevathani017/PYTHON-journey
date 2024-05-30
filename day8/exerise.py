#paint area calculator
import math

test_h=int(input("Enter height:"))
test_w=int(input("Enter weight:"))

coverage=5

def print_calc(height,width,cover):
    total_area=height*width
    total_can=math.ceil(total_area/cover)
    print(f"Number canvas required {total_can}")


print_calc(test_h,test_w,coverage)

 