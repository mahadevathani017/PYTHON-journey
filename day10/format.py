def format_name(f_name,m_name,l_name):
    formated_f_name=f_name.title()
    formated_m_name=m_name.title()
    formated_l_name=l_name.title()
    # print(f_name)
    # print(l_name)
    return f"{formated_f_name} {formated_m_name} {formated_l_name}"
    
firstName=input("Enter your first name")
middleName=input("Enter your middle name:")
lastName=input("Enter your last name")

formatName=format_name(firstName,middleName,lastName)
print(formatName)
