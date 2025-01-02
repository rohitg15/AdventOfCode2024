import sys
import re

def parse_corrupted_memory(s: str) -> int:
    """
        part #1: https://adventofcode.com/2024/day/3/#part1
    """
    pattern = r"mul\(\d+,\d+\)"
    digit_pattern = r"\d+"
    c = 0
    for match in re.findall(pattern, s):
        digits = [int(x) for x in re.findall(digit_pattern, match)]
        assert (len(digits) == 2)
        c += digits[0] * digits[1]
    
    return c

def parse_condition_corrupted_memory(s: str) -> int:
    """
        part #2: https://adventofcode.com/2024/day/3#part2
    """
    pattern = r"mul\(\d+,\d+\)|don't()|do()"
    st = []
    for match in re.finditer(pattern, s):
        val = match.group()
        if val == "do":
            # remove all don'ts encountered till now
            while len(st) >0 and st[-1] == "don't":
                st.pop()
        elif val == "don't":
            # append to stack
            st.append(val)
        elif val.find("mul") >= 0:
            # append only if don't wasn't present on top of the stack
            if len(st) == 0:
                st.append(val)
            elif st[-1] != "don't":
                st.append(val)
            # otherwise ignore this value

    c = 0
    digit_pattern = r"\d+"
    for val in st:
        if val.find("mul") >= 0:
            digits = [int(x) for x in re.findall(digit_pattern, val)]
            assert (len(digits) == 2)
            c += digits[0] * digits[1]

    return c

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 3:
        print (f"Usage: {sys.argv[0]} input_file_path part")
        sys.exit(-1)
    
input_file = sys.argv[1]
part = sys.argv[2]

text = ''
with open(input_file, "r") as file:
    text = file.read().strip('\n')

if part == "1":
    print (f"{parse_corrupted_memory(text)}")
elif part == "2":
    print (f"{parse_condition_corrupted_memory(text)}")
else:
    print (f'test')
    text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    print (f"{parse_condition_corrupted_memory(text)}")