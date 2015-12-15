import bge
import time
#posPlayer = player.worldPosition()
def Spawn():
    contP = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    Szene = scene.name
    #Obj = scene.objects
    #print (Obj)
    Kamera = scene.objects["Camera"]
    playerP = scene.objects["player"]
    Plattform1 = scene.objects["Plattform1"]
    Plattform1 = contP.owner
    if Szene == "Modul1":
        Spawnpoint = 1
    playerP = contP.owner
    while Spawnpoint == 1:
        print ("Ja")
        Plattform1.worldPosition = [0, 0, 0]
        playerP.worldPosition = [1.4,-7,0]
        Spawnpoint += 0.5
        break


Spawn()
#if Szene = "Modul1":
#    posPlayer = [x, y, 10]