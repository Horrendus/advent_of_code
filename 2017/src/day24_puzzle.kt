val possibleBridges = mutableListOf(listOf<Pair<Int, Int>>())

fun main(args: Array<String>) {
    val portConnections = mutableListOf<Pair<Int, Int>>()
    val input = mutableListOf<String>()
    println("Enter puzzle input")
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    input.forEach {
        portConnections.add(parseConnectionLine(it))
    }
    val currentPortType = 0
    val startingBridge = listOf<Pair<Int, Int>>()
    buildBridge(startingBridge, currentPortType, portConnections)
    val bridgeStrengths = possibleBridges.map { calculateBridgeStrength(it) }
    println("Maximum Strength: ${bridgeStrengths.max()}")
    val longestBridges = possibleBridges.groupBy { it.size }.maxBy { it.key }?.value ?: listOf(listOf())
    val longestBridgesStrength = longestBridges.map { calculateBridgeStrength(it) }
    println("Longest Bridge with maximum Strength: ${longestBridgesStrength.max()}")
}

private fun buildBridge(bridge: List<Pair<Int, Int>>, emptyPortType: Int,
                        availableConnections: List<Pair<Int, Int>>) {
    if (availableConnections.isEmpty()) {
        possibleBridges.add(bridge)
        return
    }
    val connections = availableConnections.filter { it.first == emptyPortType || it.second == emptyPortType }
    if (connections.isEmpty()) {
        possibleBridges.add(bridge)
        return
    }
    connections.forEach { connection ->
        // create new deep copy of bridge
        val newBridge = bridge.map { it }.toMutableList()
        newBridge.add(connection)
        val newAvailableConnections = availableConnections.filter { it != connection }
        val newPortType = if (connection.first == emptyPortType) connection.second else connection.first
        buildBridge(newBridge, newPortType, newAvailableConnections)
    }
}

private fun calculateBridgeStrength(bridge: List<Pair<Int, Int>>): Int {
    var strength = 0
    bridge.forEach { strength += (it.first + it.second) }
    return strength
}

private fun parseConnectionLine(line: String): Pair<Int, Int> {
    val splittedLine = line.split("/")
    val port0 = Integer.parseInt(splittedLine[0])
    val port1 = Integer.parseInt(splittedLine[1])
    return Pair(port0, port1)
}

