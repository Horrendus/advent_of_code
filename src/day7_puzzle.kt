fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val programs = hashMapOf<String,Node>()
    for (line in input) {
        val programName = line.split(" ")[0]
        val splittedLine = line.split("->")
        val currentNode: Node = programs[programName] ?: Node(programName,null, mutableListOf())
        if (splittedLine.size > 1) {
            var subPrograms = splittedLine[1].split(",")
            subPrograms = subPrograms.map {
                sub -> sub.trim()
            }
            var subProgramNode: Node
            subPrograms.forEach { subprogram ->
                subProgramNode = programs[subprogram] ?: Node(subprogram,null, mutableListOf())
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

}

data class Node(val name: String, var parent: Node?, val children: MutableList<Node>)