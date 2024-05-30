program_dict={"Bug":"an error","function":"piece of code"}

'''print(program_dict)
print(type(program_dict["Bug"]))
print(type(program_dict))'''

program_dict["loop"]="Do something over and over again"

program_dict["loop"]="do again"

# program_dict={}

# print(program_dict)

for thing in program_dict:
    print(thing,":",program_dict[thing])
    
