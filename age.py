def f(lst=[]):
    lst.append(1)
    return lst
print(f(), f(), f())