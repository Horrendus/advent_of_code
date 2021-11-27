function main() {
    let data = read_file("input/input_day03.txt")
    let parsed_data = parse_input(data)
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
    return input.split('')
}

function puzzle1(input) {
    let currentPosition = [0,0];
    let visitedHouses = new Set();
    visitedHouses.add(String(currentPosition));
    for (const direction of input) {
        switch (direction) {
            case "^": // north
                currentPosition[1] += 1;
                break;
            case "v": // south
                currentPosition[1] -= 1;
                break;
            case ">": // east
                currentPosition[0] += 1;
                break;
            case "<": // west
                currentPosition[0] -= 1;
                break;
            default:
                console.log("Unknown direction: ", direction)
        }
        visitedHouses.add(String(currentPosition));
    }
    console.log("Puzzle1 Unique visited houses: ", visitedHouses.size)
}

function puzzle2(input) {
    let currentPositionSanta = [0,0];
    let currentPositionRoboSanta = [0,0];
    let currentPosition = [0,0];
    let visitedHouses = new Set();
    visitedHouses.add(String(currentPosition));
    for (let i=0;i<input.length;i++) {
        const direction = input[i];
        if (i % 2 === 0) {
            currentPosition = currentPositionSanta;
        } else {
            currentPosition = currentPositionRoboSanta;
        }
        switch (direction) {
            case "^": // north
                currentPosition[1] += 1;
                break;
            case "v": // south
                currentPosition[1] -= 1;
                break;
            case ">": // east
                currentPosition[0] += 1;
                break;
            case "<": // west
                currentPosition[0] -= 1;
                break;
            default:
                console.log("Unknown direction: ", direction)
        }
        visitedHouses.add(String(currentPosition));
        if (i % 2 === 0) {
            currentPositionSanta = currentPosition;
        } else {
            currentPositionRoboSanta = currentPosition;
        }
    }
    console.log("Puzzle2 Unique visited houses: ", visitedHouses.size)
}

if (require.main === module) {
    main()
}
