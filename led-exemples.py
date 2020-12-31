import time
from rpi_ws281x import PixelStrip, Color
# LED strip configuration:
LED_COUNT = 64        # Number of LED pixels.
LED_PIN = 12          # GPIO pin connected to the pixels (18 uses $
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800$
LED_DMA = 10          # DMA channel to use for generating signal ($
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN $
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
RIGHT_BORDER = [7,15,23,31,39,47,55,63]
LEFT_BORDER = [0,8,16,24,32,40,48,56]

COLOR_BLACK=Color(0, 0, 0)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()): 
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def showArrow(color):
    start=32
    for i in range(0,8):
        strip.setPixelColor(start+i, color)
    strip.setPixelColor(start-2, color)
    strip.setPixelColor(start-11, color)
    strip.setPixelColor(start-20, color)
    strip.setPixelColor(start+14, color)
    strip.setPixelColor(start+21, color)
    strip.setPixelColor(start+28, color)
    strip.show()
    
def movingPixel(color, wait_ms):
    for i in range(0,64):
        strip.setPixelColor(i-1,COLOR_BLACK) 
        strip.setPixelColor(i,color)
        strip.show()
        time.sleep(wait_ms/1000.0)
    

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

movingPixel(Color(0,255,0), 100)
time.sleep(5)

print('Bye !')
colorWipe(strip, COLOR_BLACK, 10)
