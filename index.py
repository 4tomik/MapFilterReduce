from functools import reduce
from typing import List, Callable, TypeVar


dollars = ["32$", "15$", "12$", "17$", "20$"]

prices = map(lambda dollar: int(dollar[0:-1]), dollars)
expensive = filter(lambda price: price >= 20, prices)
total = reduce(lambda acum, price: acum + price, expensive, 0)


E = TypeVar('E')
R = TypeVar('R')
A = TypeVar('A')

def map(iterable: List[E], func: Callable[[E], R]) -> List[R]:
    mapped: List[R] = []
    for e in iterable:
        mapped.append(func(e))

    return mapped


def filter(iterable: List[E], func: Callable[[E], bool]) -> List[E]:
    filtered: List[E] = []
    for e in iterable:
        if func(e):
            filtered.append(e)

    return filtered

def reduce(iterable: List[E], func: Callable[[A, E], A], acum: A) -> A:
    for e in iterable:
        acum = func(acum, e)

    return acum

prices = map(dollars, lambda dollar: int(dollar[0:-1]))
expensive = filter(prices, lambda price: price >= 20)
total = reduce(expensive, lambda acum, price: acum + price, 0)
print(total)
