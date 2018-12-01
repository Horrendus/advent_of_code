typealias Position = Pair<Int, Int>

val directions = listOf(Position(-1, 0), Position(0, 1), Position(1, 0), Position(0, -1))

// Input is 25x25. Virus makes 1000 bursts. 2025 allows the virus to move
// the maximum of 1000 in the same direction and makes position bursts easy
private val infectionStatusMap = Array(2025) { Array(2025) { '.' } }

fun main(args: Array<String>) {
    val input = mutableListOf<String>()
    println("Enter puzzle input")
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    input.forEachIndexed { rowIndex, line ->
        line.forEachIndexed { columnIndex, c ->
            infectionStatusMap[rowIndex + 1000][columnIndex + 1000] = c
        }
    }
    val virus = Virus()
    (0 until 10000).forEach {
        virus.doBurst()
    }
    println("Infections: ${virus.infectionsDone}")
}

class Virus {
    var infectionsDone = 0
    private var currentPosition = Position(1012, 1012)
    private var orientation = directions[0]

    fun doBurst() {
        println("$currentPosition $orientation ${infectionStatusMap[currentPosition]}")
        if (infectionStatusMap[currentPosition] == '#') {
            orientation = turnOrientation(right = true)
            infectionStatusMap[currentPosition] = '.'
        } else {
            orientation = turnOrientation(right = false)
            infectionStatusMap[currentPosition] = '#'
            infectionsDone++
        }
        currentPosition += orientation
        println("new direction: $orientation new position: $currentPosition")
    }

    private fun turnOrientation(right: Boolean): Position {
        var index = directions.indexOf(orientation)
        if (right) {
            index++
            if (index >= directions.size) {
                index %= directions.size
            }
        } else {
            index--
            if (index < 0) {
                index += directions.size
            }
        }
        return directions[index]
    }
}

private operator fun Array<Array<Char>>.get(position: Position): Char {
    return this[position.first][position.second]
}

operator fun Array<Array<Char>>.set(position: Position, value: Char) {
    this[position.first][position.second] = value
}

private operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> {
    return Pair(first + other.first, second + other.second)
}
