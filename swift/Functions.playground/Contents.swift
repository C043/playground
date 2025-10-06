import Cocoa

func printGreeting(to name: String) {
    print("Hello, \(name)")
}

printGreeting(to: "C043")

func divisionDescriptionFor(numerator: Double, denominator: Double, withPunctuation punctuation: String = ".") -> String {
    return "\(numerator) divided by \(denominator) is \(numerator / denominator)\(punctuation)"
}

print(divisionDescriptionFor(numerator: 9.0, denominator: 3.0, withPunctuation: "!"))

var error = "The request failed:"
func appendErrorCode(_ code: Int, toErrorString errorString: inout String) {
    if code == 400 {
        errorString += " bad request."
    }
}

appendErrorCode(400, toErrorString: &error)
print(error)

func areaOfTriangleWith(base: Double, height: Double) -> Double {
    let rectangle = base * height
    func divide() -> Double {
        return rectangle / 2
    }
    return divide()
}

print(areaOfTriangleWith(base: 3.0, height: 5.0))

func sortedEvenOddNumbers(_ numbers: [Int]) -> (evens: [Int], odds: [Int]) {
    var evens = [Int]()
    var odds = [Int]()
    for number in numbers {
        if number % 2 == 0 {
            evens.append(number)
        } else {
            odds.append(number)
        }
    }
    return (evens, odds)
}

let aBunchOfNumbers = [10,1,4,3,57,43,84,27,156,111]
let theSortedNumbers = sortedEvenOddNumbers(aBunchOfNumbers)
print("The even numbers are: \(theSortedNumbers.evens); the odd numbers are: \(theSortedNumbers.odds)")

func grabMiddleName(fromFullName name: (String, String?, String)) -> String? {
    return name.1
}

let middlename = grabMiddleName(fromFullName: ("Alice", nil, "Ward"))
if let theName = middlename {
    print(theName)
}

// Bronze Challenge
func greetByMiddleName(fromFullName name: (first: String, middle: String?, last: String)) {
    guard let middlename = name.middle, middlename.count > 10 else {
        print("Hey there!")
        return
    }
    let firstLetterIndex = middlename.startIndex
    print("Hey, \(name.first) \(middlename[firstLetterIndex]). \(name.last)")
}

greetByMiddleName(fromFullName: ("Alice", "Richardsdfasrfasdf", "Ward"))

let evenOddFunction: ([Int]) -> ([Int], [Int]) = sortedEvenOddNumbers

// Silver Challenge
func siftBeans(fromGroceryList list: [String]) -> (beans: [String], otherGroceries: [String]){
    var beans = [String]()
    var otherGroceries = [String]()
    
    for grocery in list{
        if grocery.contains("beans") {
            beans.append(grocery)
        } else {
            otherGroceries.append(grocery)
        }
    }
    return (beans, otherGroceries)
}

let result = siftBeans(fromGroceryList: ["green beans", "milk", "black beans", "pinto beans", "apple"])

result.beans
result.otherGroceries
