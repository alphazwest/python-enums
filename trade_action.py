from enum import unique, Enum

@unique
class TradeAction(Enum):
    """Defines the actions a Trader can take"""
    BUY = 0
    SELL = 1

    @staticmethod
    def get_action_from_name(name: str) -> "TradeAction":
        """
        Given a string name of an action e.g. Buy, Sell, Hold, return the
        associated trade action.
        """
        if name.lower() == "buy":
            return TradeAction.BUY
        if name.lower() == "sell":
            return TradeAction.SELL
        raise Exception(
            f"No TradeAction found for: {name}."
            f"Must be lowercase form of the following: "
            f"{[a.name for a in TradeAction]}")

    @staticmethod
    def get_action_from_value(value: int) -> "TradeAction":
        """
        Given an integer value, map to the associated TradeAction
        """
        for action in TradeAction:
            if action.value == value:
                return action
        raise Exception(
            f"No TradeAction associated with the value: {value}."
            f"Available choices: {[a.value for a in TradeAction]}")

    def __eq__(self, other):
        """
        TradeActions are compared by their values for easy integration with Torch
        """
        if not isinstance(other, (TradeAction, int, str)):
            return False

        # direct comparison
        if isinstance(other, TradeAction):
            return other.value == self.value

        # values == names
        if isinstance(other, int):
            return self.value == other

        # case-insensitive string matching
        if isinstance(other, str):
            return self.name.lower() == other.lower()
