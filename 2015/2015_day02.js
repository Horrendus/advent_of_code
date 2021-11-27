class Cuboid {
    constructor(dimensions) {
        const arr = dimensions.split('x')
        this.length = parseInt(arr[0], 10);
        this.width = parseInt(arr[1], 10);
        this.height = parseInt(arr[2], 10);
    }

    get area() {
        const side1 = this.length * this.width;
        const side2 = this.width * this.height;
        const side3 = this.height * this.length;
        const smallest_side = Math.min(side1, side2, side3)
        return 2*side1 + 2*side2 + 2*side3 + smallest_side;
    }

    get volume() {
        return this.length * this.width * this.height;
    }

    get smallestPerimeter() {
        let sides = [this.length, this.height, this.width]
        sides.sort(function(a, b){return a-b})
        return 2 * sides[0] + 2 * sides[1]
    }

}

function main() {
    let data = read_file("input/input_day02.txt")
    const parsed_data = parse_input(data)
    puzzle1(parsed_data)
    puzzle2(parsed_data)
}

function read_file(filename) {
    const fs = require('fs')

    try {
        return fs.readFileSync(filename, 'utf8')
    } catch (err) {
        console.log("Error reading file")
        process.exit(1)
    }
}

function parse_input(input) {
    const lines = input.split("\n");
    const cuboids = lines.map(sides => new Cuboid(sides))
    return cuboids
}

function puzzle1(input) {
    const totalArea = input.reduce((acc, cube) => acc + cube.area, 0);
    console.log("Puzzle1 Total Area: ", totalArea)
}

function puzzle2(input) {
    const totalRibbon = input.reduce((acc, cuboid) => acc + (cuboid.smallestPerimeter + cuboid.volume), 0);
    let testRibbon = 0
    for (let i=0; i<5; i++) {
        let ribbon = input[i].smallestPerimeter + input[i].volume
        console.log(input[i], input[i].smallestPerimeter, input[i].volume)
        testRibbon += ribbon
    }
    console.log("TestRibbon", testRibbon)
    console.log("Puzzle2 Total Ribbon: ", totalRibbon)
}

if (require.main === module) {
    main()
}
