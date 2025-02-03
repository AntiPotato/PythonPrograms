import random
import time
import datetime


print(datetime.datetime.now())
start_time = time.time()
f = open("file2.txt", "a")

for i in range(1000000):
    random_number = random.randint(0, 32767)
    f.write(f'{random_number}\n')
f.close()
print(datetime.datetime.now())
end_time = time.time()

elapsed_time = end_time - start_time

hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)

print(f"Time taken: {hours} hours, {minutes} minutes, {seconds} seconds")
