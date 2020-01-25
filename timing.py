import time

class time_execution:
    def __init__(self, message=None):
        self.message = message or ""

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        el = int((time.time() - self.start) * 1000)
        print(f"{self.message} - {el} ms")
