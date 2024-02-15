from pyfirmata import Arduino, SERVO

PORT = "COM3"

pin = 10

board = Arduino(PORT)

board.digital[pin].mode = SERVO
led_red = board.get_pin('d:6:o')
led_green = board.get_pin('d:7:o')


def led(color):
    if color == "red":
        led_red.write(1)
        led_green.write(0)
    elif color == "green":
        led_green.write(1)
        led_red.write(0)


def rotateServo(pin, angle):
    board.digital[pin].write(angle)


def doorAutomate(val):
    if val == 0:
        rotateServo(pin, 210)
    elif val == 1:
        rotateServo(pin, 40)
