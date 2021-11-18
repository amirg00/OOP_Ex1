# ----------------------------------------------------------------------------
# Title:  Offline Elevator Scheduling Algorithm - Python
# Author: Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------

import json
from Elevator import Elevator


class Building:
    def __init__(self, file_name):
        """
             The constructor initialize the file name property with the json file name, represent the building,
             it gets. In addition, it also gets a couple properties: minFloor, maxFloor and elevator.
             Afterwards, this constructor calls json_reader with the initialized file name property.

             Parameters
             ----------
             file_name : str
                the name of the file
            Returns
            -------
            None
        """
        self.file_name = file_name
        # minFloor = the lowest floor of the building that the elevator can reach.
        self.minFloor = 0
        # minFloor = the highest floor of the building that the elevator can reach.
        self.maxFloor = 0
        # elevators is a list of all the elevators in the building.
        self.elevators = []
        self.json_reader(self.file_name)

    def json_reader(self, file_name):
        """
            The function gets the name of the json file, save the dictionary of the json file.
            Then, the function goes over the dictionary and update the properties of the class.

            Parameters
            ----------
            file_name : str
                the name of the file
            Returns
            -------
            None
        """
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
