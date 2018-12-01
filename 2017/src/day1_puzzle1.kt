fun main(args: Array<String>) {
    print("Enter puzzle input: ")
    val input = readLine()
    println("Input: $input")
    if (input != null) {
        var sum = 0
        for (i in 0 until input.length) {
            val next = (i + 1) % input.length
            if (input[i] == input[next]) {
                sum += Integer.parseInt(input[i].toString())
            }
        }
        println("Captcha: $sum")
    }
}
