# --------------------------------------------------------------------------
# Project Reality analytics module by rpoxo
#
# ~ analytics.py
#
# Description:
#
# 
#
# -------------------------------------------------------------------------

# importing python system modules
import sys
import time
import math

# importing modules from standart bf2 package
import bf2
import host

# importing project reality packages
import game.realitytimer as rtimer

# importing custom modules
import constants as C

G_TRACKED_OBJECT = None
G_UPDATE_TIMER = None
G_UPDATE_LAST = 0.0

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    host.registerGameStatusHandler(onGameStatusChanged)

# ------------------------------------------------------------------------
# DeInit
# ------------------------------------------------------------------------
def deinit():
    host.unregisterGameStatusHandler(onGameStatusChanged)


# ------------------------------------------------------------------------
# onGameStatusChanged
# ------------------------------------------------------------------------
def onGameStatusChanged(status):
    if status == bf2.GameStatus.Playing:
        # registering chatMessage handler
        host.registerHandler('ChatMessage', onChatMessage, 1)

        # test stuff2
        host.registerHandler('EnterVehicle', onEnterVehicle)
        host.registerHandler('ExitVehicle', onExitVehicle)

        debugMessage('===== FINISHED OBJMOD INIT =====')

def debugMessage(msg):
    host.rcon_invoke('echo "%s"' % (str(msg)))

def debugIngame(msg):
    debugMessage(msg)
    try:
        host.rcon_invoke('game.sayAll "%s"' % (str(msg)))
    except:
        host.rcon_invoke('echo "debugIngame(FAIL): %s"' % (str(msg)))


# 30+-5fps = ~0.33...ms is server frame, no need for updates more frequently than 0.05
def resetUpdateTimer():
    global G_UPDATE_TIMER

    if G_UPDATE_TIMER is not None:
        G_UPDATE_TIMER.destroy()
        G_UPDATE_TIMER = None

        G_UPDATE_TIMER = rtimer.Timer(onUpdate, 1, 1)
        G_UPDATE_TIMER.setRecurring(0.1)
    else:
        G_UPDATE_TIMER = rtimer.Timer(onUpdate, 1, 1)
        G_UPDATE_TIMER.setRecurring(0.1)
    
    debugMessage('resetUpdateTimer(): reloaded updated timer')

# offloading debug
# tnx pie&mats for ideas, althorugh my implementation is worse
def onUpdate(data=''):
    global G_UPDATE_LAST

    time_wall_now = host.timer_getWallTime()
    time_delta = time_wall_now - G_UPDATE_LAST
    time_epoch = time.time()
    G_UPDATE_LAST = host.timer_getWallTime()
    #debugMessage('Time: %s+%s@%s' % (time_wall_now, time_delta, time_epoch))
    if G_TRACKED_OBJECT is not None and G_TRACKED_OBJECT.isValid():
        position = G_TRACKED_OBJECT.getPosition()
        rotation = G_TRACKED_OBJECT.getRotation()


def onEnterVehicle(player, vehicle, freeSoldier=False):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = vehicle
    debugMessage('Player entered %s' % (G_TRACKED_OBJECT.templateName))
    resetUpdateTimer()


def onExitVehicle(player, vehicle):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = None
    debugMessage('Player exited %s' % (vehicle.templateName))
    resetUpdateTimer()
