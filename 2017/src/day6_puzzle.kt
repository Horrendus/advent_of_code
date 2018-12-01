fun main(args: Array<String>) {
    println("Enter puzzle input")
    val line = readLine()
    if (line != null) {
        val splittedLine = line.split("\t", " ")
        val integerList = splittedLine.map { s ->
            Integer.parseInt(s)
        }
        var memory: MutableList<Int> = integerList.toMutableList()
        var cycles = 0
        val seenMemoryConfigurations = mutableListOf<List<Int>>()
        while (!seenMemoryConfigurations.contains(memory)) {
            seenMemoryConfigurations.add(memory)
            memory = redistributeMemory(memory)
            cycles++
        }
        println("Reached previously seen memory config in $cycles cycles")
        val cyclesSinceSeenFirst = cycles - seenMemoryConfigurations.indexOf(memory)
        println("Memory config seen $cyclesSinceSeenFirst cycles before")
    }
}

fun redistributeMemory(memory: MutableList<Int>): MutableList<Int> {
    var redistributionBlocks = memory.max()
    val redistributedMemory = memory.toMutableList()
    if (redistributionBlocks != null) {
        var pos = memory.indexOf(redistributionBlocks)
        redistributedMemory[pos] = 0
        while (redistributionBlocks != 0) {
            pos++
            val currentPosition = pos % memory.size
            redistributedMemory[currentPosition]++
            redistributionBlocks--
        }
    }
    return redistributedMemory
}
