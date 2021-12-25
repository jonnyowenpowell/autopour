from tube import Tube

__maximum_moves__ = 50

def find_solutions(tubes: list[Tube], moves: int = 0) -> list[list[str]]:
    if moves > __maximum_moves__:
        return []

    if all([t.is_solid_colour() or t.is_empty() for t in tubes]):
        return [[]]

    solutions: list[list[str]] = []

    for i in range(len(tubes)):
        source_tube = tubes[i]

        if source_tube.is_solid_colour():
            continue

        pour = source_tube.will_pour()
        if pour == None:
            continue

        for j in range(len(tubes)):
            if j == i:
                continue
            target_tube = tubes[j]

            if target_tube.can_receive(pour):
                move = f'pour {i} into {j}'
                (new_source_tube, new_target_tube) = source_tube.pour_into(target_tube)
                new_state = tubes.copy()
                new_state[i] = new_source_tube
                new_state[j] = new_target_tube
                new_state_solutions = find_solutions(new_state, moves + 1)
                solutions += [[move] + s for s in new_state_solutions]

    return solutions
