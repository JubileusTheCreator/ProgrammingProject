from bge import logic           #logic editor aus der Blender game engine Importieren
scene = logic.getCurrentScene()
Key = scene.objects['Key']      #zu bewegendes Objekt festlegen

Key_ori = Key.orientation.to_euler() #Winkel in Euler umwandeln
Key_ori.z += 0.02            #Schlüssel Drehung
Key.position.z += 0.1         #Schlüssel Position in Z Richtung

Key.orientation = Key_ori   