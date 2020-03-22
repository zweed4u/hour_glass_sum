package main

import (
	"fmt"
	"math"
)

// https://www.hackerrank.com/challenges/2d-array/problem
func hourglassSum(arr [6][6]int32) (maxHourGlassSum int32) {
	for rowIndex := range arr {
		for columnIndex := range arr[0] {
			// 3 rows of overhead needed for 3 levels of the hourglass (top, middle, bottm)
			// 3 columns of overhead needed for length of top and bottom of hour glass
			if rowIndex > 3 || columnIndex > 3 {
				break
			}
			fmt.Printf("row %d  col %d\n", rowIndex, columnIndex)
			topHourGlass := arr[rowIndex][columnIndex] + arr[rowIndex][columnIndex+1] + arr[rowIndex][columnIndex+2]
			HourGlassBar := arr[rowIndex+1][columnIndex+1]
			bottomHourGlass := arr[rowIndex+2][columnIndex] + arr[rowIndex+2][columnIndex+1] + arr[rowIndex+2][columnIndex+2]

			hourGlassSum := topHourGlass + HourGlassBar + bottomHourGlass
			// initial condition for max sum
			if columnIndex == 0 && rowIndex == 0 {
				maxHourGlassSum = hourGlassSum
			}
			maxHourGlassSum = int32(math.Max(float64(maxHourGlassSum), float64(hourGlassSum)))
		}
	}
	return
}

func main() {
	arr := [6][6]int32{
		{1, 1, 1, 0, 0, 0},
		{0, 1, 0, 0, 0, 0},
		{1, 1, 1, 0, 0, 0},
		{0, 0, 2, 4, 4, 0},
		{0, 0, 0, 2, 0, 0},
		{0, 0, 1, 2, 4, 0},
	}
	fmt.Println(arr)
	sum := hourglassSum(arr)
	fmt.Println(sum)
}
