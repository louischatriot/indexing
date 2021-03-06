from timing import time_execution
from mem import print_memory_usage
from fixtures import generate_word, generate_number


# Add id here ; whenever a new doc is added, check whether it's already in the database
# in which case update it if needed as well as indexes

id_field = "id"
fields = ["email", "phone", "fingerprint", "peid"]
indexes = {}
objects = []
id_index = {}



def add_to_index(field, v, o):
    indexes[field] = indexes.get(field) or {}
    indexes[field][v] = indexes[field].get(v) or []
    indexes[field][v].append(o)


def add_to_id_index(o):
    v = o.get(id_field)

    if v is None:
        return

    if type(v) is str and len(v) == 0:
        return

    id_index[v] = o


def get_from_index(field, v):
    if indexes.get(field):
        return indexes[field].get(v) or []
    else:
        return []


def unregister_object(o):
    pass
    # Add logic to remove object from all indexes


def register_object(o):
    objects.append(o)
    add_to_id_index(o)

    for field in fields:
        if o.get(field):
            v = o[field]
            if type(v) is not str or len(v) > 0:
                add_to_index(field, v, o)





# N = 10000
# with time_execution("Creating database"):
    # for i in range(0,N):
        # doc = {
            # "id": f"id_{generate_word()}",
            # "email": generate_word(),
            # "phone": generate_number(18, 65),
            # "customer.card.fingerprint": generate_word(),
            # "is_fraud": bool(generate_number(0, 100) > 50),
        # }
        # register_object(doc)

# print_memory_usage()

# some_object = objects[generate_number(0, N)]
# some_email = some_object["email"]


# N = 100000
# res = 0

# with time_execution(f"Searching {N} times"):
    # for i in range(0,N):
        # res += len(get_from_index("email", some_email))








