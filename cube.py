import random
import time
import numpy as np


def ninety_degree(face):
    f_turn = (face[0][0], face[0][1])

    face[0][0] = face[2][0]
    face[2][0] = face[2][2]
    face[2][2] = face[0][2]
    face[0][2] = f_turn[0]

    face[0][1] = face[1][0]
    face[1][0] = face[2][1]
    face[2][1] = face[1][2]
    face[1][2] = f_turn[1]


class Cube:
    top = bottom = right = left = front = back = []
    da_moves = ""

    def __init__(self, top, bottom, right, left, front, back):
        rows, col = (3, 3)
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left
        self.front = front
        self.back = back

        self.shuffle()

        # self.top = [[0 for i in range(rows)] for j in range(col)]

    def R(self):

        ninety_degree(self.right)

        f_turn = (self.front[0][2], self.front[1][2], self.front[2][2])
        self.front[0][2] = self.bottom[0][2]
        self.front[1][2] = self.bottom[1][2]
        self.front[2][2] = self.bottom[2][2]

        self.bottom[0][2] = self.back[2][2]
        self.bottom[1][2] = self.back[1][2]
        self.bottom[2][2] = self.back[0][2]

        self.back[0][2] = self.top[2][2]
        self.back[1][2] = self.top[1][2]
        self.back[2][2] = self.top[0][2]

        self.top[0][2] = f_turn[0]
        self.top[1][2] = f_turn[1]
        self.top[2][2] = f_turn[2]

    def L(self):

        ninety_degree(self.left)

        f_turn = (self.front[0][0], self.front[1][0], self.front[2][0])

        self.front[0][0] = self.top[0][0]
        self.front[1][0] = self.top[1][0]
        self.front[2][0] = self.top[2][0]

        self.top[0][0] = self.back[2][0]
        self.top[1][0] = self.back[1][0]
        self.top[2][0] = self.back[0][0]

        self.back[0][0] = self.bottom[2][0]
        self.back[1][0] = self.bottom[1][0]
        self.back[2][0] = self.bottom[0][0]

        self.bottom[0][0] = f_turn[0]
        self.bottom[1][0] = f_turn[1]
        self.bottom[2][0] = f_turn[2]

    def U(self):

        ninety_degree(self.top)

        f_turn = (self.front[0][0], self.front[0][1], self.front[0][2])

        self.front[0][0] = self.right[0][0]
        self.front[0][1] = self.right[0][1]
        self.front[0][2] = self.right[0][2]

        self.right[0][0] = self.back[0][2]
        self.right[0][1] = self.back[0][1]
        self.right[0][2] = self.back[0][0]

        self.back[0][0] = self.left[0][2]
        self.back[0][1] = self.left[0][1]
        self.back[0][2] = self.left[0][0]

        self.left[0][0] = f_turn[0]
        self.left[0][1] = f_turn[1]
        self.left[0][2] = f_turn[2]

    def D(self):

        ninety_degree(self.bottom)

        f_turn = (self.front[2][0], self.front[2][1], self.front[2][2])

        self.front[2][0] = self.left[2][0]
        self.front[2][1] = self.left[2][1]
        self.front[2][2] = self.left[2][2]

        self.left[2][0] = self.back[2][2]
        self.left[2][1] = self.back[2][1]
        self.left[2][2] = self.back[2][0]

        self.back[2][0] = self.right[2][2]
        self.back[2][1] = self.right[2][1]
        self.back[2][2] = self.right[2][0]

        self.right[2][0] = f_turn[0]
        self.right[2][1] = f_turn[1]
        self.right[2][2] = f_turn[2]

    def F(self):

        ninety_degree(self.front)

        f_turn = (self.top[2][0], self.top[2][1], self.top[2][2])

        self.top[2][0] = self.left[2][2]
        self.top[2][1] = self.left[1][2]
        self.top[2][2] = self.left[0][2]

        self.left[0][2] = self.bottom[0][0]
        self.left[1][2] = self.bottom[0][1]
        self.left[2][2] = self.bottom[0][2]

        self.bottom[0][0] = self.right[2][0]
        self.bottom[0][1] = self.right[1][0]
        self.bottom[0][2] = self.right[0][0]

        self.right[0][0] = f_turn[0]
        self.right[1][0] = f_turn[1]
        self.right[2][0] = f_turn[2]

    def B(self):

        ninety_degree(self.back)
        ninety_degree(self.back)
        ninety_degree(self.back)

        f_turn = (self.top[0][0], self.top[0][1], self.top[0][2])

        self.top[0][0] = self.right[0][2]
        self.top[0][1] = self.right[1][2]
        self.top[0][2] = self.right[2][2]

        self.right[0][2] = self.bottom[2][2]
        self.right[1][2] = self.bottom[2][1]
        self.right[2][2] = self.bottom[2][0]

        self.bottom[2][2] = self.left[2][0]
        self.bottom[2][1] = self.left[1][0]
        self.bottom[2][0] = self.left[0][0]

        self.left[2][0] = f_turn[0]
        self.left[1][0] = f_turn[1]
        self.left[0][0] = f_turn[2]

    def rot_X(self):
        temp = self.front
        self.front = self.left
        self.left = np.flip(self.back, 1)
        self.back = np.flip(self.right, 1)
        self.right = temp

        ninety_degree(self.top)
        ninety_degree(self.top)
        ninety_degree(self.top)

        ninety_degree(self.bottom)

    def rot_Y(self):

        temp = self.front
        self.front = self.bottom
        self.bottom = np.flip(self.back, 0)
        self.back = np.flip(self.top, 0)
        self.top = temp

        ninety_degree(self.right)
        ninety_degree(self.left)
        ninety_degree(self.left)
        ninety_degree(self.left)

    def to_string(self):
        print()
        for i in range(3):
            print("\t\t\t", self.top[i])
        print()
        for i in range(3):
            print(self.left[i], "\t", self.front[i], "\t", self.right[i])
        print()
        for i in range(3):
            print("\t\t\t", self.bottom[i])
        print()
        for i in range(3):
            print("\t\t\t", self.back[i])
        print()

    def algorithm(self, alg):

        index = 0
        move = index + 1
        while move < len(alg):
            if alg[index] == alg[move]:
                move += 1
            else:
                self.da_moves += alg[index]
                index = move
                move = index + 1

        # self.da_moves += alg
        for step in alg:
            if step == 'R':
                self.R()
            elif step == 'U':
                self.U()
            elif step == 'L':
                self.L()
            elif step == 'D':
                self.D()
            elif step == 'F':
                self.F()
            elif step == 'B':
                self.B()

    def shuffle(self):
        moves = ['U', 'D', 'R', 'L', 'F', 'B', 'Rx', 'Ry']

        for _ in range(300):
            rnd = random.randint(0, 7)
            move = moves[rnd]
            if move == 'U':
                self.U()
            elif move == 'D':
                self.D()
            elif move == 'L':
                self.L()
            elif move == 'R':
                self.R()
            elif move == 'F':
                self.F()
            elif move == 'B':
                self.B()
            elif move == 'Rx':
                self.rot_X()
            elif move == 'Ry':
                self.rot_Y()


times = []
steps = []

for i in range(100):

    right = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    left = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    top = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    bottom = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    front = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
    back = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

    cube = Cube(top, bottom, right, left, front, back)
    cube.to_string()

    start_time = time.time()
    starting_color = cube.bottom[1][1]

    # Build Cross
    edge = 4

    if cube.top[0][1] == starting_color:
        edge -= 1
    if cube.top[1][0] == starting_color:
        edge -= 1
    if cube.top[1][2] == starting_color:
        edge -= 1
    if cube.top[2][1] == starting_color:
        edge -= 1

    while cube.top[0][1] != starting_color or cube.top[1][0] != starting_color \
            or cube.top[1][2] != starting_color or cube.top[2][1] != starting_color:

        # Check the bottom

        for _ in range(4):
            if edge <= 0:
                break
            while cube.top[2][1] == starting_color:
                cube.U()
            if cube.bottom[0][1] == starting_color:
                cube.algorithm("FF")
                edge -= 1
            elif cube.bottom[1][0] == starting_color:
                cube.algorithm("DFF")
                edge -= 1
            elif cube.bottom[1][2] == starting_color:
                cube.algorithm("DDDFF")
                edge -= 1
            elif cube.bottom[2][1] == starting_color:
                cube.algorithm("DDFF")
                edge -= 1
            else:
                break

        # Check front
        while cube.top[2][1] == starting_color and edge > 0:
            cube.U()

        if cube.front[1][2] == starting_color:
            cube.algorithm("R")
            while cube.top[1][2] == starting_color:
                cube.U()
            cube.algorithm("RRR")
            edge -= 1

        elif cube.front[1][0] == starting_color:
            cube.algorithm("LLL")
            while cube.top[1][0] == starting_color:
                cube.U()
            cube.algorithm("L")
            edge -= 1

        elif cube.front[0][1] == starting_color:
            cube.algorithm("FRFFF")
            while cube.top[1][2] == starting_color:
                cube.U()
            cube.algorithm("RRR")
            edge -= 1

        elif cube.front[2][1] == starting_color:
            cube.algorithm("FLLLFFF")
            while cube.top[1][0] == starting_color:
                cube.U()
            cube.algorithm("L")
            edge -= 1

        else:
            cube.rot_X()

    for _ in range(4):
        while cube.front[0][1] != cube.front[1][1]:
            cube.U()
            cube.rot_X()
        cube.algorithm("FF")
        cube.rot_X()

    print("First Cross:")
    cube.to_string()

    for _ in range(4):
        if (cube.bottom[0][2] != cube.bottom[1][1]) or (cube.front[2][2] != cube.front[1][1]) or (cube.right[2][0] != cube.right[1][1]):
            while cube.front[2][2] == starting_color or cube.bottom[0][2] == starting_color or cube.right[2][0] == starting_color:
                cube.algorithm("RURRRU")
        cube.rot_X()

    for _ in range(4):
        if (cube.bottom[0][2] != cube.bottom[1][1]) or (cube.front[2][2] != cube.front[1][1]) or (cube.right[2][0] != cube.right[1][1]):
            corner = [cube.front[1][1], cube.right[1][1], cube.bottom[1][1]]
            while (cube.front[0][2] not in corner) or (cube.top[2][2] not in corner) or (cube.right[0][0] not in corner):
                cube.U()
            while cube.bottom[0][2] != cube.bottom[1][1]:
                cube.algorithm("RURRRUUU")
        cube.rot_X()

    print("First Layer:")
    cube.to_string()

    top_color = cube.top[1][1]

    for _ in range(4):
        if (cube.front[1][0] != cube.front[1][1] or cube.left[1][2] != cube.left[1][1]) and \
                (cube.front[1][0] != top_color and cube.left[1][2] != top_color):
            while cube.front[0][1] != top_color and cube.top[2][1] != top_color:
                cube.U()
            cube.algorithm("UUULLLULUFUUUFFF")
        cube.rot_X()

    for _ in range(4):
        i = 0
        while cube.front[0][1] == top_color or cube.top[2][1] == top_color:
            if i == 4:
                break
            cube.U()
            i += 1
        if i == 4:
            break
        while cube.front[0][1] != cube.front[1][1]:
            cube.U()
            cube.rot_X()
        if cube.top[2][1] == cube.right[1][1]:
            cube.algorithm("URUUURRRUUUFFFUF")
        elif cube.top[2][1] == cube.left[1][1]:
            cube.algorithm("UUULLLULUFUUUFFF")

    print("F2L")
    cube.to_string()

    empty = True if cube.top[0][1] != top_color and cube.top[1][0] != top_color and cube.top[1][2] != top_color and cube.top[2][1] != top_color else False

    if empty:
        cube.algorithm("FRURRRUUUFFF")
    line = True if (cube.top[0][1] == top_color and cube.top[2][1] == top_color) or (cube.top[1][0] == top_color and cube.top[1][2] == top_color) else False

    if not line:
        while cube.top[0][1] != top_color or cube.top[1][0] != top_color:
            cube.U()
        cube.algorithm("FURUUURRRFFF")
    else:
        if cube.top[1][0] != top_color:
            cube.U()
            cube.algorithm("FRURRRUUUFFF")
        elif cube.top[0][1] != top_color:
            cube.algorithm("FRURRRUUUFFF")

    print("Upper Cross")
    cube.to_string()

    while cube.front[0][1] != cube.front[1][1]:
        cube.U()

    while cube.right[0][1] != cube.right[1][1]:
        cube.algorithm("RURRRURUURRR")
    if cube.left[0][1] != cube.left[1][1]:
        cube.rot_X()
        cube.algorithm("RURRRURUURRRU")

    print("Top Layer Edges")
    cube.to_string()

    corner = [cube.front[1][1], cube.top[1][1], cube.left[1][1]]
    i = 0
    while (cube.front[0][0] not in corner) or (cube.top[2][0] not in corner) or (cube.left[0][2] not in corner):
        if i == 3:
            cube.algorithm("UUULLLURUUULURRR")
        cube.algorithm("URUUULLLURRRUUUL")
        i += 1

    corner = [cube.front[1][1], cube.top[1][1], cube.right[1][1]]
    while cube.front[0][2] not in corner or cube.top[2][2] not in corner or cube.right[0][0] not in corner:
        cube.algorithm("UUULLLURUUULURRR")

    print("Top Layer Corners")
    cube.to_string()

    for _ in range(4):
        if cube.top[2][2] == cube.top[1][1]:
            cube.U()
            continue
        while cube.top[2][2] != cube.top[1][1]:
            cube.algorithm("RRRDDDRD")
        cube.U()

    cube.to_string()
    total_time = time.time() - start_time
    print(total_time)
    i = 0
    for moves in cube.da_moves:
        if i == 50:
            print()
            i = 0
        print(moves, end="")
        i += 1
    print()
    times.append(total_time)
    steps.append(len(cube.da_moves))

avg_time = 0
avg_step = 0
for t in times:
    avg_time += t
for s in steps:
    avg_step += s
print("Average Time:", avg_time/100)
print("Average Moves:", avg_step/100)
