def checkRepeat(num):
    stri = str(num)
    if len(stri) % 2 == 1:
        return False
    front = stri[:len(stri)//2]
    end = stri[len(stri)//2:]
    if front == end:
        return True
    return False


def main():
    count = 0
    intervals = []
    with open("day2.txt", 'r') as f:
        for line in f:
            l = line.strip()
            intervals += l.split(",")
        for interval in intervals:
            if interval == "":
                continue
            loc = interval.split("-")
            low = int(loc[0])
            high = int(loc[1])
            for i in range(low, high+1):
                if checkRepeat(i):
                    count += i
    print(count) # Part 1: 31000881061
if __name__ == "__main__":
    main()
