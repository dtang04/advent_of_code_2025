def calculatePart1(nums, ops):
    """
    nums: list of lists of nums (int)
    ops: list of operators (String), length must be equal to nums

    For a given index position, calculate the column-wise result by applying
    the current operator to the number column, then sum up columns to get the
    final result.

    Assumption: No column has empty entries.
    """
    if nums == None or ops == None:
        return 0
    ret = 0
    for j in range(len(nums[0])):
        op = ops[j]
        if op == "+":
            loc = 0
            for i,_ in enumerate(nums):
                loc += nums[i][j]
            ret += loc
        else: # assuming only + and * are the only supported operations
            loc = 1
            for i,_ in enumerate(nums):
                loc *= nums[i][j]
            ret += loc
    return ret

def columnOperator(lst, op):
    str_lst = [str(num) for num in lst]
    max_len = 0
    for e in str_lst:
        if len(e) > max_len:
            max_len = len(e)
    padded_lst = []
    for e in str_lst:
        e = e + ('X' * (max_len - len(e))) # pad with Xs for each element until all elements are same length
        padded_lst.append(e)
    
    i = 0
    if op == "+":
        res = 0
        while i < max_len:
            loc = ""
            for e in padded_lst:
                if e[i] == "X":
                    continue
                loc += e[i]
            res += int(loc)
            i += 1
    else:
        res = 1
        while i < max_len:
            loc = ""
            for e in padded_lst:
                if e[i] == "X":
                    continue
                loc += e[i]
            res *= int(loc)
            i += 1
    return res

def calculatePart2(nums, ops):
    """
    nums: list of lists of nums (int)
    ops: list of operators (String), length must be equal to nums

    For a given index position, calculate the right-to-left column-wise result by applying
    the current operator to the number column, then sum up columns to get the
    final result.

    Assumption: No column has empty entries.

    [Update]
    This padding approach does not work, as the spacing is needed to determine if its
    a left pad or right pad.
    """
    s = 0
    for j in range(len(nums[0])-1,-1,-1):
        op = ops[j]
        s += columnOperator([nums[i][j] for i,_ in enumerate(nums)], op)
    return s

def main():
    nums = []
    ops = []
    with open("day6.txt", "r") as f:
        isOps = False
        for line in f:
            l = line.strip()
            if "*" in l or "+" in l: # supported operators
                isOps = True
            if not(isOps):
                l_u = l.split(" ") 
                parse = [e.strip() for e in l_u]
                row = []
                for p in parse:
                    if p == "":
                        continue
                    row.append(int(p))
                nums.append(row)
            else:
                l_u = l.split(" ") 
                parse = [e.strip() for e in l_u]
                for p in parse:
                    if p == "":
                        continue
                    ops.append(p)
    print(calculatePart1(nums, ops)) # answer: 6171290547579
    print(calculatePart2(nums, ops))
if __name__ == "__main__":
    main()