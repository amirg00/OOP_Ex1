# ----------------------------------------------------------------------------
# Title:  Offline Elevator Scheduling Algorithm - Python
# Author: Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------

from enum import Enum
from Calls import Calls
from copy import deepcopy


# possible elevator's states:
class States(Enum):
    UP = 1
    DOWN = -1
    LEVEL = 0


# the class has to implement the calculation for the optimal arrival time.
class Algorithm:
    def __init__(self, calls, elevators, original_calls):
        """
            The constructor gets the calls, the original calls with the original time stamps,
            and the elevators.

            Parameters
            ----------
            calls : list
                the list of the rounded up calls' time stamps
            elevators : list
                the list of the elevators
            original_calls: list
                the list of original calls
            Returns
            -------
            None
        """
        self.calls = calls
        self.elevators = elevators
        self.original_calls = original_calls
        # an index indicates the current call.
        self.call_index = 0

    def algo_main(self):
        """
            The function goes over the calls, and allocates each to the optimal
            elevator, considering the class' calculations. This is the reason
            why we called it as a "main" function, because the main process is
            conducted by this function.

            Returns
            -------
            None
        """
        for call in self.calls:
            self.calculate_update_time(self.elevators, call)
            self.min_time_with_call()
            self.call_index += 1

    def calculate_update_time(self, elevators, call):
        """
            the function goes over the elevators, and for each checks first, whether
            the elevator has already calls or not. If so, then it inserts first,
            otherwise it means that the elevator has already calls. If it has calls
            then we shall check if the elevator would succeed fulfilling the call before
            going to destination. If so, the method merges the calls, otherwise it adds
            the call to the end of the elevator's copy lists.

            Parameters
            ----------
            elevators : list
                the list of the elevators
            call :
                the current call

            Returns
            -------
            None
        """
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
                else:
                    self.add_to_end(elev, call, d1)

    def insert_first(self, elev, call):
        """
            The function insert the first call, when the elevator time stamps and calls lists are empty.

            Therefore, the function inserts as the following:
                    call(src,dest) with copy_calls = [] -> copy_calls = [src,dest]

            and it also calculates the evaluated arrival time, by considering Boaz's simulator/cmd,
            when all the elevators are located at first at floor 0.
            Doing the following:
                              t1 = call_timestamp
                              total = t1 + time(0 -> src) + time(src -> dest)
                              -> time_stamps_copy = [t1,total]

            Parameters
            ----------
            elev :
                the current elevator
            call :
                the current call
            Returns
            -------
            None
        """
        elev.time_stamps_copy.append(call[1])
        time = call[1] + elev.get_time_for_call(0, call[2]) + elev.get_time_for_call(call[2], call[3])
        elev.time_stamps_copy.append(time)
        elev.copy_calls.append(call[2])
        elev.copy_calls.append(call[3])

    def merge_calls(self, elev, s1, d1, s2, d2, call):
        """
            Here the function considers the case in which the elevator suffices
            reaching the current call, before reaching its destination.

            Additionally, four sub-cases are considered:
                1.
                2.
                3.

            Regarding to the other sub-cases, we would have to add the call to the end of elevator's lists,
            because Boaz's cmd doesn't allow to merge up call with down calls, when the elevator
            first fulfills one direction calls and once she done with those calls, she is allowed
            switching a direction.

            Parameters
            ----------
            elev :
                the current elevator
            s1 :
                the source of the last call of the elevator
            d1 :
                the destination of the last call of the elevator
            s2 :
                the current call's source
            d2 :
                the current call's destination
            call :
                the current call
            Returns
            -------
            None
        """
        # (2 -> 8) + (4 -> 8) = (2 -> 4) + (4 -> 8)
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
        """
            The function's goal is to insert the current call to be the last call which
            the elevator fulfills.

            Therefore, it checks the following:
                1. if the call time

            Parameters
            ----------
            elev :
                the current elevator
            call :
                the current call
            d1: int
                the destination of the last call inside the elevator's list

            Returns
            -------
            None
        """
        if call[1] > elev.time_stamps_copy[len(elev.time_stamps_copy) - 1]:
            elev.time_stamps_copy.append(call[1])
            time = call[1] + elev.get_time_for_call(d1, call[2]) \
                   + elev.get_time_for_call(call[2], call[3])
        else:
            time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1] + elev.get_time_for_call(d1, call[2])
            elev.time_stamps_copy.append(time)
            time = time + elev.get_time_for_call(call[2], call[3])
        elev.time_stamps_copy.append(time)
        elev.copy_calls.append(call[2])
        elev.copy_calls.append(call[3])

    def min_time_with_call(self):
        """
            The function goes over the elevators times list, and checks which elevator
            has the minimal time with the current call. Finally, the function updates allocation value
            of the call with the id of the elected elevator, and updates the original calls
            and times of the optimal elevator with the copies, including the current call,
            then resets elevators' time stamps list and calls copies for the next incoming call.

            Returns
            -------
            None
        """
        min_elev = self.elevators[0]
        min_time = self.elevators[0].time_stamps_copy[len(self.elevators[0].time_stamps_copy) - 1]
        for elev in self.elevators:
            curr_time = elev.time_stamps_copy[len(elev.time_stamps_copy) - 1]
            if curr_time < min_time:
                min_elev = elev
                min_time = curr_time

        self.original_calls[self.call_index][5] = min_elev.id
        min_elev.time_stamps = deepcopy(min_elev.time_stamps_copy)
        min_elev.associated_calls = deepcopy(min_elev.copy_calls)

        for elev in self.elevators:
            elev.time_stamps_copy = []
            elev.copy_calls = []
