from dataclasses import dataclass

from .models import Dot


@dataclass
class DotDTO:
    x: float
    y: float
    r: float


def in_area(x: str, y: str, r: str) -> bool:
    dot_dto: DotDTO = DotDTO(x=float(x), y=float(y), r=float(r))
    return in_quarter_circle(dot_dto) or in_triangle(dot_dto) or in_rectangle(dot_dto)


def in_quarter_circle(dot: DotDTO) -> bool:
    return dot.x <= 0 and dot.y >= 0 and (dot.x ** 2 + dot.y ** 2 <= dot.r ** 2)


def in_triangle(dot: DotDTO) -> bool:
    return dot.x >= 0 and dot.y >= 0 and dot.x <= dot.r and dot.y <= dot.r and dot.y <= -dot.x + dot.r


def in_rectangle(dot: DotDTO) -> bool:
    return dot.x <= 0 and dot.y <= 0 and dot.y >= -dot.r / 2 and dot.x >= - dot.r
