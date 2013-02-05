import unittest
from bitmask import BitMask, BitMaskOptions

class BitMaskUnitTest(unittest.TestCase):

    def test_init(self):
        "It can be initialized given a set of options."

        options = ['a', 'b', 'c']
        BitMaskOptions(options)

    def test_init_mask_with_options(self):
        "The mask can be initialized with a set of options"

        options = BitMaskOptions(['a', 'b', 'c'])
        BitMask(options=options, value=15)

        b = BitMask(options=['a', 'b', 'c'], value=15)
        self.assertEqual(type(b.options), type(options))

class BitMaskManipulateValues(unittest.TestCase):

    def setUp(self):
        self.options = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        self.weekdays = BitMaskOptions(self.options)

    def test_get_options_values(self):
        "The string value of each option can be obtained using properties"

        self.assertEqual(self.weekdays.mon, "mon")
        self.assertEqual(self.weekdays.tue, "tue")
        self.assertEqual(self.weekdays.wed, "wed")

    def test_get_options_int_values(self):
        "The int value of each option can be obtained."

        self.assertEqual(self.weekdays.get_int("mon"), 1)
        self.assertEqual(self.weekdays.get_int("tue"), 2)
        self.assertEqual(self.weekdays.get_int("wed"), 4)

    def test_get_value(self):
        """The value of an option can be retrieved. They all
        start as False"""

        happy_days = BitMask(options=self.weekdays)
        self.assertFalse(happy_days.has(self.weekdays.mon))

    def test_set_value(self):
        "The value of an option can be set"

        happy_days = BitMask(options=self.weekdays)
        happy_days.add(self.weekdays.mon)
        self.assertTrue(happy_days.has(self.weekdays.mon))

    def test_iterate_options(self):
        "One can iterate over the available options"

        options_available = []
        for option in self.weekdays:
            options_available.append(option)

        self.assertEqual(options_available, self.options)

        #twice
        options_available = []
        for option in self.weekdays:
            options_available.append(option)

        self.assertEqual(options_available, self.options)

    def test_query_option(self):
        """If a MaskOptions object was provided, the mask
        can be queried directly"""

        happy_days = BitMask(options=self.weekdays)
        happy_days.add(self.weekdays.mon)
        self.assertTrue(happy_days.has(self.options[0])) # mon

    def test_set(self):
        "A value can be set as enabled"

        happy_days = BitMask(options=self.weekdays)
        happy_days.set(self.weekdays.mon, True)
        self.assertTrue(happy_days.has(self.weekdays.mon))

        happy_days.set(self.weekdays.mon, False)
        self.assertFalse(happy_days.has(self.weekdays.mon))

    def test_set_false(self):
        "A value can be set as disabled"

        happy_days = BitMask(options=self.weekdays)
        happy_days.set(self.weekdays.mon, True)
        self.assertTrue(happy_days.has(self.weekdays.mon))

        happy_days.set(self.weekdays.mon, False)
        self.assertFalse(happy_days.has(self.weekdays.mon))

        happy_days.set(self.weekdays.mon, False)
        self.assertFalse(happy_days.has(self.weekdays.mon))

if __name__ == "__main__":
    unittest.main()
