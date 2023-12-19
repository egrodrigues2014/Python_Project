class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("There is not enough capacity to deposit")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("There is not enough cookies to withdraw")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar= Jar()
jar.deposit(10)
jar.withdraw(4)
print(jar)