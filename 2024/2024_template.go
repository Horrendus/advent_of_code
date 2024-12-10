package main

import (
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func parseInput(data string) []string {
	return strings.Split(data, "\n")
}

func readFile(filename string) string {
	data, err := os.ReadFile(filename)
	check(err)
	return string(data)
}

func puzzle1(data []string) {

}

func puzzle2(data []string) {

}

func main() {
	data := readFile("input/input_day00.txt")
	parsedData := parseInput(data)
	puzzle1(parsedData)
	puzzle2(parsedData)
}
