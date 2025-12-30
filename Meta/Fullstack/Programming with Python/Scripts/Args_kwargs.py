def func(*args): # Same as ... operator in JS
    return sum(args)

print(func(1,2,3))


def func2(**kwargs):
    total = 0
    for k, v in kwargs.items():
        total += v
    return round(total, 2)

print(func2(tea=1.25, coffee=3.5, juice=5))