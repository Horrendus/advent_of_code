var grid = mutableListOf<Pair<Int, Int>>()

private val groups = mutableListOf<MutableList<String>>()
private val programs = hashMapOf<String, List<String>>()

fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = readLine()
    var used = 0
    (0..127).forEach {
        row ->
        val hashInput = input + "-" + row
        val hexHash = calculateDenseHash(hashInput)
        val binHash = hexHash.map {
            Integer.toBinaryString(Integer.parseInt(it.toString(), 16))
        }.joinToString("").padStart(128,'0')
        val usedInRow = binHash.count {
            it == '1'
        }
        used += usedInRow
        binHash.forEachIndexed {
            idx, value ->
            if (value == '1') {
                grid.add(Pair(row,idx))
            }
        }
    }
    println("Total Used: $used")

    val neighbours = listOf(Pair(-1, 0), Pair(1, 0),
            Pair(0, -1), Pair(0, 1))




    // val blocksToEvaluate = mutableListOf<Pair<Int,Int>>()

    // val regionSizes = mutableListOf<Int>()

    /*
    while (grid.isNotEmpty() && numberOfBlocks < 1) {
        var regionSize = 0
        numberOfBlocks++
        var currentPosition = grid.removeAt(0)
        blocksToEvaluate.add(currentPosition)
        while (blocksToEvaluate.isNotEmpty()) {
            println("$blocksToEvaluate")
            currentPosition = blocksToEvaluate.removeAt(0)
            var neighbourPositions = neighbours.map { it + currentPosition }
            neighbourPositions = neighbourPositions.filter { grid.contains(it) && !blocksToEvaluate.contains(it) }
            blocksToEvaluate.addAll(neighbourPositions)
            grid.removeAll(neighbourPositions)
            regionSize++
            println("${blocksToEvaluate.size}")
            //println("Grid: ${grid.size} Evaluation Blocks: ${blocksToEvaluate.size} Neighbour Pos: ${neighbourPositions.size}")
        }
        regionSizes.add(regionSize)
    }
    */
    grid.forEach {
        program ->
        var neighbourPositions = neighbours.map { it + program }
        neighbourPositions = neighbourPositions.filter { it in grid }
        val connectedPrograms = neighbourPositions.map { it.toProgramString() }
        println(connectedPrograms)
        programs[program.toProgramString()] = connectedPrograms
    }

    programs.forEach { key, _ ->
        calculateAndAddGroup(key)
    }

    println("Total Number of Regions: ${groups.size}")
    groups.forEach {
        println(it.size)
    }
}

private operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> {
    return Pair(first + other.first, second + other.second)
}

private fun Pair<Int, Int>.toProgramString() : String {
    val firstStr = (first + 1000).toString()
    val secondStr = (second + 1000).toString()
    return "p" + firstStr + secondStr
}

private fun calculateAndAddGroup(program: String) {
    val flatGroups = groups.flatten()
    if (flatGroups.contains(program)) {
        // not a new group
        return
    }
    val group = mutableListOf<String>()
    group.add(program)
    val evaluationQueue = mutableListOf<String>()
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

// same code as in Day 10 Puzzle 2
private fun calculateDenseHash(input: String): String {
    val lengthsSuffix = listOf(17, 31, 73, 47, 23)
    val lengths = input.trim().map { it.toInt() } + lengthsSuffix

    val list = listOf(0 until 256).flatten().toMutableList()

    var skip = 0
    var position = 0

    (1..64).forEach {
        lengths.forEach { length ->
            val end = position + length
            val wrappedEnd1 = if (end >= list.size) end % list.size else 0
            val wrappedEnd2 = minOf(end, list.size)
            val subList1 = list.slice(0 until wrappedEnd1)
            val subList2 = list.slice(position until wrappedEnd2)

            val reversedList = (subList2 + subList1).reversed()
            for (i in 0 until reversedList.size) {
                val listPos = (i + position) % list.size
                list[listPos] = reversedList[i]
            }
            position += length + skip
            position %= list.size
            skip++
        }
    }
    val denseHash = mutableListOf<Int>()
    for (i in 0 until list.size step 16) {
        var hash = 0
        val listSlice = list.slice(i until i + 16)
        listSlice.forEach {
            hash = hash xor it
        }
        denseHash.add(hash)
    }
    val denseHashHex = denseHash.map {
        String.format("%02x", it)
    }
    return denseHashHex.joinToString("")
}
