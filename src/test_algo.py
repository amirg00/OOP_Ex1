# ----------------------------------------------------------------------------
# Title:  Offline Elevator Scheduling Algorithm - Python
# Author: Amir Gillette
# Course: OOP
# ----------------------------------------------------------------------------

import unittest
from Calls import Calls
from Algorithm import Algorithm
from Elevator import Elevator
import math

"""Unit tests for the package."""


class MyTestCase(unittest.TestCase):
    """
        Tests for class: Calls
    """

    def test_round_call_timestamps(self):
        file_name = "test_call_file"
        c = Calls(file_name)
        self.assertEqual(c.copy_of_round_calls[0][1], 5)
        c.copy_of_round_calls = [["Elevator call", 4.37472729, 0, -1, "0", -1],
                                 ["Elevator call", 2.009, 0, -1, "0", -1]]
        c.round_call_timestamps()
        self.assertEqual(c.copy_of_round_calls[0][1], 5)
        self.assertEqual(c.copy_of_round_calls[1][1], 3)

    def test_check_call_state(self):
        src = 3
        dest = 5
        self.assertEqual(Calls.check_call_state(src, dest), 1)  # UP call
        src = 9
        dest = 1
        self.assertEqual(Calls.check_call_state(src, dest), -1)  # DOWN call
        src = 1
        dest = 2
        self.assertEqual(Calls.check_call_state(src, dest), 1)  # Up call
        src = -1
        dest = -2
        self.assertEqual(Calls.check_call_state(src, dest), -1)  # DOWN call

    def test_cast_calls_values(self):
        file_name = "test_call_file"
        c = Calls(file_name)
        c.cast_calls_values()
        self.assertEqual(c.calls, [["Elevator call", 4.37472729, 0, -1, "0", -1]])
        c.calls = [["Elevator call", "4.37472729", "0", "-1", "0", "-1"],
                   ["Elevator call", "2.009", "5", "-10", "0", "-1"]]
        c.cast_calls_values()
        ans = [["Elevator call", 4.37472729, 0, -1, "0", -1], ["Elevator call", 2.009, 5, -10, "0", -1]]
        self.assertEqual(c.calls, ans)

    """
        Tests for class: Elevator
    """

    def test_init_elevator(self):
        e = Elevator(3, 6.0, -2, 10, 4.7, 5.87, 5.333, 2.1)
        self.assertEqual(e.id, 3)
        self.assertEqual(e.speed, 6.0)
        self.assertEqual(e.min_floor, -2)
        self.assertEqual(e.max_floor, 10)
        self.assertEqual(e.close_time, 4.7)
        self.assertEqual(e.open_time, 5.87)
        self.assertEqual(e.start_time, 5.333)
        self.assertEqual(e.stop_time, 2.1)

    def test_get_time_for_call(self):
        e = Elevator(3, 6.0, -2, 10, 4.7, 5.87, 5.333, 2.1)
        delay_time = e.stop_time + e.open_time + e.close_time + e.start_time
        self.assertEqual(delay_time, 4.7 + 5.87 + 5.333 + 2.1)
        velocity = 1 / e.speed
        self.assertEqual(velocity, 1 / 6.0)
        src = 3
        dest = 10
        diff = dest - src
        self.assertEqual(e.get_time_for_call(src, dest), math.ceil(delay_time + velocity * diff))
        src = 3
        dest = 3
        diff = dest - src
        self.assertEqual(e.get_time_for_call(src, dest), diff)
        src = 9
        dest = 5
        diff = src - dest
        self.assertEqual(e.get_time_for_call(src, dest), math.ceil(delay_time + velocity * diff))

    """
        Tests for class: Elevator
    """

    def test_insert_first(self):
        e = Elevator(3, 6.0, -2, 10, 4.7, 5.87, 5.333, 2.1)
        e2 = Elevator(3, 9.0, -2, 10, 3, 2, 4, 1)
        elevators = [e, e2]
        calls = [["Elevator call", 4.37472729, 1, 6, "0", -1],
                 ["Elevator call", 2.009, 0, -1, "0", -1]]
        rounded_calls = [["Elevator call", 5, 1, 6, "0", -1],
                         ["Elevator call", 3, 0, -1, "0", -1]]
        algo = Algorithm(rounded_calls, elevators, calls)
        algo.insert_first(elevators[0], rounded_calls[0])
        copy_calls = [1, 6]
        call_a = math.ceil(4.7 + 5.87 + 5.333 + 2.1 + (6 - 1) / 6.0)  # call[1 -> 6]
        call_b = math.ceil(4.7 + 5.87 + 5.333 + 2.1 + (1 - 0) / 6.0)  # call[0 -> 1]
        t_d1 = 5 + call_a + call_b
        copy_time_stamp = [5, t_d1]
        self.assertEqual(e.copy_calls, copy_calls)
        self.assertEqual(e.time_stamps_copy, copy_time_stamp)
        # lets check the first insertion for e2 with call[0 -> -1]
        algo.insert_first(elevators[1], rounded_calls[1])
        copy_calls = [0, -1]
        call_a = math.ceil(3 + 2 + 4 + 1 + (0 - (-1)) / 9.0)  # call[1 -> 6]
        call_b = 0  # call[0 -> 0]
        t_d1 = 3 + call_a + call_b
        copy_time_stamp = [3, t_d1]
        self.assertEqual(e2.copy_calls, copy_calls)
        self.assertEqual(e2.time_stamps_copy, copy_time_stamp)


if __name__ == '__main__':
    unittest.main()
