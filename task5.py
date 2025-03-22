import random
list = random.sample(range(1,101), 20)
print(list)
for i in list:
    if i%2==0: print(i)
    if i%3 == 0: print(i)
print ("среднее арифметическое ", (sum(list)/len(list)))