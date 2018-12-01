private var programs = mutableListOf('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')

fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = readLine() ?: ""
    val commands = input.split(",")
    var i = 1
    val repetitions = 1_000_000_000
    val programsCopy = programs.toList()
    while (i <= repetitions) {
        commands.forEach { command ->
            when (command[0]) {
                's' -> spin(Integer.parseInt(command.slice(1 until command.length)))
                'x' -> {
                    val exchangeCommandTokens = command.split("/")
                    val position1 = Integer.parseInt(exchangeCommandTokens[0].slice(1 until exchangeCommandTokens[0].length))
                    val position2 = Integer.parseInt(exchangeCommandTokens[1])
                    exchange(position1, position2)
                }
                'p' -> partner(command[1], command[3])
                else -> println("ERROR: UNKNOWN COMMAND: $command")
            }
        }
        if (i == 1) {
            val programsString = programs.joinToString("")
            println("Puzzle 1 Answer: $programsString")
        }
        if (programs == programsCopy) {
            // after i iterations, programs is the same as in the beginning
            // so we don't need 1 billion iterations and can just set i to the last
            // factor of current i in 1 billion
            val repeatingFactor = repetitions / i
            i *= repeatingFactor
        }
        i++
    }
    val programsString = programs.joinToString("")
    println("Puzzle 2 Answer: $programsString")
}

fun spin(number: Int) {
    val spinIndex = programs.size - number
    val sliceEnd = programs.slice(spinIndex until programs.size)
    val sliceBeginning = programs.slice(0 until spinIndex)
    programs = (sliceEnd + sliceBeginning).toMutableList()
}

fun exchange(position1: Int, position2: Int) {
    val temp = programs[position1]
    programs[position1] = programs[position2]
    programs[position2] = temp
}

fun partner(program1: Char, program2: Char) {
    val position1 = programs.indexOf(program1)
    val position2 = programs.indexOf(program2)
    exchange(position1, position2)
}
