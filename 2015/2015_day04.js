function main() {
    let data = read_file("input/input_day04.txt")
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
    return input.trim()
}

function puzzle1(input) {
    console.log("P1: ", input)
}

function puzzle2(input) {
    console.log("Puzzle 2")
}

if (require.main === module) {
    main()
}
