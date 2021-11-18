# ----------------------------------------------------------------------------
# Title:   Offline Elevator Scheduling Algorithm - Python
# Author:  Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------
import argparse
from Building import Building
from Calls import Calls
from Algorithm import Algorithm

LONG_DESCRIPTION = r"""Exercise 1 - OOP

This main manages everything including the following:

        - Parser. the parser gets 3 parameters: json file contains the list
          elevators, the min and max floor of the elevator. In addition, it gets
          a csv file contains the calls, and for the final parameter it gets a csv
          file to have all calls with the allocated elevator column modified.

        - Algorithm. the main is also responsible to run our offline algorithm
          with the building, calls, output parser's parameters, and finally
          update the output file.

This project implements the concepts and purposes are mentioned in Github repository's README.md file.

    * main - the main function of the offline scheduling algorithm.
"""


def main():
    parser = argparse.ArgumentParser(description='Ex1: offline elevator algorithm')
    parser.add_argument('building', help='building json file')
    parser.add_argument('calls', help=' calls csv file')
    parser.add_argument('output', help='scheduled calls csv file')
    args = parser.parse_args()
    building = Building(args.building)
    calls = Calls(args.calls)
    algo = Algorithm(calls.copy_of_round_calls, building.elevators, calls.calls)
    algo.algo_main()
    calls.allocated_calls(algo.original_calls)
    calls.print_round_calls()
    calls.update_output(args.output)


if __name__ == "__main__":
    main()
