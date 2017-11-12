package main

import (
	"fmt"
)

func returnsTwo() (int, int) {
	return 2, 3
}

func printsOneOfThem(integer int) {
	fmt.Println(integer)
}

func main() {
	integer1, integer2 := returnsTwo()

	printsOneOfThem(integer1)
	printsOneOfThem(integer2)
	fmt.Println(integer1)

	_, integer3 := returnsTwo()
	fmt.Println(integer3)
}
