def euclideanDistanceHeuristic(state, problem=None):
    return math.sqrt((state[0] - problem.goal[0]) ** 2 + (state[1] - problem.goal[1]) ** 2)
    #sqrt((xA-xB)^2+(yA-yB)^2)

def weightedAStarSearch(problem, heuristic=euclideanDistanceHeuristic, epsilon = 0.5):

    solutie=[]
    exploredState = []
    start_node = problem.getStartState()
    frontier = util.PriorityQueue()
    start_heuristic = heuristic(start_node, problem)
    frontier.push((start_node, [], 0), start_heuristic)
    while not frontier.isEmpty():
        current_state, solutie, get_cost = frontier.pop()
        if problem.isGoalState(current_state):
            return solutie
        if current_state not in exploredState:
            exploredState.append(current_state)
            for coordinates, direction, successor_cost in problem.expand(current_state):
                if coordinates not in exploredState:
                    next_state = coordinates

                    actions_list = list(solutie)
                    actions_list += [direction]

                    cost_actions = problem.getCostOfActionSequence(actions_list)
                    frontier.push((next_state, actions_list, 1),
                    cost_actions + epsilon * heuristic(next_state, problem))
    return []