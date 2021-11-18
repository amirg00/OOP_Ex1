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
        self.calls = []
        self.csv_reader(file_name)
        self.cast_calls_values()
        self.copy_of_round_calls = deepcopy(self.calls)
        self.round_call_timestamps()

    def csv_reader(self, file_name):
        calls = []
        with open(file_name) as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                calls.append(row)
        self.calls = calls

    def update_output(self, csv_file):
        with open(csv_file, "w") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(self.calls)

    # The method rounds each timestamp for each call over the copy list of the calls.
    def round_call_timestamps(self):
        for element in self.copy_of_round_calls:
            element[1] = int(math.ceil(float(element[1])))

    @staticmethod
    def check_call_state(src, dest):
        return 1 if src < dest else -1

    def allocated_calls(self, calls):
        self.calls = deepcopy(calls)

    def print_round_calls(self):
        print(self.copy_of_round_calls)

    def cast_calls_values(self):
        for call in self.calls:
            call[1] = float(call[1])
            call[2] = int(call[2])
            call[3] = int(call[3])
            call[5] = int(call[5])
