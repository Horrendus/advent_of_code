fun main(args: Array<String>) {
    val gridSerialNumber = 7315
    var maximumFuelLevel = Int.MIN_VALUE
    var topLeftOfMaximum = Pair(0,0)
    for (x in 1..(300-2)) {
        for (y in 1..(300-2)) {
            var fuel = 0
            for (dx in 0..2) {
                for (dy in 0..2) {
                    val rackId = x+dx+10
                    fuel += ((((rackId * (y+dy) + gridSerialNumber) * rackId) / 100) % 10) - 5
                }
            }
            if (fuel > maximumFuelLevel) {
                maximumFuelLevel = fuel
                topLeftOfMaximum = Pair(x,y)
            }
        }
    }
    println(topLeftOfMaximum)
}
