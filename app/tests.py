import unittest


class TestDateDictNavigation(unittest.TestCase):
    test_dates_dict = {2015: {1: {10: "Data",
                                  15: "Data"},
                              2: {20: "Data"}},
                       2016: {4: {25: "Data"},
                              5: {26: "Data"}}}

    def test_next_day(self):
        from utils import has_next_day
        self.assertTrue(has_next_day(self.test_dates_dict, 2015, 1, 10))
        self.assertTrue(has_next_day(self.test_dates_dict, 2015, 1, 15))
        self.assertTrue(has_next_day(self.test_dates_dict, 2015, 2, 20))
        self.assertFalse(has_next_day(self.test_dates_dict, 2016, 5, 26))

    def test_previous_day(self):
        from utils import has_previous_day
        self.assertFalse(has_previous_day(self.test_dates_dict, 2015, 1, 10))
        self.assertTrue(has_previous_day(self.test_dates_dict, 2015, 1, 15))
        self.assertTrue(has_previous_day(self.test_dates_dict, 2015, 2, 20))
        self.assertTrue(has_previous_day(self.test_dates_dict, 2016, 4, 25))

if __name__ == '__main__':
    unittest.main()
