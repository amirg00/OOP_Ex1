# ----------------------------------------------------------------------------
# Title:  Offline Elevator Scheduling Algorithm - Python
# Author: Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------

import math


class Elevator:

    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        """
            The constructor initialize properties of the elevator.

            Parameters
            ----------
            id : int
                the id number of the current elevator
            speed : float
                the speed of the current elevator
            min_floor : int
                the minimum floor of the current elevator
            max_floor : int
                the name of the file
            close_time : float
                the close time of the current elevator
            open_time : float
                the open time of the current elevator
            start_time : float
                the start time of the current elevator
            stop_time : float
                the stop time of the current elevator
            Returns
            -------
            None
        """
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        # the associated calls list contains all calls that have optimal time with the current elevator.
        self.associated_calls = []
        # copy_calls = the copy of the associated calls list.
        self.copy_calls = []
        # the time stamps list
        self.time_stamps = []
        # the copy of the time stamp list
        self.time_stamps_copy = []

    def get_time_for_call(self, src, dest):
        """
            The function calculates the amount of time for the current elevator object to reach,
            with a call from the src floor to the dest floor.

            Parameters
            ----------
            src : int
                the source of the call
            dest : int
                the destination of the call

            Returns
            -------
            float := returns the calculated amount of arrival time, for the given call with curr elevator.

            Notes
            -------
            the function rounds up the the calculation, because that's how Boaz's simulator works.
        """
        if src == dest:
            return 0
        return math.ceil(self.stop_time + self.start_time + self.close_time + self.open_time + (abs(dest - src) / self.speed))
