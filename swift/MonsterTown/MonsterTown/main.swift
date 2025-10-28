//
//  main.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 15/10/25.
//

import Foundation

var myTown = Town()
let myTownSize = myTown.townSize
print(myTownSize)

myTown.changePopulation(by: 500)

let fredTheZombie = Zombie()
fredTheZombie.town = myTown
fredTheZombie.terrorizeTown()
fredTheZombie.town?.printDescription()

print("Victim pool: \(fredTheZombie.victimPool)")
fredTheZombie.victimPool = 500
print("Victim pool: \(fredTheZombie.victimPool)")

print(Zombie.spookyNoise)
if Zombie.isTerrifying {
    print("Run away!")
}
