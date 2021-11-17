import json
from Elevator import Elevator


class Building:
    def __init__(self, file_name):
        # file name = the name of the file.
        self.file_name = file_name
        # minFloor = the lowest floor of the building.
        self.minFloor = 0
        # minFloor = the highest floor of the building.
        self.maxFloor = 0
        # elevators is a list of all the elevators in the building.
        self.elevators = []
        self.json_reader(self.file_name)

    # The function gets the name of the json file, save the dictionary of the json file.
    # Then, the function goes over the dictionary and update the properties of the class.
    def json_reader(self, file_name):
        try:
            with open(file_name, "r+") as f:
                dictionary = json.load(f)
                self.minFloor = dictionary["_minFloor"]
                self.maxFloor = dictionary["_maxFloor"]
                elev = dictionary["_elevators"]
                for value in elev:
                    self.elevators.append(Elevator(value["_id"], value["_speed"], value["_minFloor"],
                                                   value["_maxFloor"], value["_closeTime"],
                                                   value["_openTime"], value["_startTime"], value["_stopTime"]))
        except IOError as e:
            print (e)

    # The function returns building's number of floors.
    def number_of_floors(self):
        return self.maxFloor - self.minFloor

