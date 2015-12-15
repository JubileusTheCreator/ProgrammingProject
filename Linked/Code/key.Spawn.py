import bge
import time

def Spawn():
    contP = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    Szene = scene.name
    keyP = scene.objects["Key"]
    if Szene == "Modul1":
        Spawnpoint = 1
    keyP = contP.owner
    while Spawnpoint == 1:
        print ("Ja")
        keyP.worldPosition = [2,4,0]
        Spawnpoint += 0.5
        break


Spawn()