import time


class WallClockTimer:

    def __init__(self):
        self.start_time = time.time()
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        print("Wall Time: ", self.end_time - self.start_time)


class CPUTimer:

    def __init__(self):
        self.start_time = time.process_time()
        self.end_time = 0

    def start(self):
        self.start_time = time.process_time()

    def stop(self):
        self.end_time = time.process_time()
        print("CPU Time: ", self.end_time - self.start_time)
