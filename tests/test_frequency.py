from unittest import TestCase
import Frequency


class TestFrequency(TestCase):
    """
    Suite of tests for the Frequency Enum class
    """

    def test_unique(self):
        """
        Custom check for the uniqueness of seconds' values from members
        """
        # all members have unique seconds values
        secs = set()
        for member in Frequency:
            _secs = member.as_seconds()
            if _secs in secs:
                self.fail()
            else:
                secs.add(_secs)

        # all members have unique str values
        strs = set()
        for member in Frequency:
            _str = member.as_string()
            if _str in secs:
                self.fail()
            strs.add(_str)

    def test_as_string(self):
        """
        Test getting a Frequency object's <as_string> method behaves as expected.
        """
        for member in Frequency:
            self.assertEqual(
                member.value[0],
                member.as_string()
            )

        # explicit spot checks for known trainer_common entries
        self.assertEqual(Frequency.HOUR_1.as_string(), "1h")
        self.assertEqual(Frequency.DAY_1.as_string(), "1d")
        self.assertEqual(Frequency.MIN_15.as_string(), "15m")
        self.assertEqual(Frequency.WEEK_1.as_string(), "1w")
        self.assertEqual(Frequency.MIN_5.as_string(), "5m")

    def test_as_seconds(self):
        """
        Test getting a Frequency object's <as_seconds> method behaves as expected.
        """
        for member in Frequency:
            self.assertEqual(
                member.value[1],
                member.as_seconds()
            )
        # explicit spot checks for known trainer_common entries
        self.assertEqual(Frequency.HOUR_1.as_seconds(), 3600)
        self.assertEqual(Frequency.DAY_1.as_seconds(), 86400)
        self.assertEqual(Frequency.MIN_15.as_seconds(), 900)
        self.assertEqual(Frequency.WEEK_1.as_seconds(), 604800)
        self.assertEqual(Frequency.MIN_5.as_seconds(), 300)

    def test_str(self):
        """
        Test that Frequency enums are represented by their value (str)
        """
        for member in Frequency:
            self.assertEqual(
                member.__str__(),
                member.as_string()
            )

    def test_frequency_from_str(self):
        """
        Test the frequency_from_str method to assert a valid Frequency member
        is returned when expected and that an appropriate Exception is raised
        when an invalid value is passed.
        """
        # test all members are returned when their value are passed as args
        for member in Frequency:
            self.assertEqual(
                Frequency.frequency_from_str(member.value[0]),
                member
            )

        # test exceptions are raise for invalid members
        with self.assertRaises(Exception):
            member = Frequency.frequency_from_str("1minutely")

    def test_frequency_from_secs(self):
        """
        Test the <frequency_from_seconds> method to assert a valid Frequency
        member is returned.
        """
        # test all members are returned when their value are passed as args
        for member in Frequency:
            self.assertEqual(
                Frequency.frequency_from_secs(member.value[1]),
                member
            )

        # test exceptions are raise for invalid members
        with self.assertRaises(Exception):
            member = Frequency.frequency_from_secs(69420)
