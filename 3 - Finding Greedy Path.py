def assign_pony_to_path(elevations, path, capacities):
    '''will output a list of pony assignments to
    go on each segment of the given path'''

    def sorted_pony_pairs(capacities):
        '''will take the 3 pony types as input then output a list of
        possible pony pairs/tuples and their elevation'''

        # capacities = [small, medium, large] pony size,
        # so need to find all possible combinations of pony_pairs
        x = capacities[0]
        y = capacities[1]
        z = capacities[2]
        pony_pairs = [(x, x), (x, y), (y, y), (x, z), (y, z), (z, z)]

        # Now need to sort the dictionary according to the sum of pairs,
        # as y + y not always smaller than x + z
        # If these 2 are equal, then put y + y first,
        # as according to criterion 2 smaller differences are preferred
        sorted_pd = (sorted(pony_pairs, key=lambda x: x[0] + x[1]))

        return sorted_pd

    def elevation_path(elevations, path):
        '''will output a list of the relative elevation from the
        former cell/village to the successive cell'''

        relative_elevations = []

        for i in range(len(path) - 1):
            # accessing the elevation of a village: elevations[x val][y val]
            successive_elevation = elevations[path[i + 1][0]][path[i + 1][1]]
            former_elevation = elevations[path[i][0]][path[i][1]]
            relative_elevation = successive_elevation - former_elevation
            relative_elevations.append(relative_elevation)

        return relative_elevations

    sorted_pd = sorted_pony_pairs(capacities)
    relative_elevations = elevation_path(elevations, path)

    def assigning_ponies(sorted_pd, relative_elevations):
        '''will output a list of tuples containing the most
        efficient pony pair for each segment of the path'''

        result = []

        for i in range(len(relative_elevations)):
            # need to compare each sum sorted_pd to each elevation in
            # relative_elevations, starting with the smallest sum
            for pair in sorted_pd:
                if sum(pair) >= relative_elevations[i]:
                    # if a value in sorted_pd is >= to the relative_elevation,
                    # that will be best pair for that segment of the journey
                    result.append(pair)
                    break
                elif sum(sorted_pd[-1]) < relative_elevations[i]:
                    # if the sum of the largest pony pair is still lower than
                    # the elevation for that segment, then select None
                    result.append(None)
                    break

        return result

    result = assigning_ponies(sorted_pd, relative_elevations)

    return result


def find_path_greedy(elevations, capacities):
    max_x = len(elevations) - 1  # Finds the range of the x-axis from 0
    max_y = len(elevations[0]) - 1  # Finds the range of the y-axis from 0
    x = 0
    y = 0
    path = [(x, y)]
    max_xy = (max_x, max_y)

    # if the final coordinate in path is not max_xy, then we need to append
    # cells to path until we get to the final coordinate
    while path[-1] != max_xy:

        # if journey is already at the boundary of the x-axis, then can
        # only move in the y direction until we get to max_xy
        if x == max_x:
            while y < max_y:
                y += 1
                path.append((x, y))
            break

        # if journey is already at the boundary of the y-axis, then can
        # only move in the x direction until we get to max_xy
        if y == max_y:
            while x < max_x:
                x += 1
                path.append((x, y))
            break

        # if journey is not at boundary of x or y-axis, then must choose
        # whether to go x + 1 or y + 1 route

        elv_diff_x = elevations[x + 1][y] - elevations[x][y]
        # the elevation difference if we move x + 1 direction
        elv_diff_y = elevations[x][y + 1] - elevations[x][y]
        # the elevation difference if we move y + 1 direction

        if elv_diff_x > elv_diff_y:
            # go in x direction if greater elevation raise in this direction,
            # as according to criterion 3
            x += 1
            path.append((x, y))

        elif elv_diff_y > elv_diff_x:
            # go in y direction if greater elevation raise in this direction,
            # as according to criterion 3
            y += 1
            path.append((x, y))

        else:
            # The elevation diff in both directions is the same,
            # so choose the lower direction, as according to criterion 4
            if x + 1 > y + 1:
                y += 1
                path.append((x, y))
            else:
                x += 1
                path.append((x, y))

    assignment = assign_pony_to_path(elevations, path, capacities)

    return path, assignment


