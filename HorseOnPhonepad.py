hops_map = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 6),
    4: (3, 9, 0),
    5: tuple(),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)
}

def get_positions(number):
    if number not in hops_map.keys():
        raise ValueError(f'There is no {number} on phonepad')
    return hops_map[number]

def count_hops(start, hops):
    if hops == 0:
        return 1

    counter = 0
    for position in get_positions(start):
        counter += count_hops(position, hops - 1)
    return counter
