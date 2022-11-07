function main() {
    let data = read_file("input/input_day06.txt")
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

function parse_coordinate(coordinate) {
    const [x,y] = coordinate.split(",");
    return [parseInt(x),parseInt(y)];
}

function parse_line(line) {
    let tokens = line.split(" ");
    return [tokens[tokens.length-4],parse_coordinate(tokens[tokens.length-3]), parse_coordinate(tokens[tokens.length-1])];
}

function parse_input(input) {
    const lines = input.trim().split("\n");
    return lines.map(line => parse_line(line));
}

function sumRecursiveArray(arr) {
    return arr.reduce(function(acc, value) {
        return acc + (Array.isArray(value) ? sumRecursiveArray(value) : value);
    }, 0);
}

function puzzle1(input) {
    let lights = Array(1000).fill().map(()=>Array(1000).fill(0));
    for (const instruction of  input) {
        const command = instruction[0];
        const [x_start, y_start] = instruction[1];
        const [x_end, y_end] = instruction[2];
        for (let x = x_start; x <= x_end; x++) {
            for (let y = y_start; y <= y_end; y++) {
                switch (command) {
                    case "on":
                        lights[x][y] = 1;
                        break;
                    case "off":
                        lights[x][y] = 0;
                        break;
                    case "toggle":
                        lights[x][y] = lights[x][y] ^ 1;
                        break;
                }
            }
        }
    }
    const sum = sumRecursiveArray(lights);
    console.log("Puzzle 1: ", sum);
}

function puzzle2(input) {
    let lights = Array(1000).fill().map(()=>Array(1000).fill(0));
    for (const instruction of  input) {
        const command = instruction[0];
        const [x_start, y_start] = instruction[1];
        const [x_end, y_end] = instruction[2];
        for (let x = x_start; x <= x_end; x++) {
            for (let y = y_start; y <= y_end; y++) {
                switch (command) {
                    case "on":
                        lights[x][y] += 1;
                        break;
                    case "off":
                        lights[x][y] = Math.max(0, lights[x][y]-1);
                        break;
                    case "toggle":
                        lights[x][y] +=  2;
                        break;
                }
            }
        }
    }
    const sum = sumRecursiveArray(lights);
    console.log("Puzzle 2: ", sum);
}

if (require.main === module) {
    main()
}
