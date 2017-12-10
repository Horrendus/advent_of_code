fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = readLine() ?: ""
    val lengths = input.split(",").map {
        Integer.parseInt(it.trim())
    }

    val list = listOf(0 until 256).flatten().toMutableList()
    var skip = 0
    var position = 0

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
    println("list[0] * list[1] = ${list[0] * list[1]}")
}
