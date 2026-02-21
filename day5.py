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
    print(countFresh(vals, ranges))

if __name__ == "__main__":
    main()