import Cocoa

var movieRatings = ["Tron": 4, "WarGames": 5, "Sneakers": 4]

// Accessing and modifying values
movieRatings.count
let tronRating = movieRatings["Tron"]

movieRatings["Sneakers"] = 5
movieRatings
movieRatings.updateValue(3, forKey: "Sneakers")
movieRatings

let oldRating: Int? = movieRatings.updateValue(5, forKey: "Tron")
if let lastRating = oldRating, let currentRating = movieRatings["Tron"] {
    print("old rating: \(lastRating)")
    print("current rating \(currentRating)")
}

// Adding and Removing Values
movieRatings["Hackers"] = 5
movieRatings.removeValue(forKey: "Sneakers")
movieRatings["Sneakers"] = nil

// Looping over a Dictionary
for (key, value) in movieRatings {
    print("The movie \(key) was rated \(value)")
}

for movie in movieRatings.keys {
    print("User has rated \(movie).")
}

// Translating a Dictionary to an Array
let watchedMovies = Array(movieRatings.keys)

// Silver Challenge
var teams = ["Red Pandas": ["Burb", "Testich", "Probatonich","Rubudubdub", "Andrea"], "Black Dragons": ["Sylvanovich", "Bolas", "Smaug", "Red", "Breach"], "The Marvelous": ["Ms. Marvel", "Cap", "Iron Man", "Spiderman", "Antman"]]

var players: [String] = []
for teamPlayers in teams.values {
    players += teamPlayers
}
print("The NWSL has the following players: \(players)")

// Gold Challenge
for (team, teamPlayers) in teams {
    print("\(team):")
    for i in 0...teamPlayers.count - 1 {
        print(teamPlayers[i])
    }
    print("\n")
}
