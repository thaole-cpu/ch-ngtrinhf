
input_file = open('UOCINO.txt', 'r')

n = int(input_file.readline().strip())

input_file.close()

uoc_so = []
for i in range(1,n):
        uoc_so.append(str(i))  # Thêm ước số vào danh sách dưới dạng chuỗi

# Mở file UOCOUT.txt để ghi
out_file = open('UOCOUT.txt', 'w')

# Ghi các ước số vào file, mỗi ước cách nhau một khoảng trắng
out_file.write(' '.join(uoc_so))


out_file.close()
