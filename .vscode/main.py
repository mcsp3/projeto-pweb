from math import *

def cartToPol(real, img):
    r = sqrt(real**2 + img**2)
    arcTg = atan2(img, real)

    print(f'Resultado (tg, 0): ({r:.2f}, {arcTg:.2f})')

print(cartToPol(4,30))