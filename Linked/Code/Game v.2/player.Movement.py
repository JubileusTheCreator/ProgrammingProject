# Hinweis zum Kommentar des Codes:
# "#" wird benutzt um den Code zu kommentieren
# """x""" wird benutzt um Code zu deaktivieren, wenn man denkt, er sei unnötig!
# oder für besondere Anmerkungen im Code


import bge
keyboard = bge.logic.keyboard
"""------------------------------------------------------------------------------------------------------------------"""
def move():
    # Lade den Level
    scene = bge.logic.getCurrentScene()

    # Die Kamera in den Levelraum implementieren
    Kamera = scene.objects['Camera']


    #Controller der LogicBricks-Matrix von Blender aktivieren und implemnetieren
    cont = bge.logic.getCurrentController()

    # Spielfigur (player) mit dem Controller verbinden
    player = cont.owner


    #Variable für den Tastenanschlag erstellen
    Tastenanschlag = bge.logic.KX_INPUT_ACTIVE

    # Variablen festsetzen, bei denen Integer für Ereignisse beim Tastenanschlag verteilt werden:
    # 0= Nicht aktiv; 1= Angeschlagen; 2= Taste gedrückt; 3= Taste Losgelassen
    Right = keyboard.events[bge.events.RIGHTARROWKEY]
    Left = keyboard.events[bge.events.LEFTARROWKEY]
    Up = keyboard.events[bge.events.UPARROWKEY]
    Down = keyboard.events[bge.events.DOWNARROWKEY]
    Jump = keyboard.events[bge.events.SPACEKEY]
    Reset = keyboard.events[bge.events.BKEY]

    #Code für die eigentliche Bewegung
    #Dieser Block wird erst dann ausgeführt, wenn eine Taste gedrückt wird.
    #Richtungen sind selbst erklärend, sie werden aktiviert, wenn die entsprechende Richtungstaste gedrückt (und gehalten) wird
    #Ausnahme ist das Springen, hier soll der Spieler nicht durchgehend hüpfen, sondern muss für jeden Sprung
    #die Leertaste erneut betätigen (deshalb == 1)
    if Tastenanschlag >0:
        if Right == 2 and Left == 0 and Up == 0 and Down == 0:
            player.worldPosition.y += 0.1
        if Left == 2 and Right == 0 and Up == 0 and Down == 0:
            player.worldPosition.y -= 0.1
        if Up == 2 and Right == 0 and Left == 0 and Down == 0:
            player.worldPosition.x -= 0.1
        if Down == 2 and Right == 0 and Left == 0 and Up == 0:
            player.worldPosition.x += 0.1
        if Jump == 1:
            player.worldPosition.z += 1.0
        #if Reset == 1:
            #player.worldPosition = [1.4,-7,0]
        if player.worldPosition.z <-10:
            player.worldPosition = [1.4,-7,-4]
"""------------------------------------------------------------------------------------------------------------------"""

    # Laden des Controllers. D = Distance
    contD = bge.logic.getCurrentController()

    # Laden der Szene, um Objekte ansprechen zu können
    scene = bge.logic.getCurrentScene()

    # Varaible für die Position der Spielefigur
    playerD = contD.owner

    # Liste mit allen Objekten in der Szene (im Level) laden
    objList = scene.objects

    # Objekt Key eine Variable zuschreiben
    Key = objList["Key"]

    # Objekt Lever eine Variable zuschreiben
    Lever = objList["Lever"]

    # Objekt Gate eine Variable zuschreiben
    Gate = objList["Gate"]

    # Objekt Door eine Variable zuschreiben
    Door = objList["Door"]


    # Variable, die die Distanz zwischen der Figur und dem Schlüssel beschreibt
    distanceK = playerD.getDistanceTo(Key)

    # Variable, die die Distanz zwischen der Figur und dem Schalter beschreibt
    distanceL = playerD.getDistanceTo(Lever)

    # Variable, die die Distanz  zwischen der Figur und der Tür beschreibt
    distanceD = playerD.getDistanceTo(Door)



    #print(objList)
    #print(distance)


    # Eigentliche Funkrion läuft im folgenden Programmblock ab
    # Hier geht es darum, dass, wenn ein Objekt vom Spieler berührt wird, also die Distanz zwischen beiden
    # Objekten sehr gering ist (fast 0), das berührte Objekt "eingesammelt" wird und somit nicht mehr
    # auf der Oberfläche zu sehen ist. Das berührte Objekt bekommt zusätzlich eine Varaiable zugeschrieben
    # mit der dann weiter manipuliert werden kann. Bemerke V steht für vanish (= verschwinden)!

    # Variable für einen neuen Controllertyp festlegen (steuert das Verschwinden)
    contV = bge.logic.getCurrentController()
    """Key = scene.objects['Key']"""

    # Beenden des Schlüssels
    if distanceK <2.2:
        Key.endObject()
        Schlüssel = 1

    if distanceL <2.2:
        Lever.endObject()
        Gate.endObject()

    if distanceD <2.2 and Schlüssel == 1:
        Door.endObject()
        Schlüssel = 0
"""------------------------------------------------------------------------------------------------------------------"""

move()
ObjectDistance()