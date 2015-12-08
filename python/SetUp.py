# Ipmport der Blender Game Engine in die Python API
import bge

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
    if bge.logic.KX INPUT ACTIVE == keyboard.events[bge.events.RIGHTARROWKEY]:
        player.localPosition.x +=1
    # Bewegung in -x Richtung (nach links gehen)
    if bge.logic.KX INPUT ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]:
        player.localPosition.x -=1
    # Bewegung in y Richtung (nach oben gehen)
    if bge.logic.KX INPUT ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]:
        player.localPosition.y +=1
    # Bewegung in -x Richtung (nach unten gehen)
    if bge.logic.KX INPUT ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]:
        player.localPosition.y -=1
    # Bewegung in z Richtung (springen)
    if bge.logic.KX INPUT ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]:
        player.localPosition.z +=1.5

main()

# Achtung, dies ist vorerst nur eine theoretische Version. Sie ist noch nicht getestet wurden
# und deshalb noch nicht einsatzfähig! Bitte diesen Kommentar entfernen, sobald das Skript
# funktionstüchtig ist! S.