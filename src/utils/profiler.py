# src/utils/profiler.py

import time

class Profiler:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise ValueError("Profiler not started.")
        elapsed_time = time.time() - self.start_time
        print(f"Execution Time: {elapsed_time:.4f} seconds")
        self.start_time = None
