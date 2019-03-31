# -------------------------------------------
# constants file
#
# ~ constants.py
#
# -------------------------------------------

# command key for chat commands
COMMANDKEY = '!obj'

# address and port for listening UDP server
SERVERHOST = 'localhost'  # Symbolic name meaning all available interfaces
SERVERPORT = 8888  # Arbitrary non-privileged port

# address and port for streaming client
CLIENTHOST = 'localhost'  # Symbolic name meaning all available interfaces
CLIENTPORT = 8888  # Arbitrary non-privileged port

# path to expor file
# keep in mind that if path does not exist - log file won't be created
LOGFILENAME = '/objmodv2.log'


# setting debug level, uncomment required debug
DEBUGS = [
    'file',  # debugging in files, set log path first
    'udp',  # UDP debug, sending
    'echo',  # printing debug to server console
    'ingame'  # printing debug ingame
    ]

DEBUGS_DEFAULT = [
    'file', # debugging in files, set log path first
    'udp', # UDP debug, sending
    'echo',  # printing debug to server console
    #'ingame' # printing debug ingame
    ]



DEFAULT_QUERIES = {

    'ger_ahe_tiger' : {
        'ger_ahe_tiger' : [
            #'ObjectTemplate.setPositionOffset 0.0/0.0/14.5',
            #'ObjectTemplate.setPitchOffset 0.0',
            #'ObjectTemplate.setWingLift 0.25',
            #'ObjectTemplate.setFlapLift 0.0',
            #'ObjectTemplate.inertiaModifier 1',
            ],
        'ger_ahe_tiger_WingL' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-1.0',
            #'ObjectTemplate.setWingLift 0.5',
            #'ObjectTemplate.setFlapLift 0.1',
            ],
        'ger_ahe_tiger_WingR' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-1.0',
            #'ObjectTemplate.setWingLift 0.5',
            #'ObjectTemplate.setFlapLift 0.1',
            ],
        'ger_ahe_tiger_rotor' : [
            #'ObjectTemplate.setMaxRotation 0/0/1400',
            #'ObjectTemplate.setMaxSpeed 0/0/1',
            #'ObjectTemplate.setAcceleration 0/0/20',
            #'ObjectTemplate.setDeAcceleration 0/0/200',
            #'ObjectTemplate.setUseDeAcceleration 1',
            #'ObjectTemplate.maxAngleOfAttack 12',
            #'ObjectTemplate.attackSpeed 60',
            #'ObjectTemplate.setTorque 70',
            #'ObjectTemplate.setDifferential 200',
            #'ObjectTemplate.defaultAngleOfAttack -20',
            #'ObjectTemplate.horizontalSpeedMagnifier 3.0',
            #'ObjectTemplate.decreaseAngleToZeroVerticalVel 0.01',
            #'ObjectTemplate.defaultAngleOfAttack 0.0',
            #'ObjectTemplate.horizontalDampAngle 0.1',
            #'ObjectTemplate.horizontalDampAngleFactor 0.001',
            ],
        'ger_ahe_tiger_BodyWing' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/5/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/-50/0',
            #'ObjectTemplate.setPositionOffset -5.0/0.0/0.0',
            #'ObjectTemplate.setWingLift 1.0',
            #'ObjectTemplate.setFlapLift 0.35'
            ],
        'ger_ahe_tiger_Rudder' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/-50/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.5/-3.0',
            #'ObjectTemplate.setWingLift 3.5',
            #'ObjectTemplate.setFlapLift 0.15'
            ],
        },
    
    'us_jet_a10a' : {
        'us_jet_a10a_Wing_Front' : [
            #'ObjectTemplate.setPositionOffset 0.0/0.0/10.5',
            #'ObjectTemplate.setWingLift 0.65',
            #'ObjectTemplate.setFlapLift 0.0',
            ],
        'us_jet_a10a_Winglet_Back' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-10.0',
            #'ObjectTemplate.setWingLift 0.4',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'us_jet_a10a_FlapsL' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset -7.0/0.0/2.5',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'us_jet_a10a_FlapsR' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 7.0/0.0/2.5',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'us_jet_a10a_Wing_Vertical' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/5.0',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'us_jet_a10a_Wing_Rudder' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/0.0',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'us_jet_a10a_EngineMain' : [
            #'ObjectTemplate.setMaxSpeed 0/0/500',
            #'ObjectTemplate.setAcceleration 0/0/120',
            #'ObjectTemplate.setTorque 140',
            #'ObjectTemplate.setDifferential 140',
            ],
        },

    'ru_jet_su39' : {
        'ru_jet_su39_Wing_Front' : [
            #'ObjectTemplate.setPositionOffset 0.0/0.0/10.5',
            #'ObjectTemplate.setWingLift 0.65',
            #'ObjectTemplate.setFlapLift 0.0',
            ],
        'ru_jet_su39_Winglet_Back' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-10.0',
            #'ObjectTemplate.setWingLift 0.4',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'ru_jet_su39_FlapsL' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset -7.0/0.0/2.5',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'ru_jet_su39_FlapsR' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 7.0/0.0/2.5',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'ru_jet_su39_Wing_Vertical' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/5.0',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'ru_jet_su39_Wing_Rudder' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/0.0',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'ru_jet_su39_EngineMain' : [
            #'ObjectTemplate.setMaxSpeed 0/0/500',
            #'ObjectTemplate.setAcceleration 0/0/120',
            #'ObjectTemplate.setTorque 140',
            #'ObjectTemplate.setDifferential 140',
            ],
        },
    
    }