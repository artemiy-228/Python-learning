# Basketball players

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean = sum(players) / len(players)

summ = 0

for i in players:
    summ += (mean - i)**2

variance = summ / len(players)

std = variance**0.5

c = 0

for i in players:
    if mean - std <= i <= mean + std:
        c += 1

print(c)
