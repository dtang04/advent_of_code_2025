def part1(lst):
    max_e = -1
    max_i = -1
    for i, val in enumerate(lst):
        if i == len(lst) - 1:
            break
        if val > max_e:
            max_e = val
            max_i = i
    rem = lst[max_i+1:]
    snd_e = -1
    for val in rem:
        if val > snd_e:
            snd_e = val
    return max_e * 10 + snd_e

def main():
    tot = 0
    with open("day3.txt", "r") as f:
        for line in f:
            line = line.strip()
            elements = [int(i) for i in list(line)]
            tot += part1(elements)
    print(tot) #Part 1: 17278

if __name__ == "__main__":
    main()