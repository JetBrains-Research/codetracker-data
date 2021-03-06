# Copyright (c) 2020 Anastasiia Birillo, Elena Lyulina

from typing import Callable, Tuple, List

import pytest

from src.test.test_config import to_skip, TEST_LEVEL
from src.main.util.strings_util import contains_any_of_substrings

string = 'Roses are red, violets are blue, sugar is sweet, and so are you'
contained_substrings = ['red', 'blue']
partly_contained_substrings = ['mint', 'candy', 'sugar']
not_contained_substrings = ['parsley', 'sun']


@pytest.mark.skipif(to_skip(current_module_level=TEST_LEVEL.UTIL), reason=TEST_LEVEL.UTIL.value)
class TestContainingSubstrings:

    @staticmethod
    @pytest.fixture(scope="function",
                    params=[
                        (contained_substrings, True),
                        (partly_contained_substrings, True),
                        (not_contained_substrings, False)
                    ])
    def param_contained_substrings_test(request) -> Tuple[List[str], bool]:
        return request.param

    def test_contained_substrings(self, param_contained_substrings_test: Callable) -> None:
        (in_data, expected_res) = param_contained_substrings_test
        assert contains_any_of_substrings(string, in_data) == expected_res
