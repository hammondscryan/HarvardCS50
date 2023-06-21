coordinates = []

with open('data.csv') as file:
    for line in file:
        root, square = line.rstrip().split(',')
        coordinate = {'root': root, 'square': square}
        coordinates.append(coordinate)


def get_root(coord: dict) -> int:
    return coord['root']


def get_square(coord: dict) -> int:
    return coord['square']


for x in sorted(coordinates, key=lambda x: x['root']):
    print(f"{x['root']} squared is {x['square']}.")
