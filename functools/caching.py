"""Python's caching is great for expensive repetitive functions and methods"""
from functools import cache, cached_property, lru_cache
import json
import time
import urllib.request


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@cache
def cached_fib(n):
    if n <= 1:
        return n
    return cached_fib(n - 1) + cached_fib(n - 2)


def bench_fib():
    goal = 38
    start = time.time()
    fib(goal)
    print(f"Time taken without caching: {time.time() - start:.5f} seconds")

    start = time.time()
    cached_fib(goal)
    print(f"Time taken with caching: {time.time() - start:.5f} seconds")


@lru_cache(maxsize=None)
def add_5(num):
    print(f"Adding 5 to {num}")
    return num + 5


class METAR:
    def __init__(self, icao):
        self.icao = icao.upper()

    @cached_property
    def data(self):
        print(f"Getting METAR for {self.icao}")
        res = urllib.request.urlopen(
            f"https://api.weather.gov/stations/{self.icao.upper()}/observations/latest"
        ).read()
        return json.loads(res)

    @property
    def raw(self):
        return self.data["properties"]["rawMessage"]

    @property
    def temp(self):
        return self.data["properties"]["temperature"]["value"]

    @property
    def dewpoint(self):
        return self.data["properties"]["dewpoint"]["value"]

    @property
    def wind(self):
        return "{direction}{speed}KT".format(
            direction=self.data["properties"]["windDirection"]["value"],
            speed=self.data["properties"]["windSpeed"]["value"],
        )
