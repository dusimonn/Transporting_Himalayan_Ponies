def check_path(elevations, path, capacities, assignments):
    max_x = len(elevations) - 1  # Finds the range of the x-axis from 0
    max_y = len(elevations[0]) - 1  # Finds the range of the y-axis from 0

    # Error: Cell coordinates is out of bounds
    # Check the x and y val for each path to see if within the array of the map

    for i in range(len(path)):
        if path[i][0] < 0 or path[i][0] > max_x or path[i][1] < 0 or path[i][1] > max_y:
            # print(f"({path[i]}, 'Cell coordinates is out of bounds')")
            return (path[i], 'Cell coordinate is out of bounds')

    # Error: Path should start at (0,0) coordinate
    # Check if the 1st cell within path starts at (0,0)
    if path[0] != (0, 0):
        # print(f"({path[0]}, 'Path should start at (0,0) coordinate')")
        return (path[0], 'Path should start at (0,0) coordinate')

    # Error: Path should end at (M,N) coordinate
    # Checking if the last path cell has the maximum coordinates,
    # as denoted by the village_elevations
    # Finding the destination cell according to path
    destination_cell = path[-1]
    correct_destination = (max_x, max_y)
    if destination_cell != correct_destination:
        # print(f"({path[-1]}, 'Path should end at {correct_destination} coordinate')")
        return (path[-1], f'Path should end at {correct_destination} coordinate')

    # Error: Illegal move
    # Checking if the path is always increasing by 1 in the x or y coordinate

    # path[i][0] = x1 and path[i+1][0] = x2
    # path[i][1] = y1 and path[i+1][1] = y2

    for i in range(len(path) - 1):

        # check x and y is incremented by 0 or 1, x or y doesnt increase by 1
        if (path[i + 1][0] - path[i][0] != 1 and path[i + 1][0] - path[i][0] != 0) or (
                path[i + 1][1] - path[i][1] != 1 and path[i + 1][1] - path[i][1] != 0):
            # print(f"({path[i]}, 'Illegal move')")
            return (path[i], 'Illegal move')

        # check if both x and y increment by 1 or 0, both x and y increase by 1 or 0
        elif (path[i + 1][0] - path[i][0] == 1 and path[i + 1][1] - path[i][1] == 1) or (
                path[i + 1][0] - path[i][0] == 0 and path[i + 1][1] - path[i][1] == 0):
            # print(f"({path[i]}, 'Illegal move')")
            return (path[i], 'Illegal move')

    # Error: Insufficient capacity assignment
    # Checking if assigned pony capacity is enough to get to next elevation
    # Need to find the elevations of each pony pair, then compare to the elevations between each successive cell
    # Finding the pony pair elevations and putting into a list

    pony_elevations = []
    for i in range(len(assignments)):
        pony_elevations.append(assignments[i][0] + assignments[i][1])

    # print(pony_elevations)
    # Finding the elevations between each successive cell and putting into a list
    # Relative elevations between 2 cells = village_elevations[x2 val of journey path][y2 val of journey path] - village_elevations[x1 val of journey path][y1 val of journey path]

    relative_elevations = []

    for i in range(len(path) - 1):
        successive_cell_elevation = elevations[path[i + 1][0]][path[i + 1][1]]
        former_cell_elevation = elevations[path[i][0]][path[i][1]]
        relative_elevation = successive_cell_elevation - former_cell_elevation
        relative_elevations.append(relative_elevation)

    for i in range(len(pony_elevations)):
        if pony_elevations[i] < relative_elevations[i]:
            return (path[i], 'Insufficient capacity assignment')

    # Error: Exceeding pony limit
    # Checking if a pony assignment has more than 2 ponies

    for i in range(len(assignments)):
        if len(assignments[i]) > 2:
            # print(f"({path[i]}, 'Exceeding pony limit')")
            return (path[i], 'Exceeding pony limit')

    # print(None)
    return None