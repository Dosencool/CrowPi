import random
import time
from rpi_ws281x import PixelStrip, Color
# Valeurs pour configurer les LED
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

# Creer l'objet strip avec la bonne configuration
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# initialiser (a appeler une fois au debut)
strip.begin()


def sireneDesPompiers(nb):
    for n in range(0,nb):
        for colorposition in  range(0, 64):
            strip.setPixelColor(colorposition, Color(255,0,0))
        strip.show()
        time.sleep(1)
        for colorposition in  range(0, 64):
            strip.setPixelColor(colorposition, Color(0,0,255))
        strip.show()
        time.sleep(1)


def pixelBouge(color):
    for rangee in range(0, 64):
        strip.setPixelColor(a, color)
        strip.setPixelColor(a-1, COLOR_BLACK)
        strip.show()
        time.sleep(0.1)
        
def pixelTombe(color):
    compteur=1
    while(compteur<100):
        col=random.randrange(0,8)
        compteur = compteur +1
        for rangee in range(0, 8):
            couleurPrecedente=strip.getPixelColor(rangee*8+col)
            if(couleurPrecedente==0):
                strip.setPixelColor(rangee*8+col, color)
                strip.setPixelColor((rangee-1)*8+col, COLOR_BLACK)
                strip.show()
                time.sleep(0.1)
            else:
                break
            
pixelTombe(Color(255,255,255))

#attendre n secondes
time.sleep(1)

#effacer tout avant de quitter
for blackposition in range(0,64):
    strip.setPixelColor(blackposition, COLOR_BLACK)
strip.show()