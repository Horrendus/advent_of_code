fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val programs = hashMapOf<String, Node>()
    for (line in input) {
        val programNameAndWeight = line.split(" ")
        val programName = programNameAndWeight[0]
        val weightString = programNameAndWeight[1]
        val weight = Integer.parseInt(weightString.trim('(',')'))
        val splittedLine = line.split("->")
        val currentNode: Node = programs[programName] ?: Node(programName, weight, null, mutableListOf())
        currentNode.weight = weight
        if (splittedLine.size > 1) {
            var subPrograms = splittedLine[1].split(",")
            subPrograms = subPrograms.map { sub ->
                sub.trim()
            }
            var subProgramNode: Node
            subPrograms.forEach { subprogram ->
                subProgramNode = programs[subprogram] ?: Node(subprogram, 0, null, mutableListOf())
                currentNode.children.add(subProgramNode)
                subProgramNode.parent = currentNode
                programs[subprogram] = subProgramNode
            }
        }
        programs[programName] = currentNode
    }
    var node = programs.keys.first()
    while (true) {
        node = programs[node]?.parent?.name ?: break
    }
    println("Root: $node")
    val program = programs[node]
    program?.children?.forEach {
        it.balance()
    }
}

data class Node(val name: String, var weight: Int, var parent: Node?, val children: MutableList<Node>) {

    // TODO: answer was found via looking up the balancing information printed by this function
    // TODO: create answer programmatically
    fun balance(depth: Int = 0) {
        val subTreeWeights = children.map {
            it.getStackWeight()
        }
        val indent = "\t".repeat(depth)
        println("$indent$name Weight: $weight Stackweight: ${getStackWeight()} Subtreeweights: $subTreeWeights")
        for (i in 0 until children.size) {
            if (!subTreeWeights.all { subTreeWeights[i] == it }) {
                children[i].balance(depth+1)
            }
        }

    }

    fun getStackWeight() : Int {
        return weight + children.map {
            it.getStackWeight()
        }.sum()
    }

}