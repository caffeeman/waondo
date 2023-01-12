import smbus
import time
import requests

bus = smbus.SMBus(1)        #オブジェクト作成

while True:
    i2cadr = 0x48
    adr = 0
    cnt = 2
    data = bus.read_i2c_block_data(i2cadr, adr, cnt)     #戻り値は二つ
    adc = (((data[0] & 0x7f) * 0x100) + data[1]) >> 3    #戻り値は一つ
    if(data[0] & 0x80):
        adc = adc - 4096

    temp = adc / 16.0
    strtemp = '現在の温度は:' + str(temp)

    print( strtemp )

    time.sleep(10)

