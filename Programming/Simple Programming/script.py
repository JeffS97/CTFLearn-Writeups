file = 'chal.txt'
count = 0
count1 = 0
count0 = 0

with open(file) as file1:
    lines = file1.readlines()
    for line in lines:
        count1 = line.count('1')
        count0 = line.count('0')

        if (count0%3 == 0 or count1%2 == 0):
            count+=1

print(count)
file1.close()