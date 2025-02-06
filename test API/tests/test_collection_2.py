from unittest import TestCase

from HW_Collections.collection_2 import top_of_names
from data import names_1, names_2, names_3
from data import exp_col_2_test_1, exp_col_2_test_2, exp_col_2_test_3



class TestTopNames(TestCase):

    def test_1(self):
        result = str(top_of_names(mentors=names_1))
        self.assertMultiLineEqual(result, exp_col_2_test_1)

    def test_2(self):
        result = str(top_of_names(mentors=names_2))
        self.assertMultiLineEqual(result, exp_col_2_test_2)

    def test_3(self):
        result = str(top_of_names(mentors=names_3))
        self.assertMultiLineEqual(result, exp_col_2_test_3)
