package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseInt(strNum string) int {
	num, err := strconv.ParseInt(strNum, 10, 0)

	if err != nil {
		panic(err)
	}

	return int(num)
}

func isSafe(report []string) bool {

	var isIncreasing bool
	var limit int = 3

	for i := 0; i < len(report)-1; i++ {
		num := parseInt(report[i])
		next := parseInt(report[i+1])

		if i == 0 {
			if next > num {
				isIncreasing = true
			} else if next < num {
				isIncreasing = false
			} else {
				return false
			}

		}

		if isIncreasing && next > num && next-num <= limit {
			continue
		}
		if isIncreasing == false && next < num && num-next <= limit {
			continue
		}

		return false
	}

	return true
}

func main() {
	file, err := os.Open("input.txt")

	if err != nil {
		panic(err)
	}

	defer file.Close()

	var total int = 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		report := strings.Fields(scanner.Text())
		result := isSafe(report)

		if result == true {
			total++
		}
	}

	fmt.Println(total)
}
