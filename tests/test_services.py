import unittest
import assertpy import assert_that

from services import Service


class SchedulesTest(unittest.TestCase):
    def test_save_schedule_is_persisting_data(self):
        expected_result = { 'title': 'Test save_schedule',
                            'participants': 'Over capacity',
                            'beginning': 'date',
                            'end': 'date'}

        assert_that(Service.save_schedule()).is_equal_to(expected_result)


    def test_save_schedule_returning_200_state():
        pass
    
    def test_save_schedule_returning_422_state():
        pass
