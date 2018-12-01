typealias Vector3D = Triple<Int, Int, Int>

fun main(args: Array<String>) {
    val input = mutableListOf<String>()
    println("Enter puzzle input")
    while (true) {
        val line = readLine() ?: break
        input.add(line)
    }
    val particles = input.map {
        parseLine(it)
    }
    var particlesWithCollisionDetection = particles.map { it.copy() }
    // the number of rounds needed until the nearest stays the same may be different for other inputs
    (0..400).forEach {
        particles.forEach {
            it.update()
        }
        particlesWithCollisionDetection.forEach {
            it.update()
        }
        val particleGroups = particlesWithCollisionDetection.groupBy { it.position }
        val filteredGroups = particleGroups.filter { it.value.size == 1 }
        particlesWithCollisionDetection = filteredGroups.map { it.value.first() }
    }
    val distances = particles.map {
        it.distance()
    }
    val minimalDistance = distances.min()
    val nearestParticle = distances.indexOf(minimalDistance)
    println("Nearest: $nearestParticle")
    println("Particles after Collision Detection: ${particlesWithCollisionDetection.size}")
}

fun parseLine(line: String): Particle {
    val tokens = line.split(", ")
    val position = tripleStringToTriple(tokens[0])
    val velocity = tripleStringToTriple(tokens[1])
    val acceleration = tripleStringToTriple(tokens[2])
    return Particle(position, velocity, acceleration)
}

fun tripleStringToTriple(tripleString: String): Triple<Int, Int, Int> {
    val vectorString = tripleString.substring(tripleString.indexOf("<") + 1, tripleString.indexOf(">"))
    val vectorValues = vectorString.split(",").map {
        Integer.parseInt(it)
    }
    return Triple(vectorValues[0], vectorValues[1], vectorValues[2])
}

class Particle constructor(var position: Vector3D, private var velocity: Vector3D, private val acceleration: Vector3D) {

    fun update() {
        velocity += acceleration
        position += velocity
    }

    fun distance(): Int {
        return Math.abs(position.first) + Math.abs(position.second) + Math.abs(position.third)
    }

    fun copy(): Particle {
        return Particle(position, velocity, acceleration)
    }

    override fun toString(): String {
        return "Particle(position=$position, velocity=$velocity, acceleration=$acceleration)"
    }


}
