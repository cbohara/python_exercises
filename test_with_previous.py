import unittest

from with_previous import with_previous


class WithPreviousTests(unittest.TestCase):

    """Tests for with_previous."""

    def test_three(self):
        inputs = [1, 2, 3]
        outputs = [(1, None), (2, 1), (3, 2)]
        self.assertEqual(list(with_previous(inputs)), outputs)

    def test_empty(self):
        self.assertEqual(list(with_previous([])), [])

    def test_one_item(self):
        self.assertEqual(list(with_previous([1])), [(1, None)])

    def test_none(self):
        inputs = [None, None]
        outputs = [(None, None), (None, None)]
        self.assertEqual(list(with_previous(inputs)), outputs)

    def test_string(self):
        inputs = "hey"
        outputs = [('h', None), ('e', 'h'), ('y', 'e')]
        self.assertEqual(list(with_previous(inputs)), outputs)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_lazy_iterable(self):
        inputs = (n**2 for n in [1, 2, 3])
        outputs = [(1, None), (4, 1), (9, 4)]
        self.assertEqual(list(with_previous(inputs)), outputs)


if __name__ == "__main__":
    unittest.main()
