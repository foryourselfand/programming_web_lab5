from dataclasses import dataclass
from idlelib.multicall import r

from .models import Dot



def in_area(dot: Dot) -> bool:
    return in_quarter_circle(dot) or in_triangle(dot) or in_rectangle(dot)


def in_quarter_circle(dot: Dot) -> bool:
    return dot.x <= 0 and dot.y >= 0 and (dot.x ** 2 + dot.y ** 2 <= dot.r ** 2)


def in_triangle(dot: Dot) -> bool:
    return dot.x >= 0 and dot.y >= 0 and dot.x <= dot.r and dot.y <= dot.r and dot.y <= -dot.x + dot.r


def in_rectangle(dot: Dot) -> bool:
    return dot.x <= 0 and dot.y <= 0 and dot.y >= -dot.r / 2 and dot.x >= - dot.r
