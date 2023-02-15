def count_overlapping_assignments(assignment_list):
    overlapping_assignments = 0
    for assignment in assignment_list:
        start1, end1 = map(int, assignment[0].split("-"))
        start2, end2 = map(int, assignment[1].split("-"))

        if start1 <= start2 <= end1 or start2 <= start1 <= end2:
                overlapping_assignments += 1
        elif start1 <= end2 <= end1 or start2 <= end1 <= end2:
            overlapping_assignments += 1
    return overlapping_assignments

with open("01-advent-of-code-challenge/04/sample.in", "r") as f:
    assignments = [line.strip().split(",") for line in f.readlines()]

print(count_overlapping_assignments(assignments))

