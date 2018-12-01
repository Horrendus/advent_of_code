private val instructions = mutableListOf<String>()
private val programs = listOf(Program(0), Program(1))

fun main(args: Array<String>) {
    println("Enter puzzle input")
    while (true) {
        val line = readLine() ?: break
        instructions.add(line)
    }
    var currentProgram = 0
    while (!isDeadlock() && !isFinished()) {
        programs[currentProgram].run()
        currentProgram = (currentProgram + 1) % programs.size
    }
    println("Times that Program 1 sent something: ${programs[1].valuesSent}")
}

fun isDeadlock(): Boolean {
    return programs[0].waiting && programs[1].waiting
}

fun isFinished(): Boolean {
    return programs[0].finished && programs[1].finished
}


class Program constructor(private val id: Int) {

    var valuesSent = 0
    val finished get() = currentInstruction > instructions.size || currentInstruction < 0
    private val incomingQueue = mutableListOf<Long>()
    private var waitingOnReceive = false
    val waiting get() = waitingOnReceive && incomingQueue.isEmpty()

    private var currentInstruction = 0L
    private val registers = hashMapOf<String, Long>()

    init {
        registers["p"] = id.toLong()
    }

    private fun sendTo(program: Program, value: Long) {
        // println("Program $id sending to ${program.id} value: $value")
        program.incomingQueue.add(value)
        valuesSent++
    }

    private fun getValue(register: String): Long {
        val value = register.toLongOrNull()
        return value ?: (registers[register] ?: 0)
    }

    fun run() {
        var doBreak = false
        while (!doBreak && !finished) {
            val line = instructions[currentInstruction.toInt()]
            val tokens = line.split(" ")
            doBreak = doOperation(tokens)
        }
        return
    }

    private fun doOperation(tokens: List<String>): Boolean {
        val operation = tokens[0]
        val register = tokens[1]
        val operand = tokens.getOrElse(2) { "-1" }
        when (operation) {
            "snd" -> sendTo(programs[(id + 1) % programs.size], getValue(register))
            "set" -> registers[register] = getValue(operand)
            "add" -> registers[register] = getValue(register) + getValue(operand)
            "mul" -> registers[register] = getValue(register) * getValue(operand)
            "mod" -> registers[register] = getValue(register) % getValue(operand)
            "rcv" -> if (incomingQueue.isNotEmpty()) {
                waitingOnReceive = false
                registers[register] = incomingQueue.removeAt(0)
            } else {
                waitingOnReceive = true
                return true
            }
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
}
