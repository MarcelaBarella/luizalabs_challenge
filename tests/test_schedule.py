import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from assertpy import assert_that

from domain.schedule import Schedule

class SchedulesTest(unittest.TestCase):
    def setUp(self):
        self.first_schedule = Schedule({'begin': '20/11/2016 13:00', 'end': '20/11/2016 15:00'})
        self.second_schedule = Schedule({'begin': '20/11/2016 13:00', 'end': '20/11/2016 16:00'})

    def test_colides_with_other_schedule_equals_begin_datetime(self):
        assert_that(self.first_schedule.colides_with_other_schedule(self.second_schedule)).is_true()

    def test_colides_with_other_schedule_begin_between_begin_and_end_of_other(self):
        self.second_schedule.set_begin('20/11/2016 13:30')
        assert_that(self.first_schedule.colides_with_other_schedule(self.second_schedule)).is_true()

    def test_colides_with_other_schedule_equals_ends(self):
        self.second_schedule.set_begin('20/11/2016 09:00')
        self.second_schedule.set_end('20/11/2016 15:00')
        assert_that(self.first_schedule.colides_with_other_schedule(self.second_schedule)).is_true()

    def test_colides_with_other_other_ends_on_begin_of_self(self):
        self.second_schedule.set_begin('20/11/2016 09:00')
        self.second_schedule.set_end('20/11/2016 13:00')
        assert_that(self.first_schedule.colides_with_other_schedule(self.second_schedule)).is_true()

if __name__ == '__main__':
    unittest.main()