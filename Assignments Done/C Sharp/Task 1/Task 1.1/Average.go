package main

import (
	"fmt"
)

func Average(arr []int) float64 {
	sum := 0
	for _, i := range arr {
		sum += i
	}
	avg := (float64(sum)) / (float64(len(arr)))
	return avg
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println("The numbers : ", arr)
	result := Average(arr)
	if result >= 10 {
		fmt.Println("Double digits")
	} else {
		fmt.Println("Single digits")
	} // Note : This will print "Double digits" for all numbers bigger than 9, so even 10000 is double digits.
	// And, negative numbers will print "Single digit" no matter the length. This is how the questions
	// asks to implement.
	fmt.Println("Average of the numbers : ", result)
}
