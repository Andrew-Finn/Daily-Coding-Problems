package main

import "fmt"

func main() {
	var out string
	for i := 0; i <= 100; i++ {
		out = ""
		if i%3 == 0 {
			out += "Fizz"
		}
		if i%5 == 0 {
			out += "Buzz"
		}
		if out == "" {
			fmt.Println(i)
			continue
		}
		fmt.Println(out)
	}
}
