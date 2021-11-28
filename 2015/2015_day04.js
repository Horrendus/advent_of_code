const md5 = require('md5');

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

function md5prefix(input, prefix) {
    let i = 0;
    while (true) {
        i++;
        const s = String(input + i)
        const hash = md5(s);
        if (hash.startsWith(prefix)) {
            break;
        }
    }
    return i;
}

function puzzle1(input) {
    const num = md5prefix(input, "00000");
    console.log("Puzzle 1: ", num);
}

function puzzle2(input) {
    const num = md5prefix(input, "000000");
    console.log("Puzzle 2: ", num);
}

if (require.main === module) {
    main()
}
