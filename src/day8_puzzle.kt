private var registers = hashMapOf<String, Int>()

fun main(args: Array<String>) {
    println("Enter puzzle input")
    var maximumValue = Integer.MIN_VALUE
    while (true) {
        val line = readLine() ?: break
        handleLine(line)
        val currentMaximum = registers.maxBy { it.value }
        if (currentMaximum?.value ?: Integer.MIN_VALUE > maximumValue) {
            maximumValue = currentMaximum?.value ?: maximumValue
        }
    }
    println("$registers")
    val max = registers.maxBy { it.value }
    println("Maximum Value: ${max?.value} in Register ${max?.key}")
    println("Maximum Value ever encountered: $maximumValue")
}

private fun handleLine(line: String) {
    val tokens = line.split(" ")
    val register = tokens[0]
    val operation = tokens[1]
    val operand = Integer.parseInt(tokens[2])

    val testRegister = tokens[4]
    val testOperation = tokens[5]
    val testOperand = Integer.parseInt(tokens[6])
    if (testCondition(Triple(testRegister, testOperation, testOperand))) {
        val operationResult = doOperation(Triple(register, operation, operand))
        registers[register] = operationResult
    }
}

private fun testCondition(condition: Triple<String, String, Int>) : Boolean {
    val registerValue = getValue(condition.first)
    return when (condition.second) {
        ">" -> registerValue > condition.third
        "<" -> registerValue < condition.third
        "<=" -> registerValue <= condition.third
        ">=" -> registerValue >= condition.third
        "==" -> registerValue == condition.third
        "!=" -> registerValue != condition.third
        else -> false
    }
}

private fun doOperation(operation: Triple<String, String, Int>) : Int {
    val registerValue = getValue(operation.first)
    return when (operation.second) {
        "inc" -> registerValue + operation.third
        "dec" -> registerValue - operation.third
        else -> registerValue
    }
}

private fun getValue(register: String) : Int {
    return registers[register] ?: 0
}