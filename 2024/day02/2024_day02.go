package main

import (
	"fmt"
	"github.com/samber/lo"
	"os"
	"strconv"
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

func parseReports(data []string) [][]int {
	var reports [][]int
	for _, line := range data {
		if line == "" {
			break
		}
		reportStr := strings.Split(line, " ")
		report := lo.Map(reportStr, func(l string, _ int) int {
			level, err := strconv.Atoi(l)
			check(err)
			return level
		})
		reports = append(reports, report)
	}
	return reports
}

func isReportSafe(report []int) bool {
	return isReportSafeWithSign(report, 1) || isReportSafeWithSign(report, -1)
}

func isReportSafeWithSign(report []int, sign int) bool {
	for i := 0; i < len(report)-1; i++ {
		diff := report[i+1] - report[i]
		if diff*sign < 1 || diff*sign > 3 {
			return false
		}
	}
	return true
}

func puzzle1(reports [][]int) {
	safeReports := 0
	for _, report := range reports {
		if isReportSafe(report) {
			safeReports++
		}
	}
	fmt.Println("Puzzle 1: ", safeReports)
}

func puzzle2(reports [][]int) {
	safeReports := 0
	for _, report := range reports {
		if isReportSafe(report) {
			safeReports++
		} else {
			reportCopy := make([]int, len(report))
			for i, _ := range report {
				_ = copy(reportCopy, report)
				subReport := append(reportCopy[:i], reportCopy[i+1:]...)
				if isReportSafe(subReport) {
					safeReports++
					break
				}
			}
		}
	}
	fmt.Println("Puzzle 2: ", safeReports)
}

func main() {
	data := readFile("input/input_day02.txt")
	parsedData := parseInput(data)
	reports := parseReports(parsedData)
	puzzle1(reports)
	puzzle2(reports)
}
