"""TEST KARL"""

from bge import *

controller = logic.getCurrentController()
scene = logic.getCurrentScene()

# 'Keyboard' is a keyboard sensor
sensor = controller.sensors["Keyboard"]

for key,status in sensor.events:
        # key[0] == bge.events.keycode, key[1] = status
        if status == logic.KX_INPUT_JUST_ACTIVATED:
                if key == events.WKEY:
                    # Activate Forward!
                    print("Key Pressed!")
                # if key == bge.events.SKEY:
                #     # Activate Backward!
                # if key == bge.events.AKEY:
                #     # Activate Left!
                # if key == bge.events.DKEY:
                #     # Activate Right!