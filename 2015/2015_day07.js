function main() {
    let data = read_file("input/input_day07.txt")
    let parsed_data = parse_input(data)
    const answer_puzzle1 = puzzle1(parsed_data)
    puzzle2(parsed_data, answer_puzzle1)
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

function parse_line(line) {
    const pos_arrow = line.search("->");
    const output = line.substring(pos_arrow+3);
    const command = line.substring(0, pos_arrow-1).split(" ");
    if (command.length === 3) { // AND, OR, LSHIFT, RSHIFT
        return [command[0], command[1], command[2], output];
    } else if (command.length === 2) { // NOT
        return ["", command[0], command[1], output];
    } else { // direct provision
        return ["", "PROVIDE", command[0], output];
    }
}

function parse_input(input) {
    const lines = input.trim().split("\n");
    return lines.map(line => parse_line(line));
}

function get_operand(wire_values, operand) {
    const num = Number(operand)
    if (num >= 0) {
        return Number(operand);
    } else if (operand === "") {
        return "EMPTY";
    } else {
        return wire_values[operand];
    }
}

function run_instructions(commands) {
    const wire_values = {};
    const stop_wire =  "a";
    while (true) {
        let new_commands = [];
        let count_run_commands = 0;
        for (const current_command of commands) {
            // console.log("Trying ", current_command[0], current_command[1], current_command[2], "->", current_command[3]);
            const operand1 = get_operand(wire_values, current_command[0]);
            const operand2 = get_operand(wire_values, current_command[2]);
            const operator = current_command[1];
            const output = current_command[3];
            let result = 0;
            if (operand1 !== undefined  && operand2 !== undefined) {
                // console.log("Performing ", operand1, operator, operand2, "->", output);
                switch (operator) {
                    case "PROVIDE":
                        result = operand2;
                        break;
                    case "NOT":
                        result = ~operand2;
                        break;
                    case "AND":
                        result = operand1 & operand2;
                        break;
                    case "OR":
                        result = operand1 | operand2;
                        break;
                    case "LSHIFT":
                        result = operand1 << operand2;
                        break;
                    case "RSHIFT":
                        result = operand1 >> operand2;
                        break;
                }
                wire_values[output] = result;
                count_run_commands += 1;
                if (output === stop_wire) {
                    return wire_values[stop_wire];
                }
            } else {
                // console.log("Not Perform ", operand1, operator, operand2, "->", output);
                new_commands.push(current_command);
            }
        }
        commands = new_commands;
        if (count_run_commands === 0) {
            console.log("No more commands can be run");
            console.log(JSON.stringify(new_commands));
            console.log(JSON.stringify(wire_values));
            return NaN;
        }
    }
}

function puzzle1(input) {
    const answer = run_instructions(input);
    console.log("Puzzle 1: ", answer);
    return answer;
}

function puzzle2(input, answer_puzzle1) {
    input[3] = ["", "PROVIDE", answer_puzzle1, "b"];
    const answer = run_instructions(input);
    console.log("Puzzle 2: ", answer);
}

if (require.main === module) {
    main()
}
