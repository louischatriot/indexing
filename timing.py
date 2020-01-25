import time

class time_execution:
    def __init__(self, message=None):
        self.message = message or ""

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        el = int((time.time() - self.start) * 1000)
        suffix = "ms"

        if el > 5000:
            el = int(el / 1000)
            suffix = "s"


        print(f"{self.message} - {el} {suffix}")
