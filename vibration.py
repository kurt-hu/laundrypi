from gpiozero import Button
from signal import pause
import time

# Use the internal pull-up resistor to prevent the pin from floating.
# The button is on GPIO 2 (pin 3 on the header) and connected to ground.
# This means when the button is pressed, the state will be LOW (False).
button = Button(4)
counter = 0

def isDrying():
    previous = counter
    #print("Checking if machine is drying...")
    time.sleep()

    # If the counter increased by more than 5, assume the machine is still running.
    if (counter - previous) > 1:
        return True
    else:
        return False


def button_pressed():
    global counter
    #print("Button was pressed! " + str(counter))
    counter += 1

# Attach the functions to the button's events
button.when_pressed = button_pressed

print("Ready. Press the button to see messages.")
while (True):
    print(isDrying())
pause() # This keeps the script running and listening for events.
