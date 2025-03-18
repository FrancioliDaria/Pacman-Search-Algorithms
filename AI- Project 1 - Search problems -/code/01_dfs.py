def depthFirstSearch(problem):
    
start = problem.getStartState()
c = problem.getStartState()
exploredState = []
exploredState.append(start)
states = util.Stack()
stateTuple = (start, [])
states.push(stateTuple)
while not states.isEmpty() and not problem.isGoalState(c):
    state, actions = states.pop()
    exploredState.append(state)
    successor = problem.getSuccessors(state)
    for i in successor:
        coordinates = i[0]
        if not coordinates in exploredState:
            c = i[0]
            direction = i[1]
            states.push((coordinates, actions + [direction]))
return actions + [direction]

util.raiseNotDefined()