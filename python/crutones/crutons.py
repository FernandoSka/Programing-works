import sys
import urllib3
import serial
import datetime
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
ser = serial.Serial('COM4')  # open serial port
extension = str(int(input("Ingrese la extension: ")))

while True:
    x = ser.read()     # write a string
    x = x.decode("utf-8")
    if x == "1":
        http = urllib3.PoolManager()
        fec = str(datetime.datetime.now())
        r = http.request('POST', 'http://127.0.0.1:8000/home/', fields={'fecha': fec})
        r = http.request('POST', 'https://192.168.1.32/getter.php', fields={'phone': extension})
        print(extension)
ser.close()