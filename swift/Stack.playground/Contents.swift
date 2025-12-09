import Cocoa

struct StackIterator<T>: IteratorProtocol {
    typealias Element = T
    
    var stack: Stack<T>
    
    mutating func next() -> Element? {
        return stack.pop()
    }
}

struct Stack<Element>: Sequence {
    var items = [Element]()
    
    mutating func push(_ newItem: Element) {
        items.append(newItem)
    }
    
    mutating func pop() -> Element? {
        guard !items.isEmpty else {
            return nil
        }
        return items.removeLast()
    }
    
    func map<U>(_ txform: (Element) -> U) -> Stack<U> {
        var mappedItems = [U]()
        for item in items {
            mappedItems.append(txform(item))
        }
        return Stack<U>(items: mappedItems)
    }
    
    func makeIterator() -> StackIterator<Element> {
        return StackIterator(stack: self)
    }
    
    mutating func pushAll<S: Sequence>(_ sequence: S) where S.Element == Element {
        for item in sequence {
            self.push(item)
        }
    }
}

var intStack = Stack<Int>()
intStack.push(1)
intStack.push(2)
var doubledStack = intStack.map {2 * $0}

print(String(describing: intStack.pop()))
print(String(describing: intStack.pop()))
print(String(describing: intStack.pop()))

print(String(describing: doubledStack.pop()))
print(String(describing: doubledStack.pop()))

var stringStack = Stack<String>()
stringStack.push("Hello")
stringStack.push("World")

print(String(describing: stringStack.pop()))

func myMap<T, U>(_ items: [T], _ txform: (T) -> (U)) -> [U] {
    var result = [U]()
    for item in items {
        result.append(txform(item))
    }
    return result
}

let strings = ["one", "two", "three"]
let stringLen = myMap(strings) {$0.count}
print(stringLen)

func checkIfEqual<T: Equatable>(_ first: T, _ second: T) -> Bool {
    return first == second
}

print(checkIfEqual(1,1))
print(checkIfEqual("A string", "A string"))
print(checkIfEqual("A string", "A different string"))

var myStack = Stack<Int>()
myStack.push(10)
myStack.push(20)
myStack.push(30)

var myStackIterator = StackIterator(stack: myStack)
while let value = myStackIterator.next() {
    print("got \(value)")
}

for value in myStack {
    print("for-in loop: got \(value)")
}

myStack.pushAll([1,2,3])
for value in myStack {
    print("After pushing: got \(value)")
}

var myOtherStack = Stack<Int>()
myOtherStack.pushAll([1,2,3])
myStack.pushAll(myOtherStack)
for value in myStack {
    print("after pushing items onto stack, got \(value)")
}

protocol Food {
    var menuListing: String {get}
}

struct Bread: Food {
    var kind = "sourdough"
    var menuListing: String {
        "\(kind) bread"
    }
}

func eat<T: Food>(_ food: T) {
    print("I sure love \(food.menuListing).")
}

eat(Bread())

struct Restaurant {
    private struct SlicedFood<Ingredient: Food>: Food {
        var food: Ingredient
        var menuListing: String {
            "a sliced of \(food.menuListing)"
        }
    }
    
    private struct CookedFood<Ingredient: Food>: Food {
        var food: Ingredient
        var menuListing: String {
            "\(food.menuListing), cooked to perfection"
        }
    }
    
    func makeSlicedBread() -> Food {
        return SlicedFood(food: Bread())
    }
    
    func makeToast() -> Food {
        let slicedBread = SlicedFood(food: Bread())
        return CookedFood(food: slicedBread)
    }
}

let restaurant = Restaurant()
let toast = restaurant.makeToast()
eat(toast)
