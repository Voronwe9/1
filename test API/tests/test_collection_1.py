from unittest import TestCase

from HW_Collections.collection_1 import supernames
from data import names_1, courses
from data import expect_1_test_1


class TestSupernames(TestCase):

    def test_compare_list(self):
        result = supernames(courses=courses, mentors=names_1)
        self.assertListEqual(result, expect_1_test_1)

    def test_compare_regex(self):
        result = supernames(courses=courses, mentors=names_1)

        for a, b in zip(result, expect_1_test_1):
            self.assertRegex(a, b)

        



