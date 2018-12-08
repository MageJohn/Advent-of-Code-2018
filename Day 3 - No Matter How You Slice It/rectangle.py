import re
from dataclasses import dataclass, field

START, STOP = 'start', 'stop'

# Pre-compiled regex, makes matching a little faster
#
# Raw string to avoid complaints from linter about \d being an invalid escape
# sequence
PATTERN = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


@dataclass(frozen=True)
class Rectangle:
    _left: int
    _top: int
    _width: int
    _height: int

    @property
    def left(self):
        return Side(self._left, START, self)

    @property
    def top(self):
        return Side(self._top, START, self)

    @property
    def right(self):
        return Side(self._left + self._width, STOP, self)

    @property
    def bottom(self):
        return Side(self._top + self._height, STOP, self)

    def overlap(self, other):
        """If this rectangle overlaps with other,
        return a new rectangle representing the area; else
        return False
        """
        return self.collision(other) and \
            Rectangle(max(self.left, other.left),
                      max(self.top, other.top),
                      min(self.right, other.right) - max(self.left, other.left),
                      min(self.bottom, other.bottom) - max(self.top, other.top))

    def collision(self, other):
        return self.left < other.right and \
               self.right > other.left and \
               self.top < other.bottom and \
               self.bottom > other.top


@dataclass(frozen=True)
class Claim(Rectangle):
    _id: int

    @property
    def id(self):
        return self._id


@dataclass(frozen=True, order=True)
class Coord:
    "One-dimensional coordinate"
    coord: int = field(compare=True)

    def __sub__(self, other):
        return self.coord - other.coord

    __rsub__ = __sub__

    def __add__(self, other):
        return self.coord - other.coord

    __radd__ = __add__


@dataclass(frozen=True)
class RangeEnd(Coord):
    "One end of a range"
    end: str = field(compare=False)


@dataclass(frozen=True)
class Side(RangeEnd):
    """
    The coordinate of one side of a rectangle.

    coord: The distance from the left side of the plane

    end: When scanning left
    to right, whether or not it is the start or the stop of the rectangle

    rec: The Rectangle object this is a side of
    """
    rec: Rectangle = field(compare=False)


def claim_factory(claim_string):
    """
    Takes a string representing a claim and returns a Claim object.
    """
    match = list(PATTERN.match(claim_string).groups())
    id_ = match.pop(0)
    return Claim(*[int(n) for n in match], id_)


def rec_factory(claim_string):
    """
    Takes a string representing a claim and returns a Rectangle object that
    represents area claimed.
    """
    return Rectangle(*[int(n) for n in PATTERN.match(claim_string).groups()[1:]])
