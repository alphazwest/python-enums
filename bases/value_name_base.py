from enum import Enum
from typing import List, Tuple

from common.types import Numeric


class ValueNameBase(Enum):
    """
    Base class for Enums that have a Tuple value assigned as:
        (integer value, human-readable name)
    Useful for cases like e.g. Django fields where options are needed.
    """
    def get_value(self) -> Numeric:
        return self.value[0]

    def get_name(self) -> str:
        return self.value[1]

    @staticmethod
    def as_options() -> List[Tuple[Numeric, str]]:
        """
        Returns elements in a list suitable for use as Django model
        fields options as (value, name) e.g. (1, First)
        """
        subclasses = ValueName.__subclasses__()
        members = [member for subclass in subclasses for member in subclass]
        return [(member.get_value(), member.get_name()) for member in members]

    def __eq__(self, other):
        """
        Custom equality method to allow direct comparison by either the integer
        or the string values for an object.
        Note: LT, GT, GTE, LTE, etc bear no significance at this level.
        """
        if not isinstance(other, (ValueName, int, str, float)):
            return False

        # string values may be a string version of an integer or the name of
        # the entity. Cases where a value is (1, "1") would be ambiguous, and
        # the priority is to compare against value first, name second.
        if type(other) == str:

            # stringify version of a numerical value
            try:
                return self.get_value() == float(other)
            except ValueError as e:
                pass

            # otherwise compare the names
            return self.get_name() == other

        if type(other) in (int, float):
            return self.get_value() == other

        return self.value == other.value
