import math


class Elevator:

    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.associated_calls = []
        self.copy_calls = []
        self.time_stamps = []
        self.time_stamps_copy = []
        self.curr_total_time = 0

    def get_stop_time(self):
        return int(math.ceil(self.stop_time + self.start_time + self.close_time + self.open_time))

    def get_time_for_call(self, src, dest):
        return math.ceil(self.stop_time + self.start_time + self.close_time + self.open_time + (abs(dest - src) / self.speed))
