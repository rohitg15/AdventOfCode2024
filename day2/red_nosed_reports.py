import sys
from typing import List, Optional, Tuple


def count_safe_levels(lines: List[str]) -> int:
    """
        part #1: https://adventofcode.com/2024/day/2#part1
    """
    def is_increasing(l) -> bool:
        return all(
            l[i] < l[i+1] for i in range(len(l) - 1)
            )
    def is_decreasing(l) -> bool:
        return all(
            l[i] > l[i+1] for i in range(len(l) - 1)
            )

    def is_safe(levels: List[int]) -> bool:
        """
            returns :True if all increasing or all decreasing
                        and levels differ by atleast 1 and at most 3
        """
        assert(len(levels) > 0)
        
        diffs = [abs(levels[i] - levels[i+1]) for i in range(0, len(levels) - 1)]
        for absdiff in diffs:
            if absdiff < 1 or absdiff > 3:
                return False
            
        return is_increasing(levels) or is_decreasing(levels)


    num_safe = 0
    for line in lines:
        levels = [int(x) for x in line.split()]
        num_safe += 1 if is_safe(levels) else 0
    
    return num_safe
        

def problem_dampener2(lines: List[str]) -> int:
    """
        part #2: https://adventofcode.com/2024/day/2#part2
    """
    def is_dampener_safe2(levels: List[int]) -> bool:
        def check_decreasing(levels: List[int], first_call: bool = True) -> bool:
            """
                assume this must be a decreasing sequence
            """
            for i in range(len(levels) - 1):
                if not 1 <= levels[i] - levels[i+1] <=3:
                    # try removing bad level once and check recursively 
                    return first_call and ( check_decreasing(levels[i - 1: i] + levels[i + 1:], False) or check_decreasing(levels[i: i+1] + levels[i+2:], False) )
            return True

        return check_decreasing(levels, True) or check_decreasing(levels[::-1], True)

    num_safe = 0
    for line in lines:
        levels = [int(x) for x in line.split()]
        num_safe += 1 if is_dampener_safe2(levels) else 0
    
    return num_safe


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 3:
        print (f"Usage: {sys.argv[0]} input_file_path part")
        sys.exit(-1)
    
input_file = sys.argv[1]
part = sys.argv[2]

lines = []
with open(input_file, "r") as file:
    lines = file.read().strip('\n').split('\n')

if part == "1":
    print (f"{count_safe_levels(lines)}")
else:
    print (f"{problem_dampener2(lines)}")

