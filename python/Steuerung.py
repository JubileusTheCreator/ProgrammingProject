#Ipmport der Blender Game Engine in die Python API
import bge
import time

# Sicherstellen, dass dieses Pythonprotokoll mit einem "ALWAYS"Controller verbunden ist!
# player ist eine Leerstelle für den Objektnamen. Also die Spielfigur, da diese gesteuert werden soll

#Plattform = scene.objects["Plattform 1"]
#Plattform.setPosition([-1.41206, 3.49975, 5.19047])

def main():
    cont = bge.logic.getCurrentController()
    player = cont.owner

# Lade die Blender Szene
    scene = bge.logic.getCurrentScene()
    Kamera = scene.objects["Camera"]
    Kamera.setParent("player")
    Plattform = scene.objects["Plattform 1"]
    Plattform.localPosition.x = -1.41206
    Plattform.localPosition.y = 3.49975
    Plattform.localPosition.z = 5.19047

# Lade eine Tastaturbedingte Steuerngseinheit (=KEYBOARD)
    keyboard = bge.logic.keyboard

# Keyboardinput = Steuerung
    """ Die folgende If-Bedingung wird erst dann aktiviert, sobald eine Funktionsfähige Taste angeschlagen wird.
    Die darauf folgende Aktion ist darunter beschrieben. Dabei manipuliert man mit "player.localPosition.variable +/-= Wert
    die Position der Figur im Spiel und bewegt sie dadurch."""
# Bewegung in x Richtung (nach rechts gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.RIGHTARROWKEY]:
        time.sleep(0.015)
        player.localPosition.y +=0.1
# Bewegung in -x Richtung (nach links gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]:
        time.sleep(0.015)
        player.localPosition.y -=0.1
# Bewegung in y Richtung (nach oben gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.UPARROWKEY]:
        time.sleep(0.015)
        player.localPosition.x -=0.1
# Bewegung in -x Richtung (nach unten gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DOWNARROWKEY]:
        time.sleep(0.015)
        player.localPosition.x +=0.1
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]:
        #time.sleep(0.015)
        player.localPosition.z +=0.1

main()

