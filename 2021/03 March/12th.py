# Good morning! Here's your coding interview problem for today.

# This question was asked by Riot Games.

# Design and implement a HitCounter class that keeps track of requests (or
# hits). It should support the following operations:

# record(timestamp): records a hit that happened at timestamp
# total(): returns the total number of hits recorded
# range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
# Follow-up: What if our system has limited memory?

# ---> If the system has a memory limit the soultion would be use case dependtant. If the hits were close together you
# could block some hits together ans store hits as a group.


import bisect


class HitCounter():
    def __init__(self):
        self.hit_list = []

    def record(self, timestamp):
        bisect.insort(self.hit_list, timestamp)

    def total(self) -> int:
        return len(self.hit_list)

    def range(self, start, end):
        left_index = bisect.bisect_right(self.hit_list, start - 1)
        right_index = bisect.bisect_right(self.hit_list, end)
        return len(self.hit_list[left_index:right_index])


if __name__ == "__main__":
    import time
    from random import randrange

    t = int(time.time())

    for _ in range(1000):
        hit_counter = HitCounter()

        l = sorted(
            list(set([randrange(t - 2500, t + 2500) for _ in range(500)])))
        for v in l:
            hit_counter.record(v)

        assert hit_counter.total() == len(l)
        assert hit_counter.range(t - 2500, t + 2500) == len(l)

        r1, r2 = randrange(
            1, len(l) // 2), randrange(len(l) // 2, len(l) - 1)
        assert len(l[r1:r2 + 1]) == hit_counter.range(l[r1], l[r2])
