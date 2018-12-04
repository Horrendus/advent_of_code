import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val rawSchedule = input.map { line ->
        parseInputLine(line)
    }
    val sortedSchedule = rawSchedule.sortedBy { it.first }
    val sleepSchedule = mutableMapOf<Int, MutableList<LocalDateTime>>()
    var currentGuard = 0
    var timestampFallenAsleep = LocalDateTime.MIN
    for (scheduleEntry in sortedSchedule) {
        val event = scheduleEntry.second
        when (event) {
            "falls asleep" -> {
                timestampFallenAsleep = scheduleEntry.first
            }
            "wakes up" -> {
                val minutesSlept = scheduleEntry.first.minute - timestampFallenAsleep.minute
                for (i in 0 until minutesSlept) {
                    val sleepTimeStamp = timestampFallenAsleep.plusMinutes(i.toLong())
                    sleepSchedule[currentGuard]?.add(sleepTimeStamp)
                }
            }
            else -> {
                currentGuard = event.split(" ")[1].substring(1).toInt()
                if (!sleepSchedule.containsKey(currentGuard))
                    sleepSchedule[currentGuard] = mutableListOf()
            }
        }
    }
    strategyOne(sleepSchedule)
    println("=========================")
    strategyTwo(sleepSchedule)
}

private fun parseInputLine(line: String): Pair<LocalDateTime, String> {
    val splittedLine = line.substring(1).split("]")
    val dTF = DateTimeFormatter.ofPattern("uuuu-MM-dd HH:mm")
    val date = LocalDateTime.parse(splittedLine[0], dTF)
    return Pair(date, splittedLine[1].trim())
}

private fun strategyOne(sleepSchedule: Map<Int, List<LocalDateTime>>) {
    val sleepiestGuardID = sleepSchedule.maxBy { it.value.size }?.key ?: 0
    val sleepiestGuardSleepSchedule = sleepSchedule[sleepiestGuardID] ?: mutableListOf()
    val minuteMap = mutableMapOf<Int, Int>()
    sleepiestGuardSleepSchedule.forEach { timestamp ->
        minuteMap[timestamp.minute] = minuteMap.getOrDefault(timestamp.minute, 0) + 1
    }
    val sleepiestGuardSleepiestMinute = minuteMap.maxBy { it.value }?.key ?: 0
    println("Strategy 1")
    println("Sleepiest Guard ID: $sleepiestGuardID")
    println("Sleepiest Minute: $sleepiestGuardSleepiestMinute")
    println("Sleepiest Guard ID x Sleepiest Minute: ${sleepiestGuardID * sleepiestGuardSleepiestMinute}")
}

private fun strategyTwo(sleepSchedule: Map<Int, List<LocalDateTime>>) {
    val minuteMap = mutableMapOf<Pair<Int, Int>, Int>()
    sleepSchedule.forEach {
        val guardID = it.key
        it.value.forEach { timestamp ->
            val key = Pair(guardID, timestamp.minute)
            minuteMap[key] = minuteMap.getOrDefault(key, 0) + 1
        }
    }
    val sleepiestGuardSleepiestMinutePair = minuteMap.maxBy { it.value }?.key ?: Pair(0, 0)
    val sleepiestGuardID = sleepiestGuardSleepiestMinutePair.first
    val sleepiestGuardSleepiestMinute = sleepiestGuardSleepiestMinutePair.second
    println("Strategy 2")
    println("Sleepiest Guard ID: $sleepiestGuardID")
    println("Sleepiest Minute: $sleepiestGuardSleepiestMinute")
    println("Sleepiest Guard ID x Sleepiest Minute: ${sleepiestGuardID * sleepiestGuardSleepiestMinute}")
}
