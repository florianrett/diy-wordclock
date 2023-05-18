import board
import time
import adafruit_tsl2591

i2c = board.I2C()
sensor = adafruit_tsl2591.TSL2591(i2c)

sensor.gain = adafruit_tsl2591.GAIN_HIGH
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS

while True:
    # print('Light: {0}lux'.format(sensor.lux))
    # print('Visible: {0}'.format(sensor.visible))
    # print('Infrared: {0}'.format(sensor.infrared))
    # print('Full Spectrum: {0}'.format(sensor.full_spectrum))
    # print('Raw Luminosity: {0}'.format(sensor.raw_luminosity))

    print("Visible light: {0}".format(sensor.visible))
    time.sleep(1)