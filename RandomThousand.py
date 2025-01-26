import random

f = open("file2.txt", "a")

for i in range(1000):
    random_number = random.randint(0, 32767)
    f.write(f'{random_number}\n')
f.close()
