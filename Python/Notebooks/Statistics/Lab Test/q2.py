import random

def red_ball_probability(n=10000):
    bag = ['red'] * 4 + ['green'] * 3 + ['blue'] * 2
    red_count = sum(1 for _ in range(n) if random.choice(bag) == 'red')
    return red_count / n


def same_color_probability():
    p_red = (4 / 9) * (3 / 8)
    p_green = (3 / 9) * (2 / 8)
    p_blue = (2 / 9) * (1 / 8)
    total_probability = round(p_red + p_green + p_blue,2)
    return total_probability

print(f"\nProbability of Drawing a Red Ball simulated looped over 10000 times.: {red_ball_probability()*100} %")
print(f"Probability of Drawing Two Balls of the Same Color: {same_color_probability()*100} %")