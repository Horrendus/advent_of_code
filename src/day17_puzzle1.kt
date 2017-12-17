fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = Integer.parseInt(readLine())

    val buffer = mutableListOf<Int>()
    buffer.add(0)
    var currentPosition = 0
    (1..2017).forEach { currentNumber ->
        currentPosition = (currentPosition + input) % buffer.size
        currentPosition++
        buffer.add(currentPosition, currentNumber)
    }
    val afterLastInsertion = buffer[buffer.indexOf(2017) + 1]
    println("Value after 2017 insertion: $afterLastInsertion")
}
