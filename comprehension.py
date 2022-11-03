import timeit

codeSource = """
list_no_comprehension = []
for n in range(10000):
    list_no_comprehension.append(n * n)
"""

print("time for append", timeit.timeit(codeSource, number=1000))

print("time for comprehension", timeit.timeit(
    "list_comprehension = [n * n for n in range(10000)]", number=1000))
