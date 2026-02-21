def countFresh(vals, ranges):
    count = 0
    ranges.sort()
    for val in vals:
        for r in ranges:
            low = r[0]
            high = r[1]
            if val >= low and val <= high:
                count += 1
                break
            if low > val:
                break
    return count

def countFreshIDs(ranges):
    ranges.sort()
    if len(ranges) < 1:
        return 0
    current = 0
    countIDs = 0
    for r in ranges:
        low = r[0]
        high = r[1]
        if current >= low and current <= high: # if running counter is in the middle of the current range
            if high > current: # check for this current range has any ids to add
                countIDs += high - current
            else: # running counter is greater than the entire range
                continue
        elif high <= current:
            continue
        else: # range falls entirely outside running counter
            countIDs += high - low + 1
        current = high
    return countIDs

def main():
    ranges = []
    vals = []
    with open("day5.txt", "r") as f:
        isVals = False
        for line in f: #get ranges
            l = line.strip()
            if l == "":
                isVals = True
                continue
            if not(isVals):
                r = l.split("-")
                ranges.append([int(k) for k in r])
            else:
                vals.append(int(l))
    print(countFresh(vals, ranges)) #Part 1 - 505
    print(countFreshIDs(ranges)) #Part 2 - 344423158480189

if __name__ == "__main__":
    main()