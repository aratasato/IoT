from bottle import route, run, template, post, redirect, get, static_file, TEMPLATE_PATH, HTTPResponse, jinja2_template as template
import RPi.GPIO as GPIO
import dht11, subprocess, jinja2, time
import simplejson as json

# setting template path
TEMPLATE_PATH.append("./template")

# GPIO initialize
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=14)

@route('/')
def index():
    return static_file('index.html', root='./template')

@route('/instance.json')
def instancejson():
  hum = 0
  while hum == 0:
    result = instance.read()
    hum = result.humidity
  temp = result.temperature
  body = json.dumps({'hum': hum, 'temp': temp})
  r = HTTPResponse(status=200, body=body)
  r.set_header('Content-Type', 'application/json')
  r.set_header("Access-Control-Allow-Origin", "*")
  return r

@post('/cooleron')
def coon():
    subprocess.call("irsend send_once aircon cooler".split())
    redirect("/")

@post('/cooleroff')
def coof():
    subprocess.call("irsend send_once aircon stop".split())
    redirect("/")

@get('/css/styles.css')
def css():
    return static_file('styles.css', root='template/')

@get('/js/script.js')
def js():
  return static_file('script.js', root='template')
run(host = '0.0.0.0', port = 9000, debug =True)
