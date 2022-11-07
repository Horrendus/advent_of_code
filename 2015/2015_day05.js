function main() {
    let data = read_file("input/input_day05.txt")
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
    return input.split("\n")
}

function three_vowels(input) {
    const vowels = "aeiou";
    let count = 0;
    for (const vowel of vowels) {
        const re = new RegExp(vowel, "g");
        const count_v = (input.match(re) || []).length;
        count += count_v;
        if (count >= 3) {
            return true;
        }
    }
    return false;
}

function double_letters(input) {
    let previous = input[0];
    for (let i=1;i<input.length;i++) {
        if (input[i] === previous) {
            return true;
        }
        previous = input[i];
    }
    return false;
}

function no_bad_strings(input) {
    const bad1 = "ab";
    const bad2 = "cd";
    const bad3 = "pq";
    const bad4 = "xy";
    return !(input.includes(bad1) || input.includes(bad2) || input.includes(bad3) || input.includes(bad4));
}

function good_string(input) {
    return no_bad_strings(input) && double_letters(input) && three_vowels(input);
}

function letter_pair_twice(input) {
    for (let i=0;i<input.length-3;i++) {
        let pair = input[i] + input[i+1];
        if (input.indexOf(pair,i+2) !== -1) {
            return true;
        }
    }
    return false;
}

function letter_repeats(input) {
    let previous = input[0];
    for (let i=2;i<input.length;i++) {
        if (input[i] === previous) {
            return true;
        }
        previous = input[i-1];
    }
    return false;
}

function better_string(input) {
    return letter_pair_twice(input) && letter_repeats(input);
}

function puzzle1(input) {
    const check_all = input.map(x => good_string(x));
    const good_strings = check_all.filter(y => y === true).length;
    console.log("Puzzle 1: ", good_strings);
}

function puzzle2(input) {
    const check_all = input.map(x => better_string(x));
    const better_strings = check_all.filter(y => y === true).length;
    console.log("Puzzle 2: ", better_strings);
}

if (require.main === module) {
    main()
}
