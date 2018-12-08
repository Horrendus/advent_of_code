fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val nodeMap = mutableMapOf<Char, Step>()
    for (line in input) {
        // Format of a line: e.g.
        // Step I must be finished before step Q can begin.
        val nodeKey = line[5]
        val followingNodeKey = line[36]
        var node = nodeMap.getOrPut(nodeKey) { Step(nodeKey, mutableListOf(), mutableListOf()) }
        var followingNode = nodeMap.getOrPut(followingNodeKey) { Step(followingNodeKey, mutableListOf(), mutableListOf()) }
        node.successors.add(followingNode)
        followingNode.predecessors.add(node)
    }
    part1(nodeMap)
    part2(nodeMap)
}

private data class Step(val name: Char, val successors: MutableList<Step>,val predecessors: MutableList<Step>)

private fun part1(nodeMap: Map<Char, Step>) {
    println("Part 1")
    var availableNodes = nodeMap.values.filter { it.predecessors.size == 0 }.toMutableList()
    var currentNode = availableNodes.sortedBy { it.name }[0]
    print(currentNode.name)
    val visitedNodes = mutableListOf(currentNode)
    while (currentNode.successors.size != 0) {
        //println("currentNode $currentNode")
        availableNodes.addAll(currentNode.successors)
        for (node in availableNodes.sortedBy { it.name }) {
            if (!visitedNodes.contains(node) && visitedNodes.containsAll(node.predecessors)) {
                currentNode = node
                break
            }
        }
        availableNodes.remove(currentNode)
        visitedNodes.add(currentNode)
        print(currentNode.name)
    }
    println()
}

private fun part2(nodeMap: Map<Char, Step>) {
    println("Part 2")
    val availableNodes = nodeMap.values.filter { it.predecessors.size == 0 }.toMutableList()
    val blockedNodes = mutableListOf<Step>()
    val visitedNodes = mutableListOf<Step>()
    var availableWorkers = 5
    var currentSecond = 0
    val currentSteps = mutableListOf<Pair<Int, Step>>()
    val currentStepsNodes = mutableListOf<Step>()
    while (visitedNodes.size != nodeMap.entries.size) {
        while (availableWorkers > 0 && !availableNodes.isEmpty()) {
            val nextStep = availableNodes.sortedBy { it.name }[0]
            availableNodes.remove(nextStep)
            val nextStepFinishTime = currentSecond + nextStep.name.toInt() - 4
            currentSteps.add(Pair(nextStepFinishTime, nextStep))
            currentStepsNodes.add(nextStep)
            availableWorkers--
        }
        currentSteps.sortBy { it.first }
        val finishedTask = currentSteps.removeAt(0)
        currentSecond = finishedTask.first
        availableWorkers++
        visitedNodes.add( finishedTask.second )
        availableNodes.addAll( blockedNodes.filter { visitedNodes.containsAll(it.predecessors) &&
                !visitedNodes.contains(it) && !currentStepsNodes.contains(it)})
        blockedNodes.removeIf { visitedNodes.containsAll(it.predecessors) }
        availableNodes.addAll( finishedTask.second.successors.filter { visitedNodes.containsAll(it.predecessors) &&
                !visitedNodes.contains(it) && !currentStepsNodes.contains(it) && !availableNodes.contains(it)})
        blockedNodes.addAll( finishedTask.second.successors.filter { !visitedNodes.containsAll(it.predecessors) &&
                !visitedNodes.contains(it) && !currentStepsNodes.contains(it) && !blockedNodes.contains(it)})
    }
    println(currentSecond)
}
