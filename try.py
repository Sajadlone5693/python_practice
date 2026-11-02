def make_incrementer(n, cache={}):
        if n not in cache:
            cache[n] = lambda x : x + n
        return cache[n]
f1 = make_incrementer(5)
f2 = make_incrementer(5)

print(f1 is f2)


