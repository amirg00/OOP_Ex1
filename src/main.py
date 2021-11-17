import argparse
import math
from Building import Building
from Calls import Calls
from Algorithm import Algorithm


def main():
    parser = argparse.ArgumentParser(description='offline elevator.')
    parser.add_argument('building', help='json file that contains the building')
    parser.add_argument('calls', help='csv file that contains the calls')
    parser.add_argument('output', help='csv file')
    args = parser.parse_args()
    building = Building(args.building)
    calls = Calls(args.calls)
    algo = Algorithm(calls.copy_of_round_calls, building.elevators, calls.calls)
    algo.to_main()
    calls.allocated_calls(algo.original_calls)
    # algo.print_calls()
    calls.print_round_calls()
    calls.update_output(args.output)
    print (calls.calls)


if __name__ == "__main__":
    main()
