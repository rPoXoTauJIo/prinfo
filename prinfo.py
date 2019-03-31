# --------------------------------------------------------------------------
# Project Reality prinfo by rpoxo
#
# ~ prinfo.py
#
# Description:
#   displays data about vehicle
#
# -------------------------------------------------------------------------

import time

import bf2
import host

import game.realityadmin as radmin
import game.realitytimer as rtimer

from math3d import Point3

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    WatchVehicle.init()
    #Speed.init()
    #AoA.init()

class WatchVehicle:
    reporting = False
    reporting_mode = None # default

    timer = None

    vehicle = None
    vehicle_lastposition = (0.0, 0.0, 0.0)
    vehicle_lastrotation = (0.0, 0.0, 0.0)
    vehicle_lasttime = 0.0

    @classmethod
    def init(cls):
        host.registerHandler('EnterVehicle', cls.onEnterVehicle)
        host.registerHandler('ExitVehicle', cls.onExitVehicle)

        radmin.addCommand("watch", cls.switchReporting, 777)
        radmin.addCommand("position", cls.switchReportPosition, 777)
        radmin.addCommand("rotation", cls.switchReportRotation, 777)
        radmin.addCommand("speed", cls.switchReportSpeed, 777)
    
    @classmethod
    def switchReporting(cls, args, player):
        if cls.reporting: cls._disableReporting()
        else: cls._enableReporting(player.getVehicle())
        
    @classmethod
    def switchReportPosition(cls, args, player):
        cls.reporting_mode = 'position'
    
    @classmethod
    def switchReportRotation(cls, args, player):
        cls.reporting_mode = 'rotation'
    
    @classmethod
    def switchReportSpeed(cls, args, player):
        cls.reporting_mode = 'speed'

    @classmethod
    def onEnterVehicle(cls, player, vehicle, freeSoldier=False):
        cls.vehicle = vehicle
        debugIngame('%s entered %s' % (player.getName(), vehicle.templateName))

    @classmethod
    def onExitVehicle(cls, player, vehicle):
        cls._disableReporting()
        debugIngame('%s exited %s' % (player.getName(), vehicle.templateName))

    @classmethod
    def _enableReporting(cls, vehicle):
        if vehicle is not None:
            cls.reporting = True
            cls.timer = rtimer.Timer(cls._tick, -1, 1)
            cls.timer.setRecurring(0.1) # no need to have it faster than 0.03 as ingame prinouts will get buffered
    
    @classmethod
    def _disableReporting(cls):
        cls.reporting = False
        cls.reporting_mode = None
        if cls.timer:
            cls.timer.destroy()
            cls.timer = None
        if cls.vehicle:
            cls.vehicle
    
    @classmethod
    def _tick(cls, data):
        if not cls.reporting: return
        if not cls.vehicle: return

        epoch = host.timer_getWallTime()
        position = cls.vehicle.getPosition()
        rotation = cls.vehicle.getRotation()

        if cls.reporting_mode == 'position':
            cls._position(cls.vehicle, epoch, Point3(*position))
        elif cls.reporting_mode == 'rotation':
            cls._rotation(cls.vehicle, epoch, rotation)
        elif cls.reporting_mode == 'speed':
            delta = epoch - cls.vehicle_lasttime
            cls._speed(cls.vehicle, epoch, delta, Point3(*position), Point3(*cls.vehicle_lastposition))
        else:
            debugIngame('cls.reporting_mode: %s' % cls.reporting_mode)
            debugIngame('pos_last: (%f, %f, %f)' % (cls.vehicle_lastposition[0], cls.vehicle_lastposition[1], cls.vehicle_lastposition[2]))
            debugIngame('pos_curr: (%f, %f, %f)' % (position[0], position[1], position[2]))
            debugIngame('epoch_last: %f' % cls.vehicle_lasttime)
            debugIngame('epoch_curr: %f' % epoch)
        
        cls.vehicle_lastposition = position
        cls.vehicle_lastrotation = rotation
        cls.vehicle_lasttime = epoch
    
    @classmethod
    def _position(cls, vehicle, epoch, position):
        debugIngame('%s @%.3f position:(%.3f, %.3f, %.3f)' % (vehicle.templateName, epoch, position.x, position.y, position.z))
    
    @classmethod
    def _rotation(cls, vehicle, epoch, rotation):
        debugIngame('%s @%.3f rotation:(%.3f, %.3f, %.3f)' % (vehicle.templateName, epoch, rotation[0], rotation[1], rotation[2]))

    @classmethod
    def _speed(cls, vehicle, epoch, delta, current, last):
        distance = Point3.Distance(current, last)
        speed = distance / delta
        debugIngame('%s @%.3f for %.3f: %.4f' % (vehicle.templateName, epoch, delta, speed))
    
    @classmethod
    def _angleOfAttack(cls, vehicle, epoch, position0, position1, rotation1, delta):
        pass

def debugMessage(msg):
    host.rcon_invoke('echo "%s"' % (str(msg)))

def debugIngame(msg):
    #debugMessage(msg)
    try:
        host.rcon_invoke('game.sayAll "%s"' % (str(msg)))
    except:
        host.rcon_invoke('echo "debugIngame(FAIL): %s"' % (str(msg)))


