fun main(args: Array<String>) {
    val factorA = 16807L
    val factorB = 48271L
    val divisor = 2147483647L

    print("Enter Generator A starting Value: ")
    val inputA = readLine()
    print("Enter Generator B starting Value: ")
    val inputB = readLine()

    var valueA = inputA?.toLong() ?: 0
    var valueB = inputB?.toLong() ?: 0
    var match = 0

    val rounds = 40_000_000
    (1..rounds).forEach {
        valueA = (valueA * factorA) % divisor
        valueB = (valueB * factorB) % divisor
        val valueAString = valueA.toString(2).padStart(16, '0')
        val valueBString = valueB.toString(2).padStart(16, '0')
        val sixteenBitsOfA = valueAString.substring(valueAString.length - 16, valueAString.length)
        val sixteenBitsOfB = valueBString.substring(valueBString.length - 16, valueBString.length)
        if (sixteenBitsOfA == sixteenBitsOfB) match++
    }
    println("Matches: $match")
}
