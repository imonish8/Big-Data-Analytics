
total_cards = 52


spades = 13

# coditional probability as both events are dependent

P_first_spade = spades / total_cards
P_second_spade = (spades - 1) / (total_cards - 1)


P_both_spades = P_first_spade * P_second_spade


print(f"The probability of drawing two spades in succession is: {P_both_spades:.4f}")
