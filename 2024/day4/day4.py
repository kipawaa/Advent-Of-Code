

def p1(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        puzzle = data.readlines()

        valid_words = ("XMAS", "SAMX")
        
        num_found = 0

        for r in range(len(puzzle)):
            for c in range(len(puzzle[r])):
                
                # forwards/backwards
                if c < len(puzzle[r]) - 3:
                    if puzzle[r][c:c+4] in valid_words:
                        num_found += 1

                # vertical
                if r < len(puzzle) - 3:
                    if puzzle[r][c] + puzzle[r+1][c] + puzzle[r+2][c] + puzzle[r+3][c] in valid_words:
                        num_found += 1

                # top-left/bottom-right diagonal
                if r < len(puzzle) - 3 and c < len(puzzle[r]) - 3:
                    if puzzle[r][c] + puzzle[r+1][c+1] + puzzle[r+2][c+2] + puzzle[r+3][c+3] in valid_words:
                        num_found += 1

                # top-right/bottom-left diagonal
                if r < len(puzzle) - 3 and c > 2:
                    if puzzle[r][c] + puzzle[r+1][c-1] + puzzle[r+2][c-2] + puzzle[r+3][c-3] in valid_words:
                        num_found += 1

        print(num_found)

def p2(datafile="sample.txt"):
    with open(datafile, 'r') as data:
        puzzle = data.readlines()

        valid_words = ("MAS", "SAM")

        num_found = 0

        for r in range(1, len(puzzle) - 1):
            for c in range(1, len(puzzle[r]) - 1):
                # get top-left/bottom-right diagonal
                TLBR = puzzle[r-1][c-1] + puzzle[r][c] + puzzle[r+1][c+1]

                # get top-right/bottom-left diagonal
                TRBL = puzzle[r-1][c+1] + puzzle[r][c] + puzzle[r+1][c-1]

                if TLBR in valid_words and TRBL in valid_words:
                    num_found += 1

        print(num_found)

if __name__ == "__main__":
    #p1(datafile="input.txt")
    p2(datafile="input.txt")
