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

def findAllPaths_DACFFT(current, links, dac = False, fft = False):
    """
    - Assume links is a DAG. Then, we don't have to track cycle detection, and can just look for whether a path has dac and fft. 
    - Use LRU cache memoization to cache frequent recursive calls.
    """
    @lru_cache(maxsize=1024) # memoization must take immutable parameters
    def memoized_search(current, dac, fft):
        if current == 'out':
            if dac and fft:
                return 1
            return 0

        if current == 'dac':
            dac = True
    
        if current == 'fft':
            fft = True

        neighbors = links[current]
        if len(neighbors) == 0: # Incomplete path
            return 0

        numPaths = 0
        for n in neighbors:
            numPaths += memoized_search(n, dac, fft)
        return numPaths
    
    numPaths = memoized_search(current, dac, fft)
    print(memoized_search.cache_info())

    return numPaths

def main():
    links = {}
    with open("day11.txt") as f:
        for line in f:
            lst = line.split(": ")
            key = lst[0]
            vals = lst[1].strip().split(" ")
            links[key] = vals
    print(findAllPaths("you", links)) # Part 1: 764
    """  
    # Convert dict into immutable
    for key, arr in links.items():
        stri = ""
        for e in arr:
            stri += e + " "
        links[key] = stri
    t_links = tuple(links.items())
    print(t_links)
    """
    print(findAllPaths_DACFFT("svr", links)) # Part 2: 462444153119850

if __name__ == "__main__":
    main()

