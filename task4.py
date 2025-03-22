import random
list = random.sample(range(-100,101), 10)
print(list)
print("максимальное ", max(list))
print("минимальное ", min(list))
print("сумма всех", sum(list))
print(sorted(list))