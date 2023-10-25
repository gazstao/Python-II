# BANNER
# BANNER TO RIGHT: {banner[tam - 1:]}{banner[0:tam - 1]}
# BANNER TO LEFT:  {banner[1:tam]}{banner[tam - 1:]}

import time
import keyboard

banner = ("              Gazstao")
tam = len(banner)

while True:
    banner = f"{banner[1:tam]}{banner[0:1]}"
    print(f"\r{banner}", end="")
    if (keyboard.is_pressed(' ')):
        break
    time.sleep(.3)
