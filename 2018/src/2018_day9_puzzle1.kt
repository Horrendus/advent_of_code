private const val numberOfPlayers = 465
private const val lastMarbleValue = 71498

fun main(args: Array<String>) {
    val marbleCircle = mutableListOf(0)
    var currentPlayer = 0
    var currentMarbleValue = 0
    var currentMarblePosition = 0
    var scores = mutableMapOf<Int, Int>()
    while (currentMarbleValue < lastMarbleValue) {
        currentPlayer = (currentPlayer % numberOfPlayers) + 1
        currentMarbleValue++
        if (currentMarbleValue % 23 == 0) {
            currentMarblePosition = (currentMarblePosition - 7) % marbleCircle.size
            if (currentMarblePosition < 0) { currentMarblePosition += marbleCircle.size }
            scores[currentPlayer] = (scores[currentPlayer] ?: 0) + currentMarbleValue +
                    marbleCircle.removeAt(currentMarblePosition)
        } else {
            currentMarblePosition = ((currentMarblePosition + 1) % marbleCircle.size) + 1
            marbleCircle.add(currentMarblePosition, currentMarbleValue)
        }
    }
    val highScore = scores.values.max()
    println("Highscore: $highScore")
}
