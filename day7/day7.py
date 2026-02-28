def display(lst):
    for row in lst:
        current = ""
        for e in row:
            current += e
        print(current)

def main():
    numSplits = 0
    disp = []
    with open("day7.txt", "r") as f:
            input_lst = list(f.readline().strip())
            start_pos = input_lst.index("S")
            beams = {start_pos}
            disp.append(input_lst)
            for line in f:
                line = list(line)
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
                beams = next_beams
                disp.append(line)
            display(disp)
            print(numSplits) #Part 1: 1660
if __name__ == "__main__":
    main()