import random
import time
import datetime


# Reads integers from the given file and returns them in an array.
def read_integers_from_file(file_path):
    integer_array = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                integer_array.append(int(line.strip()))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    return integer_array


# Reads integers from the given file line by line and writes them in another file after doubling.
def read_integers_from_file_and_write(file_path, output_file_path):
    f = open("newfile2.txt", "a")
    with open(file_path, 'r') as file:
        for line in file:
            try:
                f.write(f'{2 * int(line.strip())}\n')
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    f.close()


print(datetime.datetime.now())
start_time = time.time()

# Code to read all at once and write later. Uncomment to execute.
#integer_array = read_integers_from_file("file2.txt")
#f = open("newfile2.txt", "a")
#for i in integer_array:
#    f.write(f'{i * 2}\n')
#f.close()


# Code to read line by line and write it. Uncomment to execute.
# read_integers_from_file_and_write("file2.txt", "newfile2.txt")


#Code to read two files separately.
integer_array = read_integers_from_file("file2.txt")
f = open("newfile2.txt", "a")
for i in integer_array:
    f.write(f'{i * 2}\n')
f.close()
integer_array = read_integers_from_file("file3.txt")
f = open("newfile2.txt", "a")
for i in integer_array:
    f.write(f'{i * 2}\n')
f.close()



print(datetime.datetime.now())
end_time = time.time()

elapsed_time = end_time - start_time

hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)

print(f"Time taken: {hours} hours, {minutes} minutes, {seconds} seconds")
