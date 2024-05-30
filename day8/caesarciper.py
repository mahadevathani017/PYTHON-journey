#program to ceasarciper game
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

direction=input("Type 'encode' to encrpt,type 'decode' to decrypt:\n")
text=input("type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_forward_amount):
    cipher_text=""
    for letter in plain_text:
        position=alp.index(letter)
        new_postion=position+shift_forward_amount
        new_letter=alp[new_postion]
        cipher_text+=new_letter
    print(f"Encoded word is {cipher_text}")


def decrypt(new_text,shift_backward_amount):
    plain_text=""
    for letter in new_text:
        position=alp.index(letter)
        new_postion=position-shift_backward_amount
        plain_text+=alp[new_postion]
    print(f"decoded word is f{plain_text}")
    
if(direction=="encode"):
    encrypt(text,shift)
else:
    decrypt(cipher_text ,shift)
         
