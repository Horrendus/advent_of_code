fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<Int>()
    while (true) {
        val line = readLine() ?: break
        input.add(Integer.parseInt(line))
    }
    var jumps = 0
    var currentPosition = 0
    while (currentPosition < input.size && currentPosition >= 0) {
        val jump = input[currentPosition]
        when (jump >= 3) {
            true -> input[currentPosition]--
            false -> input[currentPosition]++
        }
        currentPosition += jump
        jumps++
    }
    print("Finished after $jumps Jumps")
}
