# the class has to implement the calculation for the optimal arrival time.
from enum import Enum
from Calls import Calls
from copy import deepcopy

# possible elevator's states:
class States(Enum):
    UP = 1
    DOWN = -1
    LEVEL = 0

class Algorithm:

    def __init__(self,calls,elevators):
        self.calls = calls
        self.elevators = elevators



    def calculate_update_time(self,elevators,call):
        for elev in elevators:
            if len(elev.associated_calls) == 0:
                    self.insert_first(elev,call)
            else:
                t1 = elev.time_stamps[len(elev.time_stamps)-2]
                t2 = call[1]
                s1 = elev.associated_calls[len(elev.associated_calls)-2]
                d1 = elev.associated_calls[len(elev.associated_calls)-1]
                s2 = call[2]
                d2 = call[3]
                floors = abs(s2-s1)

                if t1 < t2 and Calls.check_call_state(s1,d1) == Calls.check_call_state(s2,d2) :
                    if t1 + floors/elev.speed > t2:
                        self.merge_calls(elev, call)
                    else:
                        self.add_to_end(elev, call, d1)





    def insert_first(self,elev,call):
         elev.time_stamps_copy.append(call[1])
         time = call[1] + elev.get_time_for_call(self, 0, call[2]) + elev.get_time_for_call(self, call[2], call[3])
         elev.time_stamps_copy.append(time)
         elev.copy_calls.append(call[2])
         elev.copy_calls.append(call[3])


    def merge_calls(self, elev, call):


    def add_to_end(self, elev, call, d1):
        elev.time_stamps_copy.append(call[1])
        time = call[1] + elev.get_time_for_call(self, d1, call[2]) \
               + elev.get_time_for_call(self, call[2], call[3])
        elev.time_stamps_copy.append(time)
        elev.copy_calls.append(call[2])
        elev.copy_calls.append(call[3])

    def min_time_with_call(self):
        min_elev = self.elevators[0]
        min_time = self.elevators[0].time_stamps_copy[len(self.elevators[0].time_stamps_copy)-1]
        for elev in self.elevators:
            curr_time = elev.time_stamps_copy[len(elev.time_stamps_copy)-1]
            if curr_time < min_time:
                min_elev = elev
                min_time = curr_time

        min_elev.time_stamps = deepcopy(min_elev.time_stamps_copy)
        min_elev.copy_calls = deepcopy(min_elev.copy_calls)

        #reset of all time stamps lists and calls copies for next call:
        for elev in self.elevators:
            elev.time_stamps_copy = []
            elev.copy_calls = []


