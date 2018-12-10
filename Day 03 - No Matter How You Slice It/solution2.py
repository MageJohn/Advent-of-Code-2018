from rectangle import claim_factory


def read_input(filename):
    with open(filename) as claims:
        claims = [claim_factory(claim) for claim in claims]
    return claims


def find_no_overlap(recs):
    # This O(n^2) algorithm may be the fastest possible. Possible faster
    # algorithms involve some way of culling rectangles that definitely don't
    # intersect.
    found = None
    for rec1 in recs:
        found = rec1
        for rec2 in recs:
            if rec1 is not rec2 and rec1.overlap(rec2):
                found = None
                break
        if found:
            return found


if __name__ == "__main__":
    recs = read_input("input.txt")
    print(find_no_overlap(recs).id)
