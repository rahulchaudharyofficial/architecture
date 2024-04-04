from enum import Enum
from dataclasses import dataclass


@dataclass
class Request:
    url: str
    method: str


class CircuitBreakerState (Enum):
    """
    Closed: The request from the application is routed through to the operation
    Open: The request from the application fails immediately and an exception is returned to the application.
    Half-Open: A limited number of requests from the application are allowed to pass through and invoke
the operation
    """
    CLOSED = 0
    OPEN = 1
    HALF_OPEN = 2


class CircuitBreakerException (Exception):
    pass





class CircuitBreakerManager:
    def __init__(self):
        pass


