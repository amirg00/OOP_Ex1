class Elevator(object):
    associated_calls = []
    copy_calls = []
    time_stamps = []
    curr_total_time = 0

    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time

    def get_stop_time(self):
        return int(self.stop_time + self.start_time + self.close_time + self.open_time + 1 / self.speed)


