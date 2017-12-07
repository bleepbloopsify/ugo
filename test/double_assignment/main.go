package main

import (
	"fmt"
	"strings"
)

func returnTwo(s string) (string, string) {
	return s, strings.Join([]string{s, s}, ",")
}

func main() {
	_, s := returnTwo("yeet")

	fmt.Println(s)
}
