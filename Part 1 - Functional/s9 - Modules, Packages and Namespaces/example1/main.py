import sys

print(f"----------------------------------")

print(f"Running main.py - module name: {__name__ }")

import module1

print("imported module1 again...")
del globals()["module1"]

import module1

module1.pprint_dict("main.globals", globals())


# print(sys.path)
# print(sys.modules["module1"])

sys.modules["test"] = lambda: "Testing module caching"

import test

print(test)
print(f"----------------------------------")
