// Single line comment
/* Multi-
line comment */

// A package clause starts every source file.
// main is a special name declaring an executable rather than a library.
package main

// Import declaration declares library packages referenced in this file.
import (
	"fmt" // A package in the Go standard library.
)

/*
A function definition. Main is special. It is the entry point for the executable program. Love it or hate it, Go uses brace brackets
*/
func main() {
	// Println outputs a line to stdout
	// It comes from the package fmt
	fmt.Println("Hello World!")

	// Call another function within this package
	beyondHello()
}

// Functions have parameters in parentheses
// If there are no parameters, empty parentheses are still required.
func beyondHello() {
	var x int // Variable declaration. Variables must be declared before use.
	x = 3     // Variable assignment.
	// "Short" declarations use := to infer the type, declare, and assign.
	y := 4
	sum, prod := learnMultiple(x, y)        // Function returns two values.
	fmt.Println("sum:", sum, "prod:", prod) // Simple output.
	learnTypes()                            // < y minutes, learn more!
}

/*
Functions can have parameters and (multiple!) return values. Here `x`, `y` are the arguments and `sum`, `prod` is the signature (what's returned). Note that `x` and `sum` receive the type `int`.
*/
func learnMultiple(x, y int) (sum, prod int) {
	return x + y, x * y // Return two values.
}

// Some built-in types and literals.
func learnTypes() {
	// Short declaration usually gives you what you want.
	str := "Learn Go!" // string type.

	s2 := `A "raw" string literal
	can include line breaks.` // Same string type.

	// Non-ASCII literal. Go source is UTF-8.
	g := 'Σ' // rune type, an alias for int32, holds a unicode code point.

	f := 3.14159 // float64, an IEEE-754 64-bit floating point number.
	c := 3 + 4i  // complex128, represented internally with two float64's.

	// var syntax with initializers.
	var u uint = 7 // Unsigned, but implementation dependent size as with int.
	var pi float32 = 22. / 7

	// Conversion syntax with a short declaration.
	n := byte('\n') // byte is an alias for uint8.

	// Arrays have size fixed at compile time.
	var a4 [4]int                    // An array of 4 ints, initialized to all 0.
	a5 := [...]int{3, 1, 5, 10, 100} // An array initialized with a fixed size of five
	// elements, with values 3, 1, 5, 10, and 100.

	// Arrays have value semantics.
	a4_cpy := a4                    // a4_cpy is a copy of a4, two separate instances.
	a4_cpy[0] = 25                  //Only a4_cpy is changed, a4 stays the same.
	fmt.Println(a4_cpy[0] == a4[0]) // false

	// Slices have dynamic size. Arrays and slices each have advantages
	// but use cases for slices are much more common.
	s3 := []int{4, 5, 9}    // Compare to a5. No ellipsis here.
	s4 := make([]int, 4)    // Allocates slice of 4 ints, initialized to all 0.
	var d2 [][]float64      // Declaration only, nothing allocated here.
	bs := []byte("a slice") // Type conversion syntax

	// Slices (as well as maps and channels) have reference semantics
	s3_cpy := s3                    // Both variables point to the same instance.
	s3_cpy[0] = 0                   // Which means both are updated.
	fmt.Println(s3_cpy[0] == s3[0]) // true

	// Because they are dynamic, slices can be appended to on-demand.
	// To append elements to a slice, the built-in append() function is used.
	// First argument is a slice to which we are appending.
	// Commonly, the slice variable is updated in place, as in example below.
	s := []int{1, 2, 3}    // Result is a slice of length 3.
	s = append(s, 4, 5, 6) // Added 3 elements. Slice now has length of 6.
	fmt.Println(s)         // Updated slice is now [1 2 3 4 5 6]

	// To append another slice, instead of list of atomic elements we can
	// pass a reference to a slice literal like this, with a
	// trailing ellipsis, meaning take a slice and unpack its elements,
	// appending them to slice s.
	s = append(s, []int{7, 8, 9}...) // Second argument is a slice literal
	fmt.Println(s)                   // Updated slice is now [1 2 3 4 5 6 7 8 9]

	p, q := learnMemory() // Declares p, q to be type pointer to int.
	fmt.Println(*p, *q)   // * follows a pointer. This prints two ints.

}

// Go is fully garbage collected. It has pointers but not pointer arithmetic.
// You can make a mistake with a nil pointer, but not by incrementing a pointer.
// Unlike in C/Cpp taking and returning an address of a local variable is also safe.
func learnMemory() (p, q int) {
	// Named return values p and q have type pointer to int.
	p = new(int) // Built-in function new allocates memory.
	// The allocated int slice is initialized to 0, p is no longer nil.
	s := make([]int, 20) // Allocate 20 ints as a single block of memory.
	s[3] = 7             // Assign one of them.
	r := -2              // Declare another local variable.
	return &s[3], &r     // & takes the address of an object
}
