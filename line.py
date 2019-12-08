import queue

class Line:
    def __init__(self):
        self.queue = queue.Queue()

    def isEmpty(self):
        return self.queue == queue.empty()

    def enqueue(self, username):
        if username not in self.queue
            self.queue.put(username)
            return self.queue
        return

    def dequeue(self):
        return self.queue.get()

    def size(self):
        return self.queue.qsize()
