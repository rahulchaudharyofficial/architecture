from enum import Enum


class CircuitState (Enum):
    """
    Closed: The request from the application is routed through to the operation
    Open: The request from the application fails immediately and an exception is returned to the application.
    Half-Open: A limited number of requests from the application are allowed to pass through and invoke
the operation
    """
    CLOSED = 0
    OPEN = 1
    HALF_OPEN = 2

