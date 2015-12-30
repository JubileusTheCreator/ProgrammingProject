# Code by Steven Serra Mock
import bge

def ObjectDistance():
    # Laden des Controllers. D = Distance
    contD = bge.logic.getCurrentController()

    # Laden der Szene, um Objekte ansprechen zu können
    scene = bge.logic.getCurrentScene()

    # Varaible für die Position der Spielefigur
    playerD = contD.owner

    # Liste mit allen Objekten in der Szene (im Level) laden
    objList = scene.objects

    # Liste mit allen Objekten als Variablensammlung
    Objects = [objList["Key"], objList["Lever"], objList["Gate"], objList["Door"], objList["End"]]

    # Liste mit allen Distanzen (wird später benötigt)
    distance = [playerD.getDistanceTo(Objects[0]), playerD.getDistanceTo(Objects[1]),
                playerD.getDistanceTo(Objects[3]), playerD.getDistanceTo(Objects[4])]

    # Eigentliche Funkrion läuft im folgenden Programmblock ab
    # Hier geht es darum, dass, wenn ein Objekt vom Spieler berührt wird, also die Distanz zwischen beiden
    # Objekten sehr gering ist (fast 0), das berührte Objekt "eingesammelt" wird und somit nicht mehr
    # auf der Oberfläche zu sehen ist. Das Objekt wird unsichtbar gemacht und auf eine andere Position verschoben,
    # somit ist es weg (Es kann nicht beendet werden, da sonst das Skript nicht mehr funktioniert)

# Code by Steven Serra Mock & Jan Rehbein

    # Einsammeln des Schlüssels
    if distance[0] < 1.8:
        Objects[0].visible = False
        Objects[0].worldPosition = [0, 0, -10]

    # Öffnen der Tür, wenn man Schlüssek eingesammelt hat
    if distance[2] < 2.2 and Objects[0].visible == False:
        Objects[3].visible = False
        Objects[3].worldPosition = [0, 0, -10]

    # Wegsperre deaktivieren, wenn der Hebel berührt wurde
    if distance[1] < 1.6:
        Objects[1].visible = False
        Objects[1].worldPosition = [0, 0, -10]
        Objects[2].visible = False
        Objects[2].worldPosition = [0, 0, -10]

    # Wenn das Ende erreicht wurde, wrid das Ende eingeblendet
    if distance[3] < 1.8 and Objects[3].visible == False:
        scene.replace("Finish")

ObjectDistance()

