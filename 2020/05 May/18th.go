//Good morning! Here's your coding interview problem for today.
//
//This problem was asked by Amazon.
//
//Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. Return null if there is no such index.
//
//For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, we return 2 since it's the lowest index.

package main

import "fmt"

func findSmallestIndex(arr [] int) int{
	for i, num := range arr{
		if i == num {
			return i
		}
	}
	return -1
}

func main() {
	slc  := [] int {-5, -3, 2, 3}
	fmt.Println(findSmallestIndex(slc))
	return
}