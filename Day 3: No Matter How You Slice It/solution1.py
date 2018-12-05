from itertools import chain, tee
from rectangle import START, rec_factory


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def rec_sides_ordered(recs, direction):
    """
    Takes a list of Rectangles and returns a list of the sides of each, sorted
    by their distance from the left hand side of the plane. `direction` should
    be either 'horizonal' or 'vertical'; if it's the first the left and right
    sides are used, if it's the second the top and bottom are used.
    """
    attrs = {'vertical': ('top', 'bottom'),
             'horizontal': ('left', 'right')}[direction]
    rec_sides = list(chain.from_iterable((getattr(rec, attrs[0]), getattr(rec, attrs[1])) for rec in recs))
    return sorted(rec_sides, key=lambda s: s.coord)


def total_overlap_len(ranges):
    """
    Takes a list with starts and stops of ranges, and returns the total length
    of the overlaps.
    """
    ranges_in = 0
    overlapped_len = 0
    for endpoint in ranges:
        if endpoint.end == START:
            ranges_in += 1
            if ranges_in == 2:
                # Just entered a second range without leaving the first, so
                # there is overlap
                overlap_start = endpoint
        else:  # endpoint.end == STOP:
            ranges_in -= 1
            if ranges_in == 1:
                # Just left a range, but are still in one. Therefore the
                # overlap has ended
                overlapped_len += endpoint.coord - overlap_start.coord

    return overlapped_len


def overlapped_area(recs):
    x_side_ordering = rec_sides_ordered(recs, 'horizontal')

    y_slice = []
    overlapped_area = 0
    for side, nside in pairwise(x_side_ordering):
        if side.end == START:
            y_slice.extend((side.rec.top, side.rec.bottom))
            y_slice.sort(key=lambda s: s.coord)
            # This will be almost sorted every time, so will be
            # cheap, approx O(n).
        else:  # type(side) is rectangle.Right
            y_slice.remove(side.rec.top)
            y_slice.remove(side.rec.bottom)

        width = nside.coord - side.coord

        overlapped_area += width * total_overlap_len(y_slice)
    return overlapped_area


def read_input(filename):
    with open(filename) as claims:
        claims = [rec_factory(claim) for claim in claims]
    return claims


if __name__ == "__main__":
    recs = read_input("input.txt")
    print(overlapped_area(recs))
