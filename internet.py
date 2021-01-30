



subtract_set = {1,2,3,4,5,6,7,8,9}
def check_horizontal(i,j):
    return subtract_set - set(container[i])
def check_vertical(i, j):
    ret_set = []
    for x in range(9):
        ret_set.append(container[x][j])
    return subtract_set - set(ret_set)
def check_square(i, j):
    first = [0,1,2]
    second = [3,4,5]
    third = [6,7,8]
    find_square = [first, second, third]
    for l in find_square:
        if i in l:
            row = l
        if j in l:
            col = l
    return_set = []
    for x in row:
        for y in col:
            return_set.append(container[x][y])
    return subtract_set - set(return_set)

def get_poss_vals(i, j):
    poss_vals = list(check_square(i, j) \
                    .intersection(check_horizontal(i, j)) \
                    .intersection(check_vertical(i, j)))
    return poss_vals

def explicit_solver(container):
    for i in range(9):
        for j in range(9):
            if container[i][j] == 0:
                poss_vals = get_poss_vals(i, j)
                if len(poss_vals) == 1:
                    container[i][j] = list(poss_vals)[0]
                    print_container(container)
    return container


def implicit_solver(i, j, container):
    if container[i][j] == 0:
        poss_vals = get_poss_vals(i, j)

        # check row
        row_poss = []
        for y in range(9):
            if y == j:
                continue
            if container[i][y] == 0:
                for val in get_poss_vals(i, y):
                    row_poss.append(val)
        if len(set(poss_vals) - set(row_poss)) == 1:
            container[i][j] = list(set(poss_vals) - set(row_poss))[0]
            print_container(container)
        # check column
        col_poss = []
        for x in range(9):
            if x == i:
                continue
            if container[x][j] == 0:
                for val in get_poss_vals(x, j):
                    col_poss.append(val)
        if len(set(poss_vals) - set(col_poss)) == 1:
            container[i][j] = list(set(poss_vals) - set(col_poss))[0]
            print_container(container)
        # check square
        first = [0, 1, 2]
        second = [3, 4, 5]
        third = [6, 7, 8]
        find_square = [first, second, third]
        for l in find_square:
            if i in l:
                row = l
            if j in l:
                col = l
        square_poss = []
        for x in row:
            for y in col:
                if container[x][y] == 0:
                    for val in get_poss_vals(x, y):
                        square_poss.append(val)
        if len(set(poss_vals) - set(square_poss)) == 1:
            container[i][j] = list(set(poss_vals) - set(square_poss))[0]
            print_container(container)
    return container


def print_container(container):
    for row in container:
        print('   '.join(row))

if __name__ == "__main__":
    container =    [[0, 2, 0, 0, 0, 7, 0,"a", 0, 9, 0, 0, 0, "c", 0, 0],
                   ["e", 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 6, "f", "d", 0, 7],
                   [0, 0, 0, 0, 6, 9, 3, 0, 0, 0, 0, 0, 0, 0, 2, "o"],
                   [5, "b", 0, 0, 0, 0, 0, 0, "o", 0, 7, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, "a", 0, 0, 0, "c"],
                   [0, 9, 0, 0, "o", 0, 0, 0, 0, 6, 0, 1, "b", 0, 5, 0],
                   [0, 0, 0, "o", 7, 0, 0, 8, 0, 0, 2, 0, 0, "a", 3, 0],
                   [0, 7, 6, 1, 0, 0, "a", "f", 0, 8, 0, 4, 0, 0, 0, 0],
                   [4, 0, "d", 0, 5, 0, 0, "b", 0, 0, 6, 0, "e", 0, "a", 2],
                   [0, 0, 0, 0, "e", 0, 0, 7, 8, 0, 4, "c", 0, 0, "d", 0],
                   [0, 3, 0, 0, 0, 0, 1, "d", 5, 7, 0, 0, 0, 0, 0, 6],
                   [0, "o", 0, 0, "c", 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
                   [0, 0, 0, "d", 3, 0, 0, "o", "c", "f", 0, 0, "a", 0, 0, 0],
                   [8, 0, 0, 3, "b", "a", 0, 0, 0, 0, "o", 0, "c", 6, 0, 1],
                   [0, 0, "c", "b", 0, "f", 0, 2, 0, 0, 9, 5, 0, 0, "e", 0],
                   [0, 0, 0, 0, 9, 1, 0, 0, 0, "b", 3, 0, 5, 4, 7, 0]]
