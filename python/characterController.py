from bge import *

class GameObject:
    global controller
    global scene
    global obj

    def __init__(self):
        self.controller = logic.getCurrentController()
        self.scene = logic.getCurrentScene()
        self.obj = controller.owner
        self.scene.objects["GameManager"]
    def start(self):
        return
    def update(self):
        return


print("Script Start!")
gameObjects = []
go = GameObject()

def registerGameObject(g):
    gameObjects.append(g)

def start():
    for g in gameObjects:
        g.start()
def update():
    for g in gameObjects:
        g.update()

# def do():
#     if keyboard.events[events.WKEY] == logic.KX_INPUT_JUST_ACTIVATED:
#          print("Delta Time:")


# def update():
#     if keyboard.events[events.WKEY] == logic.KX_INPUT_JUST_ACTIVATED:
#         print("Delta Time: " + str(deltaTime))
#
#     deltaTime = time.time() - lastTime
#     lastTime = time.time()
