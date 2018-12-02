fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val boxIDSets = input.map {
        it.toSet()
    }
    var countLetterContainedExactlyTwice = 0
    var countLetterContainedExactlyThrice = 0
    for (i in 0 until input.size) {
        val boxID = input[i]
        var foundTwice = false
        var foundThrice = false
        for (letter in boxIDSets[i]) {
            if (boxID.count { it == letter } == 2 && !foundTwice) {
                foundTwice = true
                countLetterContainedExactlyTwice += 1
            }
            if (boxID.count { it == letter } == 3 && !foundThrice) {
                foundThrice = true
                countLetterContainedExactlyThrice += 1
            }
            if (foundTwice && foundThrice)
                break
        }
    }
    println("Found exactly twice: $countLetterContainedExactlyTwice")
    println("Found exactly thrice: $countLetterContainedExactlyThrice")
    println("Checksum: ${countLetterContainedExactlyTwice * countLetterContainedExactlyThrice}")
}
