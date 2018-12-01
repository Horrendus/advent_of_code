import java.io.File

val diagram = Array(202) { Array(202) { ' ' } }
val directionMapping = listOf(Pair(Pair(1, 0), '|'), Pair(Pair(0, 1), '-'), Pair(Pair(-1, 0), '|'), Pair(Pair(0, -1), '-'))

var currentPosition = Pair(0, 0)
var currentDirection = Pair(1, 0)

fun main(args: Array<String>) {
    val inputFile = File("input_day19.txt")
    val input = inputFile.readLines()
    input.forEachIndexed { lineIndex, line ->
        line.forEachIndexed { columnIndex, character ->
            diagram[lineIndex][columnIndex] = character
        }
    }
    val startingCharacter = '|'
    val startingColumn = diagram[0].indexOf(startingCharacter)
    currentPosition = Pair(0, startingColumn)
    val letters = mutableListOf<Char>()
    var currentCharacter = startingCharacter
    var steps = 0
    while (currentCharacter != ' ') {
        steps++
        when {
            currentCharacter == '+' -> changeDirection()
            currentCharacter.isLetter() -> letters.add(currentCharacter)
        }
        currentPosition += currentDirection
        currentCharacter = diagram[currentPosition]
    }
    println("Letter Order: ${letters.joinToString("")}")
    println("Number of steps: $steps")
}

private fun changeDirection() {
    for (direction in directionMapping) {
        val nextPosition = currentPosition + direction.first
        val previousPosition = currentPosition - currentDirection
        if (diagram[nextPosition] == direction.second && nextPosition != previousPosition) {
            currentDirection = direction.first
            break
        }
    }
}

private operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> {
    return Pair(first + other.first, second + other.second)
}

private operator fun Pair<Int, Int>.minus(other: Pair<Int, Int>): Pair<Int, Int> {
    return Pair(first - other.first, second - other.second)
}

private operator fun Array<Array<Char>>.get(position: Position): Char {
    return this[position.first][position.second]
}
