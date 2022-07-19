# Coin Types: 25, 20, 4, 1

# Idea
# Always select the biggest feasible coin

# Case1
# 37 cents -> 1*25 + 1*10 + 2*1
print('37 cents:', end=' ')
n = 37
count = 0
coin_types = [25, 20, 4, 1]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

# Case2
# 28 cents -> 1*25 + 3*1 (not a best answer) / 1*10 + 2*4 (best answer)


