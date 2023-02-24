def get_vision(tree_height, tree_list):
    vision = 0
    index = 0
    while index != len(tree_list):
        vision += 1
        if int(tree_list[index]) >= tree_height: 
            return vision
        index += 1
    return vision

def forest(file):
    grid = file.read().splitlines()
    highest_scenic_score = 0
    for row_index, row in enumerate(grid):
        if row_index == 0 or row_index == len(grid)-1:  
            continue
        for tree_index, tree_height in enumerate(row):
            if tree_index == 0 or tree_index == len(row)-1: 
                continue
            tree_height = int(tree_height)
            left_vision = get_vision(tree_height, row[:tree_index:][::-1])
            right_vision = get_vision(tree_height, row[tree_index+1:])
            top_trees = [row[tree_index] for row in grid[:row_index]]
            top_vision = get_vision(tree_height, top_trees[::-1])
            bottom_trees = [row[tree_index] for row in grid[row_index+1:]]
            bottom_vision = get_vision(tree_height, bottom_trees)
            vision_score = left_vision * right_vision * top_vision * bottom_vision
            if vision_score > highest_scenic_score:
                highest_scenic_score = vision_score
    print(highest_scenic_score)


file_forest = open('01-advent-of-code-challenge/08/sample.in', 'r')
forest(file_forest)