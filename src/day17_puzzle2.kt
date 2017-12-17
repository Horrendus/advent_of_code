fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = Integer.parseInt(readLine())

    val max = 50_000_000
    var currentPosition = 0
    var valueAfterZero = 0
    (1..max).forEach { currentNumber ->
        currentPosition = (currentPosition + input) % currentNumber
        currentPosition++
        if (currentPosition == 1) {
            valueAfterZero = currentNumber
        }
    }
    println("Value after Zero: $valueAfterZero")
}
