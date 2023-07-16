from enum import Enum, unique

@unique
class Frequency(Enum):
    """
    Constants used in conveying the resolution of Time-series data common 
    among financial data APIs and services.
    Note:
        - Values are not to be assumed valid for use with any API w/o custom
          mapping considerations. For example. Binance's API represents the
          period "Month" using the "M" char and period "Minute" using "m"
        - Not to be confused with Pandas Offset Frequency:
          https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
        - the "unique" decorator is only a half-measure here as it will allow
          multiple values to be duplicated in members, just not *both*. For
          example: ("1h", 3600) is not considered duplicate to ("60m", 3600)
          even though the seconds' value is problematically so.

    """
    MIN_1    = ("1m",   60)
    MIN_2    = ("2m",   120)
    MIN_3    = ("3m",   180)
    MIN_5    = ("5m",   300)
    MIN_15   = ("15m",  900)
    MIN_30   = ("30m",  1800)
    MIN_90   = ("90m",  5400)
    HOUR_1   = ("1h",   3600)
    HOUR_2   = ("2h",   7200)
    HOUR_4   = ("4h",   14_400)
    HOUR_6   = ("6h",   21_600)
    HOUR_8   = ("8h",   28_800)
    HOUR_12  = ("12h",  43_200)
    DAY_1    = ("1d",   86_400)
    DAY_3    = ("3d",   259_200)
    DAY_5    = ("5d",   432_000)
    WEEK_1   = ("1w",   604_800)

    def as_string(self) -> str:
        """
        Return a member's <str> value e.g. ("1h", 3600) == "1h"
        """
        return self.value[0]

    def __str__(self):
        return self.as_string()

    def as_seconds(self) -> int:
        """
        Return a member's <int> value e.g. ("1h", 3600) == 3600
        """
        return self.value[1]

    @staticmethod
    def frequency_from_str(freq_str: str) -> "Frequency":
        """
        Given a string representation of a Frequency like e.g. 1m, return
        the associated Frequency member such as e.g. MIN_1
        """
        for member in Frequency:
            if member.as_string() == freq_str.lower():
                return member
        raise Exception(
            f"Frequency not found for string: {freq_str}"
        )

    @staticmethod
    def frequency_from_secs(secs: int) -> "Frequency":
        """
        Given an amount of seconds, return the Frequency member matching that
        value or raise an exception if no match.
        """
        for member in Frequency:
            if member.as_seconds() == secs:
                return member
        raise Exception(f"Frequency match not found for seconds value: {secs}")
