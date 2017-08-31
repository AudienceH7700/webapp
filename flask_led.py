from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route("/LED/ON")
def led_on():
    GPIO.output(8, GPIO.HIGH)
    return "LED ON"


@app.route("/LED/OFF")
def led_off():
    GPIO.output(8, GPIO.LOW)
    return "LED OFF"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8889, debug=True)
