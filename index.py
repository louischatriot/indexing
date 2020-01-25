from timing import time_execution
from mem import print_memory_usage
from fixtures import generate_word, generate_number

print_memory_usage()

fields = ["email", "phone", "customer.card.fingerprint"]
indexes = {}
objects = []


def add_to_index(field, v, o):
    indexes[field] = indexes.get(field) or {}
    indexes[field][v] = indexes[field].get(v) or []
    indexes[field][v].append(o)


def get_from_index(field, v):
    if indexes.get(field):
        return indexes[field].get(v) or []
    else:
        return []


def register_object(o):
    objects.append(o)
    for field in fields:
        if o.get(field):
            v = o[field]
            if type(v) is not str or len(v) > 0:
                add_to_index(field, v, o)




ind = {}
address_ind = {}

N = 10000

with time_execution("Creating database"):
    for i in range(0,N):
        doc = {
            "id": f"id_{generate_word()}",
            "email": generate_word(),
            "phone": generate_number(18, 65),
            "customer.card.fingerprint": generate_word(),
            "is_fraud": bool(generate_number(0, 100) > 50),
        }
        register_object(doc)

print_memory_usage()

some_object = objects[generate_number(0, N)]
some_email = some_object["email"]


print(some_email)

N = 100000
res = 0

with time_execution(f"Searching {N} times"):
    for i in range(0,N):
        res += len(get_from_index("email", some_email))

print_memory_usage()
print(res)







