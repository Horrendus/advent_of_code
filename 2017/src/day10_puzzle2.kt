fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = readLine() ?: ""
    val hash = calculateDenseHash(input)
    println("$hash")
}

private fun calculateDenseHash(input: String): String {
    val lengthsSuffix = listOf(17, 31, 73, 47, 23)
    val lengths = input.trim().map { it.toInt() } + lengthsSuffix

    val list = listOf(0 until 256).flatten().toMutableList()

    var skip = 0
    var position = 0

    (1..64).forEach {
        lengths.forEach { length ->
            val end = position + length
            val wrappedEnd1 = if (end >= list.size) end % list.size else 0
            val wrappedEnd2 = minOf(end, list.size)
            val subList1 = list.slice(0 until wrappedEnd1)
            val subList2 = list.slice(position until wrappedEnd2)

            val reversedList = (subList2 + subList1).reversed()
            for (i in 0 until reversedList.size) {
                val listPos = (i + position) % list.size
                list[listPos] = reversedList[i]
            }
            position += length + skip
            position %= list.size
            skip++
        }
    }
    val denseHash = mutableListOf<Int>()
    for (i in 0 until list.size step 16) {
        var hash = 0
        val listSlice = list.slice(i until i + 16)
        listSlice.forEach {
            hash = hash xor it
        }
        denseHash.add(hash)
    }
    val denseHashHex = denseHash.map {
        String.format("%02x", it)
    }
    return denseHashHex.joinToString("")
}
