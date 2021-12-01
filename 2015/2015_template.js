function main() {
    let data = read_file("input/input_day00.txt")
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
    return input
}

function puzzle1(input) {
    console.log("puzzle1")
}

function puzzle2(input) {
    console.log("puzzle2")
}

if (require.main === module) {
    main()
}
