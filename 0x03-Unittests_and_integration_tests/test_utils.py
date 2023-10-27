#!/usr/bin/env python3
""" 0. Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Sequence, Union


class TestAccessNestedMap(unittest.TestCase):
    """Suite of tests for access_nested_map.
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Sequence,
                               expctd_rslt: Union[int, Dict]) -> Any:
        """Tests access_nested_map."""
        self.assertEqual(access_nested_map(nested_map, path), expctd_rslt)


if __name__ == '__main__':
    unittest.main()
