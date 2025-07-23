from reloj import Reloj
from time import sleep

r1 = Reloj()

while True:
    print(r1)
    sleep(1)
    r1.tic()