import random as r

# num_of_cards = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "ace":[1,11], "jack":10, "queen":10, "king":10}

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards)
    return card 

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and  sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(p_score, c_score):
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has blackjack"
    elif p_score == 0:
        return "Win with a blackjack"
    elif p_score > 21:
        return "You went over. You Lose"
    elif c_score > 21:
        return "Opponent went over. You Win"
    elif p_score > c_score:
        return "You win"
    else:
        return "You Lose"
    



player_card =[]
comp_card =[]
is_game_over = False
for round in range(1,3):
    new_card = deal_card()
    player_card.append(new_card) 
    comp_card.append(new_card)
while not is_game_over:
    player_score = calculate_score(player_card)
    comp_score = calculate_score(comp_card)
    print(f"Your cards: {player_card}, your score: {player_score}")
    print(f"computer's first_card: {comp_card[0]}")
    if player_score == 0 or comp_score == 0 or player_score > 21:
        is_game_over = True
    else:
        user_deal = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        if user_deal == 'y':
            new_card = deal_card()
            player_card.append(new_card) 
        else:
            is_game_over = True
while comp_score != 0 and comp_score < 17:
    comp_card.append(new_card)
    comp_score = calculate_score(comp_card)

print(compare(player_score, comp_score))




#         print(f"Round {round}")
#         player_card = r.choice(cards.keys())
#         player_result.append(cards.get(player_card))
#         comp_card = r.choice(cards.keys())
#         comp_result.append(cards.get(comp_card))
#         print(f"Player card is {player_card} and computer card is {comp_card}")

# get_result(cards =num_of_cards)