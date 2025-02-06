import unittest
from unittest import TestCase

from HW_Collections.ya_api import YandexDisk
from data_ya import token

ya = YandexDisk(token)

dir = 'unittest'

class TestYaAPI(TestCase):
    @unittest.expectedFailure
    def test_1(self):
        result = ya.create_dir(dir)
        self.assertEqual(result, 201)

    def test_2(self):
        check_ya = ' '.join(ya.get_list_dir())
        self.assertIn(dir, check_ya)




