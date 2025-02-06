import pytest
from HW_Collections.collection_3 import unic_name
from data import names_1, names_2, names_3
from data import exp_col_3_test_1, exp_col_3_test_2, exp_col_3_test_3

@pytest.mark.parametrize(
    'mentors, expect', [(names_1, exp_col_3_test_1), (names_2, exp_col_3_test_2), (names_3, exp_col_3_test_3)]
)
def test_1(mentors, expect):
    result = str(unic_name(mentors=mentors))
    assert result == expect

