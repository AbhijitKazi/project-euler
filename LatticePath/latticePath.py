import time

st = time.perf_counter()
results = {}


def routes(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return 1
    if a == b:
        if str([a - 1, b]) in results:
            return 2 * results[str([a - 1, b])]
        else:
            part1 = routes(a - 1, b)
            results[str([a - 1, b])] = part1
            return 2 * part1

    if str([a - 1, b]) in results:
        part1 = results[str([a - 1, b])]
    else:
        part1 = routes(a - 1, b)
        results[str([a - 1, b])] = part1
    if str([a, b - 1]) in results:
        part2 = results[str([a, b - 1])]
    else:
        part2 = routes(a, b - 1)
        results[str([a, b - 1])] = part2
    return part1 + part2

number = int(input("Enter n : "))
#print((routes(20, 20)))
print((routes(number, number)))
#print((results))
print((len(results)))
print(("Time took : ", time.perf_counter() - st))