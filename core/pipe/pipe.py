import inspect
from typing import Callable, Generic, TypeVar

from .pipe_error import PipeError

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
        val = self.value
        sig = inspect.signature(fn)
        num_params = len(sig.parameters)

        if not isinstance(val, (tuple, list)):
            return Pipe(fn(val))
        
        if num_params != len(val):
            raise PipeError(f"Function {fn.__name__} expects {num_params} arguments, received {len(val)}")
            
        return Pipe(fn(*val))

    @property
    def val(self) -> T:
        return self.value
