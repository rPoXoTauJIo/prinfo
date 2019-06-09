# --------------------------------------------------------------------------
# Project Reality prinfo by rpoxo
#
# ~ prinfo.py
#
# Description:
#   displays data about vehicle
#
# -------------------------------------------------------------------------

import os
import datetime

# workaround for importing outside bf2
import externals
from externals import bf2 as bf2
from externals import host as host
from externals import radmin as radmin
from externals import rtimer as rtimer

from math3d import Point3d

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    WatchVehicle.init()

def deinit():
    WatchVehicle.deinit()

class WatchVehicle:
    reporting = False
    reporting_mode = None

    logging = False
    logging_fo = None

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
        #radmin.addCommand("aoa", cls.switchReportAngleOfAttack, 777)

        radmin.addCommand("log", cls.switchLogging, 777)
    
    @classmethod
    def deinit(cls):
        if cls.logging_fo: cls.logging_fo.close()
        # let bf2 deal with destroying handlers
    
    @classmethod
    def switchReporting(cls, args, player):
        if cls.reporting: cls._disableReporting()
        else: cls._enableReporting(player.getVehicle())
        
    @classmethod
    def switchLogging(cls, args, player):
        if cls.logging: cls._disableLogging()
        else: cls._enableLogging(player.getVehicle())
        
    @classmethod
    def switchReportPosition(cls, args, player):
        cls.reporting_mode = 'position'
        if not cls.reporting: cls.switchReporting(args, player)
    
    @classmethod
    def switchReportRotation(cls, args, player):
        cls.reporting_mode = 'rotation'
        if not cls.reporting: cls.switchReporting(args, player)
    
    @classmethod
    def switchReportSpeed(cls, args, player):
        cls.reporting_mode = 'speed'
        if not cls.reporting: cls.switchReporting(args, player)
    
    @classmethod
    def switchReportAngleOfAttack(cls, args, player):
        cls.reporting_mode = 'aoa'
        if not cls.reporting: cls.switchReporting(args, player)

    @classmethod
    def onEnterVehicle(cls, player, vehicle, freeSoldier=False):
        cls.vehicle = vehicle
        debugIngame('%s entered %s' % (player.getName(), vehicle.templateName))

    @classmethod
    def onExitVehicle(cls, player, vehicle):
        cls._disableReporting()
        debugIngame('%s exited %s' % (player.getName(), vehicle.templateName))

    @classmethod
    def _enableTimer(cls):
        debugIngame('Enabling timer...')
        cls.timer = rtimer.Timer(cls._tick, -1, 1)
        cls.timer.setRecurring(0.1) # no need to have it faster than 0.03 as ingame printouts will get buffered
    
    @classmethod
    def _disableTimer(cls):
        debugIngame('Disabling timer...')
        if cls.timer:
            cls.timer.destroy()
            cls.timer = None
        elif cls.timer is None:
            debugIngame('Timer already doesnt exist')
        else:
            debugIngame('Could not destroy timer')

    @classmethod
    def _enableReporting(cls, vehicle):
        debugIngame('Enabling reporting...')
        cls.reporting = True
        if not cls.timer: cls._enableTimer()
        if vehicle is not None: cls.vehicle = vehicle
    
    @classmethod
    def _disableReporting(cls):
        debugIngame('Disabling reporting...')
        cls.reporting = False
        cls.reporting_mode = None
        if cls.timer: cls._disableTimer()
        if cls.vehicle: cls.vehicle = None

    @classmethod
    def _enableLogging(cls, vehicle):
        debugIngame('Enabling logging...')

        cls.logging = True

        filename = os.path.join(host.sgl_getModDirectory(), 'Logs', 'prinfo_' + datetime.datetime.now().strftime("%Y%m%d_%H_%M") + '.log')
        cls.logging_fo = open(filename, 'w')
        debugIngame('Log path is %s' % os.path.abspath(filename))

        cls._enableTimer()
        if vehicle is not None: cls.vehicle = vehicle
        
    @classmethod
    def _disableLogging(cls):
        debugIngame('Disabling reporting...')
        cls.logging = False
        cls.logging_fo.close()
    
    @classmethod
    def _tick(cls, data):
        if not cls.reporting and not cls.logging: return
        if not cls.vehicle: return

        epoch = host.timer_getWallTime()
        position = cls.vehicle.getPosition()
        rotation = cls.vehicle.getRotation()

        if cls.reporting_mode == 'position':
            cls._position(cls.vehicle, epoch, Point3d(*position))
        elif cls.reporting_mode == 'rotation':
            cls._rotation(cls.vehicle, epoch, rotation)
        elif cls.reporting_mode == 'speed':
            delta = epoch - cls.vehicle_lasttime
            cls._speed(cls.vehicle, epoch, delta, Point3d(*position), Point3d(*cls.vehicle_lastposition))
        elif cls.reporting_mode == 'aoa':
            #cls._aoa(cls.vehicle, epoch, Point3d(*position), Point3d(*cls.vehicle_lastposition))
            pass
        elif cls.reporting_mode == None and cls.reporting:
            debugIngame('cls.reporting_mode: %s' % cls.reporting_mode)
            debugIngame('pos_last: (%f, %f, %f)' % (cls.vehicle_lastposition[0], cls.vehicle_lastposition[1], cls.vehicle_lastposition[2]))
            debugIngame('pos_curr: (%f, %f, %f)' % (position[0], position[1], position[2]))
            debugIngame('epoch_last: %f' % cls.vehicle_lasttime)
            debugIngame('epoch_curr: %f' % epoch)

        if cls.logging:
            msg = 'position: %s\nrotation: %s\nepoch: %s\n' % (position, rotation, epoch)
            cls._log(cls.logging_fo, msg)
        
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
        distance = Point3d.Distance(current, last)
        speed = distance / delta
        debugIngame('%s @%.3f for %.3f: %.4f' % (vehicle.templateName, epoch, delta, speed))
    
    # TODO: this is bullshit tbh
    @classmethod
    def _aoa(cls, vehicle, epoch, v1, v2):
        raise NotImplementedError
    
    @classmethod
    def _log(cls, fo, msg):
        fo.write(msg)

def debugMessage(msg):
    host.rcon_invoke('echo "%s"' % (str(msg)))

def debugIngame(msg):
    #debugMessage(msg)
    try:
        host.rcon_invoke('game.sayAll "%s"' % (str(msg)))
    except:
        host.rcon_invoke('echo "debugIngame(FAIL): %s"' % (str(msg)))


