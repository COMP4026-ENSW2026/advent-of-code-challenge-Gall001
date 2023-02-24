def forest(file):
    grid = file.read().splitlines()
    visible_trees = len(grid)*2 + (len(grid[0])-2)*2
    for row_index, row in enumerate(grid):
        if row_index == 0 or row_index == len(grid)-1:
            continue
        for tree_index, tree_height in enumerate(row):
            if tree_index == 0 or tree_index == len(row)-1:
                continue
            tree_height = int(tree_height)
            visible_from_left = all(int(height) < tree_height for height in row[:tree_index])
            visible_from_right = all(int(height) < tree_height for height in row[tree_index+1:])
            top_trees = [row[tree_index] for row in grid[:row_index]]
            visible_from_top = all(int(height) < tree_height for height in top_trees)
            bottom_trees = [row[tree_index] for row in grid[row_index+1:]]
            visible_from_bottom = all(int(height) < tree_height for height in bottom_trees)
            visible_trees += any([visible_from_left, visible_from_right, visible_from_top, visible_from_bottom])
    print(str(visible_trees))

file_forest = open('01-advent-of-code-challenge/08/sample.in', 'r')
forest(file_forest)