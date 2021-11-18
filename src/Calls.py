# ----------------------------------------------------------------------------
# Title:  Offline Elevator Scheduling Algorithm - Python
# Author: Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------

import csv
from copy import deepcopy
import math


class Calls:
    def __init__(self, file_name):
        """
            The constructor initialize the file name property with the csv file name, represent the calls,
            it gets. In addition, the function is also responsible to read the csv file, case cast
            the call values from string to their actual value, and make a copy of the calls with up
            rounded time stamps.
            ----------
            file_name: str
                the name of the csv file to read from
            Returns
            -------
            None
        """
        self.calls = []
        self.csv_reader(file_name)
        self.cast_calls_values()
        self.copy_of_round_calls = deepcopy(self.calls)
        self.round_call_timestamps()

    def csv_reader(self, file_name):
        """
            the function gets the file name, and reads row by row, the file via the csv reader,
            after reading each row, the function appends each row to the calls list,
            because each row is a call in the csv file.
            Parameters
            ----------
            file_name: str
                the name of the csv file to read from
            Returns
            -------
            None
        """
        calls = []
        with open(file_name) as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                calls.append(row)
        self.calls = calls

    def update_output(self, csv_file):
        """
            By the given name of the csv file, the function updates all call
            to the given csv output file, with the csv writer.
            Parameters
            ----------
            csv_file: str
                the name of the csv file to update the calls on it
            Returns
            -------
            None
        """
        with open(csv_file, "w") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(self.calls)

    # The method rounds each timestamp for each call over the copy list of the calls.
    def round_call_timestamps(self):
        """
            the function goes over all the calls in the copy and rounds up each calls' timestamp.
            Parameters
            ----------
            Returns
            -------
            None
        """
        for element in self.copy_of_round_calls:
            element[1] = int(math.ceil(float(element[1])))

    @staticmethod
    def check_call_state(src, dest):
        """
            the function checks the call's state, then returns:
                1) 1 = UP if the src is smaller than the dest because it is an UP call.
                2) -1 = Down if the src is bigger than the destination, because it's a DOWN call.
            Parameters
            ----------
            src : int
                the source of a certain call
            dest : int
                the destination of a certain call
            Returns
            -------
            int
        """
        return 1 if src < dest else -1

    def allocated_calls(self, calls):
        """
            the function copies the allocated calls to the calls list.
            Parameters
            ----------
            calls: list
                the list contains the calls
            Returns
            -------
            None
        """
        self.calls = deepcopy(calls)

    def cast_calls_values(self):
        """
            The function goes over all calls and cast the following strings values:
                1. call[1] = the time stamp of the call (supposed to be a float value)
                2. call[2] = the source floor of the call (an integer number)
                3. call[3] = the destination floor of the call (an integer number)
                4. call[5] = the allocated elevator id (an integer number)

            each one of these is casted from string to his real value type by the function.
            Parameters
            ----------
            Returns
            -------
            None
        """
        for call in self.calls:
            call[1] = float(call[1])
            call[2] = int(call[2])
            call[3] = int(call[3])
            call[5] = int(call[5])
