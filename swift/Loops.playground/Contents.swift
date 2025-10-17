import Cocoa

for i in 0...100 {
    if i % 3 == 0 && i % 5 == 0{
        print("FIZZ BUZZ")
    } else if i % 3 == 0 {
        print("FIZZ")
    } else if i % 5 == 0 {
        print("BUZZ")
    } else {
        print(i)
    }
}

for i in 0...100 {
    switch true {
    case i % 3 == 0 && i % 5 == 0:
        print("FIZZ BUZZ")
        break
    case i % 3 == 0:
        print("FIZZ")
        break
    case i % 5 == 0:
        print("BUZZ")
        break
    default:
        print(i)
    }
}

var myFirstInt: Int = 0

for i in 1...5 {
    myFirstInt += 1
    print(myFirstInt)
    print("i is equal to \(i)")
}

for i in 1...100 where i % 3 == 0 {
    print(i)
}

var i = 1
while i < 6 {
    myFirstInt += 1
    print(myFirstInt)
    i+=1
}

var shields: Int = 5
var blasterOverheating = false
var blasterFireCount = 0
var spaceDemonsDestroyed = 0

repeat {
    print("Fire blasters!")
} while shields < 0

while shields > 0 {
    if spaceDemonsDestroyed == 500 {
        print("You beat the game!")
        break
    }
    
    if blasterOverheating {
        print("Cooldown initialted")
        sleep(5)
        print("Blaster ready to fire!")
        sleep(1)
        blasterOverheating = false
        blasterFireCount = 0
    }
    
    if blasterFireCount > 100 {
        blasterOverheating = true
        continue
    }
    
    print("Fire Blasters!")
    blasterFireCount += 1
    spaceDemonsDestroyed += 1
}

