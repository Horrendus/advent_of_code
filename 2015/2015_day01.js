function main() {
    let data = read_file("input/input_day01.txt")
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
    let level = 0
    for (let char of input) {
        if (char == '(') {
            level++
        } else if (char == ')') {
            level--
        } else {
            console.log("Unknown input: ", char)
        }
    }
    console.log(level)
}

function puzzle2(input) {
    let level = 0
    let pos = 0
    for (; pos < input.length; pos++) {
        const char = input[pos]
        if (char == '(') {
            level++
        } else if (char == ')') {
            level--
        } else {
            console.log("Unknown input: ", char)
        }
        if (level == -1) {
            break
        }
    }
    pos++ // position should start at one
    console.log(pos)
}

if (require.main === module) {
    main()
}
