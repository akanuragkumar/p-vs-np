import json
import operator

solved = False
solution = []

# Tweaked nearest neighbour algorithm done recursively, 
# so that it always produces a solution if one exists
def shortest_path_nn_rec(node, cities, citiesSorted, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += cities[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and stop trying to
    # find new solutions
    if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
        global solved
        global solution
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print("Solution:", path)
        print("Distance:", distance)
        solved = True
        solution = path
        return
    
    # Go to closest unvisited city if solution not found
    for city, dist in citiesSorted[path[-1]]:
        if (city not in path) and (not solved):
            shortest_path_nn_rec(city, dict(cities), dict(citiesSorted), list(path), distance)

# Returns a dict of sorted lists (by distance) containing tuples (city, distance)
def cities_sorted(cities):
    citiesSorted = {}
    for city in cities:
        citiesSorted[city] = sorted(cities[city].items(), key=operator.itemgetter(1))
    return citiesSorted

def unsolved():
    global solved
    solved = False

def get_nn_solution():
    global solution
    return solution

if __name__ == '__main__':
    #load cities
    with open('cities.json') as json_data:
        cities = json.load(json_data)

    # Sort distances from each city
    citiesSorted = cities_sorted(cities)

    print("Recursive nearest neighbour:")
    for city in cities:
        solved = False
        print("Start:", city)
        shortest_path_nn_rec(city, cities, citiesSorted, [], 0)
