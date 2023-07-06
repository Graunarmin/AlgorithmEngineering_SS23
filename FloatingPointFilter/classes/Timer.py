import time


class Timer:
    def __init__(self):
        self.wall_start = 0
        self.cpu_start = 0

        self.wall_time = 0
        self.cpu_time = 0

    def start(self):
        self.wall_start = time.time()
        self.cpu_start = time.process_time()

    def pause(self):
        self.wall_time += (time.time() - self.wall_start)
        self.cpu_time += (time.process_time() - self.cpu_start)

    def stop(self):
        self.wall_time += (time.time() - self.wall_start)
        self.cpu_time += (time.process_time() - self.cpu_start)

    def reset(self):
        self.wall_start = 0
        self.cpu_start = 0
        self.wall_time = 0
        self.cpu_time = 0
