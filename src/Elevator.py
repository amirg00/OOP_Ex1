# ----------------------------------------------------------------------------
# Title:  Offline Elevator Scheduling Algorithm - Python
# Author: Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------
import math


class Elevator:

    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        # the id of the current elevator.
        self.id = id
        # the speed of the current elevator.
        self.speed = speed
        # the minimum floor of the current elevator.
        self.min_floor = min_floor
        # the maximum floor of the current elevator.
        self.max_floor = max_floor
        # the close time of the current elevator.
        self.close_time = close_time
        # the open time of the current elevator.
        self.open_time = open_time
        # the start time of the current elevator.
        self.start_time = start_time
        # the stop time of the current elevator.
        self.stop_time = stop_time
        # the associated calls list contains all calls that have optimal time
        # with the current elevator.
        self.associated_calls = []
        # copy_calls = the copy of the associated calls list.
        self.copy_calls = []
        # the time stamps list
        self.time_stamps = []
        #
        self.time_stamps_copy = []
        self.curr_total_time = 0

    def get_stop_time(self):
        return int(math.ceil(self.stop_time + self.start_time + self.close_time + self.open_time))

    def get_time_for_call(self, src, dest):
        if src == dest:
            return 0
        return math.ceil(self.stop_time + self.start_time + self.close_time + self.open_time + (abs(dest - src) / self.speed))
