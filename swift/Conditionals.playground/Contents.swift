let population: Int = 5443
var message: String
let hasPostOffice: Bool = true

if population < 10000 {
    message = "\(population) is a small town!"
} else {
    message = "\(population) is pretty big!"
}

message = population < 10000 ? "\(population) is a small town!" : "\(population) is pretty big!"

print(message)

if !hasPostOffice {
    print("Where will we buy stamps?")
}
