from random import choices

ACE = 1
ACE_11 = 11
BUST_SCORE = 21
MINIMUM_COM_SCORE = 17

CARD_LIST = [1,2,3,4,5,6,7,8,9,10,10,10,10]

def calculate_score(cards: list) -> int:
    score = sum(cards)

    if ACE in cards:
        new_cards = cards.copy()
        for i in range(cards.count(ACE)):
            if (sum(new_cards) < BUST_SCORE) and ((sum(new_cards) - ACE + ACE_11)  < BUST_SCORE):
                new_cards.remove(ACE)
                new_cards.append(ACE_11)
        score = sum(new_cards)

    return score

def display_score(user_cards, computer_cards):
    print("     Your cards: {}, current score: {}".format(user_cards, calculate_score(user_cards)))
    print("     Computer's first card: {}".format(computer_cards[0]))

def display_final_score(user_cards, computer_cards):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("     Your final hand: {},       final score: {}".format(user_cards, user_score))
    print("     Computer's final hand: {}, final score: {}".format(computer_cards, computer_score))

    if user_score >= BUST_SCORE:
        print("You went over, You lose")
    elif computer_score >= BUST_SCORE:
        print("Computer went over, You win")
    elif computer_score == user_score:
        print("Draw")
    elif computer_score > user_score:
        print("You lose")
    else:
        print("You win")

def computer_play(cards):
    while MINIMUM_COM_SCORE > calculate_score(cards):    
        cards.extend(choices(CARD_LIST, k=1))

    return cards

def play_blackjack():
    user_cards = choices(CARD_LIST, k=2)
    computer_cards = choices(CARD_LIST, k=2)
    
    while True:
        display_score(user_cards, computer_cards)
        
        if calculate_score(user_cards) >= BUST_SCORE:
            display_final_score(user_cards, computer_cards)
            break
        
        need_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if  need_another_card == 'n':
            computer_play(computer_cards)
            display_final_score(user_cards, computer_cards)
            break

        user_cards.extend(choices(CARD_LIST, k=1))
            

if __name__ == "__main__":
    play = 'y'
    while play == 'y':
        play_blackjack()
        play = input("Do you want to paly a game of Blakjack? Type 'y' or 'n': ")