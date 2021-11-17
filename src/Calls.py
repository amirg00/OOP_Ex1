import csv
from copy import deepcopy
import math


class Calls:
    def __init__(self, file_name):
        self.calls = []
        self.copy_of_calls = deepcopy(self.calls)
        self.csv_reader(file_name)
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
        for element in self.copy_of_calls:
            self.copy_of_calls[element][1] = int(math.ceil(self.copy_of_calls[element][1]))

    @staticmethod
    def check_call_state(src, dest):
        return 1 if src < dest else -1
