#!/usr/bin/env python3
""" 0. Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
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
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        """Tests the output of the function get_json."""
        attrs = {'json.return_value': payload}
        with patch("requests.get", return_value=Mock(**attrs)) as fetched:
            self.assertEqual(get_json(url), payload)
            fetched.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Suite of tests for the memoize function"""
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as fn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            fn.assert_called_once()


if __name__ == '__main__':
    unittest.main()
