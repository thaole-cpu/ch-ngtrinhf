inp_file = open('TBCINP.txt', 'r')

n = int(inp_file.readline().strip())

tong = 0
for i in range(n):
    so = int(inp_file.readline().strip())
    tong += so
inp_file.close()

inp_file = open('TBCINP.txt', 'r')

n = int(inp_file.readline().strip())
tong = 0
for i in range(n):
    so = int(inp_file.readline().strip())
    tong += so
inp_file.close()

if n > 0:
    trung_binh = tong / n
else:
    trung_binh = 0

out_file = open('TBCOUT.txt', 'w')

out_file.write(str(trung_binh))

out_file.close()
