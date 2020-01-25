import os
import psutil

process = psutil.Process(os.getpid())


# In MB
def print_memory_usage():
    used = int(process.memory_info().rss / 2**20)
    print(f"Memory used: {used} MB")

