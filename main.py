voltage = 0
tempC = 0
tempF = 0

def on_forever():
    global voltage, tempC, tempF
    voltage = Math.map(pins.analog_read_pin(AnalogPin.P1), 0, 1023, 0, 3300)
    tempC = voltage - Math.idiv(500, 10)
    tempF = 1.8 * (tempC + 32)
    basic.show_string("C:" + str(tempC))
    basic.show_string("F:" + str(tempF))
basic.forever(on_forever)
