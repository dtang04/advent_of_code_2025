def display(lst):
    for row in lst:
        current = ""
        for e in row:
            current += e
        print(current)

def main():
    numSplits = 0
    disp = []
    num_lines = 1
    len_row = 0
    isFirstLine = False

    with open("day7.txt", "r") as s:
        len_row = len(list(s.readline().strip()))
        for _ in s:
            num_lines += 1

    dp = []
    for _ in range(num_lines):
        dp.append([0] * len_row)

    with open("day7.txt", "r") as f:
            input_lst = list(f.readline().strip())
            start_pos = input_lst.index("S")
            dp[0][start_pos] = 1
            beams = {start_pos}
            curr_row = 1
            prev = input_lst
            for line in f:
                line = list(line.strip())
                next_beams = set()
                for beam in beams:
                    if line[beam] != "^": #beam continues through empty space
                        line[beam] = "|"
                        next_beams.add(beam) #continue propogating current beam
                    else: 
                        numSplits += 1 #split occurs
                        if beam - 1 >= 0 and beam - 1 not in next_beams:
                            next_beams.add(beam - 1) #split on left, if no existing beam exists
                            line[beam - 1] = "|"
                        if beam + 1 < len(line) and beam + 1 not in next_beams:
                            next_beams.add(beam + 1) #split on right, if no existing beam exists
                            line[beam + 1] = "|"
                        #For part 2
                for i,sym in enumerate(prev):
                    if sym != "^":
                        dp[curr_row][i] += dp[curr_row - 1][i] # in DP array, propogate forward through empty space
                    else:
                        if i - 1 >= 0:
                            dp[curr_row][i - 1] += dp[curr_row - 1][i] # left child grabs root
                        if i + 1 < len(line):
                            dp[curr_row][i + 1] += dp[curr_row - 1][i] # right child grabs root
                curr_row += 1
                beams = next_beams
                disp.append(line)
                prev = line
            #display(disp)
            print(numSplits) #Part 1: 1660
            print(sum(dp[-1])) #Part 2: 305999729392659
    
if __name__ == "__main__":
    main()