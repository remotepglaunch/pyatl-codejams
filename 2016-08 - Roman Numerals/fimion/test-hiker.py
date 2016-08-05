from . import hiker
import unittest


class TestHiker(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        '''
        simple example to start you off
        '''

        douglas = hiker.Hiker()
        self.assertEqual("V", douglas.answer(5))
        self.assertEqual("IV",douglas.answer(4))
        self.assertEqual("I",douglas.answer(1))
        self.assertEqual("MDCCXXIX",douglas.answer(1729))
        self.assertEqual("DLXXXVI",douglas.answer(586))
        self.assertEqual("MMMMCMXCIX",douglas.answer(4999))


if __name__ == '__main__':
    unittest.main()
