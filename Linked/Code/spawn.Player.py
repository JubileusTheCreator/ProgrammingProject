import bge
import time

def Spawn():
    contP = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    Szene = scene.name
    playerP = scene.objects["player"]
    if Szene == "Modul1":
        Spawnpoint = 1
    playerP = contP.owner
    while Spawnpoint == 1:
        print ("Ja")
        playerP.worldPosition = [1.4,-7,0]
        Spawnpoint += 0.5
        break


Spawn()