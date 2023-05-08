def generatorFunc():
    for num in range(10):
        yield num


gh = (x for x in range (10))

print(next(gh))
print(next(gh))
print(next(gh))




