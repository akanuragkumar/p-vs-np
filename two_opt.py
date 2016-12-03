import json

# reverses all elements from path[i] to path[i+k] 
# example:
# route = ['MA', 'N', 'M', 'UL', 'RV', 'Z', 'BE']  
# two_opt_swap(route, 1, 3)
# route == ['MA', 'UL', 'M', 'N', 'RV', 'Z', 'BE'] : True
def two_opt_swap(path, i, k):
    path[i:i+k] = path[i:i+k][::-1]
    return path

# calculates distance in a given path
def calculate_distance(path, cities):
    distance = 0
    prevCity = path[0]

    for city in path[1:]:
        if city not in cities[prevCity]:
            return -1 
        distance += cities[prevCity][city]
        prevCity = city
    
    return distance

# 2opt is a local search algorithm which tries to take a route 
# that crosses over itself and reorders it so that it does not
def two_opt(path, cities):
    bestPath = path
    newPath = []
    bestDistance = calculate_distance(path, cities)
    betterPathFound = True

    while betterPathFound:
        betterPathFound = False
        for i in range(1, len(path)-2):
            for k in range(1, len(path)-(i+1)):
                newPath = two_opt_swap(list(path), i, k)
                newDistance = calculate_distance(newPath, cities)
                if (newDistance != -1) and (newDistance < bestDistance):
                    bestPath = newPath
                    bestDistance = newDistance
                    betterPathFound = True
    
    if bestPath != path:
        print("Better solution found:", bestPath)
        print("Distance:", bestDistance)
        return True
    else:
        print("No better solution found :(")
        return False


if __name__ == '__main__':
    #load cities
    with open('cities.json') as json_data:
        cities = json.load(json_data)

    print("Applying 2opt to known paths:")
    path = ['MA', 'N', 'M', 'UL', 'RV', 'Z', 'BE', 'BA', 'KA', 'S', 'F', 'MA']
    print("Path:", path)
    two_opt(path, cities)
    path = ['BE', 'BA', 'KA', 'S', 'MA', 'F', 'N', 'M', 'UL', 'RV', 'Z', 'BE']
    print("Path:", path)
    two_opt(path, cities)
