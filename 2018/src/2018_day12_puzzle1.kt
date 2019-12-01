import java.util.*

private val spreadingRules = mutableMapOf<String,Char>()
private val potGenerations = Array(21) { LinkedList<Char>() }

fun main(args: Array<String>) {
    println("Enter puzzle input")
    val initialStateLine = readLine() ?: return
    val splittedLine = initialStateLine.split(":")
    val initialState = LinkedList(splittedLine[1].trim().toList())
    readLine() // empty line
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    input.forEach {
        parseSpreadingRule(it)
    }
    // add two pots at beginning & end
    initialState.addFirst('.')
    initialState.addFirst('.')
    initialState.add('.')
    initialState.add('.')
    var zeroPos = 2
    potGenerations[0] = initialState
    for (g in 1..20) {
        val lastGen = potGenerations[g-1]
        val newGen = LinkedList(lastGen)
        for (i in 0 until lastGen.size) {
            var spreadPattern = ""
            spreadPattern += (lastGen.getOrElse(i-2) {'.'})
            spreadPattern += (lastGen.getOrElse(i-1) {'.'})
            spreadPattern += (lastGen.getOrElse(i) {'.'})
            spreadPattern += (lastGen.getOrElse(i+1) {'.'})
            spreadPattern += (lastGen.getOrElse(i+2) {'.'})
            val newState = spreadingRules[spreadPattern] ?: '.'
            newGen[i] = newState
        }
        if (newGen[lastGen.size-1] == '#') newGen.add('.')
        if (newGen[lastGen.size-2] == '#') newGen.add('.')
        if (newGen[0] == '#') { newGen.addFirst('.'); zeroPos++ }
        if (newGen[1] == '#') { newGen.addFirst('.'); zeroPos++ }
        potGenerations[g] = newGen
    }
    val genTwenty = potGenerations[20]
    println(genTwenty.joinToString(""))
    var sumPotsWithPlants = 0
    for (i in 0 until genTwenty.size) {
        val potNumber = i - zeroPos
        if (genTwenty[i] == '#') sumPotsWithPlants += potNumber
    }
    println(zeroPos)
    println(sumPotsWithPlants)
}

private fun parseSpreadingRule(line: String) {
    val ruleAndEnhancement = line.split("=>")
    val rule = ruleAndEnhancement[0].trim()
    val pot = ruleAndEnhancement[1].trim().toCharArray()[0]
    spreadingRules[rule] = pot
}