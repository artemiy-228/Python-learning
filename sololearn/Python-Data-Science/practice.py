# Data Science - Introduction

# #Statistic

# ##Vactination report - mean

vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3
            ]

print(sum(vac_nums) / len(vac_nums))

# ##Vactination report - variance

vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]

mean = sum(vac_nums) / len(vac_nums)

sum = 0

for i in vac_nums:
    sum += (mean - i)**2

variance = sum / len(vac_nums)

print(variance)

