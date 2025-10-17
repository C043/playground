import Cocoa

let playground = "Hello, playground"
var mutablePlayground = "Hello mutable playground"
mutablePlayground += "!"
let quote = #"I wanteed to \"say\":\n\(playground)"#
print(quote)
for c: Character in mutablePlayground {
    print("'\(c)'")
}

let start = playground.startIndex
let end = playground.index(start, offsetBy: 4)
let fifthCharacter = playground[end]

let range = ...end
let firstFive = playground[range]

// Bronze challenge
let empty = ""
if empty.isEmpty {
    print("The string is empty")
}
