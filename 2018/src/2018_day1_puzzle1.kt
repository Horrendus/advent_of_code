fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val numbers = input.map { line ->
        Integer.parseInt(line)
    }
    var sum = 0
    var seenFrequencies = mutableListOf<Int>()
    seenFrequencies.add(sum)
    var seenFrequencyTwice = false
    var firstRepetition = true
    while (!seenFrequencyTwice) {
        for (number in numbers) {
            sum += number
            if (seenFrequencies.contains(sum)) {
                println("First Frequency seen twice: $sum")
                seenFrequencyTwice = true
                if (!firstRepetition) {
                    break
                }
            } else {
                seenFrequencies.add(sum)
            }
            if (firstRepetition) {
                println("Resulting Frequency (after first Repetition: $sum")
                firstRepetition = false
            }
        }
    }
}
