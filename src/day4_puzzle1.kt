fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val validPassphrases = input.filter {
        passphraseValid(it)
    }
    val validCount = validPassphrases.count()
    print("Valid Passphrases: $validCount")
}

fun passphraseValid(passphrase: String): Boolean {
    val words = passphrase.split("\t"," ")
    for (i in 0 until words.size) {
        val word = words[i]
        for (j in i + 1 until words.size) {
            if (word == words[j]) {
                return false
            }
        }
    }
    return true
}