"""

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'

The box is rotated 90 degrees clockwise,
causing some of the stones to fall due to gravity.
Each stone falls down until it lands on an obstacle,
another stone, or the bottom of the box. Gravity does not affect the
obstacles' positions, and the inertia from the box's rotation does not
affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle,
another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation
described above.


"""

""" Advance approach
def rotate_and_apply_gravity(box):
    # Step 1: Rotate the box 90 degrees clockwise
    # Transpose and reverse each row to achieve the rotation
    rotated_box = list(zip(*box[::-1]))

    # Step 2: Apply gravity to each column of the rotated box
    result = []
    for column in rotated_box:
        column_list = list(column)
        # Collect all stones and obstacles
        stones = [c for c in column_list if c == '#']
        obstacles = [c for c in column_list if c == '*']
        empty = len(column_list) - len(stones) - len(obstacles)

        # Reconstruct the column with gravity applied
        new_column = ['.'] * empty + stones + obstacles
        result.append(new_column)

    # Step 3: Convert back to matrix format and return
    return ["".join(row) for row in zip(*result[::-1])]


# Example Input
box = [
    ["#", ".", "*", "."],
    ["#", "#", "*", "."],
    ["#", ".", ".", "."],
]

# Convert rows to strings for clearer visualization
box = [list(row) for row in box]

# Execute the function
result = rotate_and_apply_gravity(box)

# Print the result for debugging
for row in result:
    print("".join(row))



def rotateAndApplyGravity(box):
    m = len(box)
    n = len(box[0])

    rotated_box = []
    for col in range(n):
        new_row = []
        for row in range(m - 1, -1, -1):
            new_row.append(box[row][col])
        rotated_box.append(new_row)

    for col in range(n):

        column = rotated_box[col]
        stones = column.count('#')
        obstacles = column.count('*')
        empty = m - stones - obstacles
        new_column = ['.'] * empty + ['#'] * stones + ['*'] * obstacles
        rotated_box[col] = new_column

    final_result = [''.join(rotated_box[row][col] for row in range(n)) for col in range(m)]

    return final_result

"""


# Example usage
box = [
    ["#", ".", "*", "."],
    ["#", "#", "*", "."],
    ["#", ".", ".", "."]
]

result = rotateAndApplyGravity(box)
for row in box:
    print(row)

print("Resultant Box")
for row in result:
    print(row)


