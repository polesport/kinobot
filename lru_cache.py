import time


class LRUData:
    def __init__(self, payload, tm):
        self.payload = payload
        self.tm = tm


class LRUCache:
    def __init__(self, ttl: float = 86400.0):
        self._cache_data = {}
        self.ttl = ttl

    def get_data(self, genre: str, func_get_films) -> list:
        if genre in self._cache_data.keys():
            data = self._cache_data[genre]
            if (time.monotonic() - data.tm) > self.ttl:
                self._cache_data[genre] = LRUData(func_get_films(genre), time.monotonic())
                return self._cache_data[genre].payload
            else:
                return data.payload
        else:
            return self._cache_data.setdefault(genre, LRUData(func_get_films(genre), time.monotonic())).payload
