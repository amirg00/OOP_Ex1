import json
from Elevator import Elevator


class Building:
    def __init__(self, file_name):
        self.file_name = file_name
        self.minFloor = 0
        self.maxFloor = 0
        self.elevators = []
        self.json_reader(self.file_name)

    def json_reader(self, file_name):
        try:
            with open(file_name, "r+") as f:
                dictionary = json.load(f)
                self.minFloor = dictionary["_minFloor"]
                self.maxFloor = dictionary["_maxFloor"]
                elev = dictionary["_elevators"]
                for value in elev:
                    self.elevators.append(Elevator(value["_id"], value["_speed"], value["_minFloor"],
                                                   value["_maxFloor"], ["_closeTime"],
                                                   value["_openTime"], value["_startTime"], value["_stopTime"]))
        except IOError as e:
            print (e)

    def number_of_floors(self):
        return self.maxFloor - self.minFloor
