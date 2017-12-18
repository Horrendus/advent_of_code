private val registers = hashMapOf<String, Long>()
private var lastSoundFrequency = 0L
private var currentInstruction = 0L
private val instructions = mutableListOf<String>()

fun main(args: Array<String>) {
    println("Enter puzzle input")
    while (true) {
        val line = readLine() ?: break
        instructions.add(line)
    }
    while (true) {
        val doBreak = handleCurrentLine()
        if (doBreak) break
    }
    println("Last sound played: $lastSoundFrequency")
}

private fun handleCurrentLine(): Boolean {
    val line = instructions[currentInstruction.toInt()]
    val tokens = line.split(" ")
    return doOperation(tokens)
}

private fun doOperation(tokens: List<String>): Boolean {
    val operation = tokens[0]
    val register = tokens[1]
    val operand = tokens.getOrElse(2) { "-1" }
    when (operation) {
        "snd" -> lastSoundFrequency = getValue(register)
        "set" -> registers[register] = getValue(operand)
        "add" -> registers[register] = getValue(register) + getValue(operand)
        "mul" -> registers[register] = getValue(register) * getValue(operand)
        "mod" -> registers[register] = getValue(register) % getValue(operand)
        "rcv" -> if (getValue(register) != 0L) return true
        "jgz" -> {
            if (getValue(register) > 0) {
                currentInstruction += getValue(operand)
                return false
            }
        }
        else -> println("Unknown Operation")
    }
    currentInstruction++
    return false
}

private fun getValue(register: String): Long {
    val value = register.toLongOrNull()
    return value ?: (registers[register] ?: 0)
}
