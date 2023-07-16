from unittest import TestCase
from .http_status import HTTPStatus


class TestHTTPStatus(TestCase):
    """Test suite for the HTTP Status Enum class"""

    def test_code(self):
        """
        Test code method returns the expected value
        """
        for status in HTTPStatus:
            self.assertEqual(status.value[0], status.code())

    def test_desc(self):
        """
        Test the method returns the description
        """
        for status in HTTPStatus:
            self.assertEqual(status.value[1], status.desc())

    def test_get_from_code(self):
        """Test HTTPStatus objects are retrievable via a code"""
        for status in HTTPStatus:
            self.assertEqual(
                status.code(), HTTPStatus.get_from_code(status.code()).code()
            )

    def test_eq(self):
        """
        Test custom equality comparisons
        """
        for status in HTTPStatus:
            self.assertTrue(
                status.code() == HTTPStatus.get_from_code(status.code()))

    def test_gt(self):
        """
        Test custom greater-than method
        """
        for status in HTTPStatus:

            code = status.code()
            compare = HTTPStatus.get_from_code(status.code())

            # value is less
            self.assertFalse(code - 1 > compare)

            # value is equal
            self.assertFalse(code > compare)

            # value is greater
            self.assertTrue(code + 1 > compare)

    def test_ge(self):
        """
        Test custom greater-than-or-equal method
        """
        for status in HTTPStatus:

            code = status.code()
            compare = HTTPStatus.get_from_code(status.code())

            # value is less
            self.assertFalse(code - 1 >= compare)

            # value is equal
            self.assertTrue(code >= compare)

            # value is greater
            self.assertTrue(code + 1 >= compare)

    def test_lt(self):
        """
        Test custom less-than comparison
        """
        for status in HTTPStatus:

            code = status.code()
            compare = HTTPStatus.get_from_code(status.code())

            # value is less
            self.assertTrue(code - 1 < compare)

            # value is more
            self.assertFalse(code + 1 < compare)

            # value is equal
            self.assertFalse(code < compare)

    def test_le(self):
        """Test the custom less-than-or-equal method"""
        for status in HTTPStatus:

            code = status.code()
            compare = HTTPStatus.get_from_code(status.code())

            # lte - value is less
            self.assertTrue(code - 1 <= compare)

            # lte - value is equal
            self.assertTrue(code <= compare)

            # value is greater
            self.assertFalse(code + 1 <= compare)
