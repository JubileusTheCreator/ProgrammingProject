# Code by Steven Serra Mock

import bge

def Spawn():
    # Scene laden
    scene = bge.logic.getCurrentScene()

    # Szene verwendbar machen
    Szene = scene.name
    
    # Schlüssel laden
    keyP = scene.objects["Key"]

    # Schlüssel auf Position bringen
    if Szene == "MainScene":
        keyP.worldPosition = [-8.49073, 22.66491, 14]

Spawn()