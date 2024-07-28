#sum is not cross the 21 then your loose
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def cal_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
        
    return sum(cards)
    
user_cards=[]
computer_cards=[]
is_game_over=False

    
for _ in range(2):
    # new_card=deal_card()
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
user_score = cal_score(user_cards)
computer_score=cal_score(computer_cards)

print(f"your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card:{computer_cards[0]}")
if user_score==0 or computer_score==0 or user_score > 21:
    is_game_over=True
else:
    user_should_deal=input("Type 'y' ot get another card,type 'n' to pass:")
    if user_should_deal=="y":
        user_cards.append(deal_card())
    else:
        is_game_over=True
    


        
        

