import smbus
import time
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
bus = smbus.SMBus(1)    #オブジェクト作成

def ondo_get():        #温度取得関数
    i2cadr = 0x48
    adr = 0
    cnt = 2
    data = bus.read_i2c_block_data(i2cadr, adr, cnt)
    abc = (((data[0] & 0x7f) * 0x100) + data[1]) >> 3
    if(data[0] & 0x80):
        abc = abc - 4096
    ondo = abc / 16
    return ondo

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        if request.form['send'] == '温度':
            temp = ondo_get()
            m = str(temp)    #m = 'left'
            return render_template('index.html', message=m)
        if request.form['send'] == 'center':
            m = 'center'
            return render_template('index.html', message=m)
        if request.form['send'] == 'right':
            m = 'right'
            return render_template('index.html', message=m)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
