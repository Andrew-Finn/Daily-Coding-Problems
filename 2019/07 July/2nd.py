# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the
# following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


class FIFO(object):
    queue = []

    def enqueue(self, s):
        FIFO.queue.append(s)

    def dequeue(self):
        r = FIFO.queue[0]
        FIFO.queue = FIFO.queue[1:]
        return r


if __name__ == '__main__':
    test = FIFO()
    test.enqueue("1")
    test.enqueue("2")
    test.enqueue("3")
    assert test.dequeue() == "1"#
    assert test.dequeue() == "2"
    assert test.dequeue() == "3"