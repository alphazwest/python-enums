from unittest import TestCase
import TradeAction


class TestTradeAction(TestCase):
    """Tests the TradeAction Enum class"""
    def test_unique(self):
        """Test each member has unique value"""
        names = set()
        values = set()
        for name in TradeAction:
            if name.name in names:
                self.fail()
            else:
                names.add(name.name)

            if name.value in values:
                self.fail()
            else:
                values.add(name.value)
                
    def test_get_action_from_name(self):
        """Test a TradeAction can be retrieved from the associated name"""
        for action in TradeAction:
            self.assertEqual(
                action, TradeAction.get_action_from_name(action.name)
            )

    def test_get_action_from_value(self):
        """Test a TradeAction can be retrieved from the associated value"""
        for action in TradeAction:
            self.assertEqual(
                action, TradeAction.get_action_from_value(action.value)
            )
            
    def test_custom_eq(self):
        """Test the custom equality measures of the TradeAction"""
        buy = TradeAction.BUY
        sell = TradeAction.SELL
        
        # case 1: TradeAction objects should be directly comparable
        self.assertEqual(buy, TradeAction.BUY)
        self.assertEqual(sell, TradeAction.SELL)
        
        # case 2: TradeAction objects should be comparable via the integer value
        self.assertEqual(buy.value, TradeAction.BUY)
        self.assertEqual(sell.value, TradeAction.SELL)
        
        # case 3: TradeAction objects should be comparable via raw strings, in
        # a case-insensitive manner
        self.assertEqual(buy.name.upper(), TradeAction.BUY)
        self.assertEqual(buy.name.lower(), TradeAction.BUY)
        self.assertEqual(buy.name.title(), TradeAction.BUY)
        self.assertEqual(sell.name.upper(), TradeAction.SELL)
        self.assertEqual(sell.name.lower(), TradeAction.SELL)
        self.assertEqual(sell.name.title(), TradeAction.SELL)
