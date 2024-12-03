package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseStr(str string) int64 {

	num, err := strconv.ParseInt(str, 10, 64)

	if err != nil {
		panic(err)
	}

	return num
}

func bubbleSort(arr []int64) {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				temp := arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
			}
		}
	}
}

func getDistance(a int64, b int64) int64 {
	var distance int64
	if a > b {
		distance = a - b
	} else {

		distance = b - a
	}
	return distance
}

func main() {
	file, err := os.Open("input.txt")

	if err != nil {
		panic(err)
	}
	defer file.Close()

	left := []int64{}
	right := []int64{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		items := strings.Fields(scanner.Text())

		left = append(left, parseStr(items[0]))
		right = append(right, parseStr(items[1]))
	}

	bubbleSort(left)
	bubbleSort(right)

	var sum int64 = 0
	for i := 0; i < len(left); i++ {
		var similarity int64 = 0
		for j := 0; j < len(right); j++ {

			if left[i] == right[j] {
				similarity++
			}
		}

		sum += similarity * left[i]
	}
	fmt.Println(sum)
}
