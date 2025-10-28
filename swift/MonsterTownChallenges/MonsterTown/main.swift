//
//  main.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 15/10/25.
//

import Foundation

var myTown = Town()

myTown.changePopulation(by: 2)

let fredTheZombie = Zombie()
let edwardTheVampire = Vampire()
edwardTheVampire.town = myTown
edwardTheVampire.terrorizeTown()
print(edwardTheVampire.thralls)
edwardTheVampire.terrorizeTown()
print(edwardTheVampire.thralls)
edwardTheVampire.town?.printDescription()
