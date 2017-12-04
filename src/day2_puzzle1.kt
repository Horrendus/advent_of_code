fun main(args: Array<String>) {
    // val table = mutableListOf<List<Int>>()
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val splittedLines = input.map {
        line -> line.split("\t"," ")
    }
    val table = splittedLines.map { line ->
        line.map {
            s -> Integer.parseInt(s)
        }
    }
    var checksum = 0
    table.forEach {
        row -> val diff = row.max()!! - row.min()!!; checksum += diff
    }
    print("Checksum: $checksum")
}
