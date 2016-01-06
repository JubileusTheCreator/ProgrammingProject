# Beide Codeblöcke aus Platzgründen hier in ein Dokument. Sind in Blender getrennt verlinkt.

# Code by Jan Rehbein; Comment by Steven Serra Mock


# Start
# Blender Game Engine laden
import bge
# Scene laden
scene = bge.logic.getCurrentScene()

# Keyboard (Steuerung) laden
keyboard = bge.logic.keyboard

# Wenn die Leertaste gedrückt wird, wird zum Level gewechselt
if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]:
    scene.replace("MainScene")



# Restart
# Blender Game Engine laden
import bge
# Scene laden
scene = bge.logic.getCurrentScene()

# Keyboard (Steuerung) laden
keyboard = bge.logic.keyboard

# Wenn die Leertaste gedrückt wird, Neustart
if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]:
    scene.replace("Titel")