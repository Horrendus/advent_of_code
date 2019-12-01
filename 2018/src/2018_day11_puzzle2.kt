fun main(args: Array<String>) {
    val gridSerialNumber = 7315
    var maximumFuelLevel = Int.MIN_VALUE
    var topLeftOfMaximum = Triple(0, 0, 0)
    val grid = Array(300) { x ->
        Array(300) { y ->
            (((((x + 1 + 10) * (y + 1) + gridSerialNumber) * (x + 1 + 10))
                    / 100) % 10) - 5
        }
    }
    for (size in 1..300) {
        for (x in 0..(300-size)/* step size*/) {
            for (y in 0..(300-size)/* step size*/) {
                var fuel = 0
                for (dx in 0 until size) {
                    for (dy in 0 until size) {
                        fuel += grid[x + dx][y + dy]
                    }
                }
                if (fuel > maximumFuelLevel) {
                    maximumFuelLevel = fuel
                    topLeftOfMaximum = Triple(x+1,y+1,size)
                }
            }
        }
    }
    println(topLeftOfMaximum)
}
