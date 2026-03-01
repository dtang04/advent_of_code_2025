def turn(current, d, amount):
    if d == "R":
        current += amount
        if current > 99:
            while current > 99:
                current -= 100
    else:
        current -= amount
        if current < 0:
            while current < 0:
                current += 100
    return current

def main():
    part1_count = 0
    with open("day1.txt", "r") as f:
        current = 50
        for l in f:
            l = l.strip()
            direction = l[0]
            amount = int(l[1:])
            current = turn(current, direction, amount)
            if current == 0:
                part1_count += 1
    print(part1_count)

if __name__ == "__main__":
    main()