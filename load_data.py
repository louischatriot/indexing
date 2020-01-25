from timing import time_execution
from mem import print_memory_usage
from index import register_object, get_from_index, objects
import csv

filename = ""

headers = None

with time_execution("Loading database in index"):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if headers is None:
                headers = row
            else:
                o = {}
                for i in range(0, len(headers)):
                    o[headers[i]] = row[i]

                register_object(o)


print_memory_usage()


N = 100000
res = 0
some_email = ""

with time_execution(f"Searching {N} times"):
    for i in range(0,N):
        res += len(get_from_index("email", some_email))

print(len(get_from_index("email", some_email)))

print(len(objects))


