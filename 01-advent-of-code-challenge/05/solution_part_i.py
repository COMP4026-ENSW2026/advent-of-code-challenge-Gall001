def solve_crate_rearrangement(stacks, moves):
    for move in moves:
        if(move != ''):
            qty = int(move.split()[1])
            source, dest = map(int, move.split(" from ")[1].split(" to "))
            y=1
            for x in range(qty):
                item = stacks[source-1][-y]
                stacks[dest-1].append(item)
                y = y + 1
            stacks[source-1] = stacks[source-1][:-qty]

    return "".join([stack[-1] for stack in stacks])

def get_sections(file):
    txt =open('01-advent-of-code-challenge/05/sample.in', 'r')
    levels, instructions = [section.split("\n") for section in txt.read().split("\n\n")]
    levels = [crate.replace("    ", " [X] ") for crate in levels[:-1]]  
    levels = [[crate[1] for crate in level.split()] for level in levels]  
    stacks = [[] for _ in range(len(levels[0]))] 
    for level in reversed(levels):
        for index, crate in enumerate(level):
            if crate != "X":
                stacks[index].append(crate)
    return instructions, stacks, levels

input_moves, input_stacks, levels  = get_sections('01-advent-of-code-challenge/05/sample.in')

print(solve_crate_rearrangement(input_stacks, input_moves))