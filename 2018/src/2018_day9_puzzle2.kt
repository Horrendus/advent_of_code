private const val numberOfPlayers = 465
private const val lastMarbleValue = 71498 * 100

fun main(args: Array<String>) {
    var currentNode = ListNode(0, null, null)
    currentNode.next = currentNode
    currentNode.previous = currentNode
    var currentPlayer = 0
    var currentMarbleValue = 0
    var scores = mutableMapOf<Int, Long>()
    while (currentMarbleValue < lastMarbleValue) {
        currentPlayer = (currentPlayer % numberOfPlayers) + 1
        currentMarbleValue++
        if (currentMarbleValue % 23 == 0) {
            for (i in 1..7) {
                currentNode = currentNode.previous ?: currentNode
            }
            scores[currentPlayer] = (scores[currentPlayer] ?: 0) + (currentMarbleValue + currentNode.value)
            currentNode = currentNode.remove()
        } else {
            currentNode = currentNode.next?.add(currentMarbleValue) ?: currentNode
        }
    }
    val highScore = scores.values.max()
    println("Highscore: $highScore")
}

data class ListNode(val value: Int, var previous: ListNode?, var next: ListNode?) {

    // adds a new Node after this node
    fun add(value: Int) : ListNode {
        val newNode = ListNode(value, null, null)
        newNode.next = this.next
        newNode.previous = this
        this.next?.previous = newNode
        this.next = newNode
        return newNode
    }

    fun remove() : ListNode {
        this.previous?.next = this.next
        this.next?.previous = this.previous
        return this.next ?: this
    }

    fun printList(size: Int) {
        var currentNode = this
        for (i in 0..size) {
            print("${currentNode.value} ")
            currentNode = currentNode.next ?: break
        }
        println()
    }

}