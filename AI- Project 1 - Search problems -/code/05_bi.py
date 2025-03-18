def bidirectional(problem):
    # Path-ul de la start catre mijloc
    q1 = util.Queue()
    temp_q1 = []
    # Path-ul de la goal catre mijloc
    q2 = util.Queue()
    temp_q2 = []
    explorednode1 = set()
    explorednode2 = set()
    startnode = problem.getStartState()
    endnode = problem.goal
    q1.push((startnode,[]))
    q2.push((endnode, []))
    while not q1.isEmpty() and not q2.isEmpty():
        if not q1.isEmpty():
            currentnode, direction = q1.pop()
            if currentnode not in explorednode1:
                explorednode1.add(currentnode)
                if (currentnode in temp_q2) or problem.isGoalState(currentnode):
                    while not q2.isEmpty():
                        node, direc = q2.pop()
                        if node == currentnode:
                            solution = direction + direc.reverse()
                            return solution
                for(successor, action, stepCost) in problem.getSuccessors(currentnode):
                    q1.push((successor, direction + [action]))
                    temp_q1.append(successor)
        if not q2.isEmpty():
            currentnode, direction = q2.pop()
            if currentnode not in explorednode2:
                explorednode2.add(currentnode)
                if currentnode in temp_q1:
                    while not q1.isEmpty():
                        node, direc = q1.pop()
                        if node == currentnode:
                            direction.reverse()
                            solution = direc + ulta(direction)
                            return solution
                for(successor, action, stepCost) in problem.getSuccessors(currentnode):
                    q2.push((successor, direction + [action]))
                    temp_q2.append(successor)
