private val registers = hashMapOf<String, Long>()
private var mulCalled = 0
private var currentInstruction = 0L
private val instructions = mutableListOf<String>()

fun main(args: Array<String>) {
    println("Enter puzzle input")
    while (true) {
        val line = readLine() ?: break
        instructions.add(line)
    }
    while (currentInstruction < instructions.size && currentInstruction >= 0) {
        handleCurrentLine()
    }
    println("Times mul was called: $mulCalled")
}

private fun handleCurrentLine() {
    val line = instructions[currentInstruction.toInt()]
    val tokens = line.split(" ")
    doOperation(tokens)
}

private fun doOperation(tokens: List<String>) {
    val operation = tokens[0]
    val register = tokens[1]
    val operand = tokens.getOrElse(2) { "-1" }
    when (operation) {
        "set" -> registers[register] = getValue(operand)
        "sub" -> registers[register] = getValue(register) - getValue(operand)
        "mul" -> {
            registers[register] = getValue(register) * getValue(operand)
            mulCalled++
        }
        "jnz" -> {
            if (getValue(register) != 0L) {
                currentInstruction += getValue(operand)
                return
            }
        }
        else -> println("Unknown Operation")
    }
    currentInstruction++
}

private fun getValue(register: String): Long {
    val value = register.toLongOrNull()
    return value ?: (registers[register] ?: 0)
}
