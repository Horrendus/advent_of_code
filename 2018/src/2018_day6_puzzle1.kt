var maxDimensionX = 0
var maxDimensionY = 0

fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val locations = input.map {line ->
        parseInputLine(line)
    }
    var numberOfSafePoints = 0
    for (x in 0..maxDimensionX) {
        for (y in 0..maxDimensionY) {
            val p = Pair(x,y)
            var closestLocation = Location(Pair(0,0),0,false)
            var closestLocationDistance = Integer.MAX_VALUE
            var distanceToAllLocations = 0
            for (location in locations) {
                val distance = distance(p, location.coordinate)
                distanceToAllLocations += distance
                if (distance < closestLocationDistance) {
                    closestLocationDistance = distance
                    closestLocation = location
                } else if (distance == closestLocationDistance) {
                    closestLocation = Location(Pair(0,0),0,false)
                }
            }
            if (closestLocation != Location(Pair(0,0),0,false)) {
                closestLocation.areaSize++
                if (!closestLocation.hasInfiniteArea &&
                    (x == 0 || y == 0 || x == maxDimensionX || y == maxDimensionY)) {
                    closestLocation.hasInfiniteArea = true
                }
            }
            if (distanceToAllLocations < 10000) {
                numberOfSafePoints++
            }
        }
    }
    val locationsWithFiniteArea = locations.filter { location -> !location.hasInfiniteArea }
    val locationWithBiggestArea = locationsWithFiniteArea.maxBy { it.areaSize }
    println("Location with the biggest Area: $locationWithBiggestArea")
    println("Area of Safe Points: $numberOfSafePoints")
}

private fun parseInputLine(line: String) : Location {
    val splittedLine = line.split(",")
    val x = splittedLine[0].trim().toInt()
    maxDimensionX = Math.max(maxDimensionX, x)
    val y = splittedLine[1].trim().toInt()
    maxDimensionY = Math.max(maxDimensionY, y)
    val coordinate = Pair(x,y)
    return Location(coordinate, 0, false)
}

private fun distance(p1: Pair<Int,Int>, p2: Pair<Int,Int>) : Int {
    return Math.abs(p1.first - p2.first) + Math.abs(p1.second - p2.second)
}

private data class Location(val coordinate: Pair<Int,Int>, var areaSize: Int, var hasInfiniteArea: Boolean)
