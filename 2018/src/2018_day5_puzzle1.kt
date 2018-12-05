fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = readLine() ?: return
    var inputAsList = input.toMutableList()
    inputAsList = reactPolymer(inputAsList)
    println("Part1: Leftover Size of Polymer: ${inputAsList.size}")
    var minimumSize = input.length
    for (c in 'a'..'z') {
        var inputCopy = input
        inputCopy = inputCopy.replace("$c", "")
        inputCopy = inputCopy.replace("${c.toUpperCase()}", "")
        inputAsList = inputCopy.toMutableList()
        inputAsList = reactPolymer(inputAsList)
        minimumSize = Math.min(minimumSize, inputAsList.size)
    }
    println("Part2: Improved Polymer Size: $minimumSize")
}

private fun reactPolymer(inputAsList: MutableList<Char>) : MutableList<Char> {
    var i = 0
    while (i < (inputAsList.size - 1) && inputAsList.size > 1) {
        val currentUnit = inputAsList[i]
        val nextUnit = inputAsList[i+1]
        if (Math.abs(currentUnit.toInt()-nextUnit.toInt())==32) {
            inputAsList.removeAt(i)
            inputAsList.removeAt(i)
            if (i > 0)
                i--
        } else {
            i++
        }
    }
    return inputAsList
}
