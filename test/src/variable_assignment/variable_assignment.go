package main
import (
    "fmt"
)
func returns_two() (int, int) {
    return 2, 3
}

func prints_one_of_them(integer int) {
    fmt.Println(integer)
}

func main() {
    integer_1, integer_2 := returns_two()

    prints_one_of_them(integer_1)
    prints_one_of_them(integer_2)
    fmt.Println(integer_1)

    _, integer_3 := returns_two()
    fmt.Println(integer_3)
}
