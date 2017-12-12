val groups = mutableListOf<MutableList<Int>>()
val programs = hashMapOf<Int, List<Int>>()

fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    for (line in input) {
        val programAndConnections = line.split("<->")
        val programString = programAndConnections[0].trim()
        val program = Integer.parseInt(programString)
        val connectedProgramsStringSplitted = programAndConnections[1].split(",")
        val connectedPrograms = connectedProgramsStringSplitted.map {
            Integer.parseInt(it.trim())
        }
        programs[program] = connectedPrograms
    }
    programs.forEach { key, _ ->
        calculateAndAddGroup(key)
    }
    println("Size of Group0: ${groups[0].size}")
    println("Total Number of Groups: ${groups.size}")
}

fun calculateAndAddGroup(program: Int) {
    val flatGroups = groups.flatten()
    if (flatGroups.contains(program)) {
        // not a new group
        return
    }
    val group = mutableListOf<Int>()
    group.add(program)
    val evaluationQueue = mutableListOf<Int>()
    evaluationQueue.add(program)
    while (evaluationQueue.size != 0) {
        val current = evaluationQueue.removeAt(0)
        programs[current]?.forEach {
            if (!group.contains(it) && !evaluationQueue.contains(it) && it != current) {
                evaluationQueue.add(it)
            }
            if (!group.contains(it) && it != current) {
                group.add(it)
            }
        }
    }
    groups.add(group)
}
