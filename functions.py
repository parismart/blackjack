import random as rd

def initial_cards(baraja):
    initial_hand = [rd.choice(baraja), rd.choice(baraja)]
    baraja.remove(initial_hand[0])
    baraja.remove(initial_hand[1])
    return initial_hand

def get_card(baraja):
    answer = input('Quieres otra carta? y/n')
    if answer == 'y':
        card = rd.choice(baraja)
        baraja.remove(card)
        return card
    elif answer == 'n':
        return
    else:
        print('Responde "y" si quieres otra carta y "n" si quieres plantarte.')
        return (get_card(baraja))

def get_card_croupier(baraja):
    card = rd.choice(baraja)
    baraja.remove(card)
    return card

def get_value(hand):
    value = 0
    for card in hand:
        if card == None:
            return value
        elif ((card >= 2) and (card < 10)):
            value += (card)
        elif card >= 10:
            value += 10
        elif card == 1:
            if value <= 10 :
                value += 11
            else:
                value += 1
    return value

def show_cards(hand):
    for card in hand:
        if card == 1:
            card = 'A'
        elif card == 10:
            card = 'J'
        elif card == 11:
            card = 'Q'
        elif card == 12:
            card = 'K'
        else:
            str(card)
        print(card, end=' ')
    print('')

def show_dealer(hand_dealer):
    card = hand_dealer[0]
    if card == 1:
        card = 'A'
    elif card == 10:
        card = 'J'
    elif card == 11:
        card = 'Q'
    elif card == 12:
        card = 'K'
    else:
        str(card)
    print(f'La Carta descubierta del croupier es {card}')

def deal_cards(baraja, hand_player, hand_dealer):
    while get_value(hand_player) < 21:
        hand_player.append(get_card(baraja))
        if hand_player[-1] == None:
            print(f'Te has plantado, Tu puntuación final es {get_value(hand_player)}')
            break
        show_cards(hand_player)
        print(f'El valor de tu mano es {get_value(hand_player)}')

    while get_value(hand_dealer) < 16:
        hand_dealer.append(get_card_croupier(baraja))
    if get_value(hand_player) <= 21:
        print(f'El valor de la mano del croupier es {get_value(hand_dealer)}')
        show_cards(hand_dealer)

def show_results(hand_player, hand_dealer):
    value = get_value(hand_player)
    dealer = get_value(hand_dealer)
    if value > 21:
        print('You Lose')
    elif value == dealer:
        if value == 21 and len(hand_player) == 2:
            if dealer == 21 and len(hand_dealer) == 2:
                print('Empate')
            else:
                print('Black Jack, you win')
        else:
            print('Empate')
    elif value == 21 and len(hand_player) == 2:
        print('Black Jack, you win')
    elif value > dealer and value <= 21 or dealer > 21 and value <= 21:
        print('You win')
    else:
        print('You Lose')
