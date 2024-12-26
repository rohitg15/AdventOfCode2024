import sys
from typing import List


def sum_distance(left: List[int], right: List[int]) -> int:
    """
        part #1: https://adventofcode.com/2024/day/1#part1
    """
    # sort and compute sum of differences
    return sum(
        abs(l - r) for l, r in zip(
            sorted(left), sorted(right)
            )
        )

def similarity_score(left: List[int], right: List[int]) -> int:
    """
        part #2: https://adventofcode.com/2024/day/1#part2

    """
    count = {}
    for val in right:
        freq = count.get(val) 
        count[val] = 1 if freq is None else freq + 1
    

    return sum(
        val * count[val] if count.get(val) is not None else 0 for val in left
    )
    

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 3:
        print (f"Usage: {sys.argv[0]} input_file_path part")
        sys.exit(-1)
    
input_file = sys.argv[1]
part = sys.argv[2]

# parse input file into 2 lists
lines = []
with open(input_file, "r") as file:
    lines = file.read().strip('\n').split('\n')

left, right = [], []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

if part == "1":
    print (f"{sum_distance(left, right)}")
else:
    print (f"{similarity_score(left, right)}")








