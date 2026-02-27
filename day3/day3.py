NUMS_TOTAL = 12

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

def calc_Largest(lst, rem_i):
    """
    Finds the largest element, given that there is rem_i elements remaining to find.
    """
    max_e = -1
    max_i = -1
    for i, val in enumerate(lst):
        if i == len(lst) - rem_i:
            break
        if val > max_e:
            max_e = val
            max_i = i
    rem_lst = lst[max_i+1:]
    return (max_e, rem_lst)

def part2(lst):
    tot = 0
    ret = 0
    for i in range(NUMS_TOTAL-1, -1, -1):
        print(lst)
        print("i: ", i)
        (max_e, lst) = calc_Largest(lst, i)
        print("max_e: ", max_e)
        tot += max_e * (10 ** i)
    return tot

def main():
    tot_1 = 0
    tot_2 = 0
    with open("day3.txt", "r") as f:
        for line in f:
            line = line.strip()
            elements = [int(i) for i in list(line)]
            tot_1 += part1(elements)
            tot_2 += part2(elements)
    print(tot_1) #Part 1: 17278
    print(tot_2) #Part 2: 171528556468625

if __name__ == "__main__":
    main()