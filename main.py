import functions as f

baraja = list(range(1,13))*4
hand_player = f.initial_cards(baraja)
hand_dealer = f.initial_cards(baraja)

f.show_cards(hand_player)
print(f'El valor de tu mano es {f.get_value(hand_player)}')
f.show_dealer(hand_dealer)
f.deal_cards(baraja, hand_player, hand_dealer)
f.show_results(hand_player, hand_dealer)
