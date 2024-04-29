print("Welcome to bmi calacultor version 2")
weight=float(input('Enter a weight in kg='))
height=float(input("Enter a height in meters="))
bmi_cal=weight/(height*height)
print(bmi_cal)
if(bmi_cal<18.5):
    
    print("Under weight...")
elif(bmi_cal>=18.5 and bmi_cal<25):
    print("Normal weight....")
elif(bmi_cal>=25 and bmi_cal<30):
    print("Slightly overweight...")
elif(bmi_cal>=30 and bmi_cal<35):
    print("Obese....")
else:
    print("clinically obese....")
