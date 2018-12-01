import kotlin.math.sqrt
import kotlin.system.exitProcess

typealias Pattern = Array<Array<Char>>

var artwork = arrayOf(arrayOf('.','#','.'), arrayOf('.','.','#'), arrayOf('#','#','#'))

val enhancementRules = hashMapOf<String,Pattern>()

fun main(args: Array<String>) {
    val input = mutableListOf<String>()
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    input.forEach {
        parseRule(it)
    }
    val enhancementIterations = 5
    (0 until enhancementIterations).forEach {
        val artworkSquares = splitArtwork()
        val newArtworkSquares = artworkSquares.map { enhancePattern(it) }
        artwork = mergePatterns(newArtworkSquares)
        println(artwork.contentDeepToString())
    }
    val pixelsOn = countHash()
    println("Number of Pixels ON: $pixelsOn")
}

fun parseRule(line: String) {
    val ruleAndEnhancement = line.split("=>")
    val rule = ruleAndEnhancement[0].trim()
    val enhancementLines = ruleAndEnhancement[1].trim().split("/")
    val enhancementArrays = enhancementLines.map { it.toCharArray().toTypedArray() }.toTypedArray()
    enhancementRules[rule] = enhancementArrays
}

fun splitArtwork() : List<Pattern> {
    var patterns = mutableListOf<Pattern>()
    if (artwork.size % 2 == 0) {
        // split in 2x2 patterns
        (0 until (artwork.size - 1) step 2).forEach {
            lineNumber ->
            val artworkLine1 = artwork[lineNumber]
            val artworkLine2 = artwork[lineNumber+1]
            (0 until (artworkLine1.size - 1) step 2).forEach {
                columnNumber ->
                val pattern = arrayOf( arrayOf(artworkLine1[columnNumber], artworkLine1[columnNumber+1]),
                                       arrayOf(artworkLine2[columnNumber], artworkLine2[columnNumber+1]))
                patterns.add(pattern)
            }
        }
    } else {
        // split in 3x3 patterns
        (0 until (artwork.size - 2) step 3).forEach {
            line ->
            val artworkLine1 = artwork[line]
            val artworkLine2 = artwork[line+1]
            val artworkLine3 = artwork[line+2]
            (0 until (artworkLine1.size - 2) step 3).forEach {
                column ->
                val pattern = arrayOf(
                        arrayOf(artworkLine1[column], artworkLine1[column+1], artworkLine1[column+2]),
                        arrayOf(artworkLine2[column], artworkLine2[column+1], artworkLine2[column+2]),
                        arrayOf(artworkLine3[column], artworkLine3[column+1], artworkLine3[column+2]))
                patterns.add(pattern)
            }
        }
    }
    return patterns
}

fun enhancePattern(pattern: Pattern) : Pattern {
    var currentPattern = pattern.clone()
    (0..3).forEach {
        var patternStr = patternToRulesKey(currentPattern)
        if (enhancementRules.containsKey(patternStr)) {
            // println("found rule matching $patternStr")
            return enhancementRules[patternStr] as Pattern
        }
        // println("no rule found matching $patternStr")
        // println("flipping horizontally")
        patternStr = patternToRulesKey(flipPatternHorizontal(currentPattern))
        if (enhancementRules.containsKey(patternStr)) {
            // println("found rule matching $patternStr")
            return enhancementRules[patternStr] as Pattern
        }
        // println("no rule found matching $patternStr")
        // println("flipping vertically")
        patternStr = patternToRulesKey(flipPatternVertical(currentPattern))
        if (enhancementRules.containsKey(patternStr)) {
            // println("found rule matching $patternStr")
            return enhancementRules[patternStr] as Pattern
        }
        // println("no rule found matching $patternStr")
        // println("rotating")
        currentPattern = rotate(currentPattern)
    }
    println("no enhancement rule found for pattern: ${pattern.contentDeepToString()}")
    exitProcess(1)
}

fun patternToRulesKey(pattern: Pattern) : String {
    return pattern.joinToString("/") {
        patternLine ->
        patternLine.joinToString("")
    }
}

fun mergePatterns(artworkSquares: List<Pattern>) : Pattern {
    val squaresPerLine = sqrt(artworkSquares.size.toDouble()).toInt()
    val squareSize = artworkSquares[0].size
    val artworkSize = squaresPerLine*squareSize
    val newPattern = Array(artworkSize) { Array(artworkSize) { '*' }}
    (0 until artworkSize).forEach {
        line ->
        (0 until artworkSize).forEach {
            column ->
            val squareIdxLineBegin = (line / squaresPerLine) * squaresPerLine
            val squareIdx = minOf(squareIdxLineBegin + (column / squareSize),artworkSquares.size-1)
            val lineInSquare = line % squareSize
            val columnInSquare = column % squareSize
            val square = artworkSquares[squareIdx]
            newPattern[line, column] = square[lineInSquare, columnInSquare]
        }
    }
    return newPattern
}

// rotate by 90° to the right
fun rotate(pattern: Pattern) : Pattern {
    return if (pattern.size == 2) {
        // 2 x 2 Pattern
        arrayOf(arrayOf(pattern[1,0], pattern[0,0]),
                arrayOf(pattern[1,1], pattern[0,1]))
    } else {
        // 3 x 3 Pattern
        arrayOf(arrayOf(pattern[2,0], pattern[1,0], pattern[0,0]),
                arrayOf(pattern[2,1], pattern[1,1], pattern[0,1]),
                arrayOf(pattern[2,2], pattern[1,2], pattern[0,2]))
    }
}

fun flipPatternHorizontal(pattern: Pattern) : Pattern {
    return if (pattern.size == 2) {
        // 2 x 2 Pattern
        arrayOf(arrayOf(pattern[1,0], pattern[1,1]),
                arrayOf(pattern[0,0], pattern[0,1]))
    } else {
        // 3 x 3 Pattern
        arrayOf(arrayOf(pattern[2,0], pattern[2,1], pattern[2,2]),
                arrayOf(pattern[1,0], pattern[1,1], pattern[1,2]),
                arrayOf(pattern[0,0], pattern[1,2], pattern[0,2]))
    }
}

fun flipPatternVertical(pattern: Pattern) : Pattern {
    return if (pattern.size == 2) {
        // 2 x 2 Pattern
        arrayOf(arrayOf(pattern[0,1], pattern[0,0]),
                arrayOf(pattern[1,1], pattern[1,0]))
    } else {
        // 3 x 3 Pattern
        arrayOf(arrayOf(pattern[0,2], pattern[0,1], pattern[0,0]),
                arrayOf(pattern[1,2], pattern[1,1], pattern[1,0]),
                arrayOf(pattern[2,2], pattern[2,1], pattern[2,0]))
    }
}

fun countHash() : Int {
    var count = 0
    artwork.forEach {
        line ->
        count += line.count {
            it == '#'
        }
    }
    return count
}

private operator fun Pattern.get(row: Int, column: Int) : Char {
    return this[row][column]
}

private operator fun Pattern.set(row: Int, column: Int, value: Char) {
    this[row][column] = value
}
