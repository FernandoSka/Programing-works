from pyfirmata import Arduino, util

import time



placa = Arduino("COM13")


print ("INICIO")


for i in range(10):
    placa.digital[13].write(1);
    time.sleep(1)
    placa.digital[13].write(0);
    time.sleep(1)

print ("HOLA")




