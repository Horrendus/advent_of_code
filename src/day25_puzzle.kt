import java.io.Serializable

// Input has to be "translated" manually to this map
val blueprintsMap = hashMapOf(
        "beginState" to "A",
        "stepsBeforeChecksum" to 12317297,
        "A" to hashMapOf(
                0 to hashMapOf(
                        "value" to 1,
                        "direction" to 1,
                        "nextState" to "B"
                ),
                1 to hashMapOf(
                        "value" to 0,
                        "direction" to -1,
                        "nextState" to "D"
                )
        ),
        "B" to hashMapOf(
                0 to hashMapOf(
                        "value" to 1,
                        "direction" to 1,
                        "nextState" to "C"
                ),
                1 to hashMapOf(
                        "value" to 0,
                        "direction" to 1,
                        "nextState" to "F"
                )
        ),
        "C" to hashMapOf(
                0 to hashMapOf(
                        "value" to 1,
                        "direction" to -1,
                        "nextState" to "C"
                ),
                1 to hashMapOf(
                        "value" to 1,
                        "direction" to -1,
                        "nextState" to "A"
                )
        ),
        "D" to hashMapOf(
                0 to hashMapOf(
                        "value" to 0,
                        "direction" to -1,
                        "nextState" to "E"
                ),
                1 to hashMapOf(
                        "value" to 1,
                        "direction" to 1,
                        "nextState" to "A"
                )
        ),
        "E" to hashMapOf(
                0 to hashMapOf(
                        "value" to 1,
                        "direction" to -1,
                        "nextState" to "A"
                ),
                1 to hashMapOf(
                        "value" to 0,
                        "direction" to 1,
                        "nextState" to "B"
                )
        ),
        "F" to hashMapOf(
                0 to hashMapOf(
                        "value" to 0,
                        "direction" to 1,
                        "nextState" to "C"
                ),
                1 to hashMapOf(
                        "value" to 0,
                        "direction" to 1,
                        "nextState" to "E"
                )
        )
)

fun main(args: Array<String>) {
    val turingMachine = TuringMachine(blueprintsMap)
    turingMachine.run()
    val checksum = turingMachine.checksum()
    println("Checksum: $checksum")
}

class TuringMachine(private val blueprints: Map<String, Serializable?>) {

    private val tape = Array((blueprints["stepsBeforeChecksum"] as Int) * 2 + 1) { 0 }
    private var currentTapePosition = blueprints["stepsBeforeChecksum"] as Int
    private var currentState = blueprints["beginState"] as String

    fun run() {
        val stepsBeforeChecksum = blueprints["stepsBeforeChecksum"] as Int
        (0 until stepsBeforeChecksum).forEach {
            val currentValue = tape[currentTapePosition]
            if (blueprints[currentState] is HashMap<*, *>) {
                val stateInformation = blueprints[currentState] as? HashMap<*, *>
                val stateInformationForValue = stateInformation?.get(currentValue) as? HashMap<*, *> ?:
                        hashMapOf("value" to currentValue, "direction" to 0, "nextState" to currentState)
                val valueToWrite = stateInformationForValue["value"] as Int
                val direction = stateInformationForValue["direction"] as Int
                val nextState = stateInformationForValue["nextState"] as String
                tape[currentTapePosition] = valueToWrite
                currentTapePosition += direction
                currentState = nextState
            }
        }
    }

    fun checksum(): Int {
        return tape.count {
            it == 1
        }
    }
}
