# test file to verify some math

from math3d import Point3

pos_last = (-213.531235, 364.275757, -638.474731)
pos_curr = (-233.400757, 367.863708, -652.031128)
last = 224.386581
curr = 224.516510


samples = [
    {
       'position_last' : (0.0, 0.0, 0.0),
       'position_curr' : (0.0, 0.0, 0.0),
       'time_last' : 0.0,
       'time_curr' : 0.1
    },
    {
       'position_last' : (-213.531235, 364.275757, -638.474731),
       'position_curr' : (-233.400757, 367.863708, -652.031128),
       'time_last' : 224.386581,
       'time_curr' : 224.516510
    },
    {
       'position_last' : (-658.850098, 338.604614, -83.169693),
       'position_curr' : (-667.007629, 339.080719, -84.947243),
       'time_last' : 254.162415,
       'time_curr' : 254.292343
    },
    {
       'position_last' : (415.253814497, 535.726684570, -329.567199707),
       'position_curr' : (421.402923584, 533.729553223, -345.641998291),
       'time_last' : 0.0,
       'time_curr' : 0.100098
    },
]

def speed(data):
    pos_last = data['position_last']
    pos_curr = data['position_curr']
    time_last = data['time_last']
    time_curr = data['time_curr']
    
    delta = time_curr - time_last

    distance = Point3.Distance(Point3(*pos_curr), Point3(*pos_last))
    print('distance: %f' % distance)
    speed = distance / delta
    
    return speed

for sample in samples:
    print(speed(sample))