from tube import Tube

__maximum_moves__ = 50

MoveList = list[str]
State = list[Tube]
PartialSolution = tuple[State, MoveList]


def find_solution(tubes: list[Tube]) -> PartialSolution | None:
    tube_ordinals = range(len(tubes))
    partial_solutions: list[PartialSolution] = [(tubes, [])]

    observed_states: list[State] = []

    for move in range(__maximum_moves__):
        print(f"{move=}")
        print(f"{len(partial_solutions)=}")

        next_partial_solutions: list[PartialSolution] = []
        for solution_to_advance in partial_solutions:
            state = solution_to_advance[0]
            moves = solution_to_advance[1]

            if all([t.is_solid_colour() or t.is_empty() for t in state]):
                return solution_to_advance

            for i in tube_ordinals:
                source_tube = state[i]

                if source_tube.is_solid_colour():
                    continue

                pour = source_tube.will_pour()
                if pour == None:
                    continue

                poured_to_empty = False
                for j in tube_ordinals:
                    if j == i:
                        continue

                    target_tube = state[j]
                    if target_tube.is_empty():
                        if poured_to_empty:
                            continue
                        resulting_solution = make_move(
                            state, moves, source_tube, target_tube, i, j
                        )
                        next_partial_solutions += [resulting_solution]
                        poured_to_empty = True
                        continue

                    if target_tube.can_receive(pour):
                        resulting_solution = make_move(
                            state, moves, source_tube, target_tube, i, j
                        )
                        next_partial_solutions += [resulting_solution]

        deduplicated_next_partial_solutions: list[PartialSolution] = []
        for partial_solution in next_partial_solutions:
            sorted_state = sorted(partial_solution[0])
            if not sorted_state in observed_states:
                observed_states += [sorted_state]
                deduplicated_next_partial_solutions += [partial_solution]

        partial_solutions = deduplicated_next_partial_solutions

    return None


def make_move(
    state: State,
    moves: MoveList,
    source_tube: Tube,
    target_tube: Tube,
    source_tube_index: int,
    target_tube_index: int,
) -> PartialSolution:
    move = f"pour {source_tube_index + 1} into {target_tube_index + 1}"
    (new_source_tube, new_target_tube) = source_tube.pour_into(target_tube)
    new_state = state.copy()
    new_state[source_tube_index] = new_source_tube
    new_state[target_tube_index] = new_target_tube
    new_moves = moves + [move]
    return (new_state, new_moves)
