# Copyright (c) 2021 TU Delft Sustainable Systems Laboratory (https://github.com/TUDSSL/BFree/blob/main/LICENSE)

import board
import neopixel

from neural_net.demo import run_demo

# Create a single NeoPixel to write the x value of the sine to
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.5)


def set_brightness(brightness):
    """
    Sets the brightness of the initialized NeoPixel.

    Args:
        brightness: the brightness of the LED.
    """

    dot[0] = [(brightness * 0.95 + 1) * a for a in [63, 0, 0]]


# Run the provided demo code
run_demo(set_brightness)
