import random
for i in range (100):
    random.seed(i)
    ly = random.randint(0, 10)
    if ly == 5:
        yes = i
        break
print(yes)
