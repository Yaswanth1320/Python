
# Water jug problem
# problem- Given the capacity of two jugs l1 and l2 measure g amount of water by using the rules

def water_jug(c1, c2, target):
    # initial state where x and y are the amounts of water in the two jugs
    state = (0, 0)
    parent = {}
    frontier = [state]
    while frontier:
        state = frontier.pop(0)
        if state == (target, 0) or state == (0, target):
            # goal state reached
            path = [state]
            while state in parent:
                state = parent[state]
                path.append(state)
            path.reverse()
            return path
        x, y = state
        # generate all possible successor states
        states = [(c1, y), (x, c2), (0, y), (x, 0), (min(x + y, c1),
                                                     max(0, x + y - c1)), (max(0, y + x - c2), min(y + x, c2))]
        for new_state in states:
            if new_state not in parent:
                parent[new_state] = state
                frontier.append(new_state)
    return None


# c1 and c2 are the capacity of jug 1 and jug 2
c1 = 4
c2 = 3
target = 2
path = water_jug(c1, c2, target)

if path is None:
    print("No solution found.")
else:
    for state in path:
        print(state)
