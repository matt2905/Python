def fibonacci(nb_to_generate):
    if nb_to_generate >= 0:
        yield 0
    if nb_to_generate >= 1:
        yield 1
    previous_value = 0
    next_value = 1
    for counter in range(2, nb_to_generate):
        result = previous_value + next_value
        yield result
        previous_value = next_value
        next_value = result


for i in fibonacci(1000):
    print(i)
