// This needs day10_puzzle2.kt for the implementation of dense hash
fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = readLine()
    var used = 0
    (0..127).forEach {
        val hashInput = input + "-" + it
        val hexHash = calculateDenseHash(hashInput)
        val binHash = hexHash.map {
            Integer.toBinaryString(Integer.parseInt(it.toString(), 16))
        }.joinToString("")
        val usedInRow = binHash.count {
            it == '1'
        }
        used += usedInRow
    }
    println("Total Used: $used")
}
