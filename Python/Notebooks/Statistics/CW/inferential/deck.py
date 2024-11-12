import pandas as pd

data = {"Cards" : ["Queen", "King", "Diamond"], "Count" : [4,4,13]}
df = pd.DataFrame(data)
print(df)



total_cards = 52


kings_and_queens = 4 + 4
kingsqueens = df['Cards'][0]
print(kingsqueens)



probability = kings_and_queens / total_cards

kings = 4
diamonds = 13
king_of_diamonds = 1


probability = (kings + diamonds - king_of_diamonds) / total_cards

print(f"The probability of drawing a King or a Queen is: {probability:.4f}")
print(f"The probability of drawing a King or a Diamond is: {probability:.4f}")