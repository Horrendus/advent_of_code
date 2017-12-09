fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = readLine() ?: ""

    var score = 0
    var level = 0
    var removedGarbage = 0

    var inGarbage = false
    var ignoreNext = false

    for (token in input) {
        if (ignoreNext) {
            ignoreNext = false
            continue
        }
        if (inGarbage && token != '>' && token != '!') {
            removedGarbage++
            continue
        }
        when (token) {
            '!' -> ignoreNext = true
            '<' -> inGarbage = true
            '>' -> inGarbage = false
            '{' -> level++
            '}' -> { score += level; level-- }
        }
    }
    println("Score: $score Garbage removed: $removedGarbage")
}
