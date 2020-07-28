let voltage = 0
let tempC = 0
let tempF = 0
basic.forever(function () {
    voltage = Math.map(pins.analogReadPin(AnalogPin.P1), 0, 1023, 0, 3300)
    tempC = voltage - Math.idiv(500, 10)
    tempF = 1.8 * (tempC + 32)
    basic.showString("C:" + tempC)
    basic.showString("F:" + tempF)
})
