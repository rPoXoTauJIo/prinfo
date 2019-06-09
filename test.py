# test file to verify some shit outside bf2, too lazy to launch
import os
import sys
import errno

import mocksbf2

# work around for bf2&pr modules imports
def mock_bf2_imports(root, mod):
    host = mocksbf2.DummyHost(root, mod)
    sys.modules['host'] = host
    sys.modules['bf2'] = host.bf2
    sys.modules['game'] = host.game
    sys.modules['game.realityadmin'] = host.game.realityadmin
    sys.modules['game.realitytimer'] = host.game.realitytimer
    import prinfo

    return prinfo, host

def guess_PR_path(workdir):
    parts = os.path.normpath(workdir).split(os.sep)
    parts_root = []
    for part_id, part in enumerate(parts):
        if part == 'mods':
            mod = parts[part_id + 1]
            break
        parts_root.append(part)
    root = os.sep.join(parts_root)
    modPath = os.path.join(root, 'mods', mod)

    if 'PRBF2.exe' not in os.listdir(root): raise IOError('Could not find PRBF2.exe in %s' % root)
    moditems = os.listdir(modPath)
    if 'levels' not in moditems: raise IOError('Could not find levels in %s' % modPath)
    if 'clientarchives.con' not in moditems: raise IOError('Could not find clientarchives.con in %s' % modPath)
    if 'serverarchives.con' not in moditems: raise IOError('Could not find serverarchives.con in %s' % modPath)
    return root, mod

def main():
    workdir = os.getcwd()
    root, mod = guess_PR_path(workdir)
    prinfo, _ = mock_bf2_imports(root, mod)

    prinfo.WatchVehicle.switchLogging('', mocksbf2.DummyPlayer('rpoxo'))
    position = (0.0123123, -123.0123123, 612.0123123)
    rotation = (0.0123123, -123.0123123, 612.0123123)
    epoch = 123123.0123123
    msg = 'position: %s\nrotation: %s\nepoch: %s' % (position, rotation, epoch)
    print(msg)

if __name__ == '__main__':
    main()