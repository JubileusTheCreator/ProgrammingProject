# Import der Blender Game Engine Bibliothek
import bge
import time
# Erstellen einer Tastatur
keyboard = bge.logic.keyboard

# !!!Definieren der Spawnfunktion!!!
# ------------------------------------------------------------------------------------------------------
def Spawn():
    cont2 = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    Kamera = scene.objects["Camera"]
    playerP = scene.objects ["player"]
    Plattform1 = scene.objects["Plattform 1"]
    Plattform1 = cont2.owner
    playerP = cont2.owner
    Plattform1.worldPosition = [0, 0, 0]
    playerP.worldPosition = [0,0,0]


# !!!Definieren der Bewegungsfunktion!!!
# ------------------------------------------------------------------------------------------------------
def Move():
# Szene (LevelModul) laden
    scene = bge.logic.getCurrentScene()

# Kamera in Modul 1 laden
    Kamera = scene.objects["Camera"]

# Kamera mit der Spielfigur verlinken, sie folgt nun der Figur und verhindert perspektivisches verzerren
    Kamera.setParent("player")

# Verknüpfung mit dem Skriptausführenden ALWAYS-Controller
    controller = bge.logic.getCurrentController()

# PlayerVariable erstellen und diese von dem Controller steuern lassen
    player = controller.owner

# Variable erstellen, die einen Wert für den Anschlag einer Taste zugeschrieben wird
    Tastenanschlag = bge.logic.KX_INPUT_ACTIVE

# Variablen festsetzen, bei denen IntegerWerte für besonderen Tastenanschlag verteilt werden
# 0= Nicht aktiv; 1= Angeschlagen; 2= Taste gedrückt; 3= Taste Losgelassen
    Right = keyboard.events[bge.events.RIGHTARROWKEY]
    Left = keyboard.events[bge.events.LEFTARROWKEY]
    Up = keyboard.events[bge.events.UPARROWKEY]
    Down = keyboard.events[bge.events.DOWNARROWKEY]
    Jump = keyboard.events[bge.events.SPACEKEY]

#Code für die eigentliche Bewegung
#Dieser Block wird erst dann ausgeführt, wenn eine Taste gedrückt wird.
#Richtungen sind selbst erklärend, sie werden aktiviert, wenn die entsprechende Richtungstaste gedrückt (und gehalten) wird
#Ausnahme ist das Springen, hier soll der Spieler nicht durchgehend hüpfen, sondern muss für jeden Sprung
#die Leertaste erneut betätigen (deshalb == 1)
    if Tastenanschlag >0:
        if Right == 2 and Left == 0 and Up == 0 and Down == 0:
            player.localPosition.y += 0.1
        if Left == 2 and Right == 0 and Up == 0 and Down == 0:
            player.localPosition.y -= 0.1
        if Up == 2 and Right == 0 and Left == 0 and Down == 0:
            player.localPosition.x -= 0.1
        if Down == 2 and Right == 0 and Left == 0 and Up == 0:
            player.localPosition.x += 0.1
        if Jump == 1:
            player.localPosition.z += 1.0



# -------------------------------------------------------------------------------------------------------
Spawn()
Move()