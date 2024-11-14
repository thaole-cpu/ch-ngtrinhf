
input_file = open('TBCINP2.txt', 'r')
n = int(input_file.readline().strip())
ket_qua = []
for i in range(n):
    day_so = list(map(int, input_file.readline().split()))
    tong = sum(day_so)
    if len(day_so) > 0:
        trung_binh = tong / len(day_so)
    else:
        trung_binh = 0
    ket_qua.append(str(trung_binh))

input_file.close()
out_file = open('TBCOUT2.txt', 'w')
out_file.write('\n'.join(ket_qua))
out_file.close()