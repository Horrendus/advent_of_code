// needs day22_puzzle1.kt for common declarations & functions
private val bursts = 10_000_000
private val offset = bursts / 10_000

private val infectionStatusMap = Array(25 + (2 * offset)) { Array(25 + (2 * offset)) { '.' } }

fun main(args: Array<String>) {
    val input = mutableListOf<String>()
    println("Enter puzzle input")
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    input.forEachIndexed { rowIndex, line ->
        line.forEachIndexed { columnIndex, c ->
            infectionStatusMap[rowIndex + offset][columnIndex + offset] = c
        }
    }
    val virus = Virus2()
    (0 until bursts).forEach {
        virus.doBurst()
    }
    println("Infections: ${virus.infectionsDone}")
}

class Virus2 {
    var infectionsDone = 0
    private var currentPosition = Position(12 + offset, 12 + offset)
    private var orientation = directions[0]

    fun doBurst() {
        when (infectionStatusMap[currentPosition]) {
            '.' -> {
                infectionStatusMap[currentPosition] = 'W'
                orientation = turnOrientation(right = false)
            }
            'W' -> {
                infectionStatusMap[currentPosition] = '#'
                infectionsDone++
            }
            '#' -> {
                infectionStatusMap[currentPosition] = 'F'
                orientation = turnOrientation(right = true)
            }
            'F' -> {
                infectionStatusMap[currentPosition] = '.'
                orientation = reverseOrientation()
            }
        }
        currentPosition += orientation
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

    private fun reverseOrientation(): Position {
        var index = directions.indexOf(orientation)
        index += 2
        if (index >= directions.size) {
            index %= directions.size
        }
        return directions[index]
    }
}

private operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> {
    return Pair(first + other.first, second + other.second)
}

private operator fun Array<Array<Char>>.get(position: Position): Char {
    return this[position.first][position.second]
}
