enum class Direction {
    UP, DOWN, LEFT, RIGHT
}

val invalid = Pair(-1, -1)

// dimension must always be odd
val dimension = 30

var spiral = Array(dimension) { Array(dimension) { 0 } }

fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = Integer.parseInt(readLine())
    val middle = Pair(dimension / 2, dimension / 2)
    spiral[middle.first][middle.second] = 1
    spiral[middle.first][middle.second + 1] = 1
    var direction = Direction.UP
    var value = 1
    var nextCell = middle + Pair(-1, 1)
    var nextValues = Pair(direction, nextCell)
    while (nextValues.second != invalid && value < input) {
        nextCell = nextValues.second
        direction = nextValues.first
        value = calculateNumber(Pair(nextCell.first, nextCell.second))
        spiral[nextCell.first][nextCell.second] = value
        nextValues = nextCell(direction, nextCell)
    }
    print("Biggest value: $value")
}

private fun nextCell(currentDirection: Direction, cell: Pair<Int, Int>): Pair<Direction, Pair<Int, Int>> {
    val upNeighbour = neighbour(Direction.UP, cell)
    val downNeighbour = neighbour(Direction.DOWN, cell)
    val leftNeighbour = neighbour(Direction.LEFT, cell)
    val rightNeighbour = neighbour(Direction.RIGHT, cell)
    when (currentDirection) {
        Direction.UP -> {
            when (leftNeighbour != invalid && getValue(leftNeighbour) != 0) {
                true -> return Pair(Direction.UP, upNeighbour)
                false -> return Pair(Direction.LEFT, leftNeighbour)
            }
        }
        Direction.DOWN -> {
            when (rightNeighbour != invalid && getValue(rightNeighbour) != 0) {
                true -> return Pair(Direction.DOWN, downNeighbour)
                false -> return Pair(Direction.RIGHT, rightNeighbour)
            }
        }
        Direction.LEFT -> {
            when (downNeighbour != invalid && getValue(downNeighbour) != 0) {
                true -> return Pair(Direction.LEFT, leftNeighbour)
                false -> return Pair(Direction.DOWN, downNeighbour)
            }
        }
        Direction.RIGHT -> {
            when (upNeighbour != invalid && getValue(upNeighbour) != 0) {
                true -> return Pair(Direction.RIGHT, rightNeighbour)
                false -> return Pair(Direction.UP, upNeighbour)
            }
        }
    }
}

private fun neighbour(direction: Direction, cell: Pair<Int, Int>): Pair<Int, Int> {
    when (direction) {
        Direction.UP ->
            when (cell.first - 1 > 0) {
                true -> return cell + Pair(-1, 0)
                false -> return invalid
            }
        Direction.DOWN ->
            when (cell.first + 1 < dimension) {
                true -> return cell + Pair(1, 0)
                false -> return invalid
            }
        Direction.LEFT ->
            when (cell.second - 1 > 0) {
                true -> return cell + Pair(0, -1)
                false -> return invalid
            }
        Direction.RIGHT ->
            when (cell.second + 1 < dimension) {
                true -> return cell + Pair(0, 1)
                false -> return invalid
            }
    }

}

private fun calculateNumber(cell: Pair<Int, Int>): Int {
    val neighbours = listOf(Pair(-1, -1), Pair(0, -1), Pair(1, -1),
            Pair(-1, 0), Pair(1, 0),
            Pair(-1, 1), Pair(0, 1), Pair(1, 1))
    val neighbourValues = neighbours.map { getValue(cell + it) }
    return maxOf(neighbourValues.sum(), 1)
}

operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> {
    return Pair(first + other.first, second + other.second)
}

private fun getValue(cell: Pair<Int, Int>): Int {
    if (cell.first < dimension && cell.second < dimension) {
        return spiral[cell.first][cell.second]
    }
    return 0
}

private fun printArray(array: Array<Array<Int>>) {
    array.forEach {
        it.forEach {
            print("$it\t")
        }
        println()
    }
}
