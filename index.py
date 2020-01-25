from timing import time_execution
from mem import print_memory_usage
from fixtures import generate_word, generate_number

print_memory_usage()








docs = []
ind = {}

N = 1000000

with time_execution("Creating database"):
    for i in range(0,N):
        doc = {
            "id": f"id_{generate_word()}",
            "name": generate_word(),
            "age": generate_number(18, 65),
            "address": generate_word(),
            "is_fraud": bool(generate_number(0, 100) > 50),
        }
        docs.append(doc)
        ind[doc["name"]] = doc


print_memory_usage()

some_doc = docs[generate_number(0, N)]
some_name = some_doc["name"]


N = 100000
res = 0

with time_execution(f"Searching {N} times"):
    for i in range(0,N):
        res += ind[some_name]["age"]

print_memory_usage()
print(res)







