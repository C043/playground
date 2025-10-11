import Cocoa

let volunteerCounts = [1,3,40,32,2,53,77,13]

func isAscending(_ i: Int, _ j: Int) -> Bool {
    return i < j
}
var volunteersSorted = volunteerCounts.sorted(by: isAscending)

// Declaring the closure inline
volunteersSorted = volunteerCounts.sorted(by: {
    (i: Int, j: Int) -> Bool in
    return i < j
})

// Type inference
volunteersSorted = volunteerCounts.sorted(by: { i, j in i < j })

// Shorthand syntax
volunteersSorted = volunteerCounts.sorted(by: {$0 < $1})

// Trailing closure syntax
volunteersSorted = volunteerCounts.sorted {$0 < $1}

print(volunteersSorted)

// Building a function that takes a closure as parameter
func format(numbers: [Double], using formatter: (Double) -> String = {"\($0)"}) -> [String] {
    var result = [String]()
    
    for number in numbers {
        let transformed = formatter(number)
        result.append(transformed)
    }
    
    return result
}

let rounder: (Double) -> String = {
    (num: Double) -> String in
    return "\(Int(num.rounded()))"
}

let volunteerAvarages = [10.75, 4.2, 1.5, 12.12, 16.815]
let roundedAvaragesAsStrings = format(numbers: volunteerAvarages, using: rounder)
