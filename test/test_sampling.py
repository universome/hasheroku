import random
import unittest
from collections import Counter
import sys; sys.path.append('..')


from hasheroku.hasheroku import hasheroku

class Tester(unittest.TestCase):
    def test_uniformity(self):
        # Tests if generated samples are approximately uniform
        # We will draw some hashes from hasheroku, then count,
        # how much of each possible noun and adjective was obtained.
        NUM_SAMPLES = 10**4

        # We consider distribution to be uniform
        # (in our case of 10^4 samples and 64 possible outcomes)
        # if the difference between the most popular and least popular counts
        # is less than this tolerance threshold.
        # It's just a dirty heuristic, I couldn't google out how one can
        # test *discrete* variables for uniformity :|
        TOLERANCE = 100

        # Generatings samples
        strings = [str(n) for n in range(NUM_SAMPLES)]
        samples = [hasheroku(s).split('-') for s in strings]
        adj_counts = Counter(sample[0] for sample in samples)
        noun_counts = Counter(sample[1] for sample in samples)

        # For 10^4 samples and 64 possible equiprobable outcomes
        # we should have on average 156.25 events for each one
        # Assert that each one was met at least once
        assert len(adj_counts) == 64
        assert len(noun_counts) == 64

        # Now, let's test that they are equally likely to occure
        adj_counts = adj_counts.most_common()
        noun_counts = noun_counts.most_common()

        assert adj_counts[0][1] - adj_counts[-1][1] <= TOLERANCE
        assert noun_counts[0][1] - noun_counts[-1][1] <= TOLERANCE


if __name__ == '__main__':
    unittest.main()
