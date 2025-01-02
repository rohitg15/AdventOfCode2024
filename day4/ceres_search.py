import sys
from typing import List

nbrs_in_dir = {
        'E': (
            (0, 1, 'E'),
            ),
        'W': (
            (0, -1, 'W'),
            ),
        'N': (
            (-1, 0, 'N'),
            ),
        'S': (
            (1, 0, 'S'),
            ),
        'NE': (
            (-1, 1, 'NE'),
            ),
        'NW': (
            (-1, -1, 'NW'),
            ),
        'SE': (
            (1, 1, 'SE'),
            ),
        'SW': (
            (1, -1, 'SW'),
            ),
        'A': (
            (-1, -1, 'NW'), (-1, 0, 'N'), (-1, 1, 'NE'),
            (0, -1, 'W'), (0, 1, 'E'),
            (1, -1, 'SW'), (1, 0, 'S'), (1, 1, 'SE')
        )
    }

opp_dir = {
    'E': 'W',
    'W': 'E',
    'N': 'S',
    'S': 'N',
    'NE': 'SW',
    'SW': 'NE',
    'NW': 'SE',
    'SE': 'NW'
}

def search_word(grid: List[str], word: str = 'XMAS') -> int:
    """
        part #1: https://adventofcode.com/2024/day/4
    """
    assert (len(word) > 1)
    m = len(grid)
    n = len(grid[0])
    
    def find_num_occurences(cx: int, cy: int, cur: int, dir: str) -> int:
        if cur == len(word):
            # reached end of word
            return 1
        
        # start at grid[cx][cy] and expand to search for word[cur]
        # depth-first search neighbors for
        # current unmatched character from word
        num_occurences = 0
        for d in nbrs_in_dir.get(dir):
            nx , ny, direction = cx + d[0], cy + d[1], d[2]
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == word[cur]:
                # search same direction for 'A' and 'S'
                num_occurences += find_num_occurences(nx, ny, cur + 1, direction)
        
        return num_occurences

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == word[0]:
                # search all directions for 'M'
                count += find_num_occurences(i, j, 1, 'A')

    return count  


def search_xmas(grid: List[str]) -> int:
    """
        part #2: https://adventofcode.com/2024/day/4#part2
    """
    m = len(grid)
    n = len(grid[0])

    count  = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'A':
                for mdirs in ( ('NW', 'NE'), ('NE', 'SE'), ('SE', 'SW'), ('SW', 'NW') ):
                    # check 'M' is present in the current diagonal directions
                    # and 'S' is present in it's opposite diagonal directions
                    sdirs = (opp_dir[mdirs[0]], opp_dir[mdirs[1]])
                    mcoords = (nbrs_in_dir[mdirs[0]][0], nbrs_in_dir[mdirs[1]][0])
                    scoords = (nbrs_in_dir[sdirs[0]][0], nbrs_in_dir[sdirs[1]][0])
                    found_xmas = True
                    for mcoord, scoord in zip(mcoords, scoords):
                        mx, my = i + mcoord[0], j + mcoord[1]
                        sx, sy = i + scoord[0], j + scoord[1]
                        found_xmas = found_xmas and 0 <= mx < m and 0 <= my < n and 0 <= sx < m and 0 <= sy < n and grid[mx][my] == 'M' and grid[sx][sy] == 'S'
                    
                    count = count + 1 if found_xmas else count

    return count

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 3:
        print (f"Usage: {sys.argv[0]} input_file_path part")
        sys.exit(-1)
    
input_file = sys.argv[1]
part = sys.argv[2]

lines = []
with open(input_file, "r") as file:
    lines = file.read().strip().split('\n')

if part == "1":
    print (f"{search_word(lines)}")
elif part == "2":
    print (f"{search_xmas(lines)}")
else:
    print (f'test')
    print (f"{search_word(lines)}")