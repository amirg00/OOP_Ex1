# ----------------------------------------------------------------------------
# Title:  Offline Elevator Scheduling Algorithm - Python
# Author: Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------
from enum import Enum
from Calls import Calls
from copy import deepcopy
import bisect


# possible elevator's states:
class States(Enum):
    UP = 1
    DOWN = -1
    LEVEL = 0


# the class has to implement the calculation for the optimal arrival time.
class Algorithm:
    def __init__(self, calls, elevators, original_calls):
        self.calls = calls
        self.elevators = elevators
        self.original_calls = original_calls
        self.call_index = 0

    def algo_main(self):
        for call in self.calls:
            self.calculate_update_time(self.elevators, call)
            self.min_time_with_call()
            self.call_index += 1

    def calculate_update_time(self, elevators, call):
        for elev in elevators:
            elev.copy_calls = deepcopy(elev.associated_calls)
            elev.time_stamps_copy = deepcopy(elev.time_stamps)
            if len(elev.associated_calls) == 0:
                self.insert_first(elev, call)
            else:
                t1 = elev.time_stamps[len(elev.time_stamps) - 2]
                t2 = call[1]
                s1 = elev.associated_calls[len(elev.associated_calls) - 2]
                d1 = elev.associated_calls[len(elev.associated_calls) - 1]
                s2 = call[2]
                d2 = call[3]
                floors = abs(s2 - s1)

                if t1 < t2 and Calls.check_call_state(s1, d1) == Calls.check_call_state(s2, d2):
                    if t1 + floors / elev.speed > t2:
                        self.merge_calls(elev, s1, d1, s2, d2, call)
                    else:
                        self.add_to_end(elev, call, d1)
                elif t1 > t2:
                    self.add_to_end(elev, call, d1)
                elif t1 == t2:
                    if Calls.check_call_state(s1, d1) != Calls.check_call_state(s2, d2):
                        self.add_to_end(elev, call, d1)
                    else:
                        print(t1)
                        print (t2)
                        # self.equal_time_stamp(elev, s1, d1, s2, d2, call)
                        self.add_to_end(elev, call, d1)
                else:
                    self.add_to_end(elev, call, d1)
            print (elev.time_stamps_copy)
            print (elev.copy_calls)

    def insert_first(self, elev, call):
        elev.time_stamps_copy.append(call[1])
        time = call[1] + elev.get_time_for_call(0, call[2]) + elev.get_time_for_call(call[2], call[3])
        elev.time_stamps_copy.append(time)
        elev.copy_calls.append(call[2])
        elev.copy_calls.append(call[3])

    def merge_calls(self, elev, s1, d1, s2, d2, call):
        # (2 -> 8) + (4 -> 8) = (2 -> 4) + (4 -> 8)
        print ("dddsddddd")
        print (elev.copy_calls)
        print ("sssssssss")
        d1_time_stamp = elev.time_stamps_copy.pop(len(elev.time_stamps_copy) - 1)
        elev.copy_calls.append(s2)
        time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1] + elev.get_time_for_call(s1, s2)
        elev.time_stamps_copy.append(time)
        if d1 == d2 and (Calls.check_call_state(s1, s2) == States.UP or Calls.check_call_state(s1, s2) == States.DOWN):
            elev.copy_calls.append(s2)
            elev.copy_calls.append(d2)
            time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1] + elev.get_time_for_call(s1, s2)
            elev.time_stamps_copy.append(time)
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(s2, d2)
            elev.time_stamps_copy.append(time)
        elif (Calls.check_call_state(s1, s2) == States.UP and d1 < d2) \
                or (Calls.check_call_state(s1, s2) == States.DOWN and d1 > d2):
            elev.copy_calls.append(d1)
            elev.copy_calls.append(d2)
            time = time + elev.get_time_for_call(s2, d1)
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(d1, d2)
            elev.time_stamps_copy.append(time)
        elif (Calls.check_call_state(s1, s2) == States.UP and d1 > d2) \
                or (Calls.check_call_state(s1, s2) == States.DOWN and d1 < d2):
            elev.copy_calls.append(d2)
            elev.copy_calls.append(d1)
            time = time + elev.get_time_for_call(s2, d2)
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(d2, d1)
            elev.time_stamps_copy.append(time)
        else:
            elev.copy_calls.pop(len(elev.copy_calls) - 1)
            elev.copy_calls.append(d1)
            elev.time_stamps_copy.append(d1_time_stamp)
            self.add_to_end(elev, call, d1)

    def add_to_end(self, elev, call, d1):

        if call[1] > elev.time_stamps_copy[len(elev.time_stamps_copy) - 1]:
            elev.time_stamps_copy.append(call[1])
            time = call[1] + elev.get_time_for_call(d1, call[2]) \
                   + elev.get_time_for_call(call[2], call[3])
            elev.time_stamps_copy.append(time)
            elev.copy_calls.append(call[2])
            elev.copy_calls.append(call[3])
        else:
            time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1] + elev.get_time_for_call(d1, call[2])
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(call[2], call[3])
            elev.time_stamps_copy.append(time)
            elev.copy_calls.append(call[2])
            elev.copy_calls.append(call[3])

    def equal_time_stamp(self, elev, s1, d1, s2, d2, call):
        sorted_list = [s1]
        bisect.insort(sorted_list, d1)
        bisect.insort(sorted_list, s2)
        bisect.insort(sorted_list, d2)
        elev.copy_calls.pop(len(elev.copy_calls) - 1)
        elev.copy_calls.pop(len(elev.copy_calls) - 2)
        elev.time_stamps_copy.pop(len(elev.time_stamps_copy) - 1)

        if len(sorted_list) == 4:
            elev.copy_calls = elev.copy_calls + sorted_list
            time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1] \
                   + elev.get_time_for_call(sorted_list[0], sorted_list[1])
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(sorted_list[1], sorted_list[2])
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(sorted_list[2], sorted_list[3])
            elev.time_stamps_copy.append(time)
        elif len(sorted_list) == 3:
            elev.copy_calls.append(sorted_list[0])
            elev.copy_calls.append(sorted_list[1])
            elev.copy_calls.append(sorted_list[1])
            elev.copy_calls.append(sorted_list[2])
            time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1] \
                   + elev.get_time_for_call(sorted_list[0], sorted_list[1])
            elev.time_stamps_copy.append(time)
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(sorted_list[1], sorted_list[2])
            elev.time_stamps_copy.append(time)

    def min_time_with_call(self):
        min_elev = self.elevators[0]
        min_time = self.elevators[0].time_stamps_copy[len(self.elevators[0].time_stamps_copy) - 1]
        init_time = self.elevators[0].time_stamps_copy[len(self.elevators[0].time_stamps_copy) - 2]
        diff_first = min_time - init_time

        for elev in self.elevators:

            curr_time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1]
            first_time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 2]
            diff = curr_time - first_time

            if curr_time < min_time:
                min_elev = elev
                min_time = curr_time
                diff_first = diff
        self.original_calls[self.call_index][5] = min_elev.id
        min_elev.time_stamps = deepcopy(min_elev.time_stamps_copy)
        min_elev.associated_calls = deepcopy(min_elev.copy_calls)

        # reset of all time stamps lists and calls copies for next call:
        for elev in self.elevators:
            elev.time_stamps_copy = []
            elev.copy_calls = []

    def print_calls(self):
        print(self.original_calls)
