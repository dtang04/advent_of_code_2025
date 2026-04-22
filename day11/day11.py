from functools import lru_cache

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

@lru_cache # for memoization
def findAllPaths_DACFFT(current, links, trail_str = "svr"):
    if current == 'out':
        if 'dac' in trail_str and 'fft' in trail_str:
            return 1
        return 0

    neighbors = []
    for key, n in links:
        if key == current:
            neighbors = n.strip().split(" ")
            break

    if len(neighbors) == 0:
        return 0

    numPaths = 0
    trail = trail_str.split(" ")
    for n in neighbors:
        if n in trail:
            continue
        numPaths += findAllPaths_DACFFT(n, links, trail_str + " " + n)
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
    
    # Convert dict into immutable
    for key, arr in links.items():
        stri = ""
        for e in arr:
            stri += e + " "
        links[key] = stri
    t_links = tuple(links.items())
    print(t_links)
    print(findAllPaths_DACFFT("svr", t_links))

if __name__ == "__main__":
    main()

