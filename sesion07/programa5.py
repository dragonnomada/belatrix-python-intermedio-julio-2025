from reloj import Reloj

r1 = Reloj()

for _ in range(60):
    r1.tic()
r1.tic()
r1.tic()
# 00:01:02
r1.tac()
# 00:02:02
r1.toc()
# 01:02:02

print(r1)