# test file to plot historical data on minimap

import sys
import datetime
import re

try:
    import PIL
    from PIL import Image, ImageDraw
except ImportError:
    print('could not import Pillow')
    print(sys.exc_info()[0])
    exit(1)

def usage():
    print('Usage:')
    print(' plot.py logfile minimap.dds out')
    print('         logfile -historical data')
    print('         minimap.dds -path to image plot over, DDS format')
    print('         scale -decimal for map scale, base of 2')
    print('         out -OPTIONAL output image file')

logfile = sys.argv[1]
minimap = sys.argv[2]
size = sys.argv[3]
size = int(size) * 1024.0
if len(sys.argv) < 5:
    filename_out = 'plot_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M_%S") + '.png'
else:
    filename_out = sys.argv[-1]

class Frame:
    def __init__(self, x, y, z, yaw, pitch, roll, epoch):
        self.position = tuple([float(value) for value in [x, y, z]])
        self.rotation = tuple([float(value) for value in [yaw, pitch, roll]])
        self.epoch = epoch

pattern = r''
pattern = r'position: [(](?P<x>[-+]?\d+.\d+), (?P<y>[-+]?\d+.\d+), (?P<z>[-+]?\d+.\d+)[)]\n'
pattern += r'rotation: [(](?P<yaw>[-+]?\d+.\d+), (?P<pitch>[-+]?\d+.\d+), (?P<roll>[-+]?\d+.\d+)[)]\n'
pattern += r'epoch: (?P<epoch>\d+.\d+)\n'
RE = re.compile(pattern, re.MULTILINE)

frames = []
with open(logfile) as fo:
    matches = re.finditer(RE, fo.read())
    for match in matches:
        frames.append(Frame(**match.groupdict()))

frames.sort(key=lambda frame: frame.epoch)

image = Image.open(minimap)
draw = ImageDraw.Draw(image)

# plot x, z
positions = [(frame.position[0], frame.position[2]) for frame in frames]

# scale them to image size
scale = image.size[0] / size
positions = [tuple(val*scale for val in position) for position in positions]

# offset, bf2 calc from center, PIL from top-left
offset = image.size[0] / 2, image.size[1] / 2
positions = [tuple(x+z for x, z in zip(position, offset)) for position in positions]

# mirror vertically
positions = [tuple((position[0], image.size[0] - position[1])) for position in positions]

# center for debug
position = (0.0, 0.0)
center = tuple(x+z for x, z in zip(position, offset))
reticle_len = 10
ellipes_top_left = tuple(val-reticle_len for val in center)
ellipes_bottom_right = tuple(val+reticle_len for val in center)
position = (ellipes_top_left, ellipes_bottom_right)
draw.ellipse(xy=position, fill=None, outline='blue', width=2)

draw.line(xy=positions, fill='red', width=2)
image.save(filename_out)