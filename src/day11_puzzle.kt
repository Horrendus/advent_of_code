import kotlin.math.absoluteValue

// Thanks to https://www.redblobgames.com/grids/hexagons/ for the Tips on Cube Coordinates & Distance in Hex Grids
enum class HexDirection(val coordinateChange: Triple<Int, Int, Int>) {
    SW(Triple(0, -1, 1)),
    NW(Triple(1, -1, 0)),
    N(Triple(1, 0, -1)),
    NE(Triple(0, 1, -1)),
    SE(Triple(-1, 1, 0)),
    S(Triple(-1, 0, 1))
}

fun main(args: Array<String>) {
    val directionsMap = hashMapOf(
            Pair("nw", HexDirection.NW), Pair("sw", HexDirection.SW),
            Pair("ne", HexDirection.NE), Pair("se", HexDirection.SE),
            Pair("n", HexDirection.N), Pair("s", HexDirection.S))

    val center = Triple(0, 0, 0)

    println("Enter puzzle input")
    val input = readLine() ?: ""
    val walkingDirections = input.split(",").map {
        directionsMap[it]?.coordinateChange ?: center
    }
    var position = center
    var maximum = 0
    walkingDirections.forEach {
        position += it
        val currentDistance = hexDistance(position)
        maximum = maxOf(maximum, currentDistance)
    }
    println("Distance: ${hexDistance(position)} Maximum Distance ever: $maximum Position: $position")
}

operator fun Triple<Int, Int, Int>.plus(other: Triple<Int, Int, Int>): Triple<Int, Int, Int> {
    return Triple(first + other.first, second + other.second, third + other.third)
}

fun hexDistance(position: Triple<Int, Int, Int>): Int {
    return maxOf(position.first.absoluteValue, position.second.absoluteValue, position.third.absoluteValue)
}
