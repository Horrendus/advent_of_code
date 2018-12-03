private typealias Coordinate = Pair<Int, Int>

fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val fabric = mutableMapOf<Coordinate, Pair<String,Int>>()
    val rectangles = input.map {
        parseInputLine(it)
    }
    val collisionFreeIDs = mutableListOf<String>()
    for (rectangle in rectangles) {
        var collisionFree = true
        val startingPoint = rectangle.second
        val dimension = rectangle.third
        for (x in 0 until dimension.first) {
            for (y in 0 until dimension.second) {
                val currentPoint = startingPoint + Pair(x,y)
                val previousClaim = fabric.getOrDefault(currentPoint,Pair("",0))
                if (previousClaim.second > 0) {
                    collisionFree = false
                    collisionFreeIDs.remove(previousClaim.first)
                }
                fabric[currentPoint] = Pair(rectangle.first, previousClaim.second + 1)
            }
        }
        if (collisionFree) {
            collisionFreeIDs.add(rectangle.first)
        }
    }
    println("$fabric, ${fabric.size}")
    var pointsClaimedAtLeastTwice = 0
    for (claim in fabric.values) {
        if (claim.second > 1) {
            pointsClaimedAtLeastTwice++
        }
    }
    println("$pointsClaimedAtLeastTwice were claimed at least twice")
    println("Claim IDs without collisions: $collisionFreeIDs")
}

private fun parseInputLine(inputLine: String) : Triple<String, Coordinate, Pair<Int, Int>> {
    val splittedLine = inputLine.split("@",",",":","x")
    val trimmedLine = splittedLine.map { it.trim() }
    val coordinate = Pair(Integer.parseInt(trimmedLine[1]), Integer.parseInt(trimmedLine[2]))
    val dimensions = Pair(Integer.parseInt(trimmedLine[3]), Integer.parseInt(trimmedLine[4]))
    return Triple(splittedLine[0], coordinate, dimensions)
}

private operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> {
    return Pair(first + other.first, second + other.second)
}
