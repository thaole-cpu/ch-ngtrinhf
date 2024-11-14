input_file = open('DaysoINP.txt', 'r')

n = int(input_file.readline().strip())

numbers = list(map(int, input_file.readline().split()))

input_file.close()

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(str(num))

out_file = open('DaySoOUT.txt', 'w')

out_file.write(' '.join(even_numbers))

# Đóng file DaySoOUT.txt sau khi ghi xong
out_file.close()