import org.junit.jupiter.api.Assertions

internal class Day21PuzzleTest {

    @org.junit.jupiter.api.Test
    fun testRotateSize3() {
        val size3Pattern = arrayOf(arrayOf('.', '#', '.'), arrayOf('.', '.', '#'), arrayOf('#', '#', '#'))
        val expectedRotatedPattern = arrayOf(arrayOf('#', '.', '.'), arrayOf('#', '.', '#'), arrayOf('#', '#', '.'))
        val rotatedPattern = rotate(size3Pattern)
        Assertions.assertTrue(expectedRotatedPattern contentDeepEquals rotatedPattern)
    }

    @org.junit.jupiter.api.Test
    fun testRotateSize3FourTimes() {
        val size3Pattern = arrayOf(arrayOf('.', '#', '.'), arrayOf('.', '.', '#'), arrayOf('#', '#', '#'))
        var rotatedPattern = rotate(size3Pattern)
        rotatedPattern = rotate(rotatedPattern)
        rotatedPattern = rotate(rotatedPattern)
        rotatedPattern = rotate(rotatedPattern)
        Assertions.assertTrue(size3Pattern contentDeepEquals rotatedPattern)
    }

    @org.junit.jupiter.api.Test
    fun testRotateSize2() {
        val size2Pattern = arrayOf(arrayOf('.', '.'), arrayOf('.', '#'))
        val expectedRotatedPattern = arrayOf(arrayOf('.', '.'), arrayOf('#', '.'))
        val rotatedPattern = rotate(size2Pattern)
        Assertions.assertTrue(expectedRotatedPattern contentDeepEquals rotatedPattern)
    }

    @org.junit.jupiter.api.Test
    fun testParseRule() {
        val rule = "#.#/.#./... => ####/.#../..#./.###"
        val key = "#.#/.#./..."
        val value = arrayOf(
                arrayOf('#', '#', '#', '#'),
                arrayOf('.', '#', '.', '.'),
                arrayOf('.', '.', '#', '.'),
                arrayOf('.', '#', '#', '#'))
        Assertions.assertTrue(enhancementRules[key] == null)
        parseRule(rule)
        val realValue = enhancementRules[key]
        println(value.contentDeepToString())
        println(realValue?.contentDeepToString())
        Assertions.assertTrue(realValue?.contentDeepEquals(value) ?: false)
    }

    @org.junit.jupiter.api.Test
    fun testSplitArtworkSize2() {
        artwork = arrayOf(
                arrayOf('#', '.', '.', '#'),
                arrayOf('.', '.', '.', '.'),

                arrayOf('.', '.', '.', '.'),
                arrayOf('#', '.', '.', '#'))
        val expectedPatterns = listOf(
                arrayOf(arrayOf('#', '.'),
                        arrayOf('.', '.')),
                arrayOf(arrayOf('.', '#'),
                        arrayOf('.', '.')),
                arrayOf(arrayOf('.', '.'),
                        arrayOf('#', '.')),
                arrayOf(arrayOf('.', '.'),
                        arrayOf('.', '#')))
        val patterns = splitArtwork()
        Assertions.assertTrue(patterns.toTypedArray() contentDeepEquals expectedPatterns.toTypedArray())
        // reset artwork
        artwork = arrayOf(arrayOf('.', '#', '.'), arrayOf('.', '.', '#'), arrayOf('#', '#', '#'))
    }

    @org.junit.jupiter.api.Test
    fun testSplitArtworkSize3() {
        artwork = arrayOf(
                arrayOf('#', '#', '.', '#', '#', '.', '#', '#', '.'),
                arrayOf('#', '.', '.', '#', '.', '.', '#', '#', '.'),
                arrayOf('.', '.', '.', '.', '.', '.', '#', '#', '.'),

                arrayOf('#', '#', '.', '#', '#', '.', '#', '#', '.'),
                arrayOf('#', '.', '#', '#', '.', '.', '#', '#', '.'),
                arrayOf('.', '#', '.', '.', '#', '.', '#', '#', '.'),

                arrayOf('#', '#', '.', '#', '#', '.', '#', '#', '.'),
                arrayOf('#', '.', '#', '#', '.', '.', '#', '#', '.'),
                arrayOf('.', '.', '.', '.', '#', '.', '#', '#', '.'))
        val expectedPatterns = listOf(
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '.', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '.', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.')),

                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '#'),
                        arrayOf('.', '#', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '#', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.')),

                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '#'),
                        arrayOf('.', '.', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '#', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.')))

        val patterns = splitArtwork()
        Assertions.assertTrue(patterns.toTypedArray() contentDeepEquals expectedPatterns.toTypedArray())
        // reset artwork
        artwork = arrayOf(arrayOf('.', '#', '.'), arrayOf('.', '.', '#'), arrayOf('#', '#', '#'))
    }

    @org.junit.jupiter.api.Test
    fun testMerge() {
        val patterns = listOf(
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '.', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '.', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.')),

                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '#'),
                        arrayOf('.', '#', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '#', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.')),

                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '#'),
                        arrayOf('.', '.', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '.', '.'),
                        arrayOf('.', '#', '.')),
                arrayOf(arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.'),
                        arrayOf('#', '#', '.')))
        val expectedArtwork = arrayOf(
                arrayOf('#', '#', '.', '#', '#', '.', '#', '#', '.'),
                arrayOf('#', '.', '.', '#', '.', '.', '#', '#', '.'),
                arrayOf('.', '.', '.', '.', '.', '.', '#', '#', '.'),

                arrayOf('#', '#', '.', '#', '#', '.', '#', '#', '.'),
                arrayOf('#', '.', '#', '#', '.', '.', '#', '#', '.'),
                arrayOf('.', '#', '.', '.', '#', '.', '#', '#', '.'),

                arrayOf('#', '#', '.', '#', '#', '.', '#', '#', '.'),
                arrayOf('#', '.', '#', '#', '.', '.', '#', '#', '.'),
                arrayOf('.', '.', '.', '.', '#', '.', '#', '#', '.'))
        val mergedArtwork = mergePatterns(patterns)
        Assertions.assertTrue(mergedArtwork contentDeepEquals expectedArtwork)
    }

    @org.junit.jupiter.api.Test
    fun testEnhance() {
        val pattern = arrayOf(
                arrayOf('.', '.'),
                arrayOf('#', '.'))
        parseRule("../.# => ##./#../...")
        enhancePattern(pattern)
        // reset enhancementRules
        enhancementRules.clear()
    }
}

