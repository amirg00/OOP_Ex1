import argparse

from Building import Building
from Calls import Calls


def main():
    parser = argparse.ArgumentParser(description='offline elevator.')
    parser.add_argument('building', help='json file that contains the building')
    parser.add_argument('calls', help='csv file that contains the calls')
    parser.add_argument('output', help='csv file')
    args = parser.parse_args()
    building = Building(args.building)
    calls = Calls(args.calls)
    #print (calls.calls)


if __name__ == "__main__":
    main()
