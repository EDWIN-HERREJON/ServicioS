from flask import *
'''from turbo_flask import Turbo'''
app = Flask(__name__)
'''turbo = Turbo(app)'''

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led01 = 17
led02 = 18
led03 = 27
led04 = 22
GPIO.setup(led01,GPIO.OUT)
GPIO.output(led01, GPIO.LOW)
GPIO.setup(led02,GPIO.OUT)
GPIO.output(led02, GPIO.LOW)
GPIO.setup(led03,GPIO.OUT)
GPIO.output(led03, GPIO.LOW)
GPIO.setup(led04,GPIO.OUT)
GPIO.output(led04, GPIO.LOW)

volts = 0
@app.route('/')
def home():
   GPIO.output(led01,0)
   GPIO.output(led02,0)
   GPIO.output(led03,0)
   GPIO.output(led04,0)
   return render_template('indexFES.html',volts=volts)


@app.route('/<led>/<action>', methods=['GET','POST'])
def led(led, action):
   GPIO.output(led01, 0)
   GPIO.output(led02, 0)
   GPIO.output(led03, 0)
   GPIO.output(led04, 0)
   GPIO.output(int(led), int(action))
   '''print(GPIO.input(led01))
   print(GPIO.input(led02))
   print(GPIO.input(led03))
   print(GPIO.input(led04))
   
   if(GPIO.input(led01)==1):
       volts = 3
   elif(GPIO.input(led02)==1):
       volts = 5
   elif(GPIO.input(led03)==1):
       volts = 9     
   elif(GPIO.input(led04)==1):
       volts = 12      
   else:
       volts = 0'''
   return render_template('indexFES.html', volts=volts)

'''@app.route('/<url>')
def get_html(url):
    return render_template(url+".html")'''

if __name__ == '__main__':
    app.run(debug=True,host="192.168.100.7",port=80)