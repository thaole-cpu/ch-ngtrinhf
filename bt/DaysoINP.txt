
inp_file = open('DaySoINP2.txt', 'r')
n = int(inp_file.readline().strip())

numbers = list(map(int, inp_file.readline().split()))
inp_file.close()

sum_div_3 = 0
for num in numbers:
    if num % 3 == 0:
        sum_div_3 += num

# Mở file DaySoOUT2.txt để ghi
out_file = open('DaySoOUT2.txt', 'w')

