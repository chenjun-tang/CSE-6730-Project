from typing import Dict
import Vehicle

class BasicLane(object):
    def __init__(self, ID):
        self.ID = ID
        self.tail: Vehicle = None
        self.capacity: int = 0

        # This is used to connect a lane to its downstream lane
        self.exitLane = Dict[Vehicle.Intention, BasicLane]
