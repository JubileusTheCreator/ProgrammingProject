import bge
import time

def Spawn():
    contP = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    Szene = scene.name
    Plattform1 = scene.objects["Plattform1"]
    Plattform1 = contP.owner
    if Szene == "Modul1":
        Spawnpoint = 1
    playerP = contP.owner
    while Spawnpoint == 1:
        Plattform1.worldPosition = [0, 0, 0]
        Spawnpoint += 0.5
        break

Spawn()