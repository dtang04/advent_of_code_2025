def findAllPaths(current, links):
    if current == 'out':
        return 1
    neighbors = links[current]
    if len(neighbors) == 0:
        return 0
    numPaths = 0
    for n in neighbors:
        numPaths += findAllPaths(n, links)
    return numPaths


def main():
    links = {}
    with open("day11.txt") as f:
        for line in f:
            lst = line.split(": ")
            key = lst[0]
            vals = lst[1].strip().split(" ")
            links[key] = vals
    print(findAllPaths("you", links))

if __name__ == "__main__":
    main()

