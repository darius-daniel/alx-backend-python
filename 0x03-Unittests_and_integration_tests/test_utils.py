#!/usr/bin/env python3
""" 0. Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Dict, Sequence, Union, Type


class TestAccessNestedMap(unittest.TestCase):
    """Suite of tests for access_nested_map.
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Dict,
            path: Sequence,
            expected: Union[int, Dict]
    ) -> None:
        """Tests access_nested_map."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Sequence,
            expected: Type[KeyError]
    ) -> None:
        """Test KeyError raised by certain inputs"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Suite of tests for utils.get_json"""
    def test_get_json(self):
        pass


if __name__ == '__main__':
    unittest.main()
