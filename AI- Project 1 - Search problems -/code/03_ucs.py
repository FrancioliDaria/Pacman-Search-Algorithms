def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    
    start = problem.getStartState()
    exploredState = []
    states = util.PriorityQueue()
    states.push((start, []) ,0)
    while not states.isEmpty():
        state, actions = states.pop()
        if problem.isGoalState(state):
            return actions
        if state not in exploredState:
            successors = problem.getSuccessors(state)
            for succ in successors:
                coordinates = succ[0]
                if coordinates not in exploredState:
                    directions = succ[1]
                    newCost = actions + [directions]
                    states.push((coordinates, actions + [directions]), problem.getCostOfActions(newCost))
        exploredState.append(state)
    return actions
    util.raiseNotDefined()