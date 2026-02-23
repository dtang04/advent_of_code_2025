def checkRepeat(num):
    stri = str(num)
    if len(stri) % 2 == 1:
        return False
    front = stri[:len(stri)//2]
    end = stri[len(stri)//2:]
    if front == end:
        return True
    return False

def checkRepeat_p2(num):
    stri = str(num)
    for chunk_size in range(1, len(stri)):
        if len(stri) % chunk_size != 0:
            continue
        chunks = []
        for i in range(0, len(stri), chunk_size):
            chunks.append(stri[i:i+chunk_size])
        template = chunks[0]
        satisfy = True
        for i in range(1,len(chunks)):
            if chunks[i] != template:
                satisfy = False
        if satisfy:
            return True
    return False 

def main():
    count = 0
    count_p2 = 0
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
                if checkRepeat_p2(i):
                    count_p2 += i
    print(count) # Part 1: 31000881061
    print(count_p2) # Part 2: 46769308485
if __name__ == "__main__":
    main()
