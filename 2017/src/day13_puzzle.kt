val firewallLayers = hashMapOf<Int, Int>()

fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    input.forEach {
        val layerAndRange = it.split(":")
        val layer = Integer.parseInt(layerAndRange[0].trim())
        val range = Integer.parseInt(layerAndRange[1].trim())
        firewallLayers[layer] = range
    }
    val lastLayer = firewallLayers.keys.max() ?: 0
    var delay = 0
    while (true) {
        var caught = false
        val severities = mutableListOf<Int>()
        (0..lastLayer).forEach { layer ->
            val layerRange = firewallLayers[layer]
            layerRange?.let {
                val layerSeverityAndCaughtInfo = calculateSeverity(layer, layerRange, delay)
                severities.add(layerSeverityAndCaughtInfo.second)
                if (!caught && layerSeverityAndCaughtInfo.first) {
                    caught = true
                }
            }
        }

        val totalSeverity = severities.sum()
        if (delay == 0) println("Severity for Delay 0: $totalSeverity")
        if (totalSeverity == 0 && !caught) break
        delay++
    }
    println("Delay: $delay")
}

fun calculateSeverity(layer: Int, layerRange: Int, delay: Int): Pair<Boolean, Int> {
    val totalStates = layerRange + maxOf(layerRange - 2, 0)
    val currentRelativePosition = (layer + delay) % totalStates
    val currentPosition = if (currentRelativePosition >= layerRange) {
        (layerRange - 1) - (currentRelativePosition - (layerRange - 1))
    } else {
        currentRelativePosition
    }
    val caught = currentPosition == 0
    val severity = if (caught) layer * layerRange else 0
    return Pair(caught, severity)
}
