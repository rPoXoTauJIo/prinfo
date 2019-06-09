import os
import time

class DummyBF2:
    def __init__(self):
        pass

class DummyHost:

    def __init__(self, root, mod='bf2'):
        self.bf2 = DummyBF2()
        self.game = DummyGame()
        self.mod = mod
        self.root = root

    def registerHandler(self, name, handler):
        pass
    
    def timer_getWallTime(self):
        return time.time()
    
    def sgl_getModDirectory(self):
        return os.path.join(self.root, 'mods', self.mod)
    
    def rcon_invoke(self, command):
        print(command)

class DummyRealityAdmin:
    def __init__(self):
        pass
    
    def addCommand(self, key, handler, permissions):
        pass


class DummyRealityTimer:
    def __init__(self):
        pass
    
    def Timer(self, handler, delta, alwaysTrigger, data=None):
        return DummyTimer(handler, delta, alwaysTrigger, data)

class DummyTimer:
    def __init__(self, handler, delta, alwaysTrigger, data=None):
        pass

    def setRecurring(self, delta):
        pass

class DummyGame:
    def __init__(self):
        self.realityadmin = DummyRealityAdmin()
        self.realitytimer = DummyRealityTimer()

# =============================================
class DummyPlayer:

    def __init__(self, name):
        self._name = name
        self._position = (0.0, 0,0, 0.0)
        self._rotation = (0.0, 0,0, 0.0)
        self._vehicle = None

    def getVehicle(self):
        if self._vehicle: return self._vehicle
        else: return self