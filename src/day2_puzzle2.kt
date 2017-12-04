fun main(args: Array<String>) {
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
        // TODO: remove !! using null check before :)
        row ->
            for (i in 0 until row.size)
                for (j in i+1 until row.size) {
                    if (row[i] % row[j] == 0) {
                        checksum += row[i] / row[j]
                        break
                    }
                    if (row[j] % row[i] == 0) {
                        checksum += row[j] / row[i]
                        break
                    }
                }
    }
    print("Checksum: $checksum")
}
