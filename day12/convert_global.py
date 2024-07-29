num1=3
def modify_fun():
    global num1#covert into variable into global to access in function
    num1+=1
    print(num1)

modify_fun()
