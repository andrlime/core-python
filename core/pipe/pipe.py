from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Pipe(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def __or__(self, fn: Callable[[T], U]) -> Pipe[U]:
        return self.pipe(fn)

    def __rshift__(self, fn: Callable[[T], U]) -> Pipe[U]:
        return self.pipe(fn)

    def pipe(self, fn: Callable[[T], U]) -> Pipe[U]:
        return Pipe(fn(self.value))

    def unwrap(self) -> T:
        return self.value
