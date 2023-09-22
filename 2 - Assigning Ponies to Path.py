# pony_capacities = [17, 37, 73]
# journey_path = [(0,0), (0,1), (0,2), (0,3), (1,3), (1,4), (1,5)]
# pony_assignments = [(73, 73)] * 6
# village_elevations = [[100, 200, 300, 400, 100, 600], [0, 100, 200, 300, 400, 500]]
# village_elevations = [[200, 400, 600, 800, 1000, 1200], [1400, 1600, 1800, 2000, 2200, 2400]]

def assign_pony_to_path(elevations, path, capacities):
    '''will output a list of pony assignments to go on each segment of the given path'''

    def sorted_pony_pairs(capacities):
        '''will take the 3 pony types as input then output a list of
        possible pony pairs/tuples and their elevation'''

        # capacities = [small, medium, large] pony size, so need to find all possible combinations of pony_pairs
        s, m, l = capacities
        pony_pairs = [(s, s), (s, m), (m, m), (s, l), (m, l), (l, l)]

        # Now need to sort the dictionary according to the sum of pairs, as m+m not always smaller than s + l
        # If these 2 are equal, then put m + m first as according to criterion 2 smaller differences are preferred
        sorted_pd = (sorted(pony_pairs, key=lambda x: x[0] + x[1]))

        return sorted_pd

    def elevation_path(elevations, path):
        '''will output a list of the relative elevation from the former cell/village to the successive cell'''

        relative_elevations = []

        for i in range(len(path) - 1):
            # accessing the elevation of a village has format: elevations[x val][y val]
            successive_elevation = elevations[path[i + 1][0]][path[i + 1][1]]
            former_elevation = elevations[path[i][0]][path[i][1]]
            relative_elevation = successive_elevation - former_elevation
            relative_elevations.append(relative_elevation)

        return relative_elevations

    sorted_pd = sorted_pony_pairs(capacities)
    relative_elevations = elevation_path(elevations, path)

    def assigning_ponies(sorted_pd, relative_elevations):
        '''will output a list of tuples containing the most efficient pony pair for each segment of the path'''

        result = []

        for i in range(len(relative_elevations)):
            # need to compare the sum of each value of sorted_pd to each elevation in relative_elevations, starting with the smallest sum
            for pair in sorted_pd:
                if sum(sorted_pd[-1]) < relative_elevations[i]:
                    # if the sum of the largest pony pair is still lower than the elevation for that segment, then select None
                    result.append(None)
                    break
                elif sum(pair) >= relative_elevations[i]:
                    # once a value in sorted_pd is >= to the relative_elevation, that will be the most efficient pony pair (pp) for that segment of the journey
                    result.append(pair)
                    break


            if len(set(result)) == 1:
                result = f"{[result[0]]} * {len(result)}"

        return result

    result = assigning_ponies(sorted_pd, relative_elevations)

    return result

# print(assign_pony_to_path(village_elevations, journey_path, pony_capacities))
