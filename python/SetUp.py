"""ALTE STEUERUNG"""

#Ipmport der Blender Game Engine in die Python API
import bge
import time

# Sicherstellen, dass dieses Pythonprotokoll mit einem "ALWAYS"Controller verbunden ist!
# player ist eine Leerstelle für den Objektnamen. Also die Spielfigur, da diese gesteuert werden soll
def main():
    cont = bge.logic.getCurrentController()
    player = cont.owner

    # Lade die Blender Szene
    scene = bge.logic.getCurrentScene()
    # Lade eine Tastaturbedingte Steuerngseinheit (=KEYBOARD)
    keyboard = bge.logic.keyboard

    # Keyboardinput = Steuerung
    """ Die folgende If-Bedingung wird erst dann aktiviert, sobald eine Funktionsfähige Taste angeschlagen wird.
    Die darauf folgende Aktion ist darunter beschrieben. Dabei manipuliert man mit "player.localPosition.variable +/-= Wert
    die Position der Figur im Spiel und bewegt sie dadurch."""
    # Bewegung in x Richtung (nach rechts gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.RIGHTARROWKEY]:
        time.sleep(0.015)
        player.localPosition.y +=0.05
    # Bewegung in -x Richtung (nach links gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]:
        time.sleep(0.015)
        player.localPosition.y -=0.05
    # Bewegung in y Richtung (nach oben gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.UPARROWKEY]:
        time.sleep(0.015)
        player.localPosition.x -=0.05
    # Bewegung in -x Richtung (nach unten gehen)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DOWNARROWKEY]:
        time.sleep(0.015)
        player.localPosition.x +=0.05
    # Bewegung in z Richtung (springen) (Iwas funktioniert hier noch nicht!!!)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]: #and player.localPosition.z <500:
        #time.sleep(0.015)
        player.localPosition.z +=0.005

main()



neue Version: (man kann nicht mehr unendlich hoch springen)

import bge

def main():

    cont=bge.logic.getCurrentController()
    player = cont.owner

    #get the scene for mouse and other things

    scene = bge.logic.getCurrentScene()

    #get a keyboard
    keyboard = bge.logic.keyboard
    #check for a keyboard event and a specific key

    #now check keyboard input (input status)
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.UPARROWKEY]:
        player.localPosition.y += 0.1
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DOWNARROWKEY]:
        player.localPosition.y -= 0.1
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.RIGHTARROWKEY]:
        player.localPosition.x += 0.1
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]:
        player.localPosition.x -= 0.1
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]:
        player.localPosition.z += 0.1
main()
