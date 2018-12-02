fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    var common = false
    for (id1 in input) {
        for (id2 in input) {
            common = compareBoxIDs(id1, id2)
            if (common)
                break
        }
        if (common)
            break
    }
}

private fun compareBoxIDs(id1: String, id2: String): Boolean {
    var common = ""
    var commonCount = 0
    for (i in 0 until id1.length) {
        if (id1[i] == id2[i]) {
            commonCount++
            common += id1[i]
            if (i - commonCount > 0)
                continue
        }
    }
    if (commonCount == (id1.length - 1)) {
        println("Common Characters in IDs: $common")
        return true
    }
    return false
}
