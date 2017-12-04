import kotlin.math.absoluteValue
import kotlin.system.exitProcess

fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = Integer.parseInt(readLine())
    // special handling for 1
    if (input == 1) {
        print("Steps: 0")
        exitProcess(0)
    }
    var ring = 0
    var biggestNumberInCurrentRing = 1
    // find out which ring the number is located in
    while (biggestNumberInCurrentRing < input) {
        ring += 1
        biggestNumberInCurrentRing += ring * 8
    }
    val smallestNumberInCurrentRing = biggestNumberInCurrentRing - (ring*8) + 1
    val squaresInCurrentRing = ring * 8
    val innerSquaresPerSide = (squaresInCurrentRing - 4) / 4
    // find all the middleSquares (Squares exactly ring steps away from 1)
    var middleSquares = mutableListOf<Int>()
    middleSquares.add(smallestNumberInCurrentRing + (innerSquaresPerSide / 2))
    for (i in 0..2) {
        val nextMiddleSquare = middleSquares[i] + (ring * 2)
        middleSquares.add(nextMiddleSquare)
    }
    val stepsList = middleSquares.map {
        value -> (input - value).absoluteValue
    }
    val steps = stepsList.min()!! + ring
    println("Steps: $steps")
}
