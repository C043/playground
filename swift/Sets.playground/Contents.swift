import Cocoa

var groceryList = Set<String>(["Apples", "Oranges"])
var grocerySetAlternative: Set = ["Apples", "Oranges"]

// Inserting new elements in sets
groceryList.insert("Lego set")
groceryList.insert("Lightsaber")

// Pooping through a set
for food in groceryList {
    print(food)
}

// Removing element from set
groceryList.remove("Apples")

// Working with sets
let hasBananas = groceryList.contains("Bananas")

// Unions
var friendsGroceryList: Set = ["Bananas", "Cereal", "Milk", "Oranges"]
let sharedList = groceryList.union(friendsGroceryList)

// Intersections
let duplicateItems = groceryList.intersection(friendsGroceryList)

// Disjoint
let disjoint = groceryList.isDisjoint(with: friendsGroceryList)

// Moving between Types
let players = ["Mario", "Cristian", "Daniele"]
let winners = ["Daniele", "Cristian", "Daniele", "Daniele"]

let playerSet = Set(players)
let winnerSet = Set(winners)

let loserPlayers = playerSet.subtracting(winnerSet)
print(loserPlayers)

// Bronze Challenge
let myCities: Set = ["Atlanta", "Chicago", "Jacksonville", "New York", "Denver"]
let yourCities: Set = ["Chicago", "Denver", "Jacksonville"]

myCities.isSuperset(of: yourCities)

// Silver Challenge
groceryList = groceryList.intersection(friendsGroceryList)
print(groceryList)
groceryList = groceryList.union(friendsGroceryList)
print(groceryList)
