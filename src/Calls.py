import csv


class Calls:
    def __init__(self, file_name):
        self.calls = []
        self.csv_reader(file_name)

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
