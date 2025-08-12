class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = ""
        for _ in range(self._size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n
        return self._size

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size -= n
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
