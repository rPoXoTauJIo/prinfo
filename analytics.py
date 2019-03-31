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
import prdebug
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

        # test stuff
        #select_timer = rtimer.Timer(setTestVehicle, 3, 1, 'ru_jet_su27')

        # test stuff2
        host.registerHandler('EnterVehicle', onEnterVehicle)
        host.registerHandler('ExitVehicle', onExitVehicle)
        resetUpdateTimer()

        D.debugMessage('===== FINISHED OBJMOD INIT =====')


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
    
    D.debugMessage('resetUpdateTimer(): reloaded updated timer')

# offloading debug
# tnx pie&mats for idea, althorugh my implementation is worse
def onUpdate(data=''):
    global G_UPDATE_LAST

    time_wall_now = host.timer_getWallTime()
    time_delta = time_wall_now - G_UPDATE_LAST
    time_epoch = time.time()
    G_UPDATE_LAST = host.timer_getWallTime()
    #D.debugMessage('Time: %s+%s@%s' % (time_wall_now, time_delta, time_epoch))
    if G_TRACKED_OBJECT is not None and G_TRACKED_OBJECT.isValid():
        position = G_TRACKED_OBJECT.getPosition()
        rotation = G_TRACKED_OBJECT.getRotation()
        D._debug_echo('Position: %s\nRotation: %s' % (str(position), str(rotation)))
        network_message = ' '.join([str(position), str(rotation), str(time_wall_now), str(time_delta), str(time_epoch)])
        D._debug_socket(network_message)


def onEnterVehicle(player, vehicle, freeSoldier=False):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = vehicle
    D.debugMessage('Player entered %s' % (G_TRACKED_OBJECT.templateName))
    position = vehicle.getPosition()
    rotation = vehicle.getRotation()
    # for some reason this works
    try:
        D.debugMessage('Position: %s' % (str(position)))
        D.debugMessage('Rotation: %s' % (str(rotation)))
    except:
        D.errorMessage()
    resetUpdateTimer()


def onExitVehicle(player, vehicle):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = None
    D.debugMessage('Player left %s' % (vehicle.templateName))
    position = vehicle.getPosition()
    rotation = vehicle.getRotation()
    D.debugMessage('Position: %s' % (str(position)))
    D.debugMessage('Rotation: %s' % (str(rotation)))
    resetUpdateTimer()


def setTestVehicle(template, data=''):
    global G_TRACKED_OBJECT

    objects = bf2.objectManager.getObjectsOfTemplate(template)
    D.debugMessage(
        'setTestVehicle(): found %s objects of template %s' %
        (len(objects), template))
    G_TRACKED_OBJECT = objects[0]
    D.debugMessage('Selected first object of template %s at %s' % (
        G_TRACKED_OBJECT.templateName, str(G_TRACKED_OBJECT.getPosition())))


# ------------------------------------------------------------------------
# onChatMessage
# Callback that managing chat messages.
##########################################################################
# !NEVER call any messages directly from onChatMessage handler
# It causing inifite loop
##########################################################################
# ------------------------------------------------------------------------
def onChatMessage(playerId, text, channel, flags):

    # fix for local non-dedicated servers
    if playerId == -1:
        playerId = 255

    # getting player object by player index
    player = bf2.playerManager.getPlayerByIndex(playerId)

    # standart check for invalid players
    if player is None or player.isValid() is False:
        return

    # common way to filter chat message
    # clearing text as any channel except Global are prefixed
    text = text.replace('HUD_TEXT_CHAT_COMMANDER', '')
    text = text.replace('HUD_TEXT_CHAT_TEAM', '')
    text = text.replace('HUD_TEXT_CHAT_SQUAD', '')
    text = text.replace('HUD_CHAT_DEADPREFIX', '')
    text = text.replace('* ', '')
    text = text.strip()

    # splitting filtered message text to arguments
    args = text.split(' ')

    if args[0] == C.COMMANDKEY:
        del args[0]
        if len(args) == 0:
            D.debugMessage('NO ARGS IN CHAT MSG', ['echo'])
            return
        commandHandler(player, args)
    else:
        pass


# ------------------------------------------------------------------------
# commandHandler
# wrapper around function calls
# ------------------------------------------------------------------------
def commandHandler(player, args):
    """
        commandHandler
            handling functions calls for ingame debug
    """

    if args[0] == 'reload':
        reload(C)  # reloading constant file
        return G_QUERY_MANAGER.setupDefaultQueries()

    if args[0] == 'reset':
        return resetUpdateTimer()

    # createQuery(args)
    D.debugMessage('commandHandler::args = %s' % (str(args)))


# EOF
