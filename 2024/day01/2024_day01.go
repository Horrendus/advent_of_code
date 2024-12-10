package main

import (
	"fmt"
	"github.com/samber/lo"
	"os"
	"sort"
	"strconv"
	"strings"
)

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

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

func parseDistances(data []string) ([]int, []int) {
	var distances1 []int
	var distances2 []int
	for _, line := range data {
		if line == "" {
			break
		}
		distance1, err := strconv.Atoi(strings.Split(line, "   ")[0])
		check(err)
		distance2, err := strconv.Atoi(strings.Split(line, "   ")[1])
		check(err)
		distances1 = append(distances1, distance1)
		distances2 = append(distances2, distance2)
	}
	sort.Ints(distances1)
	sort.Ints(distances2)
	return distances1, distances2
}

func puzzle1(distances1 []int, distances2 []int) {
	distance := 0
	for i := range len(distances1) {
		distance += Abs(distances1[i] - distances2[i])
	}
	fmt.Println("Puzzle 1: ", distance)
}

func puzzle2(distances1 []int, distances2 []int) {
	similarilityScore := 0
	for i := range distances1 {
		count := lo.Count(distances2, distances1[i])
		similarilityScore += count * distances1[i]
	}
	fmt.Println("Puzzle 2: ", similarilityScore)

}

func main() {
	data := readFile("input/input_day01.txt")
	parsedData := parseInput(data)
	distances1, distances2 := parseDistances(parsedData)
	puzzle1(distances1, distances2)
	puzzle2(distances1, distances2)
}
