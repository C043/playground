import Cocoa

var bucketList: Array<String>
var bucketListAlternative: [String]
bucketList = ["Climb the mountain"]
bucketList.append("Read a lot of books")
bucketList.append("Become a coding god")
bucketList.append("Travel the world")
bucketList.append("Have no money problems")
bucketList.count

bucketList.remove(at: 1)

print(bucketList[...2])

bucketList[1] += " with friends"
bucketList[1]

bucketList[0] = "Climb a specific mountain"

bucketList.insert("Finish you current book", at: 0)

var newItems = [
    "The Hobbit",
    "Testing new frameworks",
    "Making the computer fans light up!"
]

bucketList += newItems

// for item in newItems {
    // bucketList.append(item)
// }

var anotherList = [
    "The Hobbit",
    "Testing new frameworks",
    "Making the computer fans light up!"
]

newItems == anotherList

let lunches = [
    "Cheese",
    "Pizza",
    "Cheese Pizza Powder",
    "Forbidden candy"
]

// Broze challenge
var toDoList = ["Take out the trash", "Pay bills", "Cross off finished items"]
toDoList.contains("Pay bills")
!toDoList.isEmpty
toDoList.count > 0

// Silver Challenge
toDoList.reverse()
print(toDoList)
toDoList.shuffle()

// Gold Challenge
var taskList = ["Take out the trash", "Learn Swift", "Buy gift"]
let indexOfTask = taskList.firstIndex(of: "Take out the trash")
var indexOfNextTask: Int?
var nextTask: String?
print(type(of: indexOfTask))

// Unwrapping
if let index = indexOfTask, taskList.count >= index + 2{
    indexOfNextTask = index + 2
    nextTask = taskList[index + 2]
} else {
    nextTask = nextTask ?? "No next task"
}

print(nextTask!)

