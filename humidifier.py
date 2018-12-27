import RPi.GPIO as GPIO
import time, dht11, datetime

state = ""

while True:
  # 現在のdatetime
  dt_now = datetime.datetime.now()

  # 日付と時刻のString
  dt_str = dt_now.strftime('%Y-%m-%d %H:%M:%S')

  GPIO.setmode(GPIO.BCM)

  #GPIO3を制御パルスの出力に設定
  gp_out = 3
  GPIO.setup(gp_out, GPIO.OUT)
  servo = GPIO.PWM(gp_out, 50)

  # dht11
  instance = dht11.DHT11(pin=14)
  hum = 0
  while hum == 0:
    result = instance.read()
    hum = result.humidity
  temp = result.temperature

  # if hum > 60 -> off
  if hum >= 56:
    if state != "off":
      servo.start(2.5)
      state = "off"
  elif hum <= 55:
    if state != "on ":
      servo.start(12)
      state = "on "

  time.sleep(1)

  print(state + " hum: " + str(hum) + "% " + dt_str)

  servo.stop()
  GPIO.cleanup()
  time.sleep(299)
