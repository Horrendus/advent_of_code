private var currentListPosition = 0

fun main(args: Array<String>) {
    println("Enter puzzle input")
    val input = readLine() ?: return
    val splittedLine = input.split(" ")
    val rawRootNodeData = splittedLine.map {
        it.toInt()
    }
    val rootNode = createNodes(rawRootNodeData)
    val metaDataSum = calculateMetaDataSum(rootNode)
    println("Part 1")
    println(metaDataSum)
    val metaDataReferenceSum = calculateMetaDataReferenceSum(rootNode)
    println("Part 2")
    println(metaDataReferenceSum)
}

private fun createNodes(rawNodeData: List<Int>) : Node18 {
    val childNodeCount = rawNodeData[currentListPosition]
    val metaDataCount = rawNodeData[currentListPosition+1]
    currentListPosition += 2
    val childNodes = mutableListOf<Node18>()
    while (childNodes.size < childNodeCount) {
        val childNode = createNodes(rawNodeData)
        childNodes.add(childNode)
    }
    val metadata = rawNodeData.subList(currentListPosition, currentListPosition + metaDataCount)
    currentListPosition += metaDataCount
    return Node18(childNodes, metadata)
}

private fun calculateMetaDataSum(node: Node18) : Int {
    return node.metadata.sum() + node.childNodes.map { calculateMetaDataSum(it) }.sum()
}

private fun calculateMetaDataReferenceSum(node: Node18): Int {
    if (!node.childNodes.isEmpty()) {
        var sum = 0
        for (position in node.metadata) {
            val childNode = node.childNodes.getOrNull(position-1)
            childNode?.let { sum += calculateMetaDataReferenceSum(childNode) }
        }
        return sum
    }
    return node.metadata.sum()
}

private data class Node18(val childNodes: List<Node18>, val metadata: List<Int>)