

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
    println("Valid Passphrases: $validCount")
}

private fun passphraseValid(passphrase: String): Boolean {
    val words = passphrase.split("\t"," ")
    for (i in 0 until words.size) {
        val word = words[i]
        for (j in i + 1 until words.size) {
            if (isAnagram(word, words[j])) {
                // println("rejecting: $words")
                return false
            }
        }
    }
    // println("accepting: $words")
    return true
}

// function returns true if the word are anagrams
private fun isAnagram(word1: String, word2: String): Boolean {
    val isAnagram = word1.all {
        word2.contains(it)
    } && word1.length == word2.length
    return isAnagram
}
