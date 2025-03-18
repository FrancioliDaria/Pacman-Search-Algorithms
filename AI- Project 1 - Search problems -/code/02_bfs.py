def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    start = problem.getStartState()
    exploredState = []
    exploredState.append(start)
    states = util.Queue()
    stateTuple = (start, [])
    states.push(stateTuple)
    while not states.isEmpty():
        state, action = states.pop()
        if problem.isGoalState(state):
            return action
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if not coordinates in exploredState:
                direction = i[1]
                exploredState.append(coordinates)
                states.push((coordinates, action + [direction]))
    return action
    util.raiseNotDefined()